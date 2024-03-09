#En el primer paso se mostraran las opciones en pantalla para que el usuario pueda escoger
print('Hola! este el sistema de gestión de inventario de la tienda Gifty')
print('Estas son las opciones que puedes realizar:')
print('1.Agregar un nuevo producto')
print('2.Actualizar información de un producto')
print('3.Eliminar un producto del inventario')
print('4.Visualizar inventario/ Alerta productos bajos en inventario')
print('5.Buscar información de un producto')
print('6.Generar Reporte de Inventario')

#Guardamos la opcion escogida por el usuario en una variable llamada opcion
opcion = int(input('Ingresa el número la opción de la actividad que deseas realizar: '))

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
    pass



if opcion == 1:
    agregar_productos(productos)
elif opcion == 2:
    actualizar_informacion(productos)
elif opcion == 3:
    eliminar_productos(productos)
elif opcion == 4:
    pass
elif opcion == 5:
    pass
elif opcion == 6:
    pass
else: 
    print("La opción ingresada no es valida")