librerias = {"Ateneo":[("Ciencias;2ed",10000),("Papelucho;3ed",3000),("LyC;1ed",5000),
("Historia;1ed",3000),("English;2ed",2000)],
"Internacional":[("Ciencias;2ed",8000),("Papelucho;1ed",5000),
("Historia;2ed",3000),("English;3ed",7500),
("Matematica;1ed",9000)],
"Nacional":[("LyC;2ed",4500),("Ciencias;1ed",9000),("Papelucho;2ed",6000),
("Literatura;1ed",3000),("Historia;2ed",3500),
("Matematica;2ed",9000)]}

def buscar_libro (librerias,libro):
    dicc = {}
    for llave, valor in librerias.items():
        for tupla in valor:
            if libro in tupla[0]:
                dicc[llave]=tupla[1]
    print (dicc)

libro = 'LyC'
buscar_libro (librerias,libro)