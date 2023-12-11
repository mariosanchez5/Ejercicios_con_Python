#Dada el siguiente diccionario Escriba la función obtener_lista_equipos(resultados) que reciba como parámetro el diccionario de resultados y retorne una lista con todos los equipos que participaron del campeonato 

resultados = {
   ('Honduras', 'Chile'):    (0, 1),
   ('Espana',   'Suiza'):    (0, 1),
   ('Suiza',    'Chile'):    (0, 1),
   ('Espana',   'Honduras'): (3, 0),
   ('Suiza',    'Honduras'): (0, 0),
   ('Espana',   'Chile'):    (2, 1),
}

def obtener_lista_equipos(resultados):
    lista = []
    for p1,p2 in resultados:
        if p1 not in lista:
            lista.append(p1)
        elif p2 not in lista:
            lista.append(p2)
    print (lista)

obtener_lista_equipos(resultados)

# Dado el siguiente diccionario Escriba la función calcular_puntos(equipo, resultados) que entregue la cantidad de puntos obtenidos por un equipo

resultados = {
   ('Honduras', 'Chile'):    (0, 1),
   ('Espana',   'Suiza'):    (0, 1),
   ('Suiza',    'Chile'):    (0, 1),
   ('Espana',   'Honduras'): (3, 0),
   ('Suiza',    'Honduras'): (0, 0),
   ('Espana',   'Chile'):    (2, 1),
}

def calcular_puntos(equipo, resultados):
    puntos = 0
    for p1,p2 in resultados:
        tup = resultados [(p1,p2)]
        r1,r2 = tup
        if p1 == equipo:
            if r1 > r2:
                puntos = puntos + 3
            elif r1 == r2:
                puntos = puntos + 1
        elif p2== equipo:
            if r2 > r1:
                puntos = puntos + 3
            elif r2 ==r1:
                puntos = puntos + 1
    print ('El equipo {} obtuvo {} puntos en el campeonato'.format(equipo,puntos))

calcular_puntos('Chile', resultados)