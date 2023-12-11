#Escriba un programa que indique si una palabra existe dentro de una oración. Tanto la palabra, como la oración serán ingresadas como entrada de datos.
#Sin importar si esta en minuscula o mayuscula

palabra  = input("Igrese una palabra: ")
letra = input("Ingrese una letra: ")

palabra = palabra.lower()
letra = letra.lower()

existe = 0

for l in palabra:
    if l == letra:
        existe = existe + 1 

if existe == 0:
    print("Su letra no esta contenida en la palabra")
else:
    print("Su letra esta contenida ",existe,"veces en la palabra")