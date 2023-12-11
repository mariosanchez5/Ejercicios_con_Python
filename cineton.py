#(mes, paıs, nombre_pelıcula, ano_filmacion, [sala1, sala2, ...])
cartelera = [
('febrero','FRANCIA','El muelle', 1962, ['sala1','sala3']),
('febrero','FRANCIA','La dama de honor', 2004, ['sala1','sala4']),
('abril','RUSIA','Padre del soldado', 1964, ['sala3','sala2','sala4']),
('enero','CHILE','Gloria', 2013, ['sala1','sala2']),
('mayo','MEXICO','Cumbres', 2013, ['sala3','sala2']),
('julio','FRANCIA','Melo', 1986, ['sala3','sala1']),
('junio','BELGICA','Rondo', 2012, ['sala4','sala2']),
('marzo','ALEMANIA','Tiempo de Canibales', 2014, ['sala1','sala2']),
('marzo','ALEMANIA','Soul Kitchen', 2009, ['sala3','sala4'])]

#Para entender mejor, en cartelera la pelıcula ‘Gloria’ (Chilena) creada en 2013, se exhibira el
#mes de ‘enero’ en las ‘sala1’ y ‘sala2’.

def pelicula_por_pais(cartelera, country):
    lista = []
    for tup in cartelera:
        mes,pais,nombre_peli,agno,sala = tup
        if country == pais:
            tuplaz = (nombre_peli,agno)
            lista.append(tuplaz)
            #print(tupla)
    return lista

#print(pelicula_por_pais(cartelera,'FRANCIA'))

def peliculas_por_sala(cartelera, sala):
    lista = []
    for tup in cartelera:
        mes,pais,nombre_peli,agno,salas = tup
        if sala in salas:
            tuplaz = (mes,nombre_peli)
            lista.append(tuplaz)
    return lista

print(peliculas_por_sala(cartelera,'sala1'))
