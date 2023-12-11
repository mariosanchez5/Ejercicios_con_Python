"""
La polic´ıa de Pythonia le ha encargado construir un programa para cursar multas a quienes
no respeten la restriccion vehicular. Para ello se cuenta con la lista ´ registro, que almacena los
datos de cada veh´ıculo en una tupla que contiene la patente, la ciudad, el dueno, y un booleano ˜
que indica si el veh´ıculo es catal´ıtico (True) o no lo es (False). Por ejemplo:
"""

registro = [
('CRTJ 32', 'Valpyraiso', 'Juan Perez', True),
('RX-2134', 'Sanpyago', 'Ana Martinez', False),
('ADNT 28', 'Pyna del Mar', 'Fernanda Jara', False),
('ZZ-9999', 'Pyca', 'Pedro Allende', True),
('AK-2130', 'Sanpyago', 'Paloma Blanco', True),
('ABCD 19', 'Copymbo', 'Ana Roa', False)]

"""
Las patentes tienen dos formatos distintos:
- 4 letras, un espacio y 2 d´ıgitos (Ejemplo: ’CRTJ 32’).
- 2 letras, un guion y 4 d ´ ´ıgitos (Ejemplo: ’RX-2134’).
Para definir la restriccion de los ´ catal´ıticos se analiza la ultima letra de la patente, es decir, la letra ´
que esta m´ as a la derecha: ´
- Lunes: patentes cuya ultima letra sea menor o igual a ´ ’G’.
- Miercoles: patentes cuya ´ ultima letra sea mayor que ´ ’G’ pero menor o igual a ’N’.
- Viernes: patentes cuya ultima letra sea mayor que ´ ’N’.
Para el caso de los no catal´ıticos la restriccion se decide en base al ´ ultimo d ´ ´ıgito:
- Lunes: Patentes terminadas en 0, 1, 2 o 3.
- Miercoles: Patentes terminadas en ´ 4, 5 o 6.
- Viernes: Patentes terminadas en 7, 8 o 9.
"""

"""
(a) Escriba la funcion´ tiene restriccion(registro, patente, dia) que reciba el registro de veh´ıculos, la patente de un veh´ıculo particular, y el d´ıa en que el veh´ıculo transito (todo ´
en mayuscula), y ´ retorne True si se le debe cursar un parte o False en caso contrario. Puede
suponer que patente existira siempre ´ en registro y que todos los datos son correctos
"""

def tiene_resticcion(registro,patente_dada,dia):
    for tupla in registro:
        patente, ciudad, nombre, catalitico = tupla
        if patente == patente_dada:
            if catalitico == True:
                patentenum = patente.replace(" ", "")
                if len(patentenum) == 7:
                    num = int(patente[1])
                else:
                    num = int(patente[3])

                if dia == 'LUNES':
                    if num <= 'g':
                        return True
                    else:
                        return False
                elif dia == 'MIERCOLES':
                    if num > 'g' and num<='n':
                        return True
                    else:
                        return False
                elif dia == 'VIERNES':
                    if num > 'n':
                        return True
                    else:
                        return False
            else:
                num = patente[-1]
                if dia == 'LUNES':
                    if num == '0' or num == '1' or num == '2' or num == '3':
                        return True
                    else:
                        return False
                elif dia == 'MIERCOLES':
                    if num == '5' or num == '5' or num == '6':
                        return True
                    else:
                        return False
                elif dia == 'VIERNES':
                    if num == '7' or num == '8' or num == '9':
                        return True
                    else:
                        return False
print(tiene_resticcion(registro, 'CRTJ 32' , 'LUNES' ))