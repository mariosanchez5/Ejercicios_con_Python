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

def obtener_multa(catalogo, prestamos,date):
    diccio = {}
    for rut,clasi,fecha in prestamos:
        atraso = 0
        multa = 0
        fecha1 = ((fecha[1]-1)*30)+fecha[0]
        date1 = ((date[1]-1)*30)+date[2]
        dias_pas = date1-fecha1
        for clasi2,name, campus, tipo in catalogo:
            if clasi == clasi2:
                if tipo == 'AD':
                    atraso = dias_pas-2
                    if atraso > 0:
                        multa = atraso * 1000
                    else:
                        multa = 0
                elif tipo == 'CG':
                    atraso = dias_pas-7
                    if atraso > 0:
                        multa = atraso * 500
                    else:
                        multa = 0
                elif tipo == 'CB':
                    atraso = dias_pas-14
                    if atraso > 0:
                        multa = atraso * 100
                    else:
                        multa = 0
                ####        
                if rut in diccio:
                    diccio[rut] = diccio[rut] + multa
                else:
                    diccio[rut] = multa
    return diccio
                
        
        
            

print (obtener_multa(catalogo, prestamos,(2017,6,1)))
print (obtener_multa(catalogo, prestamos,(2017,5,26)))