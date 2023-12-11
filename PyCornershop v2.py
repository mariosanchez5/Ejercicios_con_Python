'''
Para que la PyCornerShop pueda funcionar de manera eficiente, le solicita a Ud. que implemente
una funcion llamada buscar repartidor(usuarios,repartidores,codigo) que reciba
como parametros las listas antes mencionadas y un codigo de usuario. La funcion debe retornar
una lista de repartidores disponibles y cercanos, ordenados de manera descendente, segun el
numero de visitas que hayan realizado al usuario indicado. Un repartidor se considera cercano
si esta ubicado a menos de 4 km del usuario y para esto considere que las tuplas de ubicacion
tienen valores enteros medidos en km. Finalmente, si no hay repartidores cercanos, la funcion
debe retornar una lista vacia.

Ocupar formula de distnacia
'''

usuarios = [(1221, (5, 2)), (441, (8, 2)), (587, (10, 1))]

repartidores = [
('rayo macuin', (10, 2), True, [(1221, 5), (441, 8), (587, 2)]),
('reparti dhor', (9, 3), True, [(1221, 2), (441, 5), (587, 3)]),
('eliseo al-azar', (5, 5), False, [(1221, 8), (441, 2)])]

num = 441

def distancia(a,b):
    x1,y1 = a
    x2,y2 = b
    var = ((x1-x2)**2)+((y1-y2)**2) 
    dist = var**(1/2)
    return dist

def orden (diccionario):
    lista = []
    lista2 = []
    for llave in diccionario:
        lista.append(diccionario[llave])
    #print(lista)
    lista.sort()
    lista.reverse()
    #print(lista)
    for i in lista:
        for llave in diccionario:
            if i == diccionario[llave]:
                lista2.append(llave)
    return lista2




def buscar_repartidor (usuarios,repartidores,num):
    max = 0
    lista=[]
    dicc = {}
    for us in usuarios:
        usuario, coordenada = us
        #print (usuario)
        #print (coordenada)
        if usuario == num:
            for rep in repartidores:
                repartidor, ubic, estado, viajes = rep
                if estado == True:
                    #print(distancia(coordenada,ubic))
                    if distancia(coordenada,ubic) < 4:
                        for i in viajes:
                            cliente, veces = i
                            if cliente == num:
                                lista.append(repartidor)
                                dicc[repartidor]= veces
                                #max = veces
                else:
                    pass
        else:
            pass
    #print(dicc)
    return (orden (dicc))
    #return sorted(dicc)


print(buscar_repartidor(usuarios,repartidores,num))


