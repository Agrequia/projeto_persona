import random as rd

def int2list(valor):
    list = []
    while valor != 0:
        list.append(valor % 10)
        valor = valor // 10
    list.reverse()
    return list

def list2int(lista):
    valor = 0
    multiplicador = 10000000000
    for i in lista:
        valor = valor + (i * multiplicador)
        multiplicador = multiplicador // 10
    return valor

def dv02(cpf):
    soma = 0
    for i in range(10):
        soma = soma + cpf[i] * (11-i)
    resto = soma % 11
    if resto >= 2:
        cpf.append(11-resto)
    else:
        cpf.append(0)
    return cpf

def dv01(cpf):
    soma = 0
    for i in range(9):
        soma = soma + cpf[i] * (10-i)
    #print(soma)
    resto = soma % 11
    if resto >= 2:
        cpf.append(11-resto)
    else:
        cpf.append(0)

    cpf = dv02(cpf)    
    return cpf
    
cpf = rd.randint(100000000, 999999999)

lista_CPF = int2list(cpf)
lista_CPF = dv01(lista_CPF)
print(list2int(lista_CPF))