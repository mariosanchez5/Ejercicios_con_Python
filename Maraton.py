"""
La gran maraton de Chago city es una de las carreras mas importantes a nivel mundial.
Debido a la gran cantidad de competidores que reune este evento, se han generado las siguientes 
estructuras para ayudar con la organizacion de este:
Diccionario con los inscritos, donde se almacena el numero del corredor y los datos de este. 
"""

inscritos = { #num_corredor: (rut,nombre,apellido,id_categoria,edad)
1001: ('1111111-2', 'Carlos', 'Caszely', 2, 55),
1002: ('223244-4', 'Marcelo', 'Rios', 3, 45),
2129: ('3838292-1', 'Ivan', 'Zamorano', 4, 38),
4738: ('5940301-2', 'Erika', 'Olivera', 5, 48),
8883: ('3843993-1', 'Condor', 'ito', 3, 22),
231: ('9492922-2', 'Pepe', 'Antartico', 3, 30)}
"""
Diccionario con las categorias, el cual almacena la distancia que se corre y el premio para el
ganador.
"""
categorias = { # id_categoria: (distancia, premio)
1: ('1k', 10000),
2: ('5k', 20000),
3: ('10k', 450000),
4: ('21k', 100000),
5: ('42k', 250000)}
"""
Lista de resultados, donde se registra el numero del corredor y el tiempo que logro.
# [ (num_corredor, tiempo) ]
"""
resultados = [(1001, '00:30:12'), (1002, '00:55:43'), (2129,
'01:45:23'), (4738, '03:05:09'), (8883, '00:31:33'), (231,
'00:39:45')]

"""
Desarrolle la funcion competidores_edad(inscritos, categorias, min_edad, max_edad)
que reciba el diccionario inscritos, el diccionario categorias y los valores enteros min_edad
y max_edad (que representan la maxima y minima edad). La funcion debe retornar una lista de tu- 
plas de todos los competidores que se encuentren entre la edad minima y maxima (incluyendolos), 
donde cada tupla contenga el nombre, apellido y la distancia a correr de un individuo
"""

def competidores_edad(inscritos, categorias, min_edad, max_edad):
    lista = []
    for num, datos in inscritos.items():
        rut, nombre, apellido, id, edad = datos
        if edad >= min_edad and edad <= max_edad:
            for cat, tup in categorias.items():
                distancia, premio = tup
                if id == cat:
                    tupla = (nombre,apellido,distancia)
                    lista.append(tupla)
    return lista

print(competidores_edad(inscritos,categorias,25,40))

"""
Desarrolle la funcion tiempo_competidor(inscritos, resultados, rut) que reciba el
diccionario inscritos, la lista de tuplas resultados y el string rut. La funcion debe retornar 
el tiempo, como cadena de texto, de un competidor en particular.
"""

def tiempo_competidor(inscritos, resultados, rut):
    for num, datos in inscritos.items():
        rut_ins, nombre, apellido, id, edad = datos
        if rut_ins == rut:
            for i in resultados:
                id_res, tiempo = i
                if num == id_res:
                    return str(tiempo)

print(tiempo_competidor(inscritos,resultados,'9492922-2'))

"""
Desarrolle la funcion ganador_categoria(inscritos, categorias, resultados,
distancia) que reciba el diccionario inscritos, el diccionario categorias, la lista de tuplas
resultados y el string distancia. La funcion debe retornar una tupla con el ganador de cierta
categoria, indicando el nombre, apellido y premio obtenido.
"""

def ganador_categoria(inscritos, categorias, resultados, distancia):
    for id_cat, tup_cat in categorias.items():
        distancia_cat, premio = tup_cat
        if distancia_cat == distancia:
            id_cat_win = id_cat
            premio_win = premio

    diccio = {}
    for num, datos in inscritos.items():
        rut, nombre, apellido, id, edad = datos
        if id == id_cat_win:
            tupla_datos = nombre,apellido,premio_win
            #tupla_num = num
            diccio[num]=tupla_datos

    min = '99:99:99'
    for num, datos in diccio.items():
        for tupla in resultados:
            id, tiempo = tupla
            if num == id:
                if tiempo < min:
                    min = tiempo
                    tupla_win = datos
    return tupla_win

            



print(ganador_categoria(inscritos, categorias, resultados, '10k'))