import random as rd

def dv01(cpf):
    soma = 0
    for i in range(8):
        soma = cpf[i] * i+1
    print(soma)
    return soma
    

cpf = [0,0,0,0,0,0,0,0,0,0,0]

for i in range(8):
    cpf[i] = rd.randint(0, 9)

print(cpf)
dv01(cpf)