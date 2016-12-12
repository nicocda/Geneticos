#imports
import random
from random import randint
import copy
import matplotlib.pyplot as plt



#auxiliares
aux = [];


#funciones
def imprimir(individuo):
    print("===============================")
    for i in xrange(0,9):
        print(individuo[i])
    print("objetivo: "+str(objetivo(individuo)))
    print("===============================")

def poblacionInicial(opc, indiv):
    ind = []
    for i in xrange(9):
        fila = []
        for j in xrange(9):
            if(indiv[i][j] == 0):
                rnd = randint(1,9)
                while(rnd in fila):
                    rnd = randint(1,9)
                fila.append(rnd)    
            else:
                fila.append(indiv[i][j])
        ind.append(fila)
    return(ind)

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
    #solo descuenta una vez por numero, entonces si esta repetido no descuenta
    #es una forma de contar repetidos
    for i in xrange(1,10):
        if(i not in elemento):
            cont = cont+1
    return(cont)


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



#programa Principal
poblacion = []
poblacionInicio = []
poblacionNuevoCiclo = []
mejorIndividuo = []
caso =[]
resultadoInd = []
resultadoObj = []

opc=int(raw_input('Ingrese el caso Deseado ( 1 o 2 )\n'))
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
    
iteraciones=int(raw_input('Ingrese cantidad iteraciones: \n'))    
for i in xrange(16):
    poblacionInicio.append(poblacionInicial(opc,caso))

