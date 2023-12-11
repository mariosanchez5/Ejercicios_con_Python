lista = 10,[7,3,6,0,4,5,10]
mayor = lista[0]
total = 0

for i in lista[1]:
    if i> mayor:
        total = total +1

print("Hay",total,"numeros mayores que",mayor)
