def main():
    mi_diccionario = {
        'llave1': 1,
        'llave2': 2,
        'llave3': 3,
    }
    # print(mi_diccionario['llave1']) # asi llamamos las claves de diccionario
    # print(mi_diccionario['llave2'])
    # print(mi_diccionario['llave3'])

    poblacion_paises = {
        'Argentina': 44938712,
        'Brasil': 21014000,
        'Colombia': 50675504,
    }
    print(poblacion_paises['Colombia'])
    
    # for i in poblacion_paises.keys(): # recorremos los valores
    #     print(i)

    # for devolver los valores del diccionario
    for pais, poblacion in poblacion_paises.items():
        print(f"{pais} tiene {poblacion} de havitantes")



if __name__ == "__main__":
    main()