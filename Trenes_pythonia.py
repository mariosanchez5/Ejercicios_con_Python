"""
En la ciudad de Pythonia todos los trenes realizan el mismo recorrido, pasando por cada
una de las estaciones de la Linea P. El orden de las estaciones se encuentra en la lista linea_P.
Sin embargo, el tiempo entre una estacion y otra depende del tipo de tren. Los trenes Expreso
tardan 2 minutos en ir desde una estacion a otra, los trenes Normal demoran 5 minutos, y los
trenes Corto tardan 7 minutos. Asuma que el tiempo que el tren se detiene es despreciable y
no sera considerado para este problema. Los tipos de trenes se encuentran en el diccionario
tipos, donde la llave es el tipo y el valor una lista con los identificadores unicos de los trenes
que pertenecen a ese tipo. Finalmente, el diccionario trenes contiene como llave el identificador
unico del tren y su valor es una tupla que indica su horario de salida ('HH','MM') desde la
primera estacion de la linea, la Estacion Central de Pythonia.
"""

lineaP = ['Estacion Central',
          'Puente Sal y Santo',
          'Pytronato',
          'La Pysterna',
          'Pynstein',
          'Estadio Nacional',
          'Pio−Pio',
          'Plaza Python Alto']

trenes = {'E07' : ( '09' , '03' ) ,
          'F07' : ( '10' , '14' ) ,
          'H00' : ( '09' , '23' ) ,
          'B00' : ( '08' , '00' ) ,
          'G00' : ( '08' , '46' ) ,
          'C01' : ( '13' , '59' ) ,
          'F08' : ( '11' , '02' )}

tipos = {'Expreso' : [ 'E07','F07','F08'] , 
         'Normal' : [ 'G00', 'H00'] ,
         'Corto' : [ 'B00','C01'] }

"""
Desarrolle la funcion proximos_trenes(est, hor) donde est es un string con el nombre de
la estacion en la que se encuentra el pasajero y  hor es una tupla en formato (’HH’,’MM’) que
indica la hora actual. La funcion debe retornar un diccionario que tenga como llave el identificador 
de todos los trenes que aun no hayan pasado por la estacion actual est a la hora actual hor. El
valor de cada llave corresponde a los minutos que faltan para el arribo del tren a la estacion actual 
est. En caso de no haber trenes para la hora consultada, se debe retornar un diccionario vacio.
"""

def proximos_trenes(est, hor):
    n = 0
    num_est = 0
    for estacion in lineaP:
        if estacion == est:
            num_est = n
        n = n+1
        
    def tipo_tren(tren):
        tipo_final = ''
        for tipo, trenes in tipos.items():
            if tren in trenes:
                tipo_final =  tipo
        if tipo_final == 'Expreso':
            return 2
        elif tipo_final == 'Normal':
            return 5
        else:
            return 7

    diccio = {}
    for tren, horarios in trenes.items():
        hora1, min1 = horarios
        hora2, min2 = hor
        mult = tipo_tren(tren)
        minutos_pasados = mult*(num_est)
        minutos_total_trenes = (int(hora1)*60) + int(min1)
        minutos_total_estacion = (int(hora2)*60) + int(min2)
        if minutos_total_estacion < (minutos_total_trenes+minutos_pasados):
            tiempo = (minutos_total_trenes+minutos_pasados)-minutos_total_estacion
            diccio[tren] = tiempo
    return diccio


print(proximos_trenes('Pytronato', ('09','06')))