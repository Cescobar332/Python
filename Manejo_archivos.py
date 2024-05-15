from io import open
# #archivo_texto = open("archivo.txt", "w")
# archivo_texto = open("archivo.txt", "r")
# #archivo_texto = open("archivo.txt", "a")
archivo_texto = open("archivo.txt", "r+")

# #frase = "Estupendo día para estudiar Python \n el miércoles"
# #archivo_texto.write(frase)
# #archivo_texto.close()
# #archivo_texto.write("\n Siempre es una buena ocasión para estudiar python")
# texto = archivo_texto.read()
lineas_texto = archivo_texto.readlines()
print(lineas_texto[1])
# archivo_texto.seek(len(texto)/2)
# print(texto)
lineas_texto[1] = " Esta línea ha sido incluida desde el exterior \n"
archivo_texto.seek(0)
archivo_texto.writelines(lineas_texto)
archivo_texto.close()