# -*- coding: utf-8 -*-
menu = """
Bienvenido al conversor de monedas 💲

a - Pesos colombianos
b - Pesos argentinos
c - Pesos mexicanos

Elige una opcion: """

opcion = int(input(menu))

if opcion == 1:
    pesos = input("Cuantos pesos colombianos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 3875
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2) # tomamos el contenido de lavariable dolares y lo redondiamos
    dolares = str(dolares)
    print(f"Tienes {dolares}$ dolare")

elif opcion == 2:
    pesos = input("Cuantos pesos argentinos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 65
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2) # tomamos el contenido de lavariable dolares y lo redondiamos
    dolares = str(dolares)
    print(f"Tienes {dolares}$ dolares")

elif opcion == 3:
    pesos = input("Cuantos pesos mexicanos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 24
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2) # tomamos el contenido de lavariable dolares y lo redondiamos
    dolares = str(dolares)
    print(f"Tienes {dolares}$ dolares")

else:
    print("Ingresa una opcion valida por favor 😕")


