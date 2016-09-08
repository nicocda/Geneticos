from turtle import *
from Tkinter import *
import random
import ctypes
from random import randint, random, shuffle

#bloque def constantes
distancia = []
puntos = []

distancia.append([0,1543,1510,1203,1043,1191,1023,478,940,1040,480,715,1150,1110,790,1155,1050,620,1158,960,1455,2635,3228])
distancia.append([1543,0,99,340,500,960,860,1107,883,1198,1138,930,770,1220,1320,572,1345,1530,2200,2124,2385,3565,4158])
distancia.append([1510,99,0,307,467,948,780,1074,803,1118,1105,897,695,1145,1245,539,1227,1497,2082,2091,2352,3532,4125])
distancia.append([1203,340,307,0,160,936,768,767,791,1106,798,590,338,838,938,232,1005,1190,1860,1784,2045,3225,3818])
distancia.append([1043,500,467,160,0,776,610,607,633,948,638,430,360,810,850,212,977,1030,1567,1624,1885,3065,3658])
distancia.append([1191,960,948,936,776,0,168,713,191,506,744,1043,1136,1543,1463,988,1710,1523,2060,2117,2378,3558,4151])
distancia.append([1023,860,780,765,610,168,0,545,23,338,576,875,970,1420,1295,822,1587,1475,2012,2069,2210,3390,3983])
distancia.append([478,1107,1074,767,607,713,545,0,568,883,31,330,765,830,625,770,885,810,1347,1404,1665,2845,3438])
distancia.append([940,883,803,791,633,191,23,568,0,315,590,898,993,1398,1318,845,1565,1378,1989,2046,2187,3367,3960])
distancia.append([1040,1198,1118,1106,948,506,338,883,315,0,820,1213,1308,1758,1633,1160,1925,1660,2198,2000,2495,3675,4268])
distancia.append([480,1138,1105,798,638,744,576,31,590,820,0,361,796,861,656,801,916,841,1378,1435,1696,2876,3469])
distancia.append([715,930,897,590,430,1043,875,330,898,1213,361,0,435,500,420,440,670,600,1137,1194,1455,3635,3228])
distancia.append([1150,770,695,388,360,1136,970,765,993,1308,796,435,0,450,550,156,617,1035,1472,1629,1890,3070,3663])
distancia.append([1110,1220,1145,838,810,1543,1420,830,1398,1758,861,500,450,0,320,606,167,825,1022,1419,1680,2860,3453])
distancia.append([790,1320,1245,938,850,1463,1295,625,1318,1633,656,420,550,320,0,705,260,505,883,1099,1360,2540,3133])
distancia.append([1145,572,539,232,212,988,822,770,845,1160,801,440,156,606,705,0,773,1040,1588,1634,1895,3075,3668])
distancia.append([1050,1345,1227,1005,977,1710,1587,885,1565,1925,916,670,617,167,260,773,0,765,855,1359,1620,2800,3393])
distancia.append([620,1530,1497,1190,1030,1523,1475,810,1378,1660,841,600,1035,825,505,1040,765,0,537,594,855,2035,2628])
distancia.append([1158,2200,2082,1860,1567,2060,2012,1347,1989,2198,1378,1137,1472,1022,883,1588,855,537,0,660,750,1930,2523])
distancia.append([960,2124,2091,1784,1624,2117,2069,1404,2046,2000,1435,1194,1629,1419,1099,1634,1359,594,660,0,495,1675,2268])
distancia.append([1455,2385,2352,2045,1885,2378,2210,1665,2187,2495,1696,1455,1890,1680,1360,1895,1620,855,750,495,0,1180,1773])
distancia.append([2635,3565,3532,3225,3065,3558,3390,2845,3367,3675,2876,2635,3070,2860,2540,3075,2800,2035,1930,1675,1180,0,593])
distancia.append([3228,4158,4125,3818,3658,4151,3983,3438,3960,4268,3469,3228,3660,3453,3133,3668,3393,2628,2523,2268,1773,593,0])

