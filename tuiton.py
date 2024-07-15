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