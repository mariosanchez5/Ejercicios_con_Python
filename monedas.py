"""
Una tienda comercial acepta el pago de sus productos con diferentes tipos de monedas.
Cada tipo de moneda se encuentra en el diccionario moneda cuya llave es el codigo de la moneda ´
y el valor es una tupla de la descripcion de la moneda y el valor de cambio a peso chileno:
"""

monedas = {'US' : ('Dolares Americanos', 500),
 'EUR' : ('Euros', 600),
 'L' : ('Libras', 700),
 'CH' : ('Pesos Chilenos', 1)}

"""Las ventas diarias se encuentran en una lista de tuplas de la forma:"""

venta_diaria = [('US', 50), ('L', 200), ('EUR', 300), ('L', 100),('CH', 21000), ('US', 150), ('EUR', 100)]

"""
Escriba la funcion por_moneda(monedas, venta_diaria) que retorne un diccionario cuya
llave sea la descripcion de la moneda y el valor sea el total diario vendido con esa moneda.
"""

def por_moneda(monedas, venta_diaria):
    diccio = {}
    for moneda,valor in venta_diaria:
        if moneda in diccio:
            diccio[moneda] = diccio[moneda] + valor
        else:
            diccio[moneda] = valor
    return diccio

print(por_moneda(monedas, venta_diaria))

