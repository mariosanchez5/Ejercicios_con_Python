info_personal = [ ('Andrea Campos', '17.345.908-7', (1990,4,12)),
('Raquel Salinas', '16.231.998-k', (1987,1,12)),
('Pedro Meza', '12.677.800-3', (1975,10,8)),
('Daniel Varas', '15.123.567-9', (1991,3,30)),
('Sergio Pezoa', '9.990.234-1', (1982,12,24)),
('Alvaro Vasquez', '18.836.902-k',(1988,8,8))]

info_academica = [ ['17.345.908-7', 6743], ['12.677.800-3', 7990],
['9.990.234-1', 2455], ['16.231.998-k', 4500],
['15.123.567-9', 5431], ['18.836.902-k', 4998]]

curso = [ '17.345.908-7', '9.990.234-1', '16.231.998-k',
'15.123.567-9','18.836.902-k']

promedio = []
for rut in curso:
    for lista in info_academica:
        if rut == lista[0]:
            promedio.append(lista[1])

promedio = sum(promedio)/len(promedio)
print(promedio)

grupo1=[]
grupo2=[]
for lista in info_academica:
    if lista[1] >= promedio and lista[0] in curso:
        grupo2.append(lista[0])
    elif lista[1] < promedio and lista[0] in curso:
        grupo1.append(lista[0])

print('Promedio: ',promedio)
print('Grupo 1: ', grupo1)
print('Grupo 2: ', grupo2)

def order_lista(grupo, info_personal):
    diccio={}
    for i in grupo:
        for tupla in info_personal:
            if i == tupla[1]:
                diccio[i]=tupla[2]
    return(sorted(diccio.items(), key=lambda item: item[1]))

or1= order_lista(grupo1, info_personal)
or2= order_lista(grupo2, info_personal)
print(or1)
print(or2)


lista_grupo1=[]
lista_grupo2=[]
for i in or1:
    for tupla in info_personal:
        if i[0] == tupla[1]:
            lista_grupo1.append(tupla[0])
for i in or2:
    for tupla in info_personal:
        if i[0] == tupla[1]:
            lista_grupo2.append(tupla[0])

print(lista_grupo1)
print(lista_grupo2)



