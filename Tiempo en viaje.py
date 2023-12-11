#Un viajero desea saber cuánto tiempo tomó un viaje que realizó.

def transforma(total):
    horas = total//60
    minutos = total%60
    return (horas,minutos)

tiempo = int(input("Ingrese el tiempo en minutos que se demoro:"))
total = 0
while tiempo!=0:
    total = tiempo + total
    tiempo = int(input("Ingrese el tiempo en minutos que se demoro:"))

print("El tiempo total es de: ", total)

horas,minutos = transforma(total)
#print("Lo que es equivalente a: ", transforma(total))
print("Lo que equivale a: ", horas,"horas y ",minutos,"minutos")

