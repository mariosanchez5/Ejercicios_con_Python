"""
El producto interno de dos listas de números es la suma 
de los productos de los términos correspondientes de ambas
"""

"""
Escriba la función producto_interno(a, b) que entregue el producto interno de a y b:
"""

def producto_interno(a,b):
    contador = 0
    producto = 0
    if len(a) == len(b):
        largo = len(a)
        while contador < largo:
            producto = producto + (a[contador]*b[contador])
            contador = contador + 1
        return producto
    else:
        print('La lista de numeros debe ser de la misma extension')


a = [7,1,4,9,8]
b = range(5)

print('Producto interno de prueba: ',producto_interno(a,b))


a1 = 0
b1 = 0
a = []
b = [] 
while a1 != 'f':
    a1 = str(input('Ingresa la lista de a un valor (ingresa f para terminar): '))
    if a1 != 'f':
        a.append(int(a1))
while b1 !='f':    
    b1 = str(input('Ingresa los valores de la segunda lista de a un valor (ingresa f para terminar): '))
    if b1 != 'f':
        b.append(int(b1))


print('El producto interno de la lista a ',a,' y la lista b ',b,' es igual a:',producto_interno(a,b))


"""
Dos listas de números son ortogonales si su producto interno es cero. 
Escriba la función son_ortogonales(a, b) que indique si a y b son ortogonales
"""

def son_ortognales(a,b):
    if producto_interno(a,b) == 0:
        return True
    else:
        return False

print(son_ortognales(a,b))