poblacion = poblacionInicio
mejorObjetivo=objetivo(poblacionInicio[0])
mejorIndividuo=poblacionInicio[0]
for p in xrange(iteraciones):
    fitness= []
    objetivos=[]
    tot= 0
    for i in xrange(16):
        tot = tot + 9*9*9-objetivo(poblacion[i])
    for i in xrange(16):
        tot = float(tot)
        num = (9*9*9-objetivo(poblacion[i]))/tot
        fitness.append(num)
    #generamos objetivos y fitness


    #elitismo
    listaOrdenada = []
    for i in xrange(16):
        for j in xrange(14,i+1,-1):
            if(objetivo(poblacion[j]) > objetivo(poblacion[j+1])):
                aux = copy.deepcopy(poblacion[j])
                poblacion[j] =  copy.deepcopy(poblacion[j+1])
                poblacion[j+1] = copy.deepcopy(aux)
    for i in xrange(4):
        poblacionNuevoCiclo.append(poblacion[i])



    #tiro la ruleta 8 veces, por pares
    for o in xrange(8):
            #sumFitness es la posicion de la ruleta
        sumFitness = 0
        tirada1 = random.random()
        tirada2 = random.random()
        for n in xrange(16):
            if((tirada1 > sumFitness) and (tirada1 <= (sumFitness + fitness[n]))):
                elegido1 = n
            if((tirada2 > sumFitness) and (tirada2 <= (sumFitness + fitness[n]))):
                elegido2 = n
            sumFitness = sumFitness + fitness[n]
            
        padre1 = copy.deepcopy(poblacion[elegido1])   #le asigno el indice que fue seleccionado al azar, el cual hace corresponder su cromosoma
        padre2 = copy.deepcopy(poblacion[elegido2])
        hijo2 = copy.deepcopy(padre2)
        hijo1 = []
        hijo1 = copy.deepcopy(padre1) 
        crossRandom = random.random()  #genero un nro random para el cross [0,1]
        if(crossRandom<= 0.9):
                   #aplico crossover
            #Compara cada subCuadrado de cada padre, y el mejor se guarda en  hijo 1 
            for z in xrange(0,7,3):
                for y in xrange(0,7,3):
                    cant1 = contar(getSubCuadrado(padre1,y,z))
                    cant2 = contar(getSubCuadrado(padre2,y,z))
                    if(cant1>cant2):
                        for i in xrange(z,z+3):
                            for j in xrange(y,y+3):
                                hijo1[i][j] = padre1[i][j]
                    else:
                        for i in xrange(z,z+3):
                            for j in xrange(y,y+3):
                                hijo1[i][j] =padre2[i][j]
            #Compara cada fila de cada padre y la mejor la guarda en hijo2
            hijo2 = []
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
            if(caso[fila][posx] == 0 and caso[fila][posy] == 0):
                aux = hijo1[fila][posx]
                hijo1[fila][posx] = hijo1[fila][posy]
                hijo1[fila][posy] = aux
        mutRandom = random.random()
        if(mutRandom<=0.1):
            fila = randint(0,8)
            posx = randint(0,8)
            posy = randint(0,8)
            if(caso[fila][posx] == 0 and caso[fila][posy] == 0):
                aux = hijo2[fila][posx]
                hijo2[fila][posx] = hijo2[fila][posy]
                hijo2[fila][posy] = aux
        #mutacion columna
        mutRandom = random.random()
        if(mutRandom<=0.3):
            columna = randint(0,8)
            posx = randint(0,8)
            posy = randint(0,8)
            if(caso[posx][columna] ==0 and caso[posy][columna] ==0):
                aux = hijo1[posx][columna]
                hijo1[posx][columna] = hijo1[posy][columna]
                hijo1[posy][columna] = aux
        mutRandom = random.random()
        if(mutRandom<=0.3):
            columna = randint(0,8)
            posx = randint(0,8)
            posy = randint(0,8)
            if(caso[posx][columna] ==0 and caso[posy][columna] ==0):
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
            if(caso[subCuadradoX+posx1][subCuadradoY+posy1] == 0 and caso[subCuadradoX+posx2][subCuadradoY+posy2] ==0):
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
            if(caso[subCuadradoX+posx1][subCuadradoY+posy1] ==0 and caso[subCuadradoX+posx2][subCuadradoY+posy2] ==0):
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
            if(caso[posx][posy] ==0):
                hijo1[posx][posy] = nuevoNumero
        mutRandom = random.random()
        if(mutRandom<=0.3):
            posx = randint(0,8)
            posy = randint(0,8)
            nuevoNumero = randint(1,9)
            if(caso[posx][posy] ==0):
                hijo2[posx][posy] = nuevoNumero
        poblacionNuevoCiclo.append(hijo1)
        poblacionNuevoCiclo.append(hijo2)

    poblacion = poblacionNuevoCiclo
    poblacionNuevoCiclo = []
    posPeorObj = -1
    peorObjetivo = 0 
    #aca busco el peor de todos
    for i in xrange(16):
        if(objetivo(poblacion[i])>= peorObjetivo):
            peorObjetivo = objetivo(poblacion[i])
            posPeorObj = i
    #aca busco el mejor de todos
    cambio = 0
    mejorObjetivoRepeticion = 9*9*9 #lo maximo
    for i in xrange(16):
        if(objetivo(poblacion[i]) < mejorObjetivo):
            mejorObjetivo=objetivo(poblacion[i])
            mejorIndividuo = copy.deepcopy(poblacion[i])
            cambio = 1
        if(objetivo(poblacion[i]) < mejorObjetivoRepeticion):
            mejorObjetivoRepeticion=objetivo(poblacion[i])
            
    #imprimo el mejor individuo de cada repeticion
    #imprimir(mejorIndividuo)
    resultadoInd.append(mejorIndividuo)
    resultadoObj.append(mejorObjetivoRepeticion)
    if(cambio == 0):
        poblacion[posPeorObj] = copy.deepcopy(mejorIndividuo)
    if(mejorObjetivo == 0):
        break;

posicionMax = min(xrange(len(resultadoObj)), key = lambda x: resultadoObj[x])

plt.plot(resultadoObj)
plt.show()

for i in xrange(9):
        print(resultadoInd[posicionMax][i])

print(resultadoObj[posicionMax])


#for i in xrange(16):
  #  imprimir(poblacion[i])
'''nuevaPoblacionBin.append(hijo1) #agrego hijos a la nueva poblacion
nuevaPoblacionBin.append(hijo2)'''
