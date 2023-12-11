ando = int(input("Ingrese el multiplicando: "))
dor = int(input("Ingrese el multiplicador"))
suma=0
while dor >= 1:
    if dor%2 != 0:
        suma = suma + ando
    ando = ando*2
    dor = int(dor/2)

print (suma)


