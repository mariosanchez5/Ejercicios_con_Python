vehiculo = input('Ingrese el tipo de Vehiculo: ')
dia = input('Dia: ')
horario = input('Horario: ')

if vehiculo == 'auto':
    pass
elif vehiculo == 'camion':
    if dia == 'lunes' or dia =='martes' or dia == 'miercoles' or dia =='jueves' or dia == 'viernes':
        pass
    else:
        pass
else:
    print('El vehiculo ingresado no es correcto')

