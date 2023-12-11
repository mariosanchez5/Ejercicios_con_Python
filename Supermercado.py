#La lista productos tiene el código, el nombre, el precio y la cantidad de unidades del producto en bodega
productos = [
    (41419, 'Fideos',        450, 210),
    (70717, 'Cuaderno',      900, 119),
    (78714, 'Jabon',         730, 708),
    (30877, 'Desodorante',  2190,  79),
    (47470, 'Yogur',          99, 832),
    (50809, 'Palta',         500,  55),
    (75466, 'Galletas',      235,   0),
    (33692, 'Bebida',        700,  20),
    (89148, 'Arroz',         900, 121),
    (66194, 'Lapiz',         120, 900),
    (15982, 'Vuvuzela',    12990,  40),
    (41235, 'Chocolate',    3099,  48),
]

#La lista clientes tiene el rut y el nombre de los clientes del supermercado
clientes = [
    ('11652624-7', 'Perico Los Palotes'),
    ( '8830268-0', 'Leonardo Farkas'),
    ( '7547896-8', 'Fulanita de Tal'),
]

#La lista ventas contiene las ventas realizadas, representadas por el número de boleta, la fecha de la venta y el rut del cliente
ventas = [
    (1, (2010,  9, 12),  '8830268-0'),
    (2, (2010,  9, 19), '11652624-7'),
    (3, (2010,  9, 30),  '7547896-8'),
    (4, (2010, 10,  1),  '8830268-0'),
    (5, (2010, 10, 13),  '7547896-8'),
    (6, (2010, 11, 11), '11652624-7'),
]

#El detalle de cada venta se encuentra en la lista itemes. Cada ítem tiene asociado un número de boleta, un código de producto y una cantidad
itemes = [
    (1, 89148,  3),
    (2, 50809,  4),
    (2, 33692,  2),
    (2, 47470,  6),
    (3, 30877,  1),
    (4, 89148,  1),
    (4, 75466,  2),
    (5, 89148,  2),
    (5, 47470, 10),
    (6, 41419,  2),
]

def producto_mas_caro(productos):
    caro = 0
    p_caro = ''
    for n in productos:
     codigo, producto, precio, cantidad = n
     if precio > caro:
        caro = precio
        p_caro = producto
    return caro, p_caro

def valor_total_bodega(productos):
    total = 0
    for n in productos:
     codigo, producto, precio, cantidad = n
     total = total + (precio*cantidad)
    return total

def ingreso_total_por_ventas(itemes, productos):
    total = 0
    for n in itemes:
        boleta, codigo_i, cantidad_i = n
        for i in productos:
            codigo_p, producto, precio, cantidad_p = i
            if codigo_i == codigo_p:
                total = total + (cantidad_i * precio)
    return total

def producto_con_mas_ingresos(itemes, productos):
    mas_i = 0
    mas_p = ''
    for n in itemes:
        boleta, codigo_i, cantidad_i = n
        for i in productos:
            codigo_p, producto, precio, cantidad_p = i
            if codigo_i == codigo_p:
                if (cantidad_i * precio) > mas_i:
                    mas_i = cantidad_i * precio
                    mas_p = producto
    return mas_p

def cliente_que_mas_pago(itemes, productos, clientes):
    boleta_mas = 0
    mas_recog = 0
    for n in itemes:
        boleta, codigo_i, cantidad_i = n
        for i in productos:
            codigo_p, producto, precio, cantidad_p = i
            boleta_mas = boleta
            mas_recog = cantidad_i*precio
        for x in itemes:
            boleta_x, codigo_i_x, cantidad_i_x = x
            if boleta == boleta_x:
                for i in productos:
                    codigo_p, producto, precio, cantidad_p = i
                    mas_recog = mas_recog + cantidad_i*precio
    print (boleta_mas,mas_recog)



def total_ventas_del_mes(agno, mes, itemes, productos):
    pass

def fecha_ultima_venta_producto(codigo, itemes, ventas):
    pass

print (producto_mas_caro(productos))
print (valor_total_bodega(productos))
print (ingreso_total_por_ventas(itemes, productos))
print(producto_con_mas_ingresos(itemes, productos))
print (cliente_que_mas_pago(itemes, productos, clientes))