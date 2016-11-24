'''
Created on 24 nov. 2016

@author: nicolas
'''

#16 cromosomas

#imports
import random
from random import randint


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
def imprimir(individuo):
        print("===============================")
        for i in xrange(0,9):
                print(individuo[i])
        print("objetivo: "+str(objetivo(individuo)))
        print("===============================")

def poblacionInicial(opc):
        caso = []
        if(opc==1):
                caso.append([0,2,4,0,0,7,0,0,0])
                caso.append([6,0,0,0,0,0,0,0,0])
                caso.append([0,0,3,6,8,0,4,1,5])
                caso.append([4,3,1,0,0,5,0,0,0])
                caso.append([5,0,0,0,0,0,0,3,2])
                caso.append([7,9,0,0,0,0,0,6,0])
                caso.append([2,0,9,7,1,0,8,0,0])
                caso.append([0,4,0,0,9,3,0,0,0])
                caso.append([3,1,0,0,0,4,7,5,0])
        else:
                caso.append([0,0,0,0,3,0,9,0,1])
                caso.append([7,0,1,0,0,0,0,0,0])
                caso.append([0,0,0,0,4,0,0,8,0])
                caso.append([0,9,0,7,0,2,0,0,0])
                caso.append([0,0,0,8,0,0,6,0,0])
                caso.append([0,3,0,0,6,0,0,0,5])
                caso.append([1,6,8,0,0,4,0,9,0])
                caso.append([0,0,0,9,0,0,0,7,0])
                caso.append([0,0,4,0,0,0,0,0,0])
        for i in xrange(9):
            for j in xrange(9):
                if(caso[i][j] == 0):
                        caso[i][j] = randint(1,9)                
        return(caso)

def objetivo(ide):
    #la funcion contar devuelve la cantidad de numeros faltantes de cada (fila|columna|subcuadrado)
    contTablero=0
    for i in xrange(9):
        contTablero = contTablero + contar(ide[i])
#z es numero de columna, i es la fila del tablero
    for z in xrange(9):
        columna = []
        for i in xrange(9):
                columna.append(ide[i][z])
        contTablero = contTablero + contar(columna)
#z es numero de columna, y es el numero de fila
#xrange(0,7,3): va de 0 a 7 aumentando de a 3 posiciones (i=i+3)        
    for z in xrange(0,7,3):
        for y in xrange(0,7,3):
            #getSubCuadrado obtiene cada subCuadrado
            contTablero = contTablero + contar(getSubCuadrado(ide,y,z))
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
poblacionInicio = []
poblacionNuevoCiclo = []
mejorIndividuo = []

opc=int(raw_input('Ingrese el caso Deseado ( 1 o 2)'))
for i in xrange(16):
    poblacionInicio.append(poblacionInicial(opc))

