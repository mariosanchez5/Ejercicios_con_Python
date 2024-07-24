"""
Leonardo Parkas aburrido de su mala suerte ha decidido apostar en las ruletas del casino de
Pythonia, Pytichello. Gracias a la ayuda de su fiel amigo PyMundo, ha conseguido obtener la
informacion de los resultados de las ruletas en los juegos anteriores, los cuales estan disponibles
en un diccionario, cuya llave es un string con el identificador de la ruleta y el valor es una lista,
donde cada elemento de la lista corresponde a un numero que ha sido ganador en algun juego
anterior en la ruleta. Habran tantos numeros como juegos se hayan llevado a cabo en la ruleta.
"""

resultados = {'r1': [6,3,12,3,7,6] ,
              'r9': [12,8,12] ,
              'r2': [7,1,15,4,7,11,7,1]}

"""
En las ruletas de Pytichello los numeros a los que se puede apostar van desde el 1 hasta el 15. El 
maximo de numeros a apostar por juego es de 5. Como Parkas quiere asegurar su apuesta, le ha 
solicitado a usted implemente unas funciones que le entreguen informacion relevante para hacer 
su apuesta, para lo cual solicita lo siguiente:
"""

"""
Implemente la funcion estadisticas(ruleta, diccio) la cual recibe 2 parametros, un string ruleta
con el id de la ruleta y el diccionario diccio, con la informacion de los resultados por ruleta. Esta 
funcion debe retornar un diccionario donde cada llave correspondera a un numero ganador y su
respectivo valor correspondera a la frecuencia que se repitio dicho numero, es decir, la cantidad 
de veces que aparecio el numero dividido por la cantidad total de numeros que se han jugado en 
la ruleta
"""

def estadisticas(ruleta, diccio):
    diccio_creado = {}
    for rult,numeros in diccio.items():
        if rult == ruleta:
            for num in numeros:
                if num in diccio_creado:
                    diccio_creado[num]= diccio_creado[num] + 1
                else:
                    diccio_creado[num]= 1

    total = sum(diccio_creado.values())

    for llave, valor in diccio_creado.items():
        diccio_creado[llave] = diccio_creado[llave]/total
    
    return diccio_creado

print(estadisticas('r2',resultados))