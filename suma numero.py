#suma del numero hasta el numero entero

numero = int(input("Ingrese un numero: "))
contador = 1
suma = 0

while contador <= numero:
    cuadrado = contador ** 2
    suma = suma + cuadrado
    contador = contador +1

print ("La suma del cuadrado de todos los numeros menores a su numero es ",suma)

