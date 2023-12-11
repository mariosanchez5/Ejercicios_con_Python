num = int(input('Ingrese el numero de palabras a ingresar: '))
n=1
lista=[]

while n <= num:
    palabras = input('Palabra ')
    lista.append(palabras)
    n = n+1
print(lista)

min=100
pal_min=''
max=0
pal_max=''

for palabra in lista:
    if len(palabra)<min:
        pal_min = palabra
        min = len(palabra)

    if len(palabra)>max:
        pal_max = palabra
        max = len(palabra)

print('La palabra mas larga es: ',pal_max)
print('La palabra mas corta es: ',pal_min)
    
