import java.util.Random;
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.math.*;
public class main {

	public static void main(String[] args) 
	{
	
		//Definiciones
		
		String[] inicial = new String[10];
		int[] numeros = new int[10];
		String[] hijos = new String[10];
		double[] objetivo = new double[10];
		double[] fitness = new double[10];
		double[] promObj20 = new double[20];
		double[] maxObj20 = new double[20];
		double[] minObj20 = new double[20];
		double[] promObj100 = new double[100];
		double[] maxObj100 = new double[100];
		double[] minObj100 = new double[100];
		double[] promObj1000 = new double[1000];
		double[] maxObj1000 = new double[1000];
		double[] minObj1000 = new double[1000];
		Random rnd = new Random();
	
	
		
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
			
		//primer genetico de 20 pasadas
		for(int i=0;i<10;i++)
		{
			numeros[i]=Integer.parseInt(inicial[i],2);
		}
		for(int z=0;z<20;z++)
		{
			//Obtengo minimo, maximo y suma de Funcion Objetivo
			double sumaObj = 0;
			maxObj20[z] = 0;
			minObj20[z] = 1;
			for(int i=0;i<10;i++)
			{
				objetivo[i]= Math.pow((double)numeros[i]/coef, 2);
				if(objetivo[i]>maxObj20[z]) maxObj20[z]=objetivo[i];
				if(objetivo[i]<minObj20[z]) minObj20[z]=objetivo[i];
				sumaObj=sumaObj+objetivo[i];
			}
			
			//Obtengo Funcion Fitness
			for(int i=0;i<10;i++)
			{
				fitness[i]=objetivo[i]/sumaObj;
				
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
					if((rndRuleta>(sumfitness-fitness[i]) && (rndRuleta<sumfitness) ))
					{
						//guardamos el indice del numero que salio en un arreglo de indices llamado elegido
						 elegido[j]=i;
						 break;
					} else
					{
						sumfitness = sumfitness+fitness[i+1];
					}
				}
			}
			
			//CrossOver y Mutacion (se hace 5 veces, para los 5 pares) ( por eso aumenta de a 2)
			for(int h=0;h<10;h=h+2)
			{
				//guardo los cromosomas en un auxiliar
				String aux1=Integer.toBinaryString(numeros[elegido[h]]);
				String aux2=Integer.toBinaryString(numeros[elegido[h+1]]);
				//Mantengo el tamaño de palabra de 30
				//(al trabajar con numeros en decimal, si el numero binario empieza con 0, cuando lo pasasamos a decimal,
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
					//la posicion la generamos asi para evitar que salga un extremo, 
					//porque si sale un extremo tira error por el rndPostMut+-1
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
				//si el numero random es menor que 0.05 mutamos
				double rndMut2 = rnd.nextDouble();
				if(rndMut2<0.05)
				{
					//la posicion la generamos asi para evitar que salga un extremo, 
					//porque si sale un extremo tira error por el rndPostMut+-1
					int rndPosMut = rnd.nextInt(28)+1;
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
				
					numeros[i]=Integer.parseInt(hijos[i],2);
				
			}
				
		}
		//termina primer genetico de 20 repeticiones 
		
		//guardamos los numeros en txt para poder generar las graficas en excel
		try {
	        BufferedWriter out = new BufferedWriter(new FileWriter("C:\\Users\\nicolas\\desktop\\Geneticos\\minimo20.txt"));
	            for (int i = 0; i < 20; i++) {
	            	
	            	String numero ="0,".concat((Double.toString(minObj20[i])).substring(2, Double.toString(minObj20[i]).length()));
	                out.write(numero + " \n");
	            }
	            out.close();
	        } catch (IOException e) {
	        	e.printStackTrace();
	        }
		try {
	        BufferedWriter out = new BufferedWriter(new FileWriter("C:\\Users\\nicolas\\desktop\\Geneticos\\promedio20.txt"));
	            for (int i = 0; i < 20; i++) {
	            	
	            	String numero ="0,".concat((Double.toString(promObj20[i])).substring(2, Double.toString(promObj20[i]).length()));
	                out.write(numero + " \n");
	            }
	            out.close();
	        } catch (IOException e) {
	        	e.printStackTrace();
	        }
		try {
	        BufferedWriter out = new BufferedWriter(new FileWriter("C:\\Users\\nicolas\\desktop\\Geneticos\\maximo20.txt"));
	            for (int i = 0; i < 20; i++) {
	            	
	            	String numero ="0,".concat((Double.toString(maxObj20[i])).substring(2, Double.toString(maxObj20[i]).length()));
	                out.write(numero + " \n");
	            }
	            out.close();
	        } catch (IOException e) {
	        	e.printStackTrace();
	        }
		
		
		//comienza para 100 iteraciones
				for(int i=0;i<10;i++)
				{
					numeros[i]=Integer.parseInt(inicial[i],2);
				}
				for(int z=0;z<100;z++)
				{
					//Obtengo minimo, maximo y suma de Funcion Objetivo
					double sumaObj = 0;
					maxObj100[z] = 0;
					minObj100[z] = 1;
					for(int i=0;i<10;i++)
					{
						objetivo[i]= Math.pow((double)numeros[i]/coef, 2);
						if(objetivo[i]>maxObj100[z]) maxObj100[z]=objetivo[i];
						if(objetivo[i]<minObj100[z]) minObj100[z]=objetivo[i];
						sumaObj=sumaObj+objetivo[i];
					}
					
					//Obtengo Funcion Fitness
					for(int i=0;i<10;i++)
					{
						fitness[i]=objetivo[i]/sumaObj;
						
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
							if((rndRuleta>(sumfitness-fitness[i]) && (rndRuleta<sumfitness) ))
							{
								//guardamos el indice del numero que salio en un arreglo de indices llamado elegido
								 elegido[j]=i;
								 break;
							} else
							{
								sumfitness = sumfitness+fitness[i+1];
							}
						}
					}
					
					//CrossOver y Mutacion (se hace 5 veces, para los 5 pares) ( por eso aumenta de a 2)
					for(int h=0;h<10;h=h+2)
					{
						//guardo los cromosomas en un auxiliar
						String aux1=Integer.toBinaryString(numeros[elegido[h]]);
						String aux2=Integer.toBinaryString(numeros[elegido[h+1]]);
						//Mantengo el tamaño de palabra de 30
						//(al trabajar con numeros en decimal, si el numero binario empieza con 0, cuando lo pasasamos a decimal,
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
							//la posicion la generamos asi para evitar que salga un extremo, 
							//porque si sale un extremo tira error por el rndPostMut+-1
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
						//si el numero random es menor que 0.05 mutamos
						double rndMut2 = rnd.nextDouble();
						if(rndMut2<0.05)
						{
							//la posicion la generamos asi para evitar que salga un extremo, 
							//porque si sale un extremo tira error por el rndPostMut+-1
							int rndPosMut = rnd.nextInt(28)+1;
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
						
							numeros[i]=Integer.parseInt(hijos[i],2);
						
					}
						
				}
				//termina primer genetico de 20 repeticiones 
				
				//guardamos los numeros en txt para poder generar las graficas en excel
				try {
			        BufferedWriter out = new BufferedWriter(new FileWriter("C:\\Users\\nicolas\\desktop\\Geneticos\\minimo100.txt"));
			            for (int i = 0; i < 100; i++) {
			            	
			            	String numero ="0,".concat((Double.toString(minObj100[i])).substring(2, Double.toString(minObj100[i]).length()));
			                out.write(numero + " \n");
			            }
			            out.close();
			        } catch (IOException e) {
			        	e.printStackTrace();
			        }
				try {
			        BufferedWriter out = new BufferedWriter(new FileWriter("C:\\Users\\nicolas\\desktop\\Geneticos\\promedio100.txt"));
			            for (int i = 0; i < 100; i++) {
			            	
			            	String numero ="0,".concat((Double.toString(promObj100[i])).substring(2, Double.toString(promObj100[i]).length()));
			                out.write(numero + " \n");
			            }
			            out.close();
			        } catch (IOException e) {
			        	e.printStackTrace();
			        }
				try {
			        BufferedWriter out = new BufferedWriter(new FileWriter("C:\\Users\\nicolas\\desktop\\Geneticos\\maximo100.txt"));
			            for (int i = 0; i < 100; i++) {
			            	
			            	String numero ="0,".concat((Double.toString(maxObj100[i])).substring(2, Double.toString(maxObj100[i]).length()));
			                out.write(numero + " \n");
			            }
			            out.close();
			        } catch (IOException e) {
			        	e.printStackTrace();
			        }
				//termina para 100 iteraciones
				
				//empieza para 1000 iteraciones
				for(int i=0;i<10;i++)
				{
					numeros[i]=Integer.parseInt(inicial[i],2);
				}
				for(int z=0;z<1000;z++)
				{
					//Obtengo minimo, maximo y suma de Funcion Objetivo
					double sumaObj = 0;
					maxObj1000[z] = 0;
					minObj1000[z] = 1;
					for(int i=0;i<10;i++)
					{
						objetivo[i]= Math.pow((double)numeros[i]/coef, 2);
						if(objetivo[i]>maxObj1000[z]) maxObj1000[z]=objetivo[i];
						if(objetivo[i]<minObj1000[z]) minObj1000[z]=objetivo[i];
						sumaObj=sumaObj+objetivo[i];
					}
					
					//Obtengo Funcion Fitness
					for(int i=0;i<10;i++)
					{
						fitness[i]=objetivo[i]/sumaObj;
						
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
							if((rndRuleta>(sumfitness-fitness[i]) && (rndRuleta<sumfitness) ))
							{
								//guardamos el indice del numero que salio en un arreglo de indices llamado elegido
								 elegido[j]=i;
								 break;
							} else
							{
								sumfitness = sumfitness+fitness[i+1];
							}
						}
					}
					
					//CrossOver y Mutacion (se hace 5 veces, para los 5 pares) ( por eso aumenta de a 2)
					for(int h=0;h<10;h=h+2)
					{
						//guardo los cromosomas en un auxiliar
						String aux1=Integer.toBinaryString(numeros[elegido[h]]);
						String aux2=Integer.toBinaryString(numeros[elegido[h+1]]);
						//Mantengo el tamaño de palabra de 30
						//(al trabajar con numeros en decimal, si el numero binario empieza con 0, cuando lo pasasamos a decimal,
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
							//la posicion la generamos asi para evitar que salga un extremo, 
							//porque si sale un extremo tira error por el rndPostMut+-1
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
						//si el numero random es menor que 0.05 mutamos
						double rndMut2 = rnd.nextDouble();
						if(rndMut2<0.05)
						{
							//la posicion la generamos asi para evitar que salga un extremo, 
							//porque si sale un extremo tira error por el rndPostMut+-1
							int rndPosMut = rnd.nextInt(28)+1;
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
						
							numeros[i]=Integer.parseInt(hijos[i],2);
						
					}
						
				}
				//termina primer genetico de 20 repeticiones 
				
				//guardamos los numeros en txt para poder generar las graficas en excel
				try {
			        BufferedWriter out = new BufferedWriter(new FileWriter("C:\\Users\\nicolas\\desktop\\Geneticos\\minimo1000.txt"));
			            for (int i = 0; i < 1000; i++) {
			            	
			            	String numero ="0,".concat((Double.toString(minObj1000[i])).substring(2, Double.toString(minObj1000[i]).length()));
			                out.write(numero + " \n");
			            }
			            out.close();
			        } catch (IOException e) {
			        	e.printStackTrace();
			        }
				try {
			        BufferedWriter out = new BufferedWriter(new FileWriter("C:\\Users\\nicolas\\desktop\\Geneticos\\promedio1000.txt"));
			            for (int i = 0; i < 1000; i++) {
			            	
			            	String numero ="0,".concat((Double.toString(promObj1000[i])).substring(2, Double.toString(promObj1000[i]).length()));
			                out.write(numero + " \n");
			            }
			            out.close();
			        } catch (IOException e) {
			        	e.printStackTrace();
			        }
				try {
			        BufferedWriter out = new BufferedWriter(new FileWriter("C:\\Users\\nicolas\\desktop\\Geneticos\\maximo1000.txt"));
			            for (int i = 0; i < 1000; i++) {
			            	
			            	String numero ="0,".concat((Double.toString(maxObj1000[i])).substring(2, Double.toString(maxObj1000[i]).length()));
			                out.write(numero + " \n");
			            }
			            out.close();
			        } catch (IOException e) {
			        	e.printStackTrace();
			        }
				
		
	}
	
}
