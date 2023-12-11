alumnos = [
('201021056-k', 'fis100', 60), ('201304119-3', 'mat021', 85),
('201341039-4', 'mat021', 49), ('201304119-3', 'iwi131', 98),
('201341039-4', 'qui010', 60), ('201021056-k', 'mat021', 68),
('201341039-4', 'fis100', 56), ('201021056-k', 'qui010', 70),
('201021056-k', 'elo270', 82), ('201304119-3', 'fis100', 80)
]

def promedio_asignatura(asignatura,alumnos):
    contador = 0
    suma = 0
    for tup in alumnos:
        rol,asigna,prom = tup
        if asigna == asignatura:
            suma = suma + prom
            contador = contador + 1
    return round(suma/contador,0)

print(promedio_asignatura('mat021',alumnos))

def resumen_academico_semestral(rol,alumnos):
    dicci = {}
    for tup in alumnos:
        rola,asigna,prom = tup
        if rola == rol:
            dicci[asigna]=prom
    return dicci

print(resumen_academico_semestral('201021056-k',alumnos))

def resumen_asignaturas(alumnos,ramos):
    lista = []
    for ramo in ramos:
        suma = 0
        cont = 0
        for tup in alumnos:
            rol,asigna,prom = tup
            if ramo == asigna:
                suma = suma + prom
                cont = cont + 1
        tup = (ramo, round(suma/cont,0))
        lista.append(tup)
    return(lista)

print(resumen_asignaturas(alumnos, ["iwi131","fis100","mat021"]))