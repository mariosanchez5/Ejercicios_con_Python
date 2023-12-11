conciertos = set([('Pythonia', 2000), ('Santiago', 15000), ('Pelotillehue', 4000), ('Valparaiso', 5000), ('Vina del mar', 3000)])
entradas = {'Pythonia': (2000, 6000), 'Santiago': (7000, 8000),'Pelotillehue': (100, 4000), 'Valparaiso': (1000, 4000),'Vina del mar': (200, 5000),}

def  menor_publico(conciertos):
    min = 1000000
    for i in conciertos:
        ciu, pub = i
        if pub < min:
            min = pub
            tup = (ciu,pub)
    return (tup)

print(menor_publico(conciertos))
    
def gira(conciertos):
    ordenada = sorted(conciertos, key=lambda x: x[1], reverse=True)
    lista = []
    for i in conciertos:
        ciu, pub = i
        lista.append(ciu)
    return lista

print(gira(conciertos))

