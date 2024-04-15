import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#2. Copiar los datos en un dataframe
df = pd.read_csv('public_transportation_statistics_by_zip_code.csv')
print('Vemos las primeras filas')
print(df.head())
print(type(df))

#Vemos una pequeña estadistica descriptiva
print('Vemos las columnas, tipo de dato y cantidad de datos no nulos')
print(df.info())

print('Verificamos los datos nulos')
print(df.isnull().sum())

print('Vemos una estadistica descriptiva de las columnas numericas')
print(df.describe())

#3.Encontramos los porcentajes maximos y minimos de cada columna
print('El porcentaje mínimo de public_transportation_pct es: ',df['public_transportation_pct'].min())
print('El porcentaje máximo de public_transportation_pct es: ',df['public_transportation_pct'].max())
print('El porcentaje mínimo de public_transportation_population es: ',df['public_transportation_population'].min())
print('El porcentaje máximo de public_transportation_population es: ',df['public_transportation_population'].max())

#Limpiamos los datos que son menores a 0 y comprobamos que se eliminaron
df_limpio = df.loc[df['public_transportation_pct'] >= 0]
print(df_limpio.describe())

#4.Ventas potenciales promedio para clientes que viven en zonas de alto y bajo transporte publico
mas_10 = 0
menos_10 = 0
cont_mas_10 = 0
cont_menos_10 = 0
for indice, fila in df_limpio.iterrows():
    if fila[1] > 10:
        mas_10 = mas_10 + fila[2]
        cont_mas_10 += 1
    elif fila[1] <= 10:
        menos_10 = menos_10 + fila[2]
        cont_menos_10 += 1

print('El promedio de las zonas de mas de 10% es: ', round(mas_10/cont_mas_10,1))
print('El promedio de las zonas de menos de 10% es: ', round(menos_10/cont_menos_10,1))

#5.Graficar Histograma
plt.hist(df_limpio['public_transportation_pct'], bins=100,color='skyblue', edgecolor='black')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.title('Histograma de datos')
plt.show()

plt.hist(df_limpio['public_transportation_population'], bins=100,color='skyblue', edgecolor='black')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.title('Histograma de datos')
plt.show()

#6. Agrupar a los potenciales clientes en funcion del uso de transporte publico por codigo postal
#Y estimar numero de ventas
#Crear diagrama de dispercion para comprender relacion entre el uso del transporte publico y potenciales ventas
#Exportar datos a excel

promedio_agrupado = df_limpio.groupby('public_transportation_pct')['public_transportation_population'].mean().reset_index()
print(promedio_agrupado)

plt.scatter(promedio_agrupado['public_transportation_pct'], promedio_agrupado['public_transportation_population'], alpha=0.5)
plt.xlabel('Porcentaje de población que utiliza transporte público (%)')
plt.ylabel('Promedio de población que utiliza transporte público para ir al trabajo')
plt.title('Relación entre uso de transporte público y promedio de ventas agrupadas')
plt.grid(True)
plt.show()

promedio_agrupado.to_excel("promedio_agrupado.xlsx", index=False)







