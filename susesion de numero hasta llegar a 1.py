#susesion de numero hasta llegar a 1
#si el numero es par se debe dividir por 2
#si el numero es impar se debe multiplicar por 3 y sumarle 1

numero = int(input("Ingrese un numero: "))

while numero != 1:
    if numero%2 ==0:
        numero = numero/2
        print(numero)
    else:
        numero = (numero*3)+1
        print(numero)



