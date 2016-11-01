#16 cromosomas

#imports
from random import randint

#auxiliares
aux = [];


#funciones

def poblacionInicial(caso):
        for i in xrange(9):
            for j in xrange(9):
                if(caso[i][j] == 0):
                    caso[i][j] = randint(0,9)
        return(caso)

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
objetivos=[]


#programa Principal caso 1

for i in xrange(16):
    poblacion.append(poblacionInicial(caso1))
    objetivos.append(objetivo(identPoblacion[i]))

for i in xrange(16):
    fitnessP.append(objetivos[i]/(float)sum(objetivos))
#genere 


print(objetivo(caso1))
print(objetivo(caso2))




