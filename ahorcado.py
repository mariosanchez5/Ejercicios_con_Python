####### Este ciclo agrega las palabras a una lista
pal = ""
lista = []
while pal != "0":
    pal = input("Ingrese una palabra: ")
    lista.append(pal)
lista.remove("0")

###### Este ciclo agrega las letras a una lista
le = ""
lista2 = []
while le != "0":
    le = input("Ingrese las letras a mostrar: ")
    lista2.append(le)
lista2.remove("0")

### Haremos un for para recorrer cada palabra en la lista

for palabra in lista:
    largo = len(palabra)
    guione = "_"*largo
    guiones = list(guione)
    for letras in lista2:
        contador = 0
        for let in palabra:
            if letras == let:
                del guiones[contador]
                guiones.insert(contador,let)
            contador = contador+1
    print (guiones)


    while "_" in guiones:
        jugando = input("Ingrese una letra:")
        conta = 0
        for letr in palabra:
            if letr == jugando:
                del guiones[conta]
                guiones.insert(conta,letr)
                print (guiones)
            conta = conta+1
        #print (guiones)


print (guiones)
print(lista)
