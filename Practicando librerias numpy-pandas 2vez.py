import numpy as np #Numpy es la librería

#Diferencia entre lista y array: Principalemente array del mismo tipo, tiene menos funciones y por lo mismo mucho mas rapida
#Pero son bastante similares
lista = [1,2,3,4,5]
my_array = np.array(lista)
print(lista)
print(my_array)
#Con array se puede crear un vector, matrices o cubos

#Podemos crear de distintas formas vectores o matrices, esta es un ejemplo
print(np.zeros(5))

#Podemos saber sus atributos como su tipo, forma o cantidad de datos
print(my_array.dtype)

#Podemos acceder a sus datos como una lista
print(my_array[1])

#Se puede filtrar un array mediante condiciones como las listas
print(my_array[(my_array>2)])

#Se puede operar matematicamente con los array
print(my_array*2)

#Como tambien hay distintas funciones listas para operar con algebra matricial, compo por ejemplo la matriz traspuesta
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a)
print(a.T)

#E incluso resolver sistemas de ecuaciones
# Sistema de dos ecuaciones y dos incógnitas
# x + 2y = 1
# 3x + 5y = 2 
a = np.array([[1, 2], [3, 5]])
b = np.array([1, 2])
print(np.linalg.solve(a, b))



############################################## PANDAS ##########################################3
import pandas as pd
### CREACION DE UNA SERIE

#A partir de una lista
s = pd.Series(['Mate','Progra','Fisica','Finanzas'])
print(s)

#A partir de un diccionario
s2 = pd.Series({'Mate':6, 'Progra':7, 'Fisica':5, 'Finanzas':6})
print(s2)

### ATRIBUTOS DE UNA SERIE
print('size ',s.size)
print('index ',s.index)
print('dtype ',s.dtype)


### ACCESO A LOS ELEMENTOS DE UNA SERIE

#Por posicion
print(s[1:2])

#Por nombre
print(s2['Progra'])

### RESUMEN DESCRIPTIVO
print('count ',s2.count())
print('sum ',s2.sum())
#print('cusum ',s2.cusum()) #no aplica
print('value_counts ',s2.value_counts())
print('min ',s2.min())
print('max ',s2.max())
print('mean ',s2.mean())
print('var ',s2.var())
print('std ',s2.std())
print('describe ',s2.describe())

### OPERACIONES A UNA SERIE
s3 = pd.Series([6,1,2,3,4,5])
print(s3*2)

### FUNCIONES A UNA SERIE
print(s3.apply(np.log))

### FILTRAR UNA SERIE
print(s3[s3>2])

### ORDENAR UNA SERIE
print(s3.sort_values())
print(s3.sort_index(ascending=False))

### ELIMNAR DATOS DESCONOCIDOS
s4 = pd.Series(['Mario','Maida','Rocky',np.nan, None])
print(s4.dropna())


################# DF

### CREACION DE UN DF

#Dicionario de listas
datos = {'nombre':['mario','maida'],
         'edad':[28,16],
         'grado':['datos','psico']}
df = pd.DataFrame(datos)
print(df)
#Lista de listas
df2 = pd.DataFrame([['Mario',28],['Maida',26]],columns=['Nombre','Edad']) 
print(df2)
#Lista de diccionarios
df3 = pd.DataFrame([{'Nombre':'Mario','Edad':28},{'Nombre':'Maida','Edad':26}])
print(df3)
#Un array
df4 = pd.DataFrame(np.random.rand(4,3),columns=['a','b','c'])
print('df4: ',df4)
#Un CSV o Excel
#df = pd.read_csv('abc.csv',sep=';',decimal=',')

### EXPORTACION DE FICHERO

#df.to_csv('fichero.csv',sep=';',columns=True,index=True)

### ATRIBUTOS DE UN DF

print('Info: ',df.info())
print('Shape: ',df.shape)
print('Size: ',df.size)
print('Columns: ',df.columns)
print('Index: ',df.index)
print('Dtype: ',df.dtypes)
print('Head: ',df.head(5))
print('Tail: ',df.tail(5))

### RENOMBRAR LOS NOMBRES DE LAS FILAS Y LAS COLUMNAS
print(df)
print(df.rename(columns={'nombre':'Name','edad':'Age','grado':'grade'},index={0:10,1:20}))

### CAMBIAR EL INDICE DE UN DF
print(df.set_index('nombre'))#Ahora el indice es esa columna

### REINDEXAR UN DF
print(df.reindex(index=[4,3],columns=['nombre','edad','grado']))

