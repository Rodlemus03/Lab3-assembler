def hexa_deci(numero):

    digit1 = int(numero[0], 16)
    digit2 = int(numero[1], 16)
    digit3 = int(numero[2], 16)

    decimal = digit1 * 16*2 + digit2 * 161 + digit3 * 16*0

    return decimal

def deci_hexa(numero):
    respuesta=""
    while numero>0:
        residuo=numero%16
        if residuo<=9:
            respuesta+=str(residuo)
        else:
            respuesta+=chr(residuo+55)
        numero//=16
    return respuesta[::-1]


print("BIENVENIDO ")
print("Deseas pasar \n1. Hexadecimal a decimal\n2. Decimal a hexadecimal")
r=input("--> ")

if r=="1":
    hexa=input("Ingresa tu numero hexadecimal ")
    r1=hexa_deci(hexa)
    print(r1)
elif r=="2":
    base10=input("Ingresa tu numero decimal ")
    print("")
    respuestaSecundaria=deci_hexa(int(base10))
    print(respuestaSecundaria)
else:
    print("Ingresa un caracter valido ")