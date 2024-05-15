# listaUno = []
#
# for ex in range(6):
#     listaUno.append(10 ** ex)
#
# listaDos = [10 ** ex for ex in range(6)]
#
# print(listaUno)
# print(listaDos)
# lst = [1 if x % 2 == 0 else 0 for x in range(10)]
# print(lst)
#
# for v in [1 if x % 2 == 0
#            else 0 for x in range(10)]:
#     print(v, end=' ')
# print()
# def imprimirFuncion(args, fun):
#     for x in args:
#         print('f(', x, ')=', fun(x), sep='')
# imprimirFuncion([x for x in range
# (-2, 3)], lambda x: 2 * x ** 2 - 4 * x + 2)
# from os import strerror
# try:
#     cnt = 0
#     s = open('text.txt', "rt")
#     ch = s.read(1)
#     while ch != '':
#         print(ch, end='')
#         cnt += 1
#         ch = s.read(1)
#     s.close()
#     print("/n/nCaracteres en el archivo: ", cnt)
# except IOError as e:
#     print("Se produjo un error de E/S: ", strerror(e.errno) )

#CURSO PYTHON
#FUNCIONES
import math
def suma(num1, num2):
    resultado=num1+num2
    return resultado

def mensaje():
    print("Estamos aprendiendo Python")
    print("Estamos aprendiendo instrucciones básicas")
    print("Poco a poco iremos avanzando")
almacena_resultado=suma(5,8)
print(almacena_resultado)
mensaje()
print("Ejecutando código fuera de función")
print(suma(5,7))
print(suma(2,3))
print(suma(35,358))

#LISTAS
miLista=["María", "Pepe", "Marta", "Antonio"]
print(miLista[:])
print(miLista[2])
print(miLista[-3])
miLista.insert(2, "Sandra")
print(miLista[:2])
print(miLista[1:3])
miLista.extend(["Sandra", "Ana", "Lucía"])
print(miLista[2:])
print(miLista.index("Antonio"))
print("Pepe" in miLista)
print("Abio" in miLista)
miLista=["María", 5, True, 78.35]
print(miLista[2])
miLista.extend(["Sandra", "Ana", "Lucía"])
miLista.remove("Ana")
print(miLista[:])
miLista.remove(5)
print(miLista[:])
miLista.pop()
print(miLista[:])
miLista2=["Sandra", "Lucía"]
miLista3=miLista+miLista2
print(miLista3[:])
miLista=["María", 5, True, 78.35]*3
print(miLista[:])

#TUPLAS
mitupla=("Juan", 13, 1, 1995)
print(mitupla[2])
miLista=list(mitupla)
print(miLista)
miLista=["Juan", 13, 1, 1995]
mitupla=tuple(miLista)
print(mitupla)
print("Juan" in mitupla)
print(mitupla.count(13))
print(len(mitupla))
mitupla=("Juan",)
print(len(mitupla))
mitupla="Juan", 13, 1, 1995
print(mitupla)
mitupla=("Juan", 13, 1, 1995)
nombre, dia, mes, agno=mitupla
print(nombre)
print(mes)
print(agno)
print(dia)
print(mitupla.index(1995))

