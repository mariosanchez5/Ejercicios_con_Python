vuelos = [(10, (2014,1,2)), (11, (2014,1,2)), (12, (2014,1,3)), (13, (2014,5,1)), (14, (2014,5,1))]
destinos = { 10:{('Lima','Peru'), ('San Jose','Costa Rica'), ('Los Angeles','USA')}, 11:{('San Jose','Costa Rica'), ('C. de Panama','Panama')}, 12:{('Sao Paulo','Brasil'), ('San Jose','Costa Rica')}, 13:{('Lima','Peru'), ('San Jose','Costa Rica'), ('C. de Panama','Panama')}, 14:{('San Jose','Costa Rica'), ('Buenos Aires','Argentina')}}

def vuelos_a_destino(destino, fecha):
    lista =[]
    for llave, valor in destinos.items():
        if destino in valor:
            #print('funciona')
            lista.append(llave)
    final = []
    for i in lista:
        for fly,date in vuelos:
            if fly == i and date == fecha:
                final.append(fly)
    print(final)
        

vuelos_a_destino(('San Jose', 'Costa Rica'), (2014,5,1))

"""    
    for i in vuelos:
        fly,date = i
        if date == fecha:
            vuelo = fly
"""