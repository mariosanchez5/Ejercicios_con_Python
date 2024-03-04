"""
La compania nacional de telecomunicaciones BTP esta empecinada en automatizar algunos 
procesos y consultas en su empresa, ya que hasta el momento eran los pobres practicantes quienes
tenian que revisar los registros uno por uno y encontrar cierta informacion necesaria para satisfacer 
las consultas hechas por los altos directivos. Los datos de los cliente, de las visitas y de los tecnicos, 
para el mes de Marzo, estan almacenados en las siguientes estructuras: 
"""

# {id_cliente:[(serv1,serv2,serv3),saldo_mensual,[canalprem1,canalprem2], Deuda]}
clientes = {23: [('telefonia', 'cable', 'internet'), 23000, ['GameKidTV'], False],
66: [('internet', 'telefonia', 'cable'), 34000, ['WolfSports', 'ZDFPremium'], True],
120:[('cable', 'internet'), 30000, ['HVOPrem'], True]}

#[(id_cliente, id_tecnico, fecha_visita)]
visitas_tecnicas = [(23, 65, '30-03-2015'), (66, 65, '31-03-2015'),(120, 33, '28-03-2015')]

#{(id_tecnico, nombre)}
tecnicos = {(65, 'Guy Cable'), (33, 'Dexter Morgan')}

"""
Desarrollar la funcion monto_total_deuda(clientes) que reciba el diccionario clientes
y retorne una tupla con el monto total adeudado por los clientes y el id del cliente con mayor
deuda
"""

def monto_total_deuda(clientes):
    deuda_total = 0
    max = 0
    for id, lista in clientes.items():
        servicios, saldo, canales, deuda = lista
        if deuda == True:
            deuda_total = deuda_total + saldo
            if saldo > max:
                max = saldo
                max_name = id
    return deuda_total,max_name

print(monto_total_deuda(clientes))

"""
Durante el mes de marzo se tiene la promocion que consiste, en que si el cliente tiene sus cuentas 
al dia (no tiene deuda) y ademas tiene contratado los 3 servicios (telefonia, cable e internet) se le
da gratis el canal premium GameKidTV. Si el cliente ya tiene contratado el canal, se le descuentan
$500 pesos de su saldo mensual.
Desarrollar la funcion promocion(clientes) que reciba el diccionario clientes y retorne un
diccionario igual al de clientes, pero aplicando la promocion de marzo a los clientes.
"""

def promocion(clientes):
    diccio = {}
    for id, lista in clientes.items():
        servicios, saldo, canales, deuda = lista
        if deuda == False:
            for canal in canales:
                if canal == 'GameKidTV':
                    saldo = saldo - 500
                else:
                    canales.append('GameKidTV')
        diccio[id]=[servicios,saldo,canales,deuda]

    return diccio

print(promocion(clientes))