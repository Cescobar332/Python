nombre = str(input("Nombre del estudiante: "))
n1 = float(input("Ingrese la primera nota: "))
n2 = float(input("Ingrese la segunda nota: "))
n3 = float(input("Ingrese la tercera nota: "))
n4 = float(input("Ingrese la cuarta nota: "))
prom = (n1 + n2 + n3 + n4) / 4
if prom >= 3:
    print("El promedio del estudiante ", nombre, " es :", prom, " , pasó la materia")
else:
    print("El promedio del estudiante ", nombre, " es :", prom, " , perdió la materia")
