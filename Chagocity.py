"""
La gran maraton de Chago city es una de las carreras mas importantes a nivel mundial. 
Debido a la gran cantidad de competidores que reune este evento, se han generado las siguientes
estructuras para ayudar con la organizacion de este
"""

"""
Diccionario con los inscritos, donde se almacena el numero del corredor y los datos de  este.
"""
#num_corredor: (rut,nombre,apellido,id_categoria,edad)
inscritos = { 1001: ('1111111-2', 'Carlos', 'Caszely', 2, 55),
1002: ('223244-4', 'Marcelo', 'Rios', 3, 45),
2129: ('3838292-1', 'Ivan', 'Zamorano', 4, 38),
4738: ('5940301-2', 'Erika', 'Olivera', 5, 48),
8883: ('3843993-1', 'Condor', 'ito', 3, 22),
231: ('9492922-2', 'Pepe', 'Antartico', 3, 30)}

"""
Diccionario con las categorias, el cual almacena la distancia que se corre y el premio para el
ganador.
"""

# id_categoria: (distancia, premio)
categorias = { 1: ('1k', 10000),
2: ('5k', 20000),
3: ('10k', 450000),
4: ('21k', 100000),
5: ('42k', 250000)}

"""
Lista de resultados, donde se registra el numero del corredor y el tiempo que logro.
"""

#[ (num_corredor, tiempo) ]
resultados = [(1001, '00:30:12'), (1002, '00:55:43'), (2129,'01:45:23'), (4738, '03:05:09'), (8883, '00:31:33'), (231,'00:39:45')]

"""
Desarrolle la funcion competidores_edad(inscritos, categorias, min_edad, max_edad)
que reciba el diccionario inscritos, el diccionario categorias y los valores enteros min_edad
y max_edad (que representan la maxima y minima edad). La funcion debe retornar una lista de tu-
plas de todos los competidores que se encuentren entre la edad minima y maxima (incluyendolos), 
donde cada tupla contenga el nombre, apellido y la distancia a correr de un individuo.
"""

def competidores_edad(inscritos, categorias, min_edad, max_edad):
    lista = []
    for llave, valor in inscritos.items():
        rut,nombre,apellido,id_categoria,edad = valor
        if edad >= min_edad and edad <=max_edad:
            for llave2,valor2 in categorias.items():
                distancia, premio = valor2 
                if llave2 == id_categoria:
                    tupla = (nombre,apellido,distancia)
            lista.append(tupla)
    return lista


print(competidores_edad(inscritos, categorias, 25, 40))

"""
Desarrolle la funcion tiempo_competidor(inscritos, resultados, rut) que reciba el
diccionario inscritos, la lista de tuplas resultados y el string rut. La funcion debe retornar
el tiempo, como cadena de texto, de un competidor en particular.
"""

def tiempo_competidor(inscritos, resultados, rut2):
    for llave, valor in inscritos.items():
        rut,nombre,apellido,id_categoria,edad = valor
        if rut == rut2:
            for tupla in resultados:
                id,tiempo = tupla
                if id == llave:
                    return tiempo


print(tiempo_competidor(inscritos,resultados,'9492922-2'))