"""
El servicio de inteligencia de la UTFSM ha detectado una amenaza inminente a sus
instalaciones por parte de un grupo terrorista que busca impedir que la universidad se convierta
en el mejor centro educacional del mundo. Dada la gravedad de esta amenaza, se ha solicitado
que la division de agentes “IWI-131” analice los datos obtenidos por los infiltrados que el servicio
de inteligencia posee en otras universidades. Los datos con los que se trabajara se encuentran
en un diccionario llamado terroristas (variable global) que tiene por llave el identificador de
cada terrorista y, por valor, una lista de tuplas que indica las universidades en las que ha sido
visto el terrorista junto con la fecha correspondiente.
terroristas = {
2352: [('Stanfox', '2010-05-02'), ('Hardyard', '2010-06-07'), (
'Yon Jopkins', '2010-05-02')],
1352: [('Stanfox', '2010-05-02'), ('Stanfox', '2011-06-08')],
352: [('Hardyard', '2009-03-03')],
22: [('Yon Jopkins', '2012-11-16')]}
Un diccionario llamado experticias (variable global) que tiene por llave el identificador de
cada terrorista y, por valor, la experticia de dicho terrorista.
experticias = { 2352: 'TNT', 1352: 'TNT', 352: 'rayos laser', 22: '
teletransportacion'}
"""

"""
Desarrolle la funcion terroristas_se_conocen(terrorista1, terrorista2) que reciba
como parametros los identificadores de dos terroristas y que retorne True si ambos se conocen o
False si no. Dos terroristas se conocen si ambos han sido vistos en el mismo lugar en la misma
fecha.
"""

terroristas = {
2352: [('Stanfox', '2010-05-02'), ('Hardyard', '2010-06-07'), (
'Yon Jopkins', '2010-05-02')],
1352: [('Stanfox', '2010-05-02'), ('Stanfox', '2011-06-08')],
352: [('Hardyard', '2009-03-03')],
22: [('Yon Jopkins', '2012-11-16')]}

experticias = { 2352: 'TNT', 1352: 'TNT', 352: 'rayos laser', 22: 'teletransportacion'}

def terroristas_se_conocen(terrorista1, terrorista2):
    defecto = False
    for iden, lista in terroristas.items():
        if terrorista1 == iden:
            for tupla in lista:
                u,fecha = tupla
                for iden2, lista2 in terroristas.items():
                    if terrorista2 == iden2:
                        for tupla2 in lista2:
                            u2,fecha2 = tupla2
                            if u==u2 and fecha==fecha2:
                                #print('Se conocen')
                                defecto = True
                            #else:
                                #print('No se han visto')
        return defecto

print(terroristas_se_conocen(2352, 1352))
print(terroristas_se_conocen(2352, 352))