puntos.append([36,69.5])
puntos.append([-56,239.5])
puntos.append([-57.1,228.5])
puntos.append([-54,194.5])
puntos.append([-44,180.5])
puntos.append([50,206.5])
puntos.append([34,189.5])
puntos.append([9,118.5])
puntos.append([42,187.5])
puntos.append([85,184.5])
puntos.append([14,115.5])
puntos.append([-40,123.5])
puntos.append([-77,150.5])
puntos.append([-101,118.5])
puntos.append([-68,88.5])
puntos.append([-64,171.5])
puntos.append([-103,96.5])
puntos.append([-39,35.5])
puntos.append([-91,-4.5])
puntos.append([-23,-34.5])
puntos.append([-50,-71.5])
puntos.append([-86,-210.5])
puntos.append([-70,-258.5])

#bloque funciones

def capitalInicial():
    print("Lista de ciudades\n"
          " 1- Buenos Aires \n 2- San S. de Jujuy \n 3-Salta \n 4- S.M. de Tucuman\n"
          " 5- Sgo. del Estero \n 6- Formosa \n 7-Resistencia \n 8- Santa Fe\n"
          " 9- Corrientes \n 10- Posadas \n 11- Parana \n 12- Cordoba \n 13- La Rioja \n"
          " 14- San Juan \n 15- San Luis \n 16- Catamarca \n 17- Mendoza \n 18- Santa Rosa \n"
          " 19- Neuquen \n 20- Viedma \n 21- Rawson \n 22- Rio Gallegos \n 23- Ushuaia ")
    ciudadActual = input("Seleccione la ciudad de origen: ")-1
    return menorRecorrido(ciudadActual)

def SinCapitalInicial():
    kilometros = []
    for x in xrange(22):
        recorrido = menorRecorrido(x)
        kms = contarKilometros(recorrido)
        kilometros.append(kms)
    num = min(kilometros)
    index = kilometros.index(num)
    return menorRecorrido(index) 

def geneticos():
    inicial = [[0 for c in range(23)] for y in range(50)]
    auxiliar = [[0 for c in range(23)] for y in range(50)]
    minimosRecorridos = []
    minimasDistancias = []
    f = open('recorrido.txt', 'w')
    #genero poblacion inicial y calculo recorrido total
    total = 0;
    for c in xrange(50):
        for y in xrange(23):
            inicial[c][y] = y
        shuffle(inicial[c])
        total = total + contarKilometros(inicial[c])
    for h in xrange(200):    
        #acumulo los complementos
        totalCompl = 0
        for c in xrange(50):
            totalCompl = totalCompl + (total - contarKilometros(inicial[c]))
        #calculo el fitness de cada individuo
        fitness = []
        for c in xrange(50):
            obj = contarKilometros(inicial[c]) / float(totalCompl)
            fit = 1 - obj
            fitness.append(fit)
        #tiro la ruleta 25 veces, por pares
        for m in xrange(25): 
            sumFitness = 0
            tirada1 = random()
            for n in xrange(50):
                if((tirada1 > sumFitness) & (tirada1 < (sumFitness + fitness[n]))):
                    elegido1 = n
                    break
                else:
                    sumFitness = sumFitness + fitness[n]
            
            sumFitness = 0
            tirada2 = random()
            for n in xrange(50):
                if((tirada2 > sumFitness) & (tirada2 < (sumFitness + fitness[n]))):
                    elegido2 = n
                    break
                else:
                    sumFitness = sumFitness + fitness[n]
            crom1 = inicial[elegido1]
            crom2 = inicial[elegido2]
            #crossOver
            rnd = random()
            if(rnd < 0.75):
                estan = []
                estan.append(crom1[0])
                comparador = crom2[0]
                i=0
                while(comparador != crom1[0]):  
                    if(comparador is not estan):
                        if(comparador == crom1[i]):
                            estan.append(crom1[i])
                            comparador = crom2[i] 
                    if(i>=22):
                        i=0
                    else:
                        i=i+1
                
                for z in xrange(23):
                    
                    if(crom1[z] is not estan):
                        aux = []
                        aux = crom1[z]
                        crom1[z] = crom2[z]
                        crom2[z] = aux     
             #mutacion
            rnd1 = random()
            if(rnd1 < 0.05):
                pos1 = randint(0,22)
                pos2 = randint(0,22)
                aux = crom1[pos1]
                crom1[pos1] = crom1[pos2]
                crom1[pos2] = aux
            rnd2 = random()
            if(rnd2 < 0.05):
                pos1 = randint(0,22)
                pos2 = randint(0,22)
                aux = crom2[pos1]
                crom2[pos1] = crom2[pos2]
                crom2[pos2] = aux
            auxiliar[2*m] = crom1
            auxiliar[2*m+1] = crom2
        inicial = auxiliar
        kmsMin = []
        for c in xrange(50):
            kmsMin.append(contarKilometros(inicial[c]))
        numMin = min(kmsMin)
        f.write(str(numMin)+'\n')
        indiceMinimo = kmsMin.index(numMin)
        minimosRecorridos.append(inicial[indiceMinimo])
        minimasDistancias.append(numMin)
    f.close()
    numMin = min(minimasDistancias)
    indiceMinimo = minimasDistancias.index(numMin)
    print("Minima Distancia: " + str(numMin))
    print(minimosRecorridos[indiceMinimo])   
    

