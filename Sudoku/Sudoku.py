#imports
from random import randint

#funciones
def ident(caso):
    for i in xrange(9):
        identidad.append([])
        for j in xrange(9):
            if(caso[i][j]>0):
                identidad[i].append(1)
            else:
                identidad[i].append(0)
    return(identidad)

def poblacionInicial(caso):
        for i in xrange(9):
            for j in xrange(9):
                if(caso[i][j] == 0):
                    rand = randint(0,9)
                    while(rand in caso[i]):
                        rand = randint(0,9)
                    caso[i][j]=rand
                
        return(caso)

def objetivo(ide):
    cont=0
    for i in xrange(9):
            for j in xrange(9):
               if(ide[i][j] == 1):
                   cont= cont+1
    return(cont)              
    
def fitness(ideP):
    tot = 0
    for i in xrange(16):
        tot = tot + objetivo(ideP[i]) #Guardo la cantidad de unos totales de los 16 individuos de la poblacion
    for k in xrange(16):
        fit = objetivo(ideP[k])/float(tot)
        fitnessP.append(fit)

def fijarNumero(indv, identIndv):
    for i in xrange(9):
            for j in xrange(9):
                bandera = validaColumna(indv, indv[i][j], j)
                bandera2 = validaSubCuadro(indv, indv[i][j], i, j)
                if(bandera & bandera2):
                    identIndv[i][j] = 1
    return(identIndv)

def validaColumna(indv, num, columna):
    cont = 0
    for i in xrange(9):
        if(indv[i][columna] == num):
            cont = cont +1
    if(cont>1):
        bandera = True
    else:
        bandera = False
    return(bandera)

def validaSubCuadro(indv, num, fila, columna):
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
    cont = 0
    for i in xrange(scf,scf+3):
        for j in xrange(scc,scc+3):
            if(indv[i][j]== num):
                cont = cont+1
    if(cont>1):
        bandera = True
    else:
        bandera = False
    return(bandera)
        

    

#constantes

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

identidad = []
poblacion = []
identPoblacion = []
fitnessP= []


#programa Principal

for i in xrange(16):
    poblacion.append(poblacionInicial(caso1))
    identPoblacion.append(ident(caso1))
    objetivo(identPoblacion[i])

for i in xrange(16):
    identPoblacion[i] = fijarNumero(poblacion[i], identPoblacion[i])
fitness(identPoblacion)

print(fitnessP)




