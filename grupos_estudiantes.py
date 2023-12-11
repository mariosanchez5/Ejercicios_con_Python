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

#Grupo 1: Estudiantes bajo el promedio
#Grupo 2: Estudiantes sobre el promedio
#Dentro de cada grupo los estudiantes se ordenan por edad de menor a mayor


suma = 0
cont = 0
for ru in curso:
    for i in info_academica:
        rut = i[0]
        priori = i[1]
        if ru == rut:
            suma = suma + priori
            cont = cont + 1
media = suma/cont
#print(media)

grupo1=[]
grupo2=[]
for ru in curso:
    for i in info_academica:
        rut = i[0]
        priori = i[1]
        if ru == rut:
            if priori < media:
                #Grupo1
                grupo1.append(rut)
            else:
                #Grupo2
                grupo2.append(rut)

grupo1_new = []
for rut_est in grupo1:
    for tup in info_personal:
        nombre, rut, fecha = tup
        if rut_est == rut:
            edad = 2023 - fecha[0]
            tupla = (nombre,edad)
            grupo1_new.append(tupla)

grupo2_new = []
for rut_est2 in grupo2:
    for tup in info_personal:
        nombre, rut, fecha = tup
        if rut_est2 == rut:
            edad = 2023 - fecha[0]
            tupla = (nombre,edad)
            grupo2_new.append(tupla)

orden1 = []
min = 100
for tup11 in grupo1_new:
    nombre1, edad1 = tup11
    if edad < min:
        orden1.append(nombre1)

orden2 = []
min = 100
for tup22 in grupo2_new:
    nombre2, edad2 = tup22

print('Grupo 1: ', grupo1_new)
print('Grupo 2: ', grupo2_new)