poblacion = poblacionInicio
mejorObjetivo=objetivo(poblacionInicio[0])
mejorIndividuo=poblacionInicio[0]
for j in xrange(100):
        for i in xrange(16):
                objetivos.append(objetivo(poblacion[i]))
                
        for i in xrange(16):
            num = objetivos[i]/float(sum(objetivos))
            fitness.append(num)
        #generamos objetivos y fitness


        #tiro la ruleta 8 veces, por pares
        for i in xrange(8): 
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
            hijo1 = poblacion[elegido1]
            hijo2 = poblacion[elegido2]
            crossRandom = random.random()  #genero un nro random para el cross [0,1]
            if(crossRandom<= 0.9):        #aplico crossover
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
        #mutacion Fila
        mutRandom = random.random()
        if(mutRandom<=0.1):
            fila = randint(0,8)
            posx = randint(0,8)
            posy = randint(0,8)
            aux = hijo1[fila][posx]
            hijo1[fila][posx] = hijo1[fila][posy]
            hijo1[fila][posy] = aux
        mutRandom = random.random()
        if(mutRandom<=0.1):
            fila = randint(0,8)
            posx = randint(0,8)
            posy = randint(0,8)
            aux = hijo2[fila][posx]
            hijo2[fila][posx] = hijo2[fila][posy]
            hijo2[fila][posy] = aux
        #mutacion columna           
        mutRandom = random.random()
        if(mutRandom<=0.3):
            columna = randint(0,8)
            posx = randint(0,8)
            posy = randint(0,8)
            aux = hijo1[posx][columna]
            hijo1[posx][columna] = hijo1[posy][columna]
            hijo1[posy][columna] = aux
        mutRandom = random.random()
        if(mutRandom<=0.3):
            columna = randint(0,8)
            posx = randint(0,8)
            posy = randint(0,8)
            aux = hijo2[posx][columna]
            hijo2[posx][columna] = hijo2[posy][columna]
            hijo2[posy][columna] = aux
        #mutacion subCuadrado
        mutRandom = random.random()
        if(mutRandom<=0.3):
            subCuadradoX = randint(0,2)*3 #(0=>0; 1=>3; 2=>6)
            subCuadradoY = randint(0,2)*3 #(0=>0; 1=>3; 2=>6)
            #posx1 y las demas son posiciones relativas dentro del cuadrado
            posx1 = randint(0,2)
            posy1 = randint(0,2)
            posx2 = randint(0,2)
            posy2 = randint(0,2)
            #como son relativas, para llegar a la absoluta tengo que sumarle el cuadrado
            aux = hijo1[subCuadradoX+posx1][subCuadradoY+posy1]
            hijo1[subCuadradoX+posx1][subCuadradoY+posy1] = hijo1[subCuadradoX+posx2][subCuadradoY+posy2]
            hijo1[subCuadradoX+posx2][subCuadradoY+posy2] = aux
        mutRandom = random.random()
        if(mutRandom<=0.3):
            subCuadradoX = randint(0,2)*3 #(0=>0; 1=>3; 2=>6)
            subCuadradoY = randint(0,2)*3 #(0=>0; 1=>3; 2=>6)
            #posx1 y las demas son posiciones relativas dentro del cuadrado
            posx1 = randint(0,2)
            posy1 = randint(0,2)
            posx2 = randint(0,2)
            posy2 = randint(0,2)
            #como son relativas, para llegar a la absoluta tengo que sumarle el cuadrado
            aux = hijo2[subCuadradoX+posx1][subCuadradoY+posy1]
            hijo2[subCuadradoX+posx1][subCuadradoY+posy1] = hijo2[subCuadradoX+posx2][subCuadradoY+posy2]
            hijo2[subCuadradoX+posx2][subCuadradoY+posy2] = aux
        #mutacion de un numero del individuo
        mutRandom = random.random()
        if(mutRandom<=0.3):
            posx = randint(0,8)
            posy = randint(0,8)
            nuevoNumero = randint(1,9) #este es del 1 al 9 porque son los valores
            hijo1[posx][posy] = nuevoNumero
        mutRandom = random.random()
        if(mutRandom<=0.3):
            posx = randint(0,8)
            posy = randint(0,8)
            nuevoNumero = randint(1,9)
            hijo2[posx][posy] = nuevoNumero
        poblacionNuevoCiclo.append(hijo1)
        poblacionNuevoCiclo.append(hijo2)
        imprimir(poblacionNuevoCiclo[1])
        poblacion = poblacionNuevoCiclo
        poblacionNuevoCiclo = []
        posPeorObj = -1
        peorObjetivo = 9*9*9+1 #lo maximo
        #aca busco el peor de todos
        for i in xrange(16):
            if(objetivo(poblacion[i])<= peorObjetivo):
                peorObjetivo = objetivo(poblacion[i])
                posPeorObj = i
        #aca busco el mejor de todos
        cambio = 0
        for i in xrange(16):
            if(objetivo(poblacion[i]) > mejorObjetivo):
                mejorObjetivo=objetivo(poblacion[i])
                mejorIndividuo = poblacion[i]
                cambio = 1
        if(cambio == 0):
                poblacion[posPeorObj] = mejorIndividuo
        if(mejorObjetivo == 9*9*9):
                break;   
'''nuevaPoblacionBin.append(hijo1) #agrego hijos a la nueva poblacion
nuevaPoblacionBin.append(hijo2)'''



