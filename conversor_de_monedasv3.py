# -*- coding: utf-8 -*-


def convertir(tipo_pesos, valor_dolar):
     pesos = input("Cuantos pesos " +  tipo_pesos + " tienes?: ")
     pesos = float(pesos)
     dolares = pesos / valor_dolar
     dolares = round(dolares, 2) # tomamos el contenido de lavariable dolares y lo redondiamos
     dolares = str(dolares)
     print(f"Tienes {dolares}$ dolare")

menu = """
Bienvenido al conversor de monedas 💲

a - Pesos colombianos
b - Pesos argentinos
c - Pesos mexicanos

Elige una opcion: """

opcion = int(input(menu))

if opcion == 1:
    convertir("colombianos", 3875)

elif opcion == 2:
   convertir("aregentinos", 65)

elif opcion == 3:
    convertir("mexicanos", 24)

else:
    print("Ingresa una opcion valida por favor 😕")

