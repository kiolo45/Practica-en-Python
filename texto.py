# -*- coding: utf-8 -*-

# travajando con texto

# metodos 

nombre = input("Cual es tu nombre: ")

# colocar al texto en mayusula .upper()
nombre = nombre.upper()
print(nombre)

# primera letra en mayuscula
nombre = nombre.capitalize()
print(nombre)

# eliminar espacios basura
nombre = nombre.split()

# seva a transformar en minnuscula
#nombre = nombre.lower()

# reemplasar letras 
#nombre = nombre.replace('a', 'e')

# indices 
print(nombre[0]) # contamos desde 0
# debuelve la primera letra de tu nombre

# funcion len()
print(len(nombre)) # nos cuenta los caracteres que tenga la variable nombre

# slices

nombre1 = "Hola, Juan"
print(len(nombre1))
# H o l a ,   J u a n
# 0 1 2 3 4 5 6 7 8 9

nombre = nombre[0:6] # partimos del 0 asta el 6 osea quedaria Hola, 
print(nombre1[0:6])  # partimos del 0 asta el 6 osea quedaria Hola,
# podemos saltarnos poner el 0 simplemente ponemos el elemento que queremos llegrar [:6]

print(nombre1[3:]) # esto es partimos del indice 3 asta el final de todo
# a, Juan

nombre = nombre[0:7:2]# le decimos a python que vamos del indice 0 asta el 7 pero de 2 en 2
print(nombre1[0:7:2]) # seria Hl,J


print(nombre1[::]) # esto me traeria todo el string completo
# desde el indice inicial asta el final

print(nombre1[1::3])# desde el indice inicial asta el final pero de 3 en 3

# pasos negativos
print(nombre1[::-1])# en este caso python entiende que vamos desde el indice inicial asta el final pero al reves
# nauJ ,aloH



