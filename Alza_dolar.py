
dias = int(input('Cuantos días desea evaluar: '))
lista = []

for i in range(dias):
    dia = int(input('Día {}: '.format(i+1)))
    lista.append(dia)

mayor = 0
for n in range(dias-1):
    alza = lista[n+1]-lista[n]
    if alza >= mayor:
        mayor = alza

print('La mayor alza fue de {}'.format(mayor))
