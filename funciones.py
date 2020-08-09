# -*- coding: utf-8 -*-
# funciones en python def

# def imprimir_mensaje():
#     print("hola")
#     print("juan")
#     print("hola como estas?")
#     print("adios")
#     print("hola")
#     print("juan")
#     print("hola como estas?")
#     print("adios")
#     print("hola")
#     print("juan")
#     print("hola como estas?")
#     print("adios")


# imprimir_mensaje()


def suma(a,b):
   print("la suma de dos numero")
   resultado = a + b
   return resultado

sumatoria = suma(10, 3)



# ree utilizamos el codigo sin repetir
# def conversar(mensaje):
#     print("hola")
#     print("como estas")
#     print(mensaje)
#     print("adios")

opcion = int(input("Elige una opcion (1, 2, 3): ")) # pedimos una opcion al usuario

if opcion == 1:
   conversar("Elegiste la opcion 1")

elif opcion == 2:
   conversar("Elegiste la opcion 2")
elif opcion == 3:
     conversar("Elegiste la opcion 3")
else:
    print("Escribe la opcion correcta")
