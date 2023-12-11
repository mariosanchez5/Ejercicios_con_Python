#cachipun entre 2 jugadores

contador1 = 0
contador2 = 0

def felcitaciones (contador1,contador2):
    if contador1>contador2:
        print("Felicidades Jugador 1 eres el mejor")
    else:
        print("Felicidades jugador 2 eres el mejor")

while contador1< 3 and contador2<3:
    jug1 = input("Jugador 1 Ingrese su jugada: ")
    jug2 = input("Jugador 2 Ingrese su jugada: ")

    #piedra le gana a tijera
    if jug1=="piedra" and jug2=="tijera":
        contador1 = contador1 + 1
    elif jug2=="piedra" and jug1=="tijera":
        contador2 = contador2 + 1
    #papel le gana a piedra
    elif jug1=="papel" and jug2=="piedra":
        contador1 = contador1 + 1
    elif jug2=="papel" and jug1=="piedra":
        contador2 = contador2 + 1
    #tijera le gana a papel
    elif jug1=="tijera" and jug2=="papel":
        contador1 = contador1 + 1
    elif jug2=="tijera" and jug1=="papel":
        contador2 = contador2 + 1
    
    print("Jugador 1: ",contador1,"Jugador 2: ",contador2)
    
print("Fin de la partida")
felcitaciones(contador1,contador2)
    