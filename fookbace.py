'''
La red social Fookbace almacena la información de sus usuarios en un diccionario. 
Las llaves son un código numérico entero asignado a cada usuario, y los valores son tuplas con el nombre, la ciudad y la fecha de nacimiento del usuario. 
La fecha de nacimiento es una tupla (año, mes, día)

Escriba la función misma_ciudad(u1, u2), que indique si los usuarios con códigos u1 y u2 viven en la misma ciudad:
'''

usuarios = {
    522514: ('Jean Dupont',        'Marseille',  (1989, 11, 21)),
    587125: ('Perico Los Palotes', 'Valparaiso', (1990,  4, 12)),
    189471: ('Jan Kowalski',       'Krakow',     (1994,  4, 22)),
    914210: ('Antonio Nobel',      'Valparaiso', (1983,  7,  1)),
    198471: ('Anto Nob',      'Valparaiso', (1985,  7,  1)),
    781118: ('Antoni Nobe',      'Valparaiso', (1983,  7,  1))}

def misma_ciudad(u1, u2):
    for user in usuarios:
        if user == u1:
            nombre1,ciudad1,fecha1 = usuarios[user]
        elif user == u2:
            nombre2,ciudad2,fecha2 = usuarios[user]

    if ciudad1 == ciudad2:
        return True
    else:
        return False

print(misma_ciudad(914210, 587125))
print(misma_ciudad(522514, 189471))

'''
Escriba la función diferencia_edad(u1, u2), que retorne la diferencia de edad entre los usuarios cuyos códigos son u1 y u2. 
(Utilice sólo el año de nacimiento de los usuarios para calcular la diferencia, no el mes ni el día).
'''

def diferencia_edad(u1, u2):
    for user in usuarios:
        if user == u1:
            nombre1,ciudad1,fecha1 = usuarios[user]
        elif user == u2:
            nombre2,ciudad2,fecha2 = usuarios[user]

    return abs(fecha1[0]-fecha2[0])

print(diferencia_edad(914210, 587125))

'''
Para guardar la información sobre cuáles de sus usuarios son amigos entre sí, Fookbace utiliza el conjunto amistades, 
que contiene tuplas con los códigos de dos usuarios. Si la tupla (a, b) está dentro del conjunto, significa que los usuarios con códigos a y b son amigos. 
En todas las tuplas se cumple que a < b.
'''

amistades = {(198471, 289142), (138555, 429900), (289142, 781118)}

'''
Escriba la función obtener_amigos(u), que retorne el conjunto de los códigos de los amigos de u.
'''

def obtener_amigos(u):
    conjunto = set()
    for tup in amistades:
        a,b = tup
        if a == u:
            conjunto.add(b)
        elif b == u:
            conjunto.add(a)
    return conjunto

print (obtener_amigos(429900))



'''
Escriba la función recomendar_amigos(u), que retorne el conjunto de los códigos de los usuarios que cumplen todas estas condiciones a la vez:

son amigos de un amigo de u,
no son amigos de u,
viven en la misma ciudad que u, y
tienen menos de diez años de diferencia con u.

En ambas funciones, el parámetro u es el código de un usuario, y el valor de retorno es un conjunto de códigos de usuarios. 
Recuerde que c.add(x) agrega el valor x al conjunto c.
'''
def obtener_amigos_sinset(u):
    for tup in amistades:
        a,b = tup
        if a == u:
            return b
        elif b == u:
            return a
print (obtener_amigos_sinset(429900))
'''
def recomendar_amigos(u):
    con = set()
    amigo = (obtener_amigos_sinset(u))
    #print (amigo)
    ami_ami = (obtener_amigos_sinset(amigo))
    #print (ami_ami)
    dif = diferencia_edad(amigo, ami_ami)
    print (dif)
    ciu = misma_ciudad(amigo, ami_ami)
    print (ciu)
    if amigo != ami_ami and dif < 10 and ciu == True:
        con.add(ami_ami)
    return con

print('ULTIMA FUNCION')
'''
#print (recomendar_amigos(198471))

def recomendar_amigos(u):
    con = set()
    amigos = obtener_amigos(u)
    for amigo in amigos:
        amigos_de_amigo = obtener_amigos(amigo)
        for amigo_de_amigo in amigos_de_amigo:
            if amigo_de_amigo != u and diferencia_edad(u, amigo_de_amigo) < 10 and misma_ciudad(u, amigo_de_amigo):
                con.add(amigo_de_amigo)
    return con

print (recomendar_amigos(198471))