def menorRecorrido(ciudadActual):
    visitadas = []
    visitadas.append(ciudadActual)
    aux = []
    aux = list(distancia[ciudadActual])
    aux.pop(ciudadActual)
    minimo = min(aux)
    ciudadActual = distancia[ciudadActual].index(minimo)
    
    for x in xrange(22):
        visitadas.append(ciudadActual)
        aux = []
        aux = list(distancia[ciudadActual])
        
        for z in visitadas:
            aux.remove(distancia[ciudadActual][z]) #elimino ciudades visitadas de la lista auxiliar
            
        if(len(aux) != 0):
            minimo = min(aux)
            indice = distancia[ciudadActual].index(minimo) #guardo el indice del minimo 
            ciudadActual = indice
    return visitadas
        
def contarKilometros(resultado):
    cont = 0
    for i in xrange(22):    #contar el recorrido total
       cont = cont + distancia[resultado[i]][resultado[i+1]]
    cont = cont +  distancia[resultado[22]][resultado[0]]
    return cont         
                
def dibujar(recorrido):
    setup(400,627,0,0)
    bgpic("350px-Argentina.gif") 

    penup()
    
    goto(puntos[recorrido[0]][0],puntos[recorrido[0]][1])
    dot(10, "blue")
    pendown()
    speed(1)
    pencolor("lightblue")
    pensize(3)
    
    for x in xrange(1,len(recorrido)):
        goto(puntos[recorrido[x]][0],puntos[recorrido[x]][1])
        dot(10, "blue")
    goto(puntos[recorrido[0]][0],puntos[recorrido[0]][1])    
    done() 

def imprimirResultados(resultado):
    cont = contarKilometros(resultado)
    dibujar(resultado)
    ctypes.windll.user32.MessageBoxA(0, "Recorrido total: "+str(cont)+"km", "Mapa de Argentina", 1)  #ventana muestra recorrido total

#programa Principal
print("Bienvenido al sistema del Viajante, el sistema recorrera las distintas capitales de la republica argentina y devolvera el menor recorrido")
print("Seleccione la opcion deseada")
print(" 1- Seleccionando Capital de inicio \n 2- Distancia minima por Heuristico \n 3- Distancia minima por Algoritmos Geneticos")
opc = input()
   
if(opc == 1):
   resultado = capitalInicial()       
   imprimirResultados(resultado)  
if(opc == 2):
    resultado = SinCapitalInicial()
    imprimirResultados(resultado)
if(opc == 3):
    geneticos()   

      
    
