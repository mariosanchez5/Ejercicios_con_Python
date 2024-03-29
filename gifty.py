#En el primer paso se mostraran las opciones en pantalla para que el usuario pueda escoger
print('Hola! este el sistema de gestión de inventario de la tienda Gifty')
print()
print('Estas son las opciones que puedes realizar:')
print('1.Agregar un nuevo producto')
print('2.Actualizar información de un producto')
print('3.Eliminar un producto del inventario')
print('4.Visualizar inventario/ Alerta productos bajos en inventario')
print('5.Buscar información de un producto')
print('6.Generar Reporte de Inventario')
print()

#Guardamos la opcion escogida por el usuario en una variable llamada opcion
opcion = int(input('Ingresa el número la opción de la actividad que deseas realizar: '))
print()

#Crearemos un diccionario con los productos existentes en la tienda. Con la siguiente estructura:
#productos = {id:[nombre,precio,cantidad]}
productos = {1:['Pulsera',10000,5],2:['Billetera',45000,10],3:['anillo',30000,2]}

#Crearemos una funcion para cada opcion disponible
def agregar_productos(productos):
    print('A continuación ingresa los datos del producto a agregar:')
    nombre = input('Ingresa el nombre del producto: ')
    precio = int(input('Ingresa el precio del producto: '))
    cantidad = int(input('Ingresa la cantidad de productos: '))
    max_id = max(productos) #Vemos cual es el mayor valor del id, para otorgarle un valor consecuente
    llave = max_id+1 #Le sumamos 1 al mayor valor para que sea distinto
    productos[llave] = [nombre,precio,cantidad] #Agregamos el producto con los datos proporcionados y su llave respectiva
    print('Listo, tu producto fue agregado al inventario.')
    print(productos) #Vemos en pantalla que efectivamente el producto fue agregado correctamente

def actualizar_informacion(productos):
    print('Estos son los productos que hay disponibles: ')
    print(productos) #Mostramos los productos disponibles para que el usuario pueda ver el id del producto que quiere modificar
    id_ingresado = int(input('Ingresa el id del produto a modificar:'))
    for id,lista in productos.items(): #Recorremos el diccionario para extraer su id
        if id == id_ingresado: #Cuando el id del diccionario coincida con el id del producto a modificar ingresamos
            print('A continuación ingresaras los datos del producto, si no quieres modificar algun dato, ingreso los datos que tenía el producto previamente')
            nombre = input("Ingresa el nombre del producto: ")
            precio = int(input('Ingresa el precio del producto: '))
            cantidad = int(input('Ingresa la cantidad del producto: ')) 
            productos[id]=[nombre,precio,cantidad] #Reemplazamos los datos del producto
            print('Tu producto fue modificado exitosamente!')
            print(productos) #Vemos como ha quedado el nuevo diccionario de productos

def eliminar_productos(productos):
    print('Estos son los productos que hay disponibles: ')
    print(productos)
    productos_copia = productos.copy()#Creamos una copia del diccionario original ya que nos daba un error porque no era posible iterar sobre un diccionario que se elimina un elemento
    id_ingresado = int(input('Ingresa el id del produto a eliminar:'))
    for id,lista in productos_copia.items(): 
        if id == id_ingresado:
            del productos[id]
            pass
    print('El producto fue eliminado exitosamente!')
    print(productos)

def visualizar_inventario(productos):
    control = []
    for id,lista in productos.items():
        nombre,precio,cantidad = lista
        print('Producto: {} - Precio: ${} - Cantidad: {}'.format(nombre,precio,cantidad))
        if cantidad < 3:
            control.append([nombre,cantidad])
    print()
    print('Alerta!!!')
    print('Los productos con baja cantidad de stock son:')
    for prod in control:
        nom,cant = prod
        print('Producto: {} - Cantidad: {}'.format(nom,cant))

def buscar_producto(productos):
    print(productos)
    print('Si deseas buscar por nombre ingresa 1')
    print('Si deseas buscar por codigo ingresa 2')
    op = int(input("Ingresa la opción: "))
    if op == 1:
        name = input('Ingresa el nombre del producto a buscar: ')
        for id,lista in productos.items():
            nombre,precio,cantidad = lista
            if nombre == name:
                print('Producto: {} - Precio: ${} - Cantidad: {}'.format(nombre,precio,cantidad))
    elif op == 2:
        cod = int(input('Ingresa el codigo del produto a buscar: '))
        for id,lista in productos.items():
            nombre,precio,cantidad = lista
            if cod == id:
                print('Producto: {} - Precio: ${} - Cantidad: {}'.format(nombre,precio,cantidad))
    else:
        print('La opción no es valida')

def reporte(productos):
    nombre = 'informe.txt'
    
    with open(nombre, 'w') as archivo_txt:
        # Escribimos el encabezado
        archivo_txt.write("ID\tProducto\tPrecio\tStock\n")

        # Escribimos los datos del inventario
        for id, detalles in productos.items():
            linea = f"{id}\t{detalles[0]}\t{detalles[1]}\t{detalles[2]}\n"
            archivo_txt.write(linea)
    
    print(f'Se ha creado el archivo TXT {nombre}')


if opcion == 1:
    agregar_productos(productos)
elif opcion == 2:
    actualizar_informacion(productos)
elif opcion == 3:
    eliminar_productos(productos)
elif opcion == 4:
    visualizar_inventario(productos)
elif opcion == 5:
    buscar_producto(productos)
elif opcion == 6:
    reporte(productos)
else: 
    print("La opción ingresada no es valida")