#Un profesor guarda las notas de sus alumnos en una lista de diccionarios, por ejemplo:

alumnos = [
    {"nombre": "Pedro", "notas": [4.5, 5.0, 6.0]},
    {"nombre": "Juan", "notas": [3.5, 4.0, 4.2]},
    {"nombre": "Diego", "notas": [6.0, 6.5, 7.0]}
]

"""
El programa debe:
Calcular el promedio de cada alumno.
Mostrar al alumno con el promedio más alto y el más bajo.
Preguntar al usuario un nombre y mostrar su promedio 
(si no existe, mostrar un mensaje adecuado).
"""
dict_promedios = {}
for alumno in alumnos:
    nombre = alumno["nombre"]
    notas = alumno["notas"]
    promedio = sum(notas) / len(notas)
    dict_promedios[nombre] = round(promedio,2)

print(dict_promedios)

max_alumno = max(dict_promedios, key=dict_promedios.get)
min_alumno = min(dict_promedios, key=dict_promedios.get)
print(f"El alumno con el promedio más alto es {max_alumno} con un promedio de {dict_promedios[max_alumno]}")
print(f"El alumno con el promedio más bajo es {min_alumno} con un promedio de {dict_promedios[min_alumno]}")

usuario = input("Ingrese el nombre del alumno: ")
if usuario in dict_promedios:
    print(f"El promedio de {usuario} es {dict_promedios[usuario]}")
else:
    print(f"No existe un alumno con el nombre {usuario}.")