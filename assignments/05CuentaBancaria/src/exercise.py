def main():
    #escribe tu código abajo de esta línea
    saldo= float(input("Dame el saldo del mes anterior:"))
    ingresos=  float(input("Dame los ingresos:"))
    egresos= float(input("Dame los egresos:"))
    cheques= int(input("Dame el número de cheques:"))
    saldomensual= (saldo+ingresos-egresos-(13*cheques))
    intereses = (saldomensual * 0.075)
    saldofinal = saldomensual - intereses
    print ("El saldo final de la cuenta es: ",saldofinal)
    
    pass



if __name__ == '__main__':
    main()
