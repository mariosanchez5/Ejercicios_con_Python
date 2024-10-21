"""
El sistema binario es un sistema de numeración en los cuales los números se representan sólo utilizando 0 y 1.

Realice una función llamada binario(n), la cual entrada el número binario correspondiente para un número n entero.

Para transformar un número decimal a binario se debe dividir el número por 2 y almacenar el resto, proceso que se repite hasta que el resultado de dicha división sea 0. Finalmente, el número deseado es el recorrido en orden inverso de los restos almacenados.
"""

"""

De la misma forma, para poder pasar un número binario a entero decimal, se logra entender el procedimiento.

Primero se invierte el número y se comienza multiplicar cada elemento por las potencia de 2:

Nrooriginal:1101Nroinvertido:1011Mult:1×20+0×21+1×23+1×24:25
Desarrolle una función decimal(n) la cual haga el trabajo de transformar el binario a una representación de entero decimal
"""

def binario(n):
    entero = 1
    binario = ''
    while entero != 0:
        entero = int(n/2)
        resto = n%2
        binario = binario+str(resto)
        n = entero
    return binario

print(binario(3))
print(binario(7))
        