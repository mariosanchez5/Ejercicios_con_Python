val = ''
valores = []
while val != 'fin':
    val = input('Ingrese los valores: ')
    valores.append(val)

valores.remove(val)

suma = 0
cont = 0
for i in valores:
    suma = float(i) + suma
    cont = cont +1

promedio = suma/cont

numerador = 0
for a in valores:
    numerador = numerador + (float(a) - promedio)**2

varianza = numerador / (cont-1)
desv = varianza ** (1/2)

print(desv)