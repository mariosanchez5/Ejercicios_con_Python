#Encontrar el maximo de un numero

numero = int(input("Ingrese numeros de a uno, para parar ingrese 0: "))
max = 0

while numero != 0:
    if numero > max:
        max = numero
    numero = int(input("Ingrese otro numero, para parar ingrese 0: "))

print("El mayor de los numeros ingresados es ",max)
   


