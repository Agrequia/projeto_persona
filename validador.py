def string2list(valor):
    list = []
    i = 0
    while i < 11:
        list.append(valor[i])
        i = i + 1
    return list

def dv02(cpf):
    soma = 0
    for i in range(10):
        soma = soma + int(cpf[i]) * (11-i)
    resto = soma % 11
    if ((resto >= 2) & (int(cpf[10]) == (11-resto))) | ((resto < 2) & (int(cpf[10]) == 0)):
        print("CPF válido!")
    else:
        print("CPF inválido! Digito Verificador 02 incorreto.")

def dv01(cpf):
    soma = 0
    for i in range(9):
        soma = soma + int(cpf[i]) * (10-i)
    resto = soma % 11
    if ((resto >= 2) & (int(cpf[9]) == (11-resto))) | ((resto < 2) & (int(cpf[9]) == 0)):
        cpf = dv02(cpf)
    else:
        print("CPF inválido! Digito Verificador 01 incorreto.")
    
cpf = input("Insira o CPF: ")
lista_CPF = string2list(cpf)
lista_CPF = dv01(lista_CPF)







#08925848902