prueba = "Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit"
print("Texto de prueba:", prueba)
if prueba == prueba.upper():
    abc = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
else:
    abc = "abcdefghijklmnñopqrstuv"
k = 2
cifrad = ""
for c in prueba:
    if c in abc:
        cifrad += abc[(abc.index(c) + k) % (len(abc))]
    else:
        cifrad += c
print("Texto cifrado: ", cifrad)
print(len(prueba))
des = "Ngsag rqttq sakusacñ guv sak fqnqtgñ kruañ sakc fqnqt ukv cñgv, eqougevgvat, cfkrkuek bgnkv"
if des == des.upper():
    abc = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
else:
    abc = "abcdefghijklmnñopqrstuv"
k = 2
cifrad = ""
for c in des:
    if c in abc:
        cifrad += abc[(abc.index(c) + (-k)) % (len(abc))]
    else:
        cifrad += c
print("Texto descifrado: ", cifrad)


texto=input("Tu texto: ")
if len(texto)<=5000:
    if texto==texto.upper():
        abc="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    else:
        abc="abcdefghijklmnñopqrstuv"
    k=int(input("Valor de desplazamiento: "))
    cifrad=""
    for c in texto:
        if c in abc:
            cifrad += abc[(abc.index(c)+k)%(len(abc))]
        else:
            cifrad+=c
    print("Texto cifrado: ", cifrad)
    print(len(texto))
    if cifrad == cifrad.upper():
        abc = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    else:
        abc = "abcdefghijklmnñopqrstuv"
    cifrad2 = ""
    for c in cifrad:
        if c in abc:
            cifrad2 += abc[(abc.index(c) + (-k)) % (len(abc))]
        else:
            cifrad2 += c
    print("Texto descifrado: ", cifrad2)
    print(len(texto))
else:
    print("Cantidad máxima excedida, máximo 5000 caracteres, pusiste: ", len(texto))