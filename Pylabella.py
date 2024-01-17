"""
La tienda Pylabella maneja la informacion de sus clientes en un diccionario cuya clave 
corresponde al RUT del cliente y su valor a una lista con su informacion. Esta informacion
esta compuesta por el nombre del cliente, su edad, la sucursal donde realiz  o su inscripcion, y 
una tupla con los montos de las tres ultimas compras. Considere la siguiente estructura como
ejemplo:
"""

clientes = {
#RUT: [nombre,edad,sucursal,(monto1,monto2,monto3)]
'16034124-5': ('Fernando Ruiz Diaz', 30,'Vina', (100,200,300)),
'5436576-2': ('Mike Portnoy',20, 'Quilpue', (100, 100, 50)),
'3333333-3': ('Slash', 50,'Vina', (500,550,300)),
'1234567-8': ('Cliff Burton', 35,'Valparaiso', (50,50,100))}

"""
Escriba la funcion misma_sucursal(RUT1,RUT2,clientes) que reciba el RUT de dos clientes,
RUT1 y RUT2, ademas del diccionario clientes y retorne True en caso de que los clientes se
inscribieron en la misma sucursal o False en caso contrario.
"""

def misma_sucursal(RUT1,RUT2,clientes):
    for rut,datos in clientes.items():
        if rut == RUT1:
            sucursal1 = datos[2]
        elif rut== RUT2:
            sucursal2 = datos[2]
    
    if sucursal1==sucursal2:
        return True
    else:
        return False

print(misma_sucursal('16034124-5','3333333-3',clientes))
print(misma_sucursal('5436576-2','3333333-3',clientes))

"""
Escriba la funcion mayores_que(edad_minima,clientes), que devuelva una lista con los
nombres de todos los clientes cuya edad sea mayor o igual al parametro edad_minima.
"""
def mayores_que(edad_minima,clientes):
    lista = []
    for rut,datos in clientes.items():
        edad = datos[1]
        if edad >= edad_minima:
            lista.append(datos[0])
    return lista


print(mayores_que(50,clientes))
print(mayores_que(25,clientes))

"""
Escriba la funcion es_cliente_vip(RUT, monto_compra,clientes), la cual recibe como
parametro el RUT de un cliente, el monto_compra que representa el monto minimo para ser
considerado cliente VIP y el diccionario clientes. Esta funcion debe retornar True si la suma
de las 3 ultimas compras del cliente es superior o igual al  monto_compra, y False en caso
contrario.
"""

def es_cliente_vip(RUT, monto_compra,clientes):
    for rut,datos in clientes.items():
        if RUT == rut:
            compras = datos[3]
            total = 0
            for i in compras:
                total = total + i
            if total >= monto_compra:
                return True
            else:
                return False

print(es_cliente_vip('5436576-2',500,clientes))
print(es_cliente_vip('3333333-3',500,clientes))
print(es_cliente_vip('1234567-8',150,clientes))
