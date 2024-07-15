"""
En la red social tuiton, un usuario puede seguir a muchos otros usuarios. Esta informacion
se encuentra en el siguiente diccionario:
"""

tuiton = {# usuario: conjunto de usuarios a quienes sigue
    '@progra_usm': {'@kena123', '@anamontain'},
    '@luismi': {'@huaiqui', '@jvivar'}, 
    '@jvivar': {'@anamontain', '@progra_usm'},
    '@huaiqui': {'@anamontain', '@luismi'},
    '@anamontain': {'@luismi', '@progra_usm', '@huaiqui'},
    '@kena123': {'@luismi', '@huaiqui'}}

"""
Por ejemplo, @jvivar sigue a @anamountain y @progra_usm. Note ademas que @luismi
sigue a @jvivar, pero no al reves
"""

"""
Implemente la funcion numero_de_seguidores(usuario, tuiton) que retorne
la cantidad de personas que siguen a usuario.
"""

def numero_de_seguidores(usuario, tuiton):
    cantidad = 0
    for llave, valor in tuiton.items():
            for seguido in valor:
                if usuario == seguido:
                    cantidad = cantidad + 1
    return cantidad

print(numero_de_seguidores('@luismi', tuiton))

"""
Implemente la funcion son_amigos(usuario1, usuario2, tuiton) que retorne
True si usuario1 y usuario2 se siguen mutuamente; de lo contrario, retornar False.
"""

def son_amigos(usuario1, usuario2, tuiton):
    for llave, valor in tuiton.items():
         if llave == usuario1:
            for seguido in valor:
                 if seguido == usuario2:
                      one = True

    for llave2, valor2 in tuiton.items():
         if llave2 == usuario2:
            for seguido2 in valor2:
                 if seguido2 == usuario1:
                      two = True

    if one == True and two == True:
         return True
    else:
         return False

print(son_amigos('@anamontain', '@huaiqui', tuiton))