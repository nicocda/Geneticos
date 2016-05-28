#bloque def constantes
combin = pow(2,10)
vol = 4200 



#bloque funciones

def proporcion(val,peso):
    return val/float(peso)

#programa principal

elementos = [] #arreglo elementos
propor = []
orden = []

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

for i in xrange(10):

    p = proporcion(elementos[i][1],elementos[i][0])

    propor.append([p,i])

propor.sort(reverse=True)


acum = 0

for i in xrange(10):

    acum = acum + elementos[propor[i][1]][0] #peso del objeto i

    if(acum <= vol):

        orden.append(propor[i][1])
    else:
        acum = acum - elementos[propor[i][1]][0]

sumValor = 0
sumPeso = 0

print('Metodo Greedy')
print('Elementos de la mochila')
for i in xrange(len(orden)):

    print(orden[i]+1,elementos[orden[i]])

    sumValor = sumValor+ elementos[orden[i]][1]
    sumPeso = sumPeso + elementos[orden[i]][0]

print('Valor de la mochila: ',sumValor)
print('Peso de la mochila: ',sumPeso)



    




            

        
    
        
