#bloque def constantes
combin = pow(2,10)
vol = 4200 



#bloque funciones

#programa principal

elementos = [] #arreglo elementos

elementos.append([150,20])
elementos.append([325,40])
elementos.append([600,50])
elementos.append([805,36])
elementos.append([430,25])
elementos.append([1200,64])
elementos.append([770,54])
elementos.append([60,18])
elementos.append([930,46])
elementos.append([353,28])

maxi = 0  

for i in xrange(combin):
    nroBin = bin(i)[2:].zfill(10)

    valorMochila = 0
    pesoMochila = 0
    
    for j in xrange(10):
        
        valorMochila = valorMochila + elementos[j][1]*int(nroBin[j], base=2)
        pesoMochila = pesoMochila + elementos[j][0]*int(nroBin[j], base=2)

    if(pesoMochila <= vol):

        if(valorMochila > maxi):

            maxi = valorMochila
            maxPeso = pesoMochila
            nroMax = nroBin


print('Elementos de la mochila')

for i in xrange(10):

    if(nroMax[i]=='1'):

        print(i+1,elementos[i])

print('Valor maximo mochila: ',maxi)
print('Peso mochila: ',maxPeso)




            

        
    
        
