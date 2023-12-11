from random import randrange

num = randrange(101)
#print (num)

numero = int(input('Ingrese un número del 1 al 100: '))
if num == numero:
    print('Exacto, eres un adivino')

while num != numero:
    if num > numero:
        print('Prueba con un número mayor')
    else:
        print('Prueba con un número menor')
    numero = int(input('Ingrese el nuevo número: '))

print('Exacto, eres un adivino')
    