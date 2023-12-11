"""
PyCornerShop es una aplicacion que le permite a sus usuarios conseguir productos del supermercado 
desde la comodidad del hogar usando sus telefonos moviles. La informacion de los repartidores y usuarios 
se encuentra almacenada en dos diccionarios llamados repartidores y usuarios respectivamente. 

El diccionario repartidores tiene los nombres de los repartidores como llave y como valor una tupla
que contiene la ubicacion del repartidor en el plano de la ciudad y su estado de disponibilidad: True
(disponible) o False (no disponible). A continuacion, se muestra un ejemplo de este diccionario: 
repartidores = {'rayo macuin': ((10, 2), True), 'reparti dhor': ((9, 3), True),
'eliseo al-azar': ((5, 5), False), ...}

El diccionario usuarios contiene el codigo del usuario como llave y como valor la ubicacion del mismo 
en el plano de la ciudad. A continuacion se muestra un ejemplo: 
usuarios = {1221: (5, 2), 441: (8, 2), 587: (10, 1), ...}

Existe un diccionario llamado visitas donde cada llave es el nombre de un repartidor y como valor tiene
una lista de tuplas. Cada tupla se compone de un codigo de usuario y de la cantidad de veces que dicho 
repartidor (llave del diccionario) visito a dicho usuario. Tenga en consideracion que si un usuario nunca ha 
solicitado reparto, no aparecera en el diccionario visitas. A continuacion un ejemplo: 
visitas = {'rayo macuin': [(1221, 5), (441, 8), (587, 2)],
'reparti dhor': [(1221, 2), (441, 5), (587, 3)],
'eliseo al-azar': [(1221, 8), (441, 2), (587, 1)],...}

Para que la compania PyCornerShop pueda funcionar de manera eficiente, le solicita a Ud. que implemente
una funcion llamada: buscar_repartidor(repartidores,usuarios,visitas,codigo) que reciba
como parametros los diccionarios antes mencionados y un codigo de usuario (formato int). La funcion
debe retornar una lista de repartidores disponibles y cercanos, ordenados de manera descendente, segun el 
numero de visitas que estos hayan realizado al usuario requerido. Un repartidor sera considerado cercano
si esta ubicado a menos de 4 km del usuario y para esto considere que las tuplas de ubicacion tienen 
valores enteros medidos en km. Finalmente, si no hay repartidores cercanos, la funcion debe retornar una 
lista vacia.

Recuerde que los puntos suspensivos en los contenedores indican que existen mas datos. Ademas considere
los siguientes ejemplos de ejecucion para construir su solucion: 
>>> print buscar_repartidor(repartidores,usuarios,visitas,587)
['reparti dhor', 'rayo macuin']
>>> print buscar_repartidor(repartidores,usuarios,visitas,441)
['rayo macuin', 'reparti dhor']
>>> print buscar_repartidor(repartidores,usuarios,visitas,1221)
[]
Nota: Para calcular la distancia d entre un usuario ubicado en (x1, y1) y un repartidor ubicado en (x2, y2)
se debe utilizar la ecuacion:  d =raiz[(x1 - x2)**2 + (y1 - y2)**2]
"""

repartidores = {'rayo macuin': ((10, 2), True), 'reparti dhor': ((9, 3), True), 'eliseo al-azar': ((5, 5), False)}
usuarios = {1221: (5, 2), 441: (8, 2), 587: (10, 1)}
visitas = {'rayo macuin': [(1221, 5), (441, 8), (587, 2)], 'reparti dhor': [(1221, 2), (441, 5), (587, 3)], 'eliseo al-azar': [(1221, 8), (441, 2), (587, 1)]}

def buscar_repartidor(repartidores,usuarios,visitas,codigo):
    habilitados = {}
    for repartidor, valor in repartidores.items():
        ubi, estado = valor
        if estado == True:
            habilitados[repartidor] = valor
    
    ubi_user = usuarios[codigo]
    x1,y1 = ubi_user

    disponibles = {}
    for repartidor, valor in habilitados.items():
        ubi, estado = valor
        x2,y2 = ubi
        distancia = (((x1-x2)**2)+((y1-y2)**2))*1/2
        if distancia < 4:
            for rep,tup in visitas.items():
                if rep == repartidor: 
                    for i in tup:
                        cod, cant = i
                        if cod == codigo:
                            disponibles[rep] = cant
    
    return sorted(disponibles.keys(), key=lambda r: disponibles[r], reverse=True)


print(buscar_repartidor(repartidores,usuarios,visitas,441))