clientes = [('Don Ramon', 3500, (9, 4, 2014)), ('Miguel', 2785, (30, 10, 2014)), ('Cesar', 100, (28, 5, 2015))]

def deuda_total(clientes):
    deuda_total = 0
    for user, deuda, fecha in clientes:
        deuda_total = deuda_total + deuda
    
    return deuda_total



print(deuda_total(clientes))

def mayor_deudor(clientes, ultimo):
    max = 0
    for user, deuda, fecha in clientes:
        if deuda > max:
            max = deuda
            user_max = user
    print(user_max)
    for user, deuda, fecha in clientes:
        date_max = 0
        if user == user_max and fecha[2]==ultimo:
            print(deuda)


mayor_deudor(clientes, 2015)


