# listas

numeros = [1,3,4,5,8,9,17,90] # contiene varios elementos listas
# pueden contener datos del mismo tipo o de diferentes tipos

cosas = ['juan',True,1,4]

#aceder a objetos de listas
print(cosas[0]) # en este caso accedemos a juan

# agregar objetos a listas
cosas.append(False)
print(cosas)

# borrar cosas de las listas
cosas.pop(1) # en este caso borre True

for i in cosas:
    print(i) # recorrer la lista

numeros1 = [1,2,3,4,5] # esto es una lista y podemos modificarla
numero2 = [6,7,8,9]
suar_lista = numeros1 + numero2 # podemos sumar listas
print(suar_lista)
