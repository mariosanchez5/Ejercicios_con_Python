"""
Una organizacion internacional de conservacion construyo un domo de cristal para mantener 
un micro clima en una cierta superficie. Para esto, se instalaron miles de paneles de cristal,
contando cada uno de ellos con varios sensores que reportan informacion diariamente a un 
computador central. Cada sensor transmite una vez al dia una tupla con su medicion, indicando 
la fecha, su identificador unico y el valor de la medicion. Como ejemplo, una medicion seria:
(2016, 3, 27, 'aa:01:10', 0.0021).
Todas estas mediciones son colocadas en una lista en el computador central, la cual es mantenida
ordenada descendentemente por el valor medido. Esto facilita la recuperacion posterior de 
mediciones, debido a que por el gran volumen del registro resulta imposible ordenarlo con
cualquiera de los algoritmos disponibles en la actualidad. A modo de ejemplo, un posible registro
seria:

"""
registro = [ (2016, 1, 25, 'd2:00:10', 0.0112),
(2015, 10, 24, '3e:15:c2', 0.0105),
(2015, 11, 3, '28:0b:5c', 0.0009)]

"""
Usted debe:

Construir la funcion agregar_medicion(registro, A, M, D, id, val), la que agrega la
informacion capturada al registro. Considere A el ano, M el mes y D el dia de la medicion.

"""

def agregar_medicion(registro, A, M, D, id, val):
    tupla = (A,M,D,id,val)
    registro.append(tupla)
    print("Resultado Ejercicio 1")
    registro_ordenado = sorted(registro, key=lambda reg : reg[4],reverse=True)
    #print(registro)
    print(registro_ordenado)

agregar_medicion(registro, 2016, 3, 27, 'aa:01:10', 0.0021)

"""
Construir la funcion corregir_medicion(registro, A, M, D, id, nvo_valor) que corrige el valor medido de un sensor. La funcion recibe como parametro el registro, el ano, mes y
dia de la medicion a corregir, el identificador unico y el nuevo valor medido. Considere que luego
de esta actualizacion el registro debe permanecer ordenado como se indicio en el enunciado.
"""

def corregir_medicion(registro, A, M, D, id, nvo_valor):
    registro_v2 = registro
    cont = 0
    for tupla in registro:
        agno,mes,dia,id_tupla, valor = tupla
        if id_tupla==id and A==agno and mes==M and dia==D:
            del registro_v2[cont]
            registro_v2.append((A,M,D,id,nvo_valor))
        cont += 1
    print("Resultado Ejercicio 2")
    #print(registro_v2)
    registro_ordenado = sorted(registro_v2, key=lambda reg : reg[4],reverse=True)
    print(registro_ordenado)

corregir_medicion(registro, 2016, 3, 27, 'aa:01:10', 0.0221)

"""
c) Construir la funcion sensores_sobre_umbral(registro, u), la que recibe un valor de
medicion usado como umbral y tambien el  registro. Esta funcion entrega un listado con todos 
aquellos sensores, cuyo valor medido se encontro por sobre el umbral  u entregado. Este listado
no debe contener identificadores duplicados.
"""

def sensores_sobre_umbral(registro, u):
    lista = []
    for tupla in registro:
        agno,mes,dia,id_tupla, valor = tupla
        if valor > u:
            if valor not in lista:
                lista.append(id_tupla)
    print("Resultado Ejercicio 3")
    print(lista)

sensores_sobre_umbral(registro, 0.01)
#['aa:01:10', 'd2:00:10', '3e:15:c2']