
uno = input('Ingresa un numero:')
lista = []
while uno != 'fin':
    lista.append(uno)
    uno = input('Ingresa otro numero:')

#print (lista)

def promedio (lista):
    suma = 0
    largo = int(len(lista))
    for n in lista:
        suma = suma + int(n)
    prom = suma / largo
    return prom

print(promedio(lista)) 



        
