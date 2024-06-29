"""
 El registro de pacientes de una clinica se encuentra en la lista de tuplas pacientes. Cada
tupla corresponde a una ficha del paciente que contiene el rut (como string) y los datos personales
(en un diccionario):
"""

datos1 = {'nombre' : 'Oliver',
          'apellido' : 'Atton',
          'edad' : 31,
          'peso' : 87.0,
          'estatura' : 1.8,
          'presion arterial': 90.,
          'ritmo cardiaco' : 60.}
datos2 = {'nombre' : 'Jimmy',
          'apellido' : 'Page',
          'edad' : 55,
          'peso' : 100.0,
          'estatura' : 1.75,
          'presion arterial': 90.,
          'ritmo cardiaco' : 60.}
pacientes = [('15000111-7', datos1), ('15111222-3', datos2)]

#La lista pacientes tiene datos de muchos pacientes y ademas es una variable global.

"""
Escriba la funcion nuevo_paciente(ficha), que reciba como parametro la ficha de un paciente
y retorne el mensaje Ingresado si se pudo almacenar el registro en la lista pacientes. De lo
contrario, retorne Ya existe en caso que el rut del cliente ya se encuentre en pacientes.
"""

ficha = ('14999888-6', datos1)

def nuevo_paciente(ficha):
    rut_2, datos_2 = ficha
    for paciente in pacientes:
        rut,dato = paciente
        if rut == rut_2:
            bo = 'El paciente ya está ingresado'
            return bo
    bo = 'El paciente no está ingresado'
    return bo
    
    datos3 = {}

    print('Ingresaremos el paciente.')
    rut_entrada = input('Ingrese el rut: ')
    nombre = input('Ingresa el nombre: ')
    apellido = input('Ingresa el apellido: ')
    edad = input('Ingresa edad: ')
    peso = input('Ingresa el peso: ')
    estatura = input('Ingresa estatura: ')
    presion = input('Ingresa presion: ')
    ritmo = input('Ingresa ritmo: ')
    datos3['nombre'] = nombre
    datos3['apellido'] = apellido
    datos3['edad'] = edad
    datos3['peso'] = peso
    datos3['estatura'] = estatura
    datos3['presion alterial'] = presion
    datos3['ritmo cardiaco'] = ritmo
    pacientes.append((rut_entrada,datos3))
    print('Paciente agregado exitosamente!')
    print(pacientes)

print(nuevo_paciente(ficha))
print(nuevo_paciente(ficha))