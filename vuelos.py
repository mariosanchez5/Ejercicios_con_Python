"""
 El Aeropuerto-Internacional SansanoAirport desea mantener la informacion acerca de las 
salidas y llegadas de sus distintos vuelos; para ello, ha implementado un sistema de informacion
basado en Python, utilizado, desarrollado y mantenido por Sansanos. La base de dicho sistema
es un diccionario llamado SansaVuelos el cual almacena la informacion de cada uno de los 
vuelos.
La clave del diccionario es un string que representa el codigo del vuelo y el valor del diccionario 
es una tupla compuesta respectivamente por el nombre de la aerolinea, el lugar de partida,
destino, una lista de strings con las escalas y el tiempo promedio de todos los vuelos realizados
entre los destinos (medido en minutos).
SansaVuelos = { # codigo: (nombre, partida, destino, escalas,
tiempo_promedio),
'NH217': ('All Nippon Airways', 'Tokyo', 'Santiago', ['Atlanta'],
1620),
'AY154': ('Finnair','Helsinki', 'Moscu', ['Riga'], 175),
'OV171': ('Estonian Air', 'Tallin', 'Paris', ['Amsterdam','Berlin'
], 205), ...
}
Tambien se cuenta con un  diccionario Vuelo, cuya clave es un entero identificador, y cuyo
valor es una Tupla compuesta respectivamente por el codigo del vuelo y una fecha (en forma de
tupla (ano,mes,dia)).
Vuelo = { # identificador: codigo, fecha
3542: ('AY154', (2013,12,25)),
6433: ('NH217', (2013,12,31)),
1313: ('NH217', (2013,11,6)), ...
}
Realice las siguientes funciones para ayudar al correcto funcionamiento de tan respetado aeropuerto:

a. Escriba la funcion vuelos_entre_fechas(fecha1,fecha2,Vuelo) que reciba un par de
fechas y el Vuelo y retorne el conjunto de todos los codigos de los vuelos que se hayan realizado 
entre tales fechas (ambas inclusive).
"""
SansaVuelos = { 'NH217': ('All Nippon Airways', 'Tokyo', 'Santiago', ['Atlanta'],1620), 
'AY154': ('Finnair','Helsinki', 'Moscu', ['Riga'], 175),
'OV171': ('Estonian Air', 'Tallin', 'Paris', ['Amsterdam','Berlin'], 205)}

Vuelo = {3542: ('AY154', (2013,12,25)),
6433: ('NH217', (2013,12,31)),
1313: ('NH217', (2013,11,6))}

def vuelos_entre_fechas(fecha1,fecha2,Vuelo):
    for i in Vuelo:
        fecha = Vuelo[i][1]
        if fecha1 <= fecha >= fecha2:
            print(fecha)


print(vuelos_entre_fechas((2013,7,22),(2014,7,22),Vuelo))