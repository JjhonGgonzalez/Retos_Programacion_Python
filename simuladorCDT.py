def CDT(usuario:str, capital:int, tiempo:int):
    if tiempo <=2:
        valor_perder = capital * 0.02
        valor_total = capital - valor_perder
    else:
        valor_intereses = (capital * 0.03 * tiempo) /12
        valor_total = valor_intereses+capital

    print("Para el usuario{0} La cantidad de dinero a recibir, segun el monto inicial{1} para un tiempo de {2} meses es: {3}".format(usuario,capital,tiempo,valor_total))

    print("Ingrese el usuario: ")
    usuario = input()
    print("Ingrese el monto inicial: ")
    capital = int(input())
    print("Ingrese el tiempo: ")
    tiempo = int(input())

    CDT(usuario,capital,tiempo)