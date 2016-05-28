#bloque def constantes
combin = pow(2,10)
vol = 3000 



#bloque funciones

def proporcion(val,peso):
    return val/float(peso)

#programa principal

elementos = [] #arreglo elementos
propor = []
orden = []

elementos.append([1800,72])
elementos.append([600,36])
elementos.append([1200,60])


for i in xrange(3):

    p = proporcion(elementos[i][1],elementos[i][0])

    propor.append([p,i])

propor.sort(reverse=True)


acum = 0

for i in xrange(3):

    acum = acum + elementos[propor[i][1]][0] #peso del objeto i

    if(acum <= vol):

        orden.append(propor[i][1])
    else:
        acum = acum - elementos[propor[i][1]][0]

sumValor = 0
sumPeso = 0
print('Metodo Greedy (3 elementos)')
print('Elementos de la mochila')
for i in xrange(len(orden)):

    print(orden[i]+1,elementos[orden[i]])

    sumValor = sumValor+ elementos[orden[i]][1]
    sumPeso = sumPeso + elementos[orden[i]][0]

print('Valor de la mochila: ',sumValor)
print('Peso de la mochila: ',sumPeso)



    




            

        
    
        
