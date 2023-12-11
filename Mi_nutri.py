#En este programa llevare mi dieta y todo lo que conlleva

import datetime
#fecha_actual = datetime.datetime.now()
fecha_actual = datetime.datetime.now().strftime('%d-%m-%Y')

#Quieres calcular tus calorias desde 0 o registrar constancia
#punto_partida = int(input('Si quieres calcular tus calorias inciciales presiona 1, si quieres registrar tus avances presiona 2:'))


#Medidas
edad = int(input('Ingresa tu edad: '))
peso = float(input('Ingresa tu peso actual en kilos: '))
altura = float(input('Ingresa tu estatura en centimetros: '))
porc_grasa = float(input('Ingresa tu porcentake de grasa: '))
act_fisica = float(input('Ingresa tu nivel de actividad fisica (1.2 Sedentario - 1.6 Muy activo): '))
gym = float(input('Ingresa la cantidad de tiempo que le dedicas al gym en horas: '))
bicicleta = float(input('Ingresa la cantidad de tiempo que le dedicas a la bicicleta en horas: '))
cuerda = float(input('Ingresa la cantidad de tiempo que le dedicas a la cuerda en horas: '))
wod = float(input('Ingresa la cantidad de tiempo que le dedicas al wod en horas: '))

#Calculos de metabolimo basal en homres
def metabolismo_basal_hombres(peso, altura, edad, porc_grasa): 
    harris = 66.473 + (13.751 * peso) + (5.003*altura) - (6.755*edad)
    mifflin = (10*peso) + (6.25 * altura) - (5*edad) + 5
    lbm = ((100-porc_grasa)/100)*peso
    cunnighan = 500 + (22*lbm)
    promedio = (harris+mifflin+cunnighan)/3
    print('Tu tasa metabolica basal es : ', promedio)
    return promedio

#Calculo del gasto total
def gasto_metabolico_total(act_fisica, gym, bicicleta, cuerda, wod, peso):
    gaf = act_fisica * metabolismo_basal_hombres(peso,altura,edad,porc_grasa)
    gasto_gym = gym * peso * 5
    gasto_bici = bicicleta * peso * 6
    gasto_cuerda = cuerda * peso * 10
    gasto_wod = wod * peso * 7
    gasto_total = gasto_gym + gasto_bici + gasto_cuerda + gasto_wod
    get = gasto_total + gaf
    print('Tu gasto total diario cuando entrenas es de: ',get)
    print('Tu gasto total diario cuando no entrenas es de: ',gaf)
    print('######################################################')
    print('Para definir, cuando entrenas debes comenzar con: ',get*0.75)
    print('Para definir, cuando no entrenas debes comenzar con: ',gaf*0.75)
    print('######################################################')
    print('Para aumentar, cuando entrenas debes comenzar con: ',get+300)
    print('Para aumentar, cuando no entrenas debes comenzar con: ',gaf+300)
    print('######################################################')
    proteina_def = 2*peso
    grasa_def = 0.8*peso
    hidratos_def = 2*peso
    print('Para definir, deberias consumir {} gramos de proteina, {} gramos de grasa y {} gramos de hidratos de carbono aprox.'.format(proteina_def,grasa_def,hidratos_def))
    proteina_aum = 1.8*peso
    grasa_aum = 1.3*peso
    hidratos_aum = 5*peso
    print('Para aumentar, deberias consumir {} gramos de proteina, {} gramos de grasa y {} gramos de hidratos de carbono aprox.'.format(proteina_aum,grasa_aum,hidratos_aum))


gasto_metabolico_total(act_fisica, gym, bicicleta, cuerda, wod, peso)
#metabolismo_basal_hombres(peso,altura,edad,porc_grasa)