#DICCIONARIOS
midiccionario={"Alemania":"Berlín", "Francia":"París", "Reino Unido":"Londres", "España":"Madrid"}
midiccionario["Italia"]="Lisboa"
print(midiccionario)
print(midiccionario["Francia"])
midiccionario["Italia"]="Roma"
print(midiccionario)
del midiccionario["Reino Unido"]
print(midiccionario)
midiccionario2={"Alemania":"Berlín", 23:"Jordan", "Mosqueteros":3}
print(midiccionario2)
mitupla2=["España", "Francia", "Reino Unido", "Alemania"]
midiccionario3={mitupla2[0]:"Madrid", mitupla2[1]:"París", mitupla2[2]:"Londres", mitupla2[3]:"Berlín"}
print(midiccionario3["Francia"])
midiccionario2={23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago", "anillos":{"temporadas":[1991, 1992, 1993, 1996, 1997, 1998]}}
print(midiccionario2)
print(midiccionario2["anillos"])
print(midiccionario2.keys())
print(midiccionario2.values())
print(len(midiccionario2))
print("Programa de evaluación de notas de alumnos")
nota_alumno=(input("Ingrese la nota del alumno:"))

#CONDICIONALES
def evaluacion(nota):
    valoracion="aprobado"
    if nota<5:
        valoracion="suspenso"
    return valoracion
print(evaluacion(int(nota_alumno)))

print("Verificación de acceso")
edad_usuario=int(input("Introduce tu edad, por favor"))
if edad_usuario<18:
    print("No puedes pasar")
elif edad_usuario>100:
    print("Edad incorrecta")
else:
    print("Puedes pasar")

nota_alumno=int(input("Introduce tu nota: "))
if nota_alumno<5:
    print("Insuficiente")
elif nota_alumno<6:
    print("Suficiente")
elif nota_alumno<7:
    print("Bien")
elif nota_alumno<9:
    print("Notable")
else:
    print("Sobresaliente")

edad=int(input("Ingresa tu edad: "))
if 0<edad<100:
    print("Edad es correcta")
else:
    print("Edad incorrecta")

salario_presidente=int(input("Introduce el salario del presidente: "))
print("Salarios presidente: ", salario_presidente)
salario_director=int(input("Introduce el salario del director: "))
print("Salarios director: ", salario_director)
salario_jefe_area=int(input("Introduce el salario del jefe de área: "))
print("Salarios jefe de área: ", salario_jefe_area)
salario_administrativo=int(input("Introduce el salario del administrativo: "))
print("Salarios administrativo: ", salario_administrativo)
if salario_administrativo<salario_jefe_area<salario_director<salario_presidente:
    print("Todo funciona correctamente")
else:
    print("Algo va mal en la empresa")

print("Programa de becas Año 2022")
distancia_escuela=int(input("Introduce la distancia a la escuela en km: "))
print(distancia_escuela)
numero_hermanos=int(input("Introduce el n de hermanos en el centro: "))
print(numero_hermanos)
salario_familiar=int(input("Introduce el salario anual bruto"))
print(salario_familiar)
if distancia_escuela>40 and numero_hermanos>2 or salario_familiar<=20000:
    print("Tienes derecho a beca")
else:
    print("No tienes derecho a beca")

print("Asignaturas Optativas")
print("Informática gráfica - Pruebas de software - Usabilidad y accesibilidad")
opcion=input("Escribe la asignatura escogida: ")
asignatura=opcion.lower()
if asignatura in ("informática gráfica", "pruebas de software", "usabilidad y accesibilidad"):
    print("Asignatura elegida: ", asignatura)
else:
    print("No está entre las opciones a elegir")

#BUCLES
for i in [1, 2, 3]:
    print("Hola")

for i in ["primavera", "verano", "otoño", "invierno"]:
    print("Hola", end=' ')
    print(i)

email=False
miEmail=input("Introduce tu dirección de email: ")
for i in miEmail:
    if(i=="@"):
        email=True
if email==True:
    print("Email es correcto")
else:
    print("El email no es correcto")

contador=0
miEmail=input("Introduce tu dirección de email: ")
for i in miEmail:
    if(i=="@" or i=="."):
        contador=contador+1
if contador == 2:
    print("Email es correcto")
else:
    print("El email no es correcto")

for i in range(5):
    print("Hola")
    print(i)

for i in range(5, 50, 3):
    print(f"valor de la variable {i}")

valido=False
miEmail=input("Introduce tu dirección de email: ")
for i in range(len((miEmail))):
    if miEmail[i]=="@":
        valido=True
if valido:
    print("Email correcto")
else:
    print("Email incorrecto")

i=1
while i<=10:
    print("Ejecución ", str(i))
    i=i+1
print("Terminó la ejecución")

edad=int(input("Introduce tu edad: "))
while edad<5 or edad>100:
    print("Has introducido una edad incorrecta. Vuelve a intentarlo")
    edad = int(input("Introduce tu edad: "))
print("Gracias por colaborar. Puedes pasar")
print("Edad del aspirante: ", str(edad))

#import math
print("Programa de cálculo de raíz cuadrada")
numero=int(input("Introduce un número por favor: "))
intentos=0
while numero<0:
    print("No se puede hallar la raíz de un número negativo")
    if intentos==2:
        print("Has consumido demasiados intentos. El programa ha finalizado")
        break
    numero = int(input("Introduce un número por favor: "))
    if numero<0:
        intentos=intentos+1
if intentos<2:
    solucion=math.sqrt(numero)
    print("La raíz cuadrada de", str(numero), " es ", str(solucion))

for letra in "Python":
    if letra=="h":
        continue
    print("Viendo la letra: ", letra)

nombre="Píldoras Informáticas"
contador=0
for i in nombre:
    if i==" ":
        continue
    contador+=1
print(contador)

# while True:
#     pass
# class MiClase:
#     pass #Para implementar más tarde
email=input("Introduce tu email: ")
for i in email:
    if i=="@":
        arroba=True
        break
else:
    arroba=False
print(arroba)

#GENERADORES
# def generaPares(Limite):
#     num=1
#     miLista=[]
#     while num<Limite:
#         miLista.append(num*2)
#         num=num+1
#     return miLista
# print(generaPares(10))
def generaPares(Limite):
    num=1
    while num<Limite:
        yield num*2
        num=num+1
devuelvePares=generaPares(10)
print(next(devuelvePares))
print("Aquí podría ir más código")
print(next(devuelvePares))
print("Aquí podría ir más código")
print(next(devuelvePares))

def devuelve_ciudades(*ciudades):
    for elemento in ciudades:
        yield from elemento
ciudades_devueltas=devuelve_ciudades("Madrid", "Barcelona", "Bilbao", "Valencia")
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))

