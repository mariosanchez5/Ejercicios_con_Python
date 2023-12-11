#Escriba la función todos_iguales(lista) que indique si todos los elementos de una lista son iguales:

lista = [6, 6, 1]
def mas_de_un_igual(lista):
    cont = 0
    for uno in lista:
        for dos in lista:
            if uno == dos:
                cont = cont + 1
    
    if cont > len(lista):
        return True
    else:
        return False

print (mas_de_un_igual(lista))

def todos_iguales(lista):
    band = True
    for uno in lista:
        for dos in lista:
            if uno != dos:
                band = False
    return band

print (todos_iguales(lista))