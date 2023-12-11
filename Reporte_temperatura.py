temp = {
  'Vina del Mar':  ( 9, 26),
  'Valparaiso':    (10, 24),
  'Quilpue' :      ( 7, 30),
  'Olmue':         ( 5, 29),
  'Limache':       ( 9, 23),
  'Villa Alemana': ( 9, 22),
}

fecha = (2022,11,30)
dicc = {}


def mayusculas (temp):
    for ciudad, temperatura in temp.items():
        if temperatura[1] > 25:
            #ciudad = ciudad.upper()
            dicc[ciudad.upper()] = temperatura
        else:
            dicc[ciudad]=temperatura
    return dicc

dicc = mayusculas(temp)
#print (dicc)

def crear_reporte (fecha, dicc):
    archivo = open('reporte-{}-{}-{}.text'.format(fecha[0],fecha[1],fecha[2]),'w')
    for ciu, tem in dicc.items():
        archivo.write('{}: max:{} min:{}\n'.format(ciu,tem[1],tem[0]))
    archivo.close()

crear_reporte(fecha,dicc)