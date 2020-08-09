def main():
    # for contar in range(1000):
    #     if contar % 2 != 0:
    #         continue
    #     print(contar)

    # for i in range(0, 9999):
    #     print(i)
    #     if i == 5678:
    #         break


    texto = input('Escribe un texto: ')
    for letra in texto:
        if letra == 'o':
            break
        print(letra)


if __name__ == "__main__":
    main()