num = int(input('Cuantos alumnos tiene el curso: '))
alumnos = {}

for i in range (num):
    i = i+1
    nombre = input('Ingrese el nombre del alumno número {}: '.format(i))
    c1 = int(input('Ingrese la nota del C1: '))
    c2 = int(input('Ingrese la nota del C2: '))
    c3 = int(input('Ingrese la nota del C3: '))
    alumnos[nombre] = (c1,c2,c3)

def promedio_alum(alumnos):
    for name,notas in alumnos.items():
        ce1,ce2,ce3 = notas
        prom = (ce1+ce2+ce3)/3
        print('El promedio de {} es {}'.format(name,prom))

promedio_alum(alumnos)

def promedio_curso_certamenes(alumnos):
    cer1 = []
    cer2 = []
    cer3 = []
    for name,notas in alumnos.items():
        ce1,ce2,ce3 = notas
        cer1.append(ce1)
        cer2.append(ce2)
        cer3.append(ce3)

    prom_c1 = sum(cer1)/len(cer1)
    prom_c2 = sum(cer2)/len(cer2)
    prom_c3 = sum(cer3)/len(cer3)
    prom_gral = (prom_c1 + prom_c2 + prom_c3) / 3
    print('El promedio del certamen 1 es: {}'.format(prom_c1))
    print('El promedio del certamen 2 es: {}'.format(prom_c2))
    print('El promedio del certamen 3 es: {}'.format(prom_c3))
    print('El promedio general del curso es de :{}'.format(prom_gral))

promedio_curso_certamenes(alumnos)

def aprobados_reprobados(alumnos):
    aprobados = 0
    reprobados = 0
    for name,notas in alumnos.items():
        ce1,ce2,ce3 = notas
        prom = (ce1+ce2+ce3)/3
        if prom >= 55:
            aprobados +=1
        else:
            reprobados +=1
    print('Aprobados:{}'.format(aprobados))
    print('Reprobados:{}'.format(reprobados))

aprobados_reprobados(alumnos)

def ordenar_alum(alumnos):
    alum_ord = {}
    for name,notas in alumnos.items():
        ce1,ce2,ce3 = notas
        prom = (ce1+ce2+ce3)/3
        alum_ord[name]= prom
    
    

