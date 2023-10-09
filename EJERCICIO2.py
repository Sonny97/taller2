while True:
  base = float(input("Digita el numero de la base: "))
  exponente = int(input("Digita el numero de la exponente: "))

  if exponente < 0:
    print("El exponente debe ser un número entero positivo")
  else:
    resultado = 1
    for x in range(exponente):
      resultado *= base
    print(f"El resultado es: {resultado}")
    break