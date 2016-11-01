
#16 cromosomas

#imports
from random import *


#constantes
'''
caso1 = []
caso1.append([0,2,4,0,0,7,0,0,0])
caso1.append([6,0,0,0,0,0,0,0,0])
caso1.append([0,0,3,6,8,0,4,1,5])
caso1.append([4,3,1,0,0,5,0,0,0])
caso1.append([5,0,0,0,0,0,0,3,2])
caso1.append([7,9,0,0,0,0,0,6,0])
caso1.append([2,0,9,7,1,0,8,0,0])
caso1.append([0,4,0,0,9,3,0,0,0])
caso1.append([3,1,0,0,0,4,7,5,0])

caso2 = []

caso2.append([0,0,0,0,3,0,9,0,1])
caso2.append([7,0,1,0,0,0,0,0,0])
caso2.append([0,0,0,0,4,0,0,8,0])
caso2.append([0,9,0,7,0,2,0,0,0])
caso2.append([0,0,0,8,0,0,6,0,0])
caso2.append([0,3,0,0,6,0,0,0,5])
caso2.append([1,6,8,0,0,4,0,9,0])
caso2.append([0,0,0,9,0,0,0,7,0])
caso2.append([0,0,4,0,0,0,0,0,0])
'''



#auxiliares
aux = [];


#funciones

def poblacionInicial():
        caso1 = []
        caso1.append([0,2,4,0,0,7,0,0,0])
        caso1.append([6,0,0,0,0,0,0,0,0])
        caso1.append([0,0,3,6,8,0,4,1,5])
        caso1.append([4,3,1,0,0,5,0,0,0])
        caso1.append([5,0,0,0,0,0,0,3,2])
        caso1.append([7,9,0,0,0,0,0,6,0])
        caso1.append([2,0,9,7,1,0,8,0,0])
        caso1.append([0,4,0,0,9,3,0,0,0])
        caso1.append([3,1,0,0,0,4,7,5,0])
        for i in xrange(9):
            for j in xrange(9):
                if(caso1[i][j] == 0):
                        caso1[i][j] = randint(0,9)                
        return(caso1)

def objetivo(ide):
    #la funcion contar devuelve la cantidad de numeros distintos de cada (fila|columna|subcuadrado)
    contTablero=0
    for i in xrange(9):
        contTablero = contTablero + contar(ide[i])
#z es numero de columna, i es la fila del tablero
    for z in xrange(9):
        columna = []
        for i in xrange(9):
                columna.append(ide[i][z])
        conTablero = contTablero + contar(columna)
#z es numero de columna, y es el numero de fila
    for z in xrange(0,7,3):
        for y in xrange(0,7,3):
            #getSubCuadrado obtiene cada subCuadrado
            ContTablero = contTablero + contar(getSubCuadrado(ide,y,z))
    return(contTablero)
        

def contar(elemento):
    cont = 0
    for i in xrange(9):
        if(i in elemento):
            cont = cont+1
    return(cont)

     
     
def fitness(poblacion):
    tot = 0
    for i in xrange(16):
        #poblacion[i] es cada tablero
        tot = tot + contar(poblacion[i])
    return(tot)


def getSubCuadrado(indv, fila, columna):
    #scc = SubCuadradoColumna; scf = SubCuadradoFila
    subCuadrado = []
    scc=0
    scf=0
    if(fila<=2):
        scf = 0
        if(fila<=5):
            scf= 3
        else:
            scf=6
    if(columna<=2):
        scc = 0
        if(columna<=5):
            scc= 3
        else:
            scc=6
    for i in xrange(scf,scf+3):
        for j in xrange(scc,scc+3):
            subCuadrado.append(indv[i][j])
    return subCuadrado
        

    



#programa Principal caso 1
poblacion = []
fitness= []
objetivos=[]
for i in xrange(16):
    poblacion.append(poblacionInicial())
    objetivos.append(objetivo(poblacion[i]))

for i in xrange(16):
    num = objetivos[i]/float(sum(objetivos))
    fitness.append(num)
#generamos objetivos y fitness


   
for i in xrange(8): #tiro la ruleta 8 veces, por pares
        #sumFitness es la posicion de la ruleta
	sumFitness = 0
	tirada1 = random.random()
	
	for n in xrange(16):
	    if((tirada1 > sumFitness) & (tirada1 < (sumFitness + fitness[n]))):
		elegido1 = n
		break
	    else:
		sumFitness = sumFitness + fitness[n]
	
	sumFitness = 0
	tirada2 = random.random()
	
	for n in xrange(16):
	    if((tirada2 > sumFitness) & (tirada2 < (sumFitness + fitness[n]))):
		elegido2 = n
		break
	    else:
		sumFitness = sumFitness + fitness[n]   

	padre1 = poblacion[elegido1]    #le asigno el indice que fue seleccionado al azar, el cual hace corresponder su cromosoma
	padre2 = poblacion[elegido2]

	
	crossRandom = random.random()  #genero un nro random para el cross [0,1]

	if crossRandom <= 0.9:        #aplico crossover
        #Compara cada subCuadrado de cada padre, y el mejor se guarda en  hijo 1 (No creo que ande. REVISAR)
	    for z in xrange(0,7,3):
                for y in xrange(0,7,3):
                  cant1 = contar(getSubCuadrado(padre1,y,z))
                  cant2 = contar(getSubCuadrado(padre2,y,z))
                  if(cant1>=cant2):
                         for i in xrange(z,z+3):
                                for j in xrange(y,y+3):
                                   hijo1[y][z] =padre1[i][j]
                  else:
                          for i in xrange(z,z+3):
                                for j in xrange(y,y+3):
                                   hijo1[y][z] =padre2[i][j]
        #Compara cada fila de cada padre y la mejor la guarda en hijo2
           for i in xrange(9):
               cant1 = contar(padre1[i])
               cant2 = contar(padre2[i])
               if(cant1>=cant2):
                   hijo2.append(padre1[i])
               else:
                   hijo2.append(padre2[i])
	else:
        #si no hay crossover, los hijos son iguales a los padres
	    hijo1 = padre1
	    hijo2 = padre2
	    
	###################
	#
	#
	#
	#
	#
	#INSERT MUTACION HERE
	#
	#
	#
	#
	#######################

	'''nuevaPoblacionBin.append(hijo1) #agrego hijos a la nueva poblacion
	nuevaPoblacionBin.append(hijo2)'''



