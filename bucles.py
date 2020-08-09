def main():
    LIMITE = 1000000 # constante

    contar = 0 
    potencia_2 = 2**contar
    while potencia_2 < LIMITE:
        print(f'2 elevado a {contar} es igual a: {potencia_2}')
        contar += 1
        potencia_2 += 2**contar




if __name__=='__main__':
    main()