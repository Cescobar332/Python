cobro=9.5
opc=float(input("1. Insertar peso en libras.// 2. Insertar peso en kilos: "))
opc2=float(input("1. Insertar moneda en USD.// 2. Insertar moneda en pesos colombianos: "))
if (opc==1):
    peso=float(input("Inserte el peso: "))
    if (opc2==1):
        result=peso*cobro
        print("El envío tiene un valor total de: $",result, " dólares")
    elif(opc2==2):
        pesos = 3788
        pesos = pesos * cobro
        result = peso * pesos
        print("El envío tiene un valor total de: $",result," pesos")
elif(opc==2):
    kilos=float(input("Inserte cuánto pesa el paquete en kilos: "))
    kilos=kilos*2.2
    if (opc2==1):
        result=kilos*cobro
        print("El envío tiene un valor total de: $",result, " dólares")
    elif(opc2==2):
        pesos=3788
        pesos=pesos*cobro
        result=kilos*pesos
        print("El envío tiene un valor total de: $",result, " pesos")