### ACCESO A LOS ELEMENTOS DE UN DF
#Mediante posiciones
print(df.iloc[1,1])
#Mediante nombre
print(df.loc[1,'grado'])

### OPERACIONES CON LAS COLUMNAS DE UN DF
#Añadir una columna
df['cumpleanos']=pd.Series(['12-10-1995','21-02-1997'])
print(df)
#Operacion sobre columna
print(df['edad']*100)
#Aplicar funciones sobre columnas
print(df['edad'].apply(np.log))
#Convertir una columna al tipo datetime
df2=pd.to_datetime(df.cumpleanos, format='%d-%m-%Y')
print(df2)
#Eliminar columna de un df
cumple = df.pop('cumpleanos')
print(cumple)

### RESUMEN DESCRIPTIVO DE UN DF
df = pd.DataFrame(np.random.rand(4,3),columns=['a','b','c'])
print('count: ',df.count())
print('sum: ',df.sum())
print('cumsum: ',df.cumsum())
print('min: ',df.min())
print('max: ',df.max())
print('mean: ',df.mean())
print('var: ',df.var())
print('std: ',df.std())
print('cov: ',df.cov())
print('corr: ',df.corr())
print('describe: ',df.describe())

### OPERACIONES CON LAS FILAS DE UN DF
#df = df.append(pd.Series([1,2,4], index=['a','b','c']))
print(df)
print(df.drop([1]))
print(df[(df['a']>0.5)])
print(df.sort_values('a'))
print(df.dropna())

### AGRUPACIONES DE UN DF
datos = {'nombre':['pedro','juan','carmen','maria'],
         'sexo':['m','m','f','f'],
         'edad':[28,29,23,34]}
df = pd.DataFrame(datos)
print(df)
print(df.groupby('sexo').groups)

### REESTRUCTURAR UN DF
datos = {'nombre':['pedro','juan','carmen','maria'],
         'mate':[28,29,23,34],
         'progra':[28,29,23,34],
         'econo':[28,29,23,34]}
df = pd.DataFrame(datos)
print(df)
print(df.melt(id_vars=['nombre'],var_name='Asignatura',value_name='nota'))

### COMBINAR VARIOS DF
datos = {'nombre':['pedro','juan','carmen','maria'],
         'sexo':['m','m','f','f'],
         'edad':[28,29,23,34]}
df1 = pd.DataFrame(datos)
df2 = pd.DataFrame(datos)
print(pd.concat([df1,df2]))

############################################ matplotlib

import matplotlib.pyplot as plt

#DIAGRAMA DE BARRA VERTICALES
fig,ax = plt.subplots()
ax.bar([1,2,3],[3,2,1])
plt.show()

#DIAGRAMA DE BARRA HORIZONTALES
fig,ax = plt.subplots()
ax.barh([1,2,3],[3,2,1])
plt.show()

#HISTOGRAMA
x = np.random.normal(5,1.5, size=1000)

fig,ax = plt.subplots()
ax.hist(x)
plt.show()

#DIAGRAMA DE SECTORES
fig,ax = plt.subplots()
ax.pie([5,4,3,2,1])
plt.show()

#DIAGRAMA DE CAJA Y BIGOTES
fig,ax = plt.subplots()
ax.boxplot([1,2,1,2,4,3,3,3,5,7])
plt.show()

#DIAGRAMA DE VIOLIN
fig,ax = plt.subplots()
ax.violinplot([1,2,1,2,3,4,3,3,5,7])
plt.show()

#DIAGRAMA DE DISPERCION
fig,ax = plt.subplots()
ax.scatter(x=[1,2,3], y=[3,2,1])
plt.show()

#DIAGRAMA DE LINEAS
fig,ax = plt.subplots()
ax.plot([1,2,3,4], [1,2,0,0.5])
plt.show()


#DIAGRAMA DE AREAS
fig,ax = plt.subplots()
ax.fill_between([1,2,3,4],[1,2,0,0.5])
plt.show()

#DIAGRAMA DE CONTORNO
x = np.linspace(-3,3,100)
y = np.linspace(-3,3,100)
x,y = np.meshgrid(x,y)
z = np.sqrt(x**2 + 2*y**2)

fig,ax = plt.subplots()
ax.contourf(x,y,z)
plt.show()


#MAPAS DE CALOR
x = np.random.random((16,16))

fig,ax = plt.subplots()
ax.imshow(x)
plt.show()

#COMBINACION