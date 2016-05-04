import java.util.Random;
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.math.*;
import java.util.Scanner;

public class main {

	public static void main(String[] args) 
	{
	
		//Definiciones	
		String[] inicial = new String[10];
		int[] numeros = new int[10];
		String[] hijos = new String[10];
		double[] objetivo = new double[10];
		double[] fitness = new double[10];
		double[] promObj = new double[1120];
		double[] maxObj = new double[1120];
		double[] minObj = new double[1120];
		String[] numMax = new String[1120];
		Scanner sc = new Scanner(System.in);
		int numSel=0;
		
		
		Random rnd = new Random();
		
		//menu
		System.out.println("Desea utilizar elitismo? \n 1- No \n 2-Elitismo de 2 \n 3-Elitismo de 4");
		int opt = sc.nextInt();
		if(opt==1) numSel=0;
		else if(opt==2) numSel=2;
		else if (opt==3) numSel=4;
		
		
		
		
		
		//Coeficiente
		int coef=(int)Math.pow(2, 30) -1;
		
		//genero cromosoma inicial (agrego el primer digito, y le concateno los otros 29)
		for(int i=0;i<10;i++)
		{	
			inicial[i]=Integer.toString(rnd.nextInt(2));
			for(int j=0;j<29;j++)
			{
				inicial[i]=inicial[i].concat(Integer.toString(rnd.nextInt(2)));
			}
		}
		
		int cantTirada=20;
		int menor =0;
		for(int y=0;y<3;y++)
		{
			
			if(y==1) 
			{
				cantTirada=120;
				menor=20;
			}
			if(y==2)
			{
				cantTirada=1120;
				menor=100;
			}
		
		//primer genetico de 20 pasadas
		for(int i=0;i<10;i++)
		{
			numeros[i]=Integer.parseInt(inicial[i],2);
		}
		
		for(int z=menor;z<cantTirada;z++)
		{
			//Obtengo minimo, maximo y suma de Funcion Objetivo
			double sumaObj = 0;
			maxObj[z] = 0;
			minObj[z] = 10;
			int indiceMax=-1;
			for(int i=0;i<10;i++)
			{
				objetivo[i]= Math.pow((double)numeros[i]/coef, 2);
				if(objetivo[i]>maxObj[z]) 
					{
					maxObj[z]=objetivo[i];
					indiceMax=i;
					}
				if(objetivo[i]<minObj[z]) minObj[z]=objetivo[i];
				sumaObj=sumaObj+objetivo[i];
			}
			//MANTENEMOS TAMAÑO DE PALABRA DE 30
			String fix = "000000000000000000000000000000";
			String number = Integer.toBinaryString(numeros[indiceMax]);
			numMax[z] = fix.substring(0,30-number.length()).concat(number);
			promObj[z]=sumaObj/10;
			//Obtengo Funcion Fitness
			for(int i=0;i<10;i++)
			{
				fitness[i]=objetivo[i]/sumaObj;
			}
			
			//ordenamiento
			if(numSel>0)
			{
				for(int j=0;j<9;j++)
				{
					for(int i=0;i<9;i++)
					{
						if(numeros[i]<numeros[i+1])
						{
							//intercambio el numero y la funcion objetivo
							int auxNum = numeros[i];
							numeros[i] = numeros[i+1];
							numeros[i+1] = auxNum;
						}
					}
				}	
			}
		
			
			 for(int i=0;i<numSel;i++)
			 {
				
				 	//fix me mantiene el tamaño de palabra de 30
					String numero = Integer.toBinaryString(numeros[i]);
					hijos[i] = fix.substring(0,30-numero.length()).concat(numero);
				  
			 }
			
			
			
			//RULETA
			//lo que hacemos es separar por intervalos consecutivos, y comparar el numero random con el principio y el fin del intervalo
			//los intervalos son de 0 al primer fitnes; y despues van desde el fin del fitnes anterior hasta el fin del fitness concurrente
			//la suma de todos los fitness es igual a 1
			int[] elegido = new int[10];
			for(int j=0;j<10;j++)
			{
				double rndRuleta = rnd.nextDouble();
				double sumfitness = fitness[0];
				
				for(int i=0;i<10;i++)
				{
					//sumFitness lleva el tope del campo, si le resto fitness[i] obtengo el inicio del campo
					if((rndRuleta>sumfitness) && (rndRuleta<(sumfitness+fitness[i])) )
					{
						//guardamos el indice del numero que salio en un arreglo de indices llamado elegido
						 elegido[j]=i;
						 break;
					} else
					{
						sumfitness = sumfitness+fitness[i];
					}
				}
			}
			
			//CrossOver y Mutacion (se hace 5 veces, para los 5 pares) ( por eso aumenta de a 2)
			for(int h=numSel;h<10;h=h+2)
			{
				//guardamos los cromosomas en un auxiliar
				String aux1=Integer.toBinaryString(numeros[elegido[h]]);
				String aux2=Integer.toBinaryString(numeros[elegido[h+1]]);
				//Mantenemos el tamaño de palabra de 30
				//(al trabajar con numeros en decimal, si el numero binario empieza con 0, cuando lo pasamos a decimal,
				//y lo volvemos a pasar a binario, nos queda la cadena mas corta, 
				//entonces lo que hacemos es agregar tantos 0 al inicio 
				//como sea necesario para llegar al tamaño de palabra de 30
				for (int i=0;i<10;i++)
				{
					while(aux1.length() <30)
					{
						String cadena = aux1;
						aux1="0".concat(cadena);
					}
					while(aux2.length() <30)
					{
						String cadena = aux2;
						aux2="0".concat(cadena);
					}	
				}
				
				//generamos numero random y si el numero es menor que 0.75 hacemos crossOver
				double rndCrossOver = rnd.nextDouble();
				if(rndCrossOver <0.75)
				{
					int rndPosCross = rnd.nextInt(30);
					//cambio
					hijos[h]=aux1.substring(0, rndPosCross)+aux2.substring(rndPosCross,30);
					hijos[h+1]=aux2.substring(0, rndPosCross)+aux1.substring(rndPosCross,30);
				}
				else
				{
					hijos[h]=aux1;
					hijos[h+1]=aux2;
				}
				
				//si el numero random es menor que 0.05 mutamos
				double rndMut1 = rnd.nextDouble();
				if(rndMut1<0.05)
				{
					int rndPosMut = rnd.nextInt(29);
					if(rndPosMut== 0)
					{
						if(hijos[h].charAt(rndPosMut) == '0')
						{
							hijos[h]="1".concat(hijos[h].substring(1, hijos[h].length()-1));
						}
						else
						{
							hijos[h]="0".concat(hijos[h].substring(1, hijos[h].length()-1));
						}
					}else if( rndPosMut == 29)
					{
						if(hijos[h].charAt(rndPosMut) == '0')
						{
							hijos[h]=hijos[h].substring(0, hijos[h].length()-2).concat("1");
						}
						else
						{
							hijos[h]=hijos[h].substring(0, hijos[h].length()-2).concat("0");
						}
					}else 
					{
						String primera = hijos[h].substring(0,(rndPosMut-1));
						String segunda = hijos[h].substring((rndPosMut+1));
						if(hijos[h].charAt(rndPosMut) == '0')
						{
							hijos[h]=primera.concat("1").concat(segunda);
						}
						else
						{
							hijos[h]=primera.concat("0").concat(segunda);
						}
					}
				}
				
				//si el numero random es menor que 0.05 mutamos
				double rndMut2 = rnd.nextDouble();
				if(rndMut2<0.05)
				{			
					int rndPosMut = rnd.nextInt(29);
					if(rndPosMut== 0)
					{
						if(hijos[h+1].charAt(rndPosMut) == '0')
						{
							hijos[h+1]="1".concat(hijos[h+1].substring(1, hijos[h+1].length()-1));
						}
						else
						{
							hijos[h+1]="0".concat(hijos[h+1].substring(1, hijos[h+1].length()-1));
						}
					}else if( rndPosMut == 29)
					{
						if(hijos[h+1].charAt(rndPosMut) == '0')
						{
							hijos[h+1]=hijos[h+1].substring(0, hijos[h+1].length()-2).concat("1");
						}
						else
						{
							hijos[h+1]=hijos[h+1].substring(0, hijos[h+1].length()-2).concat("0");
						}
					}else 
					{
						String primera = hijos[h+1].substring(0,(rndPosMut-1));
						String segunda = hijos[h+1].substring((rndPosMut+1));
						if(hijos[h+1].charAt(rndPosMut) == '0')
						{
							hijos[h+1]=primera.concat("1").concat(segunda);
						}
						else
						{
							hijos[h+1]=primera.concat("0").concat(segunda);
						}
					}
				}
				
			}
			
			for(int i=0;i<10;i++)
			{
				
					numeros[i]=Integer.parseInt(hijos[i],2);
				
			}
				
		}
		//termina primer genetico de 20 repeticiones 
	}//fin for 3 repeticiones
		
		//imprimimos resultados
		System.out.println("   Iteracion       Cromosoma                         minF(X)                 promF(X)                maxF(X)");
		for(int i=0;i<20;i++)
		{
			System.out.println("      "+(i+1)+"           "+numMax[i]+"    "+minObj[i]+"    "+promObj[i]+"   "+maxObj[i]);
		}
		System.out.println("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n");
		System.out.println("   Iteracion       Cromosoma                         minF(X)                 promF(X)                maxF(X)");
		for(int i=20;i<120;i=i+5)
		{
			System.out.println("      "+(i+1-20)+"           "+numMax[i]+"    "+minObj[i]+"    "+promObj[i]+"   "+maxObj[i]);
		}
		System.out.println("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n");
		System.out.println("   Iteracion       Cromosoma                         minF(X)                 promF(X)                maxF(X)");
		for(int i=120;i<1120;i=i+50)
		{
			System.out.println("      "+(i+1-120)+"           "+numMax[i]+"    "+minObj[i]+"    "+promObj[i]+"   "+maxObj[i]);
		}
		
		
		//guardamos los numeros en txt para poder generar las graficas en excel
		try {
	        BufferedWriter out = new BufferedWriter(new FileWriter("C:\\Users\\nicolas\\desktop\\Geneticos\\minimo20.txt"));
	            for (int i = 0; i < 20; i++) {
	            	
	            	String numero ="0,".concat((Double.toString(minObj[i])).substring(2, Double.toString(minObj[i]).length()));
	                out.write(numero + " \n");
	            }
	            out.close();
	        } catch (IOException e) {
	        	e.printStackTrace();
	        }
		try {
	        BufferedWriter out = new BufferedWriter(new FileWriter("C:\\Users\\nicolas\\desktop\\Geneticos\\promedio20.txt"));
	            for (int i = 0; i < 20; i++) {
	            	
	            	String numero ="0,".concat((Double.toString(promObj[i])).substring(2, Double.toString(promObj[i]).length()));
	                out.write(numero + " \n");
	            }
	            out.close();
	        } catch (IOException e) {
	        	e.printStackTrace();
	        }
		try {
	        BufferedWriter out = new BufferedWriter(new FileWriter("C:\\Users\\nicolas\\desktop\\Geneticos\\maximo20.txt"));
	            for (int i = 0; i < 20; i++) {
	            	
	            	String numero ="0,".concat((Double.toString(maxObj[i])).substring(2, Double.toString(maxObj[i]).length()));
	                out.write(numero + " \n");
	            }
	            out.close();
	        } catch (IOException e) {
	        	e.printStackTrace();
	        }
		try {
	        BufferedWriter out = new BufferedWriter(new FileWriter("C:\\Users\\nicolas\\desktop\\Geneticos\\numeros20.txt"));
	            for (int i = 0; i < 20; i++) {
	            	out.write(numMax[i] + " \n");
	            }
	            out.close();
	        } catch (IOException e) {
	        	e.printStackTrace();
	        }
		
		//imprimo para 100
		try {
	        BufferedWriter out = new BufferedWriter(new FileWriter("C:\\Users\\nicolas\\desktop\\Geneticos\\minimo100.txt"));
	            for (int i = 20; i < 120; i=i+5) {
	            	
	            	String numero ="0,".concat((Double.toString(minObj[i])).substring(2, Double.toString(minObj[i]).length()));
	                out.write(numero + " \n");
	            }
	            out.close();
	        } catch (IOException e) {
	        	e.printStackTrace();
	        }
		try {
	        BufferedWriter out = new BufferedWriter(new FileWriter("C:\\Users\\nicolas\\desktop\\Geneticos\\promedio100.txt"));
	            for (int i = 20; i < 120; i=i+5) {
	            	
	            	String numero ="0,".concat((Double.toString(promObj[i])).substring(2, Double.toString(promObj[i]).length()));
	                out.write(numero + " \n");
	            }
	            out.close();
	        } catch (IOException e) {
	        	e.printStackTrace();
	        }
		try {
	        BufferedWriter out = new BufferedWriter(new FileWriter("C:\\Users\\nicolas\\desktop\\Geneticos\\maximo100.txt"));
	            for (int i = 20; i < 120; i=i+5) {
	            	
	            	String numero ="0,".concat((Double.toString(maxObj[i])).substring(2, Double.toString(maxObj[i]).length()));
	                out.write(numero + " \n");
	            }
	            out.close();
	        } catch (IOException e) {
	        	e.printStackTrace();
	        }
		try {
	        BufferedWriter out = new BufferedWriter(new FileWriter("C:\\Users\\nicolas\\desktop\\Geneticos\\numeros100.txt"));
	            for (int i = 20; i < 120; i=i+5) {
	                out.write(numMax[i] + " \n");
	            }
	            out.close();
	        } catch (IOException e) {
	        	e.printStackTrace();
	        }
		
		//imprimo para 1000
		try {
	        BufferedWriter out = new BufferedWriter(new FileWriter("C:\\Users\\nicolas\\desktop\\Geneticos\\minimo1000.txt"));
	            for (int i = 120; i < 1120; i=i+50) {
	            	
	            	String numero ="0,".concat((Double.toString(minObj[i])).substring(2, Double.toString(minObj[i]).length()));
	                out.write(numero + " \n");
	            }
	            out.close();
	        } catch (IOException e) {
	        	e.printStackTrace();
	        }
		try {
	        BufferedWriter out = new BufferedWriter(new FileWriter("C:\\Users\\nicolas\\desktop\\Geneticos\\promedio1000.txt"));
	            for (int i = 120; i < 1120; i=i+50) {
	            	String numero ="0,".concat((Double.toString(promObj[i])).substring(2, Double.toString(promObj[i]).length()));
	                out.write(numero + " \n");
	            }
	            out.close();
	        } catch (IOException e) {
	        	e.printStackTrace();
	        }
		try {
	        BufferedWriter out = new BufferedWriter(new FileWriter("C:\\Users\\nicolas\\desktop\\Geneticos\\maximo1000.txt"));
	            for (int i = 120; i < 1120; i=i+50) {
	            	
	            	String numero ="0,".concat((Double.toString(maxObj[i])).substring(2, Double.toString(maxObj[i]).length()));
	                out.write(numero + " \n");
	            }
	            out.close();
	        } catch (IOException e) {
	        	e.printStackTrace();
	        }
		try {
	        BufferedWriter out = new BufferedWriter(new FileWriter("C:\\Users\\nicolas\\desktop\\Geneticos\\numeros1000.txt"));
	            for (int i = 120; i < 1120; i=i+50) {
	            	out.write(numMax[i] + " \n");
	            }
	            out.close();
	        } catch (IOException e) {
	        	e.printStackTrace();
	        }
	

	}//fin main
}//fin clase
