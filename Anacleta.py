destino = input('Ingrese su destino: ')
auto = int(input('Ingrese su autonomia: '))

avanzar = 0
avanzar = avanzar + auto

if destino == 'b':
    while avanzar <= 16:
        if avanzar == 5:
            print('Acampa en km 4')
            avanzar = avanzar - 1
        else:
            print('Acampa en km ',avanzar)
        avanzar = avanzar + auto
    print('Llega a B')

elif destino == 'c':
    while avanzar <= 21:

        if avanzar == 5:
            print('Acampa en km 4')
            avanzar = avanzar - 1
        elif avanzar == 14:
            print('Acampa en km 13')
            avanzar = avanzar - 1
        else:
            print('Acampa en km ',avanzar)
        avanzar = avanzar + auto 
    print('Llega a C')

else:
    print('Destino no valido')
