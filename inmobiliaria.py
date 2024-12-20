"""
Construir una función que permita hacer búsqueda de inmuebles en función de un 
presupuesto dado. La función recibirá como entrada la lista de inmuebles y un precio, 
y devolverá otra lista con los inmuebles cuyo precio sea menor o igual que el dado. 
Los inmuebles de la lista que se devuelva deben incorporar un nuevo par a cada diccionario 
con el precio del inmueble, donde el precio de un inmueble se calcula con las siguiente 
fórmula en función de la zona:

Zona A: precio = (metros * 1000 + habitaciones * 5000 + garaje * 15000) * (1-antiguedad/100)
Zona B: precio = (metros * 1000 + habitaciones * 5000 + garaje * 15000) * (1-antiguedad/100) * 1.5
"""

inmuebles = [{'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'},
{'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'},
{'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'},
{'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'},
{'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}]

agno_actual = 2025
for i in inmuebles:
    agno = i['año']
    metros = i['metros']
    habitaciones = i['habitaciones']
    garaje = i['garaje']
    zona = i['zona']
    antiguedad = int(agno_actual) -  int(agno)
    if zona == 'A':
        precio_zona_a = (metros * 1000 + habitaciones * 5000 + garaje * 15000) * (1-antiguedad/100)
        i['precio']= precio_zona_a
    else:
        precio_zona_b = (metros * 1000 + habitaciones * 5000 + garaje * 15000) * (1-antiguedad/100) * 1.5
        i['precio']= precio_zona_a

def funcion(inmuebles, precio):
    lista = []
    for i in inmuebles:
        precio_dado = i['precio']
        if precio_dado <= precio:
            lista.append(i)
    return lista

print(funcion(inmuebles, 80000))


