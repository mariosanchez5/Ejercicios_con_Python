"""
La plataforma de citas en linea MatchMaker ha decidido contratarlo para ayudarles en el
analisis de su base de datos. Por suerte, la base de datos corresponde a una lista de diccionarios
de python como el siguiente:
"""

MatchMaker = [{'nombre': 'Sheldon Cooper', 'sexo': 'M', 'pasatiempos': {'Sheldon', 'ciencia', 'fisica', 'trenes'}},{'nombre': 'Leonard Hofsadter', 'sexo': 'M', 'pasatiempos': {'fisica','comics'}},{'nombre': 'Howard Wolowitz', 'sexo': 'M', 'pasatiempos': {'ingenieria', 'comics'}},{'nombre': 'Raj Koothrappali', 'sexo' :'M', 'pasatiempos': {'astronomia', 'comics'}},{'nombre': 'Penny', 'sexo':'F', 'pasatiempos': {'ciencia', 'peliculas','compras'}},{'nombre': 'Bernadette Rostenkowski', 'sexo': 'F', 'pasatiempos': {'biologia', 'compras'}},{'nombre': 'Amy Farrah Fowler', 'sexo': 'F', 'pasatiempos': {'ciencia','fisica', 'biologia', 'Sheldon'}}]

"""
Obviamente, la base de datos real tiene muchos mas datos. Sin embargo, puede asumir que cada 
nombre es unico en la base de datos. 
Se le pide crear funciones para cumplir con los siguientes requerimientos:
"""

"""
Escriba la funcion posicion(MatchMaker, nombre) que indique la posicion ( indice) en la
base de datos de la persona nombre. Si el nombre no existe, retornar None.
"""
def posicion(MatchMaker, nombre):
    pos = 0
    for persona in MatchMaker:
        if persona['nombre']== nombre:
            return pos
        pos= pos+1
        

print(posicion(MatchMaker, 'Leonard Hofsadter'))
print(posicion(MatchMaker, 'Penny'))
print(posicion(MatchMaker, 'Barney Stinson'))

"""
Escribe la funcion cantidad_pasatiempos(MatchMaker) que regrese un diccionario con el
numero de personas por cada pasatiempo que existen en la base de datos.
"""

def cantidad_pasatiempos(MatchMaker):
    diccio = {}
    for persona in MatchMaker:
        for pasa in persona['pasatiempos']:
            if pasa in diccio:
                diccio[pasa] = diccio[pasa] + 1
            else:
                diccio[pasa] = 1
    return diccio

print(cantidad_pasatiempos(MatchMaker))