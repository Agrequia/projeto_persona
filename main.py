import random as rd

cpf = [0,0,0,0,0,0,0,0,0,0,0]

for i in cpf:
    if i < 10:
        cpf[i] = rd.randint(0, 9)
        i = i + 1

print(cpf)