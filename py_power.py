# surtidor: [(litros venta, dia), ...],
gasolinera = { 1: [(43.3, 1), (28.2, 3)], 2: [(45.0, 2), (34.9, 3),(41.5, 4)], 6: [(16.0, 2), (21.5, 5), (45.0, 2)], 5: [], 4: [(5.2,10)], 9: [(15.2, 1), (2.5, 1)]}

surtidores = {(4, 'Py-power'), (9, 'diesel'), (2, '95'), (1, '93'), (6,'97'), (5, 'Py-power')}

def diccionario_bencinas(surtidores):
    diccio = {}
    for surtidor, tipo in surtidores:
        if tipo in diccio:
            lista.append(surtidor)
            diccio[tipo]= lista
        else:
            lista = []
            lista.append(surtidor)
            diccio[tipo]= lista
    return diccio

print(diccionario_bencinas(surtidores))

p= {'93': 38, 'diesel': 54, '95': 41, 'Py-power': 49, '97': 45}

def mayor_beneficio(gasolinera, surtidores, p):
    total = 0
    diccio_t = {}
    diccio_surt = diccionario_bencinas(surtidores)
    for tipo,surt in diccio_surt.items():
        for i in surt:
            for surt_2, lista in gasolinera.items():
                if surt == surt_2:
                    for litro, dia in lista:
                        total = total + litro
        diccio_t[tipo]=total
    print(diccio_t)

mayor_beneficio(gasolinera, surtidores, p)

        