grupo1 = {
'rick':(172,10), 'daryl':(136,11), 'michonne':(80,6),
'glenn':(73,0), 'maggie':(55,4), 'carl':(62,1),
'tyreese':(35,0), 'carol':(17,3) }

#Desarrolle la funcion´ total(grupo) que recibe como parametro un ´ diccionario con las estad´ısticas del grupo, retornando como una tupla el total de walkers y el total de humanos eliminados.

def total(grupo):
    total_kill_walker = 0
    total_kill_human = 0
    for miembro, numeros in grupo.items():
        kill_walker, kill_human = numeros
        total_kill_walker = total_kill_walker + kill_walker
        total_kill_human = total_kill_human + kill_human
    total_kill = (total_kill_walker,total_kill_human)
    return (total_kill)

print(total(grupo1))

"""Desarrolle la funcion puntaje(grupo) que recibe como parametro un  diccionario con las
estadisticas del grupo, y retorna un diccionario cuya clave es el nombre del miembro del
grupo y valor el puntaje asociado. Este puntaje se calcula como: walkers/total walkers + 2 por
(humanos/total humanos), en donde walkers representa a los walkers eliminados por el miembro
del grupo, y el total walkers representa al total de walkers eliminado por todo el grupo. humanos
y total humanos sigue la misma logica."""

def puntaje(grupo):
    total_walker, total_human = total(grupo1)
    diccio = {}
    for miembro, numeros in grupo.items():
        kill_walker, kill_human = numeros
        puntaje = kill_walker/total_walker + 2*(kill_human/total_human)
        #print(miembro,puntaje)
        diccio[miembro] = round(puntaje,2)
    return (diccio)

print(puntaje(grupo1))

"""Desarrolle la funcion ranking(grupo) que recibe como parametro un  diccionario con las
estadisticas del grupo, y retorna una lista con los nombres de los miembros del grupo ordenados
de mayor a menor (segun el puntaje definido en la parte b)."""

def ranking(grupo):
    diccio = puntaje(grupo1)
    maximo = []
    rank = sorted(diccio.items(), key=lambda x: x[1], reverse=True)
    #for miembro, score in diccio.items(): 
    #    pass
    return rank

print(ranking(grupo1))