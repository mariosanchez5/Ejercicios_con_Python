"""
La conocida aplicacion ”SpotiPhy”necesita determinar cuales son los albumes y los artistas mejores 
evaluados en su plataforma. Para lograrlo dispone de una lista de tuplas que tienen la siguiente forma:
(cancion, album, artistas, f echa evaluacion, nota), en donde cancion y  album estan en formato string, 
artistas es una lista que contiene los nombres de los artistas (una cancion puede tener mas de un artista) en
formatro string, la fecha es una tupla (A,M,D) y la nota es un entero entre 1 y 5. A continuacion se muestra
un ejemplo de la estructura evaluaciones:
"""

evaluaciones = [('Phypocrita', 'Hasta abajo', ['Pynuel'], (2018, 6, 30), 4),
('Sin Phyjama', 'Nuevo Estilo', ['Becky T', 'Turize'], (2018, 4, 14), 3),
('Vaina Crazy', 'del Weno', ['Ozune', 'Turize'], (2018, 7, 18), 5),
('Phypocrita', 'Hasta abajo', ['Pynuel'], (2018, 8, 20), 5),
('Quiero Beber Agua', 'Hasta abajo', ['Pynuel'], (2018, 2, 25), 5)]

"""
Notar que una misma cancion pudo ser evaluada en distintos momentos. De acuerdo a la informacion
anterior, se le solicita implementar las siguientes funciones:

a.- Escriba la funcion notas por artista(lista), donde lista es del tipo evaluaciones. Esta
funcion debe retornar un diccionario donde la llave es un  string con el nombre del artista y como valor
tienen una lista de enteros que corresponden a todas las evaluaciones de canciones en las que ha participado.
Recuerde que una misma cancion puede tener varias evaluaciones y todos estos valores deben estar en la
lista.
"""

def notas_por_artista(evaluaciones):
    diccio = {}
    for tupla in evaluaciones:
        cancion, album, artista,fecha, nota = tupla
        for art in artista:
            if art not in diccio:
                diccio[art]=[nota]
            else:
                diccio[art].append(nota)
    return diccio

print(notas_por_artista(evaluaciones))

