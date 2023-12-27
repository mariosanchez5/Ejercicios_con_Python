"""
La empresa fruticola Pythonfrut se dedica a la produccion, procesamiento y exportacion
de distintos tipos de frutas. Ellos tienen registradas las frutas cosechadas en cada mes en una
lista de conjuntos, donde el indice en la lista indica el mes y el conjunto contiene las frutas que se
cosechan en este.
"""

frutas = [
set(['manzana', 'frutilla', 'platano', 'mora']),
set(['manzana', 'frutilla', 'mora']),
set(['manzana', 'pera', 'durazno', 'mora'])]

"""
Desarrollar la funcion cantidades(frutas) que reciba como parametro la lista de conjuntos
de frutas y retorne una lista de tuplas, donde cada tupla almacena una fruta y la cantidad de
meses donde se cosecha.
"""

def cantidades(frutas):
    diccio = {}
    for tupla in frutas:
        for fruta in tupla:
            if fruta in diccio:
                diccio[fruta] = diccio[fruta] + 1
            else:
                diccio[fruta]= 1
    #return(diccio)
    return tuple(diccio.items())


print(cantidades(frutas))

"""
Desarrollar la funcion frutas_mas_repetidas(frutas) que reciba como parametro la lista 
de conjuntos de frutas y retorne una lista con los nombres de las frutas que se producen en la
mayor cantidad de meses.
"""

def frutas_mas_repetidas(frutas):
    diccio = {}
    for tupla in frutas:
        for fruta in tupla:
            if fruta in diccio:
                diccio[fruta] = diccio[fruta] + 1
            else:
                diccio[fruta]= 1
    
    max = 0
    for llave, valor in diccio.items():
        if valor > max:
            max = valor
            lista = [llave]
            for llave2, valor2 in diccio.items():
                if valor2 == max and llave2 not in lista:
                    lista.append(llave2)

    return lista


print(frutas_mas_repetidas(frutas))

"""
Desarrolle la funcion fruta_exclusiva(frutas, mes) que reciba como parametro la lista de
conjuntos de frutas y un entero correspondiente al mes, los que estan enumerados desde cero. 
La funcion debe retornar un conjunto con las frutas que solo se producen en dicho mes. En caso 
de no haber, debe retornar un conjunto vacio.
"""

def fruta_exclusiva(frutas, mes):
    diccio = {}
    for tupla in frutas:
        for fruta in tupla:
            if fruta in diccio:
                diccio[fruta] = diccio[fruta] + 1
            else:
                diccio[fruta]= 1

    lista = []
    for llave, valor in diccio.items():
        if valor == 1:
            tupla_mes = frutas[mes]
            for i in tupla_mes:
                if i == llave:
                    lista.append(llave)
    return(tuple(lista))
                
            

print(fruta_exclusiva(frutas, 0))
