CONTRASEÑA  = 'hola0368*'
puerta = True
while (puerta):
    ingresoUsuario = input("Por favor Digite la contraseña: ")
    if(CONTRASEÑA == ingresoUsuario):
        print("Correcto!!!")
        puerta = False
    else:
        print("Esa monda esta mal, sigue intentando")

print("Programa terminado, Bye...")