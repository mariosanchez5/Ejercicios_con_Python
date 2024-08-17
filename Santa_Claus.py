"""
Santa Claus ha comprado un sistema hecho en Python para administrar la Navidad 2015.
Basicamente, el sistema maneja una lista de tuplas, donde cada tupla corresponde a los registros 
de una persona con el formato (nombre, (x, y), tipo), donde (x, y) son las coordenadas
en el mapa de la ubicacion de la persona y tipo indicaba como se ha portado la persona ('B':
Bueno; 'M': Malo). Ver ejemplo:
"""

personas = [('Erick Lopez', (12.9887, 1.5567), 'M'), ('Cesar Moltedo',(12.1986, 2.5321), 'M'), ('Andrew Ng', (-2.9001, 7.6453), 'M'), ('Zafradaa', (12.2316, 5.0089), 'B')]

"""
Nota: Asuma que cada nombre aparece solo una vez. 
Ahora usted debe:
"""

"""
Desarrolle la funcion persona_mas_cerca(personas, posicion) que reciba la lista personas
y la posicion actual (posicion) de Santa Claus. La funcion debe retornar el nombre de la persona
mas cercana a la posicion de Santa Claus. Para calcular esta distancia recuerde que, en R2
, si se
tiene un punto (x1, y1) y un punto (x2, y2), entonces la distancia entre los dos puntos viene dada
por raiz[(x2 − x1)2 + (y2 − y1)2]
"""

def persona_mas_cerca(personas, posicion) :
    min = 100000000
    x1,y1 = posicion
    for tupla in personas:
        nombre, ubicacion, estado = tupla
        x2,y2 = ubicacion
        distancia = ((x2-x1)**2 + (y2-y1)**2)**(1/2)
        if distancia < min:
            min = distancia
            nom = nombre 
    return nom

print(persona_mas_cerca(personas, (12.9676, 1.4991)))


"""
Santa Claus ha determinado que la mejor ruta para repartir todos los regalos es ir siempre a la
persona mas cercana (con cuidado de no repetirlas) desde la posicion en la que se encuentra. Usted 
debe crear la funcion mejor_ruta(personas, posicion) que reciba la lista personas y la
posicion inicial de Santa Claus, y retorne una lista con la ruta a seguir identificada por el nombre
de las personas.
Nota: No altere la lista original de personas.
"""

def mejor_ruta(personas, posicion):
    x1,y1 = posicion
    lista = []
    for tupla in personas:
        nombre, ubicacion, estado = tupla
        x2,y2 = ubicacion
        distancia = round(((x2-x1)**2 + (y2-y1)**2)**(1/2),1)
        lista.append((nombre,distancia))
    lista_ordenada = sorted(lista, key=lambda x: x[1])
    return lista_ordenada

print(mejor_ruta(personas, (0.0, 0.0)))