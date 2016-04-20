import java.util.Random;
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.math.*;
public class main {

	public static void main(String[] args) 
	{
	
		//Definiciones
		
		int[][] cromosoma = new int[10][30];
		int[] numeros = new int[10];
		String[] hijos = new String[10];
		double[] objetivo = new double[10];
		double[] fitness = new double[10];
		Random rnd = new Random();
		double[] sumaObj = new double[1000];
		double[] promObj = new double[1000];
		double[] maxObj = new double[1000];
		double[] minObj = new double[1000];
		double[] sumaFit = new double[1000];
		double[] promFit = new double[1000];
		double[] maxFit = new double[1000];
	
		
		//Coeficiente
		int coef=(int)Math.pow(2, 30) -1;
		
		//genero cromosoma inicial
		//Con el if, obligo a que tengo si o si 30 digitos, porque salian menores tambien
		for(int i=0;i<10;i++)
		{	
			int var = rnd.nextInt(coef);
			if(var>Math.pow(2, 29))
			{
				numeros[i]=var;
			}
			else
			{
				while(var<Math.pow(2, 29))
				{
					var=rnd.nextInt(coef);
				}
				numeros[i]=var;
			}
		}
			
		
		for(int z=0;z<1000;z++)
		{
			//Obtengo maximo y suma de Funcion Objetivo
			sumaObj[z] = 0;
			maxObj[z] = 0;
			minObj[z] = 1;
			for(int i=0;i<10;i++)
			{
				objetivo[i]= Math.pow((double)numeros[i]/coef, 2);
				if(objetivo[i]>maxObj[z]) maxObj[z]=objetivo[i];
				if(objetivo[i]<minObj[z]) minObj[z]=objetivo[i];
				sumaObj[z]=sumaObj[z]+objetivo[i];
			}
			
			//Obtengo maximo y suma de Funcion Fitness
			sumaFit[z] = 0;
			 maxFit[z] = 0;
			 
			for(int i=0;i<10;i++)
			{
				fitness[i]=objetivo[i]/sumaObj[z];
				if(fitness[i]>maxFit[z]) maxFit[z]=fitness[i];
				sumaFit[z] = sumaFit[z] + fitness[i];
			}
			
			//Tabla  de resultados
			System.out.println("N°                                 Decimal       Objetivo                Fitness ");
			for(int i=0;i<10;i++)
			{
				System.out.println(i+" "+Integer.toBinaryString(numeros[i])+" "+numeros[i]+" "+objetivo[i]+" "+fitness[i]);
			}
			promObj[z]=sumaObj[z]/10;
			promFit[z]=sumaFit[z]/10;
			System.out.println("suma "+sumaObj[z]+" "+sumaFit[z]);
			System.out.println("promedio "+promObj[z]+" "+promFit[z]);
			System.out.println("maximo "+maxObj[z]+" "+maxFit[z]);
			
			//RULETA
			int[] elegido = new int[10];
			for(int j=0;j<10;j++)
			{
				double rndRuleta = rnd.nextDouble();
				double sumfitness = fitness[0];
				
				for(int i=0;i<10;i++)
				{
					//sumFitness lleva el tope del campo, si le resto fitness[i] obtengo el inicio del campo
					if((rndRuleta<sumfitness) && (rndRuleta>(sumfitness-fitness[i])))
					{
						 elegido[j]=i;
						 break;
					} else
					{
						sumfitness = sumfitness+fitness[i+1];
					}
				}
			}
			
			//CrossOver y Mutacion (se hace 5 veces, para los 5 pares)
			for(int h=0;h<10;h=h+2)
			{
				double rndCrossOver = rnd.nextDouble();
				String aux1=Integer.toBinaryString(numeros[elegido[h]]);
				String aux2=Integer.toBinaryString(numeros[elegido[h+1]]);
				//Mantengo el tamaño de palabra de 30
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
				double rndMut1 = rnd.nextDouble();
				double rndMut2 = rnd.nextDouble();
				if(rndMut1<0.05)
				{
					int rndPosMut = rnd.nextInt(28)+1;
					String primera = hijos[h].substring(0,(rndPosMut-1));
					String segunda = hijos[h].substring((rndPosMut+1));
					if(hijos[h].charAt(rndPosMut) == 0)
					{
						
						hijos[h]=primera.concat("1").concat(segunda);
					}
					else
					{
						hijos[h]=primera.concat("0").concat(segunda);
					}
					
				}
				if(rndMut2<0.05)
				{
					//Le sumo 1 para evitar que me genere un 0
					int rndPosMut = rnd.nextInt(28)+1;
					System.out.println(rndPosMut);
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
			
			for(int i=0;i<10;i++)
			{
				//En la primera iteracion tengo solo las 2 primeras posiciones cargadas, el resto null
				//if(hijos[i]!=null){
					numeros[i]=Integer.parseInt(hijos[i],2);
				//}
			}
				
		}
		try {
	        BufferedWriter out = new BufferedWriter(new FileWriter("C:\\Users\\nicolas\\desktop\\minimo.txt"));
	            for (int i = 0; i < 1000; i++) {
	            	
	            	String numero ="0,".concat((Double.toString(minObj[i])).substring(2, Double.toString(minObj[i]).length()));
	                out.write(numero + " \n");
	            }
	            out.close();
	        } catch (IOException e) {
	        	e.printStackTrace();
	        }
		try {
	        BufferedWriter out = new BufferedWriter(new FileWriter("C:\\Users\\nicolas\\desktop\\promedio.txt"));
	            for (int i = 0; i < 1000; i++) {
	            	
	            	String numero ="0,".concat((Double.toString(promObj[i])).substring(2, Double.toString(promObj[i]).length()));
	                out.write(numero + " \n");
	            }
	            out.close();
	        } catch (IOException e) {
	        	e.printStackTrace();
	        }
		try {
	        BufferedWriter out = new BufferedWriter(new FileWriter("C:\\Users\\nicolas\\desktop\\maximo.txt"));
	            for (int i = 0; i < 1000; i++) {
	            	
	            	String numero ="0,".concat((Double.toString(maxObj[i])).substring(2, Double.toString(maxObj[i]).length()));
	                out.write(numero + " \n");
	            }
	            out.close();
	        } catch (IOException e) {
	        	e.printStackTrace();
	        }
		//Muestro evaluacion de proyecto
		for(int z=0;z<20;z++)
		{	
			 
			System.out.println("Interaccion N°: "+(z+1));
			System.out.println("      Funcion Objetivo");
			System.out.println("Minimo: "+minObj[z]);
			System.out.println("promedio: "+promObj[z]);
			System.out.println("maximo: "+maxObj[z]);
		}
	}
	
}