#EXCEPCIONES
def suma(num1, num2):
    return num1 + num2


def resta(num1, num2):
    return num1 - num2


def multiplica(num1, num2):
    return num1 * num2


def divide(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print("No se puede dividir entre 0")
        return "Operación errónea"

while True:
    try:
        op1 = (int(input("Introduce el primer número: ")))

        op2 = (int(input("Introduce el segundo número: ")))
        break

    except ValueError:
        print("Los valores introducidos no son correctos. Inténtalo de nuevo")

operacion = input("Introduce la operación a realizar (suma,resta,multiplica,divide): ")

if operacion == "suma":
    print(suma(op1, op2))

elif operacion == "resta":
    print(resta(op1, op2))

elif operacion == "multiplica":
    print(multiplica(op1, op2))

elif operacion == "divide":
    print(divide(op1, op2))

else:
    print("Operación no contemplada")

print("Operación ejecutada. Continuación de ejecúción del programa ")

def divide():
    try:
        op1=(float(input("Introduce el primer número")))
        op2 = (float(input("Introduce el segundo número")))
        print("La división es: ", str(op1/op2))
    except ValueError:
        print("El valor introducido es erróneo")
    except ZeroDivisionError:
        print("No se puede dividir entre 0")
    finally:
        print("Cálculo finalizado")
divide()

def evaluaEdad(edad):
    if edad <0:
        raise TypeError("No se permiten edades negativas")
    elif edad<20:
        return "eres muy joven"
    elif edad<40:
        return "Eres joven"
    elif edad<65:
        return "Eres maduro"
    elif edad<100:
        return "Cuídate"
print(evaluaEdad(-15))

#import math
def calculaRaiz(num1):
    if num1<0:
        raise ValueError("El número no puede ser negativo")
    else:
        return math.sqrt(num1)
op1=(int(input("Introduce un número: ")))
try:
    print(calculaRaiz(op1))
except ValueError as ErrorDeNumeroNegativo:
    print(ErrorDeNumeroNegativo)
print("Programa terminado")

#