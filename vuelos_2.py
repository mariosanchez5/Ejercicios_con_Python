vuelos = {
# codigo: destino, fecha (anno, mes, dia) , distancia (km)
140: ('Cancun', (2013, 6, 28), 6751),
141: ('Rio de Janeiro', (2013, 6, 13), 2772),
142: ('New York', (2013, 9, 12), 7546),
143: ('Tokio', (2013, 8, 17), 14248),
144: ('New York', (2014, 1, 1), 3792),
145: ('Rio de Janeiro', (2013, 12, 20), 2819),
146: ('Punta Cana', (2013, 8, 18), 5444)
}

itinerario = {
# pasajero, vuelos por realizar
"Daniel": {140,146},
"Juan": {144,140},
"Rodrigo": {142,144,141},
"Pedro": {145,146}
}

def  vuelo_mas_tardio(vuelos):
    fecha_min = 0
    vuelo_min = 0
    for llave,valor in vuelos.items():
        destino, fecha, km = valor
        if fecha_min < fecha[0]:
            fecha_min = fecha[0]
            vuelo_min = llave
    return vuelo_min, fecha_min

print(vuelo_mas_tardio(vuelos))

def kilometros_por_volar(pasajero,itinerario,vuelos):
    dist_total = 0
    lista = []
    for llave,valor in itinerario.items():
        if llave == pasajero:
            for i in valor:
                #print(i)
                for llave2, valor2 in vuelos.items():
                    if i == llave2:
                        destino, fecha, km = valor2
                        dist_total = dist_total + km
                        lista.append(km)
    print(lista)
    print(dist_total)
    

kilometros_por_volar("Rodrigo", itinerario, vuelos)