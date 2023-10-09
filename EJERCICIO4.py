import random

number = random.randint(1, 100)

puerta = True
while (puerta):
    print("****************************************")
    print("Recuerda que si dijistas '0' se cerrara el programa \n")
    digitadoUsuario = int(input("Por favor digita el numero que creas es el correcto: "))

    if(number == digitadoUsuario):
        print("Felicitaciones, adivinaste... :D")
        puerta = False
    elif (digitadoUsuario == 0):
        print(f"Derrota, te has rendido el numero era: {number}, Bye bye...")
        puerta = False
    elif(number > digitadoUsuario):
        print("Estas por debajo del valor, sigue intentando...")
    elif(number < digitadoUsuario):
        print("Estas por encima del valor, sigue intentando...")