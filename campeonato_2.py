competencia={
'pista':{'v100mt','v400mt','v800mt','v3000mt','d100mt','d400mt'},
'campo':{'vbala','vdisco','vlargo','dbala'} }

puntaje={'lugar 1': 12, 'lugar 2': 9, 'lugar 3': 7, 'lugar 4': 5,
'lugar 5': 4, 'lugar 6': 3, 'lugar 7': 2, 'lugar 8': 1}

resultado={
'usm':[ ('mrios','v400mt',9),('nmassu','v3000mt',12),
('jrojas','vdisco',12)],
'usach':[('jramos','d400mt',5),('lsoto','d400mt',9),
('mruiz','v800mt',7)],
'uc':[ ('mhard','v100mt',3), ('msolis','d3000mt',5),
('lrozas','dbala',5)]}

def participante_prueba(competencia, resultado, prueba):
    lista = []
    campos = competencia['campo']
    pista = competencia['pista']
    for llave,valor in resultado.items():
        for tupla in valor:
            nombre,campo,lugar = tupla
            if prueba == 'campo':
                if campo in campos:
                    lista.append(nombre)
            elif prueba == 'pista':
                if campo in pista:
                    lista.append(nombre)

    return(lista)


print(participante_prueba(competencia, resultado, 'campo'))

def mayor_cantidad(resultado, puntaje):
    lugar_1 = 12
    lugar_2 = 9
    lugar_3 = 7
    tuplas = []
    for u, lista in resultado.items():
        puntaje = 0
        for tup in lista:
            name, prueba, lugar = tup
            puntaje = puntaje + lugar
        tup = (u,puntaje)
        tuplas.append(tup)

    ganador = 0
    for uni,punt in tuplas:
        pass
    print(tuplas)


mayor_cantidad(resultado, puntaje)