numero = int(input("Ingrese su numero:"))
numeros = numero + 1
rango = range(numeros)
print (rango)

kuno = 1
kdos = 0

for i in rango:
    if i > 1:
        fn = kuno + kdos
        kdos = kuno
        kuno = fn

if numero == 0:
    print("F",numero,"=",kdos)
elif numero ==1:
    print("F",numero,"=",kuno)
else:
    print("F",numero,"=",fn)
