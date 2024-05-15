clas=[]
i=0
print(":Bienvenido al baloto Clásico, escoja 5 números: ")
while i<=4:
    baloto=int(input("Ingrese el número de la balota, tiene que ir desde el 1 hasta el 69: "))
    if 1<=baloto<=69:
        clas.append(baloto)
        i=i+1
    else:
        print("El número debe estar en el rango entre 1 y 69, inténtalo de nuevo.")
print("Balotas escogidas: ", clas)

power=[]
i=0
print(" Bienvenido al baloto PowerBall, escoja un número: ")
while i<=0:
    baloto=int(input("Ingrese el número de la balota que desea escoger, debe de estar entre el 1 y el 26: "))
    if 1<=baloto<=26:
        power.append(baloto)
        i=i+1
    else:
        print("El número debe estar en el rango entre 1 y 26, intente de nuevo.")
print("Balotas escogidas: ", power)

print("Moneyball:")
import random
moneyball=['$0', '$10', '$20', '$50', '$100']
random.choice(moneyball)
print("Gracias por participar, ten un obsequio: ", random.choice(moneyball))

print("Get Lucky: ")
from random import randint, choice, sample
print("Baloto: ", end=' ')
for i in range(5):
    print(randint(1, 69), end=' ')

print()
from random import randint, choice, sample
print("Baloto Powershell: ", end=' ')
for i in range(1):
    print(randint(1, 26))
moneyball=['$0', '$10', '$20', '$50', '$100']
random.choice(moneyball)
print("Moneyball: " , random.choice(moneyball))
