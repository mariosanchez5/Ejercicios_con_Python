#Este es el primer programa de vuelta para no parar

print("Hello World")

num1 = int(input("Ingresa un numero: "))
num2 = int(input("Ingresa un segundo numero: "))

suma = num1+num2

print("La suma de los dos numeros es igual a: ",suma)

edad = int(input("Ingresa tu edad: "))

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

palabra = input("Escribe una palabra: ")

print("Tu palabra por 2 es: ",palabra * 2)

#Un programa que determine el area de un circulo

radio = float(input("Ingresa el radio del circulo: "))
area = 3.14 * (radio**2)

print("El area del cirulo es de ",area)

#Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 y no por 400

ano = int(input("Ingrese un año: "))

if ano%4 == 0:
    if ano%100 == 0 and ano%400 != 0:
        print("No es año bisiesto")
    else:
        print("Es año bisiesto")
else:
    print("No es año bisiesto")



    