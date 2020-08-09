#-*- coding: utf-8 -*-

# funcion palindromo
def palindromo(palabra):
    palabra = palabra.replace(' ', '')# borra los espacios basura
    palabra = palabra.lower() # la combierte en minuscula
    palabra_invertida = palabra[::-1] # desde el indice inicial asta el final pero en negativo
    if palabra == palabra_invertida:
        return True
    else:
        return False    


# funcion principal
def main():
    palabra = input('Escribe una palabra: ') # pedir la palabra al usuario
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print('Es palindromo')
    else:
        print('No es palindromo')




if __name__ == '__main__':
    main()
