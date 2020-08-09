def es_primo(numero):
    contar = 0
    for i in range(1, numero + 1):
        if i == 1 or 1 == numero:
            continue
        if numero % i == 0:
            contar += 1
    if contar == 0:
        return True
    else:
        return False    


def main():
    numero = int(input("Escribe un numero: "))
    if es_primo(numero):
        print("Es primo")
    else:
        print("No es primo")    










if __name__ == "__main__":
    main()