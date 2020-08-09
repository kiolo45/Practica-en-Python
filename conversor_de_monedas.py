# -*- coding: utf-8 -*-
pesos = input("Cuantos pesos colombianos tienes?: ")
pesos = float(pesos)
valor_dolar = 3875
dolares = pesos / valor_dolar
dolares = round(dolares, 2) # tomamos el contenido de lavariable dolares y lo redondiamos
dolares = str(dolares)
print(f"Tienes {dolares}$ dolares")
