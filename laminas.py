from random import randrange

def nuevo_sobre():
    lista = []
    for n in range(1,6):
        num = randrange(1,641)
        lista.append(num)
    print(lista)

nuevo_sobre()

laminas_total = []
def agregar_laminas(laminas_pepito, m):
    for i in laminas_pepito:
        laminas_total.append(i)
    print(laminas_total)

