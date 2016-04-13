import java.util.Random;
import java.math.*;
public class main {

	public static void main(String[] args) {
	
		int[][] cromosoma = new int[10][30];
		int[] numeros = new int[10];
		int[] hijos = new int[10];
		double[] objetivo = new double[10];
		double[] fitness = new double[10];
		Random rnd = new Random();
		int coef=(int)Math.pow(2, 30);
		for(int i=0;i<10;i++)
		{
			numeros[i]= rnd.nextInt(coef);
		}
	
			double sumaObj = 0;
			double maxObj = 0;
			for(int i=0;i<10;i++)
			{
				objetivo[i]= Math.pow((double)numeros[i]/coef, 2);
				if(objetivo[i]>maxObj) maxObj=objetivo[i];
				sumaObj=sumaObj+objetivo[i];
			}
			double sumaFit = 0;
			double maxFit = 0;
			for(int i=0;i<10;i++)
			{
				fitness[i]=objetivo[i]/sumaObj;
				if(fitness[i]>maxFit) maxFit=fitness[i];
				sumaFit = sumaFit + fitness[i];
			}
			for(int i=0;i<10;i++)
			{
				System.out.println(i+" "+Integer.toBinaryString(numeros[i])+" "+numeros[i]+" "+objetivo[i]+" "+fitness[i]);
			}
			System.out.println("suma "+sumaObj+" "+sumaFit);
			System.out.println("promedio "+sumaObj/10+" "+sumaFit/10);
			System.out.println("maximo "+maxObj+" "+maxFit);
			
			//RULETA
			int[] elegido = new int[10];
			for(int j=0;j<10;j++)
			{
				double rndRuleta = rnd.nextDouble();
				double sumfitness = fitness[0];
				
				for(int i=0;i<10;i++)
				{
					if(rndRuleta<sumfitness)
					{
						 elegido[j]=i;
					} else
					{
						sumfitness = sumfitness+fitness[i+1];
					}
				}
			}
			for(int h=0;h<10;h=h+2)
			{
				double rndCrossOver = rnd.nextDouble();
				if(rndCrossOver <0.75)
				{
					int rndPosCross = rnd.nextInt(30);
					for(int i=0;i<rndPosCross;i++)
					{
						hijos[h]=Integer.parseInt(Integer.toBinaryString(numeros[elegido[h]]).substring(0, rndPosCross)+Integer.toBinaryString(numeros[elegido[h+1]]).substring(rndPosCross,30));
						hijos[h+1]=Integer.parseInt(Integer.toBinaryString(numeros[elegido[h+1]]).substring(0, rndPosCross)+Integer.toBinaryString(numeros[elegido[h]]).substring(rndPosCross,30));
					}
				}
				double rndMut1 = rnd.nextDouble();
				if(rndMut1<0.05)
				{
					int rndPosMut1 = rnd.nextInt(30);
					//TODO MUTAR EL BIT CORRESPONDIENTE A LA POSICION "rndPosMut1"
				}
				
				
			}
				
		}
	

}
