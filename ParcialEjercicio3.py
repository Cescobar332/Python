import random
print("Bienvenido a la Pizzería Autónoma, qué desea ordenar?")
print("Tipos de masa: 1. Masa napolitana, · 2. Masa romana · 3. Masa estilo Chicago. Todas las masas valen $2000")
print("Tipos de queso: 1. Mozzarella, vale $800 · 2. Queso Gouda, vale $1500 · 3. Queso parmesano, vale $1000 · 4. Queso cuartirolo, vale $2000 · 5. Queso Roquefort, vale $3000")
print("Carnes disponibles: 1. Molida, vale $500 · 2. Salami, vale $1000 · 3. Pepperoni, vale $1200 · 4. Jamón, vale $800 · 5. Cábano, vale $1500")
print("Verduras disponibles: 1. Tomates, vale $1300 · 2. Rúgula, vale $2000 · 3. Cebolla, vale $1500 · 4. Cilantro, vale $700")
print("Bebidas: 1. Cocacola, vale $2000 · 2. Sprite, vale $1700 · 3. Quatro, vale $1400 · 4. Pepsi, vale $1000 · 5. Mr Tea, vale $900")
orden = []
num=random.randint(0, 1000)
precio=0
precio1=0
precio2=0
precio3=0
precio4=0
masa = int(input("Elija su tipo de masa: "))
if masa==1:
    orden.extend(["Masa napolitana"])
    precio=precio+2000
elif masa==2:
    orden.extend(["Masa romana"])
    precio=precio+2000
elif masa==3:
    orden.extend(["Masa estilo Chicago"])
    precio=precio+2000
queso = int(input("Elija su tipo de queso: "))
if queso ==1:
    orden.extend(["Mozzarella"])
    precio1=precio1+800
elif queso == 2:
    orden.extend(["Queso gouda"])
    precio1=precio1+1500
elif queso == 3:
    orden.extend(["Queso parmesano"])
    precio1=precio1+1000
elif queso == 4:
    orden.extend(["Queso cuartirolo"])
    precio1=precio1+2000
elif queso == 5:
    orden.extend(["Queso Roquefort"])
    precio1=precio1+3000
carne = int(input("Elija su carne: "))
if carne == 1:
    orden.extend(["Molida"])
    precio2=precio2+500
elif carne == 2:
    orden.extend(["Salami"])
    precio2=precio2+1000
elif carne == 3:
    orden.extend(["Pepperoni"])
    precio2=precio2+1200
elif carne == 4:
    orden.extend(["Jamón"])
    precio2=precio2+800
elif carne == 5:
    orden.extend(["Cábano"])
    precio2=precio2+1500
verdura = int(input("Elija su verdura: "))
if verdura == 1:
    orden.extend(["Tomate"])
    precio3 = precio3 + 1300
elif verdura == 2:
    orden.extend(["Rúgula"])
    precio3 = precio3 + 2000
elif verdura == 3:
    orden.extend(["Cebolla"])
    precio3 = precio3 + 1500
elif verdura == 4:
    orden.extend(["Cilantro"])
    precio3 = precio3 + 700
bebida = int(input("Elija su bebida: "))
if bebida == 1:
    orden.extend(["Cocacola"])
    precio4 = precio4 + 2000
elif bebida == 2:
    orden.extend(["Sprite"])
    precio4 = precio4 + 1700
elif bebida == 3:
    orden.extend(["Quatro"])
    precio4 = precio4 + 1400
elif bebida == 4:
    orden.extend(["Pepsi"])
    precio4 = precio4 + 1000
elif bebida == 5:
    orden.extend(["Mr Tea"])
    precio4 = precio4 + 900
valor=precio+precio1+precio2+precio3+precio4
print("Número de orden: ",num ,". Su orden es la siguiente: ", orden[:], " y tiene un valor total de $", valor)