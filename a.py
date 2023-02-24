numero=input("Ingresa el numero en binario ")

def sumar_binarios(bin1, bin2):
    num1 = int(bin1, 2)
    num2 = int(bin2, 2)
    suma = bin(num1 + num2)[2:]
    max_len = max(len(bin1), len(bin2))
    suma = suma.zfill(max_len)
    return suma

def a1(numero):

    numeroa1=""
    for i in numero:
        if i=="1":
            numeroa1+="0"
        elif i=="0":
            numeroa1+="1"
        else:
            pass
    return numeroa1
def a2(numero):
    auxa1=a1(str(numero))
    result=sumar_binarios(auxa1,"1")
    return result


convertidoa1=a1(numero)
convertidoa2=a2(numero)

print(f"Normal------->: {numero}")
print(f"A1----------->: {convertidoa1}")
print(f"A2----------->: {convertidoa2}")


