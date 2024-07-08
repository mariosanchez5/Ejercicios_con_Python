"""
Inversiones RCaray esta siendo investigada por una presunta estafa millonaria. Su presidente 
genero una asociacion ilicita utilizando los dineros de cientos de personas durante los tres
ultimos anos por medio de varias empresas fantasma. Las investigaciones pudieron reunir una 
informacion parcial acerca de las personas y las sumas de dineros involucradas. La policia ha
recaudado esta informacion en una lista llamada esta f ados, la que almacena tuplas de la forma
(rut, deuda, empresa, f echa), donde rut esta en formato string, deuda en formato entero, empresa
en formato string y fecha es una tupla (dd, mm, aaaa). A continuacion se muestra un ejemplo de
la estructura esta fados:
"""

estafados = [('12.234.567-8', 2000000, 'pelados_furiosos', (25, 5, 2015)),
             ('9.111.567-k', 5500000, 'multibank', (1, 10, 2014)),
             ('14.987.007-1', 100000000, 'inversiones_seguras', (30, 11, 2016)),
             ('12.234.567-8', 10000000, 'multibank', (2, 7, 2015)),
             ('12.234.567-8', 2500000, 'multibank', (18, 1, 2016))]

"""
Una misma persona pudo ser estafada por varias empresas en distintas fechas. De acuerdo a la
informacion anterior, se le solicita implementar las siguientes funciones: 
"""

"""
estafado por(lista,rut), funcion que recibe 2 parametros, la lista de tuplas estafados y un string
correspondiente al rut de la persona. Esta debe retornar una lista con las distintas empresas que
estafaron a la persona con dicho rut. En caso de que el rut ingresado no se encuentre, entregar el
mensaje: ”Rut no estafado”.
"""

def estafado_por(lista,rut):
    lista2 = []
    for tupla in lista:
        rut2, monto, empresa, fecha = tupla
        if rut == rut2:
            lista2.append(empresa)

    if len(lista2) > 0:
        return lista2
    else:
        print('Persona no estafada')

print(estafado_por(estafados, '12.234.567-8'))
print(estafado_por(estafados, '19.678.222-2'))