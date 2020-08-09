import random

# funcion grnerador de contraseña
def generar_password():
    mayusculas = ['A', 'B', 'C', 'D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    minusculas = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']
    simbolos = ['%','!','/','(',')','-','&','$','{','}','#']
    numeros = ['1','2','3','4','5','6','7','8','9','0']

    caracteres = mayusculas + minusculas + simbolos + numeros

    password = []

    for i in range(15):
        caracterer_random = random.choice(caracteres)
        password.append(caracterer_random)

    password = ''.join(password) # lo combierte a string
    return password    
        

# funcion principal
def main():
    password = generar_password()
    print(f"Tu nueva contraseña es: {password}")


if __name__ == "__main__":
    main()