"""
Las Bibliotecas USM poseen un sistema de prestamo y devolucion de libros para alumnos,
funcionarios y profesores. Su catalogo de libros esta dado por la lista de tuplas catalogo, donde
cada tupla tiene el numero de clasificacion, nombre, campus y tipo de prestamo para un libro en
particular.
"""

catalogo = [('010.245C1', 'Programacion en Python', 'CCV', 'AD'),
('145.261D7', 'Algebra Lineal', 'CSJ', 'CB'),
('121.748F2', 'Fisica Universitaria', 'CSV', 'CG')]

"""
El tipo de prestamo puede ser AD (Alta Demanda), CG (Coleccion General) o CB (Coleccion
Basica) con devolucion en 2, 7 y 14 dias despues de la fecha de prestamo, respectivamente. Los
prestamos vigentes de libros se manejan en la estructura prestamos, donde se guarda el rut del
usuario, el numero de clasificacion y la fecha de prestamo en el formato  (dia, mes, ano).
"""
prestamos = {('12422532-2', '145.261D7', (24, 5, 2017)),
('14025935-K', '145.261D7', (13, 5, 2017)),
('12422532-2', '010.245C1', (10, 5, 2017))}

"""
A continuacion, se desea conocer para  una fecha de consulta posterior a la fecha de todos
los prestamos del sistema, la multa que le corresponde a cada usuario por no devolver uno o 
varios libros a tiempo. Para ello debe crear la funcion obtener multa(catalogo, prestamos,
fecha consulta) que reciba como parametros el catalogo de libros, los prestamos registrados 
en el sistema y la fecha de consulta como una tupla en el formato (ano, mes, dia). Esta
funcion debe entregar un diccionario, cuyas llaves corresponden a los ruts de los usuarios de 
la biblioteca y el valor corresponde a un entero con el monto adeudado. Ademas, considere lo 
siguiente:
La multa por dia de atraso corresponde a $1000, $500 y $100 para los libros de Alta Demanda,
Coleccion General y Coleccion Basica, respectivamente. 
Todos los meses del ano tienen 30 dias.
Usted puede crear las funciones que estime necesarias para la resolucion de este problema.
"""

def obtener_multa(catalogo, prestamos,fecha):
    pass

print (obtener_multa(catalogo, prestamos,(2017,6,1)))