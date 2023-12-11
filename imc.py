#Este programa indicará el imc de la persona y si esta en condicion de riesgo o no dependiendo de su edad e imc

edad = int(input("Ingrese su edad: "))
peso = float(input("Ingrese su peso: "))
altura = float(input("Ingrese su altura: "))

imc = peso/(altura**2)
print("Su IMC es de: ",imc)

if edad <45:
    if imc < 22:
        print("Su condición de riesgo es bajo")
    else:
        print("Su condición de riesgo es medio")
else:
    if imc < 22:
        print("Su condición de riesgo es medio")
    else:
        print("Su condición de riesgo es alto")