"""
Desarrollar la funcion diferencias_poder(superheroes, diferenciapoder, umbral)
que reciba el diccionario superheroes, el valor diferenciapoder y un valor de umbral. La
funcion debe retornar una lista de tuplas de todos los superheroes que tengan una diferencia de
poder (diferencia min-poder y max-poder) mayor o igual a diferenciapoder y un min-poder
superior al umbral. Cada tupla debe contener nombre, detalle, habilidad y max-poder.
"""

# nombre: [detalle, edad, habilidad, (min-poder, max-poder)]
superheroes = {
'Iron man': ['mk42', 50 , 'uni-rayo', (45, 95)],
'Thor': ['hijo de odin', 10000 , 'mjolnir', (50, 100)],
'Condorito':['de pelotillehue', 40, 'washington', (1, 10)],
'Chapulin Colorado': ['no contaban con mi astucia', 40, 'chipotechillon', (40, 90)]}

def diferencias_poder(superheroes, diferenciapoder, umbral):
    lista = []
    for super,desc in superheroes.items():
        det,edad,hab,pod = desc
        min,max = pod
        dif = max-min
        if dif > diferenciapoder and min > umbral:
            tupla= (super,det,hab,max)
            lista.append(tupla)
    return lista

diferenciapoder = 30
umbral = 39
print(diferencias_poder(superheroes, diferenciapoder, umbral))

"""
Ultron necesita saber quien es amigo de quien. Dos asociados se consideran amigos si cada uno
tiene al otro en el diccionario asociados. Genere una funcion amigos(asociados) que reciba el
diccionario asociados y retorne un diccionario con los amigos, donde la llave es el superheroe y
como valor un conjunto con los amigos de este. Si un superheroe no tiene amigos, no se agrega.
"""

# nombre : nombre_asociados
asociados = {'Iron man': set(['Thor', 'Black Widow', 'Hawkeye', 'Hulk']),
'Thor': set(['Iron man', 'Hulk', 'Chapulin Colorado']),
'Condorito' : set(['Don Chuma', 'Hulk']),
'Chapulin Colorado' : set(['Condorito', 'Thor'])}

def amigos(asociados):
    diccio = {}
    for super, amigos in asociados.items():
        lista = []
        for super2,amigos2 in asociados.items():
            if super!= super2:
                for i in amigos2:
                    if i == super:
                        for a in amigos:
                            if a== super2:
                                lista.append(super2)
                                #print('son amigos',super,super2)
        diccio[super]= set(lista)
    return diccio

print(amigos(asociados))

"""
Gracias a la manipulacion mental de Scarlet Witch, Ultron lograra que los superheroes amigos que
posean una diferencia de poder superior a 40 y ademas que superen un umbral de min-poder de
30 luchen entre ellos. Se pide generar una funcion versus(superheroes, asociados) que
reciba el diccionario superheroes, el diccionario asociados y retorne una lista de tuplas con
los enfrentamientos de los amigos. NOTA: no se deben repetir las parejas.
"""
def versus(superheroes, asociados):
    print('ULTIMA FUNCION!!!!!!!!!!!!!!!!')
    lista = diferencias_poder(superheroes, 40, 30)
    amigos_dict = amigos(asociados)
    batalla=[]
    for super1,det,hab,pod in lista:
        for super, amig in amigos_dict.items():
            if super1 == super:
                for i in amig:
                    for super2,det2,hab2,pod2 in lista:
                        if super2==i:
                            tupla2 = (super1,i) 
                            tupla3 = (i,super1)
                            if tupla2 not in batalla and tupla3 not in batalla:
                                batalla.append(tupla2)
    return batalla

print(versus(superheroes,asociados))