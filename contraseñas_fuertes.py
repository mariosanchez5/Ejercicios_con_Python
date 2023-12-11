frase = "Quiero mi password segura."
diccionario = {'a':4,'e':1,'i':6,'o':7,'.':'?'}

for letra in frase:
    for dic in diccionario:
        if letra == dic:
            dicio = str(diccionario[dic])
            frase = frase.replace(letra,dicio)

print(frase)