#Genere un codigo para cotizar departamentos en un edificio con 25 pisos y 8 deptos por piso (101,102, 201,1001,1008,2501,2508)

#Todos los departamentos del primer piso valen 100, y todos los departamentos del ultimo piso valen 400.

#Para los pisos intermedios, se ha fijado un precio base de 245; el precio de los departamentos con vista al mar se aumentara en 13 %, y el de los con vista al cerro se rebajar a en 17 %. Los decimales se redondearan hacia abajo. 

# Departamento 807 es hospedado generalmente por famosos por lo cual se debe fijar su precio en 500.

cliente = (input('Ingrese el departamento que desee cotizar: '))
piso_1 = 100
piso_25 = 400
piso_int = 245
depto_807 = 500

if len(cliente) == 3:
    piso = cliente[0]
    depto = cliente[1:]
    #print(piso,depto)
    if piso == '1':
        print('El valor del departamento es de $100')
    elif cliente == '807':
        print('El valor del departamento es de $500')
    elif depto == '04' or depto == '00':
        valor = 245 * 0.87
        print('El valor del departamento es de $',valor)
    elif depto == '07' or depto == '03':
        valor = 245 * 1.13
        print('El valor del departamento es de $',valor)
    else:
        print('El valor del departamento es de $245')
elif len(cliente) == 4:
    piso = cliente[0:2]
    depto = cliente[2:]
    #print(piso,depto)
    if piso == '25':
        print('El valor del departamento es de $400')
    elif depto == '04' or depto == '00':
        valor = 245 * 0.87
        print('El valor del departamento es de $',valor)
    elif depto == '07' or depto == '03':
        valor = 245 * 1.13
        print('El valor del departamento es de $',valor)
    else:
        print('El valor del departamento es de $245')
else:
    print('Departamento invalido')
