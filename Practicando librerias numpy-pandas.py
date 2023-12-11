import numpy as np

#Array similar a las listas, pero mucho mas rápido ideal para procesar vectores y matrices de grandes dimensiones - Debe tener mismo tipo de dato
# Array se ocupa para vectores y matrices -- En pandas para formar dataframe
lista = [1,2,3,4,5]
lista2 = [[6,7,8,9,10],[11,12,13,14,15]]
mi_array = np.array(lista)
mi_matriz = np.array(lista2)
print(mi_array)
print(mi_matriz)

print(np.empty(5))
print(np.zeros(5)) #Vector de 5 zeros
print(np.ones(5))  #Vector de 5 unos
print(np.full(5,5)) #Vector de 5 5
print(np.identity(5)) #Matriz identidad de 1
print(np.arange(1,10,2)) #Vecor que comienza en 1 y termina en 10 de 2 en 2
print(np.linspace(1,10,2))
print(np.random.random(5)) #Vector de 5 con numeros aleatorios

print(mi_matriz.ndim) #Dimension
print(mi_matriz.shape) #Tupla dimension
print(mi_matriz.size) #Cantidad elementos
print(mi_matriz.dtype) #Tipo de array

#Tambien se puede tener acceso a los array igual que las listas
#Filtar un elementos similiar a las listas a[condicion]
#Operaciones matematicas con los array sumar restar etc
mi_array = mi_matriz

#Algebra matricial
#print(mi_array @ mi_matriz)
#print(mi_array.dot(mi_matriz))
print(np.linalg.norm(mi_matriz))
print(mi_array.T)
#print(mi_matriz.trace())
#print(np.linalg.det(mi_matriz))
#print(np.linalg.inv(mi_matriz))
#print(np.linalg.eigvals(mi_matriz))
#print(np.linalg.eig(mi_matriz))
#print(np.linalg.solve(mi_array, mi_matriz))

#################################################################################   PANDAS   #########################################################33
import pandas as pd
print('VAMOS CON PANDASSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS')
#Tenemos basicamente 3 estructuras
#Series: estructuras de una dimension, similar a Array * pero esta tiene un indice para cada valor - Deben tener mismo tipo de datos
#Dataframe: tablas - cada columa es una serie ej:edad (mismo tipo de datos, puros numeros) - Contiene dos indices, asi se puede acceder
#panel:cubos

################ SERIES

s = pd.Series(['Matemáticas', 'Historia', 'Economía', 'Programación', 'Inglés'], dtype='string')
print(s)

s = pd.Series({'Matemáticas': 6.0,  'Economía': 4.5, 'Programación': 8.5})
print(s)

print(s.size) #Tamaño
print(s.index) #Indices
print(s.dtype) #Tipo de objetos

print(s[1:3]) #Acceso por posicion
print(s[['Programación', 'Matemáticas']]) #Acceso por indice

#Resumen descriptivo de una serie
print(s.count())
print(s.sum())
print(s.cumsum())
print(s.value_counts())
print(s.min())
print(s.max())
print(s.mean())
print(s.var())
print(s.std())
print(s.describe())

#Aplicar operaciones a una serie
print(s*2)

#Aplicar funciones a una serie
#print(s.apply(log))

#filtrar una serie
print(s[s>5])

#Ordenar una serie
print(s.sort_index(ascending = False))

#Eliminar valores desconocidos
print(s.dropna())

############ DATAFRAME

#Creacion a partir de diccionario
datos = {'nombre':['María', 'Luis', 'Carmen', 'Antonio'],
 'edad':[18, 22, 20, 21],
 'grado':['Economía', 'Medicina', 'Arquitectura', 'Economía'],
 'correo':['maria@gmail.com', 'luis@yahoo.es', 'carmen@gmail.com', 'antonio@gmail.com']
 }
df = pd.DataFrame(datos)
print(df)

#Creacion a partir de listas
df = pd.DataFrame([['María', 18], ['Luis', 22], ['Carmen', 20]], columns=['Nombre', 'Edad'])
print(df)

#Creacion a partir de una lista de diccionarios
df = pd.DataFrame([{'Nombre':'María', 'Edad':18}, {'Nombre':'Luis', 'Edad':22}, {'Nombre':'Carmen'}])
print(df)

#Creacion a partir de un array
df = pd.DataFrame(np.random.randn(4, 3), columns=['a', 'b', 'c'])
print(df)

#Creacion a partir de un excel o csv
#df = pd.read_csv('https://raw.githubusercontent.com/asalber/manual-python/master/datos/colesteroles.csv', sep=';', decimal=',')
#print(df.head())

#Exportar ficheros
# df.to_csv(fichero.csv, sep=separador, columns=booleano, index=booleano)
# df.to_excel(fichero.xlsx, sheet_name = hoja, columns=booleano, index=booleano)

#Atributos de un DF
print(df.info())
print(df.shape)
print(df.size)
print(df.columns)
print(df.index)
print(df.dtypes)
print(df.head(2))
print(df.tail(2))

#Renombrar los nombres de las filas y las columnas
#Cambiar el indice de un df
#Reindezar un df
#Acceso a los elementos de un df
#Operaciones con las columnas de un df
#Operaciones con las filas de un df
#Agrupación de un df
#Reestructurar un df
#Combinar varios df