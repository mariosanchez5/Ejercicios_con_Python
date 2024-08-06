"""
El exitoso juego Pukamon GOES entra en etapa de actualizacion, para implementar batallas
entre entrenadores que poseen diversos Pukamones. Para esto se utilizar a la informacion contenida 
en las siguientes estructuras: El diccionario pukadex contiene como llave el nombre del Pukamon,
y como valor una tupla con el tipo principal, el tipo secundario y el numero del pukamon (el tipo 
secundario no siempre esta presente). El diccionario relacion contiene como llave el tipo de un
Pukamon, y como valor una tupla con todos los tipos de Pukamon que son debiles respecto a la
llave.
"""

pukadex = {'Pukachu1S': ('Electrico','Psiquico','026'),
           'Bulmasaur': ('Planta','Veneno','001'),
           'Kaku Topo': ('Electrico','Hada','785'),
           'NewTwo': ('Psiquico','','150'),
           'Pukachu': ('Electrico','','025'),
           'Escuartul': ('Agua','','007'),
           'Lukagrio': ('Pelea','Metal','448'),
           'Chorizard': ('Fuego','Volador','006'),
           'Donphunk': ('Tierra','','232')}

relacion = { 'Dragon': ('Dragon'),
            'Fuego': ('Planta','Hielo','Bicho','Metal'),
            'Electrico': ('Agua','Volador'),
            'Volador': ('Planta','Pelea','Bicho'),
            'Agua': ('Fuego','Tierra','Roca')}

"""
Desarrollar la funcion pukamones tipo(pukadex,tipo) que retorna una lista de tuplas con
todos los Pukamones del tipo tipo ordenados ascendentemente por numero de Pukamon. 
Debe respetar el formato y los tipos de datos del ejemplo
"""

def pukamones_tipo(pukadex,tipo):
    lista = []
    for llave, valor in pukadex.items():
        tipo_1,tipo_2,num = valor
        if tipo_1 == tipo:
            lista.append((int(num),llave))

    lista_ordenada = sorted(lista)
    return(lista_ordenada)

print(pukamones_tipo(pukadex,'Electrico'))


"""
Desarrollar la funcion tipos desventaja(tipo1,tipo2,relacion), la cual retorna un conjunto de tipos de Pukamon que son debiles respecto del tipo1 o tipo2 de un Pukamon.
Nota: tipo1 y tipo2 seran siempre strings no vacios definidos en el diccionario relacion
"""

def tipos_desventaja(tipo1,tipo2,relacion):
    lista = []
    for llave, valor in relacion.items():
        if llave == tipo1 or llave == tipo2:
            for debilidad in valor:
                lista.append(debilidad)
    
    return(set(lista))

print(tipos_desventaja('Fuego','Volador',relacion))

"""
Desarrollar la funcion pukamones desventaja(pukadex,relacion,pukamon) cuyo valor
de retorno es una lista de todos los pokemones debiles respecto al Pukamon pukamon. La
lista debe estar ordenada por el numero del Pukamon.
"""

def pukamones_desventaja(pukadex,relacion,pukamon):
    lista = []
    for llave, valor in pukadex.items():
        if llave == pukamon:
            tipo1,tipo2,num = valor
            for llave2, valor2 in relacion.items():
                if tipo1 == llave2 or tipo2 == llave2:
                    for desv in valor2:
                        for llave_1, valor_1 in pukadex.items():
                            tipo1_2, tipo2_2, num2 = valor_1
                            if desv == tipo1_2 or desv == tipo2_2:
                                lista.append((int(num2),llave_1))
    return(lista)

print(pukamones_desventaja(pukadex,relacion,'Escuartul'))