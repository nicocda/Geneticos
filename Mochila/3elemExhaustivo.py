#bloque def constantes
combin = pow(2,3)
vol = 3000



#bloque funciones

#programa principal

elementos = [] #arreglo elementos

elementos.append([1800,72])
elementos.append([600,36])
elementos.append([1200,60])

maxi = 0  

for i in xrange(combin):
    nroBin = bin(i)[2:].zfill(3)

    valorMochila = 0
    pesoMochila = 0
    
    for j in xrange(3):
        
        valorMochila = valorMochila + elementos[j][1]*int(nroBin[j], base=2)
        pesoMochila = pesoMochila + elementos[j][0]*int(nroBin[j], base=2)

    if(pesoMochila <= vol):

        if(valorMochila > maxi):

            maxi = valorMochila
            maxPeso = pesoMochila
            nroMax = nroBin

print('Metodo Exhaustivo ( 3 elementos)')
print('Elementos de la mochila')

for i in xrange(3):

    if(nroMax[i]=='1'):

        print(i+1,elementos[i])

print('Valor maximo mochila: ',maxi)
print('Peso mochila: ',maxPeso)




            

        
    
        
