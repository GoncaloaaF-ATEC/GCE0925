"""

tipos de dados
Var
in/out
op com var

Comentarios
    1 linha
    multi linha

condições
    if-elif-else
    match-case

loops
    while


"""

"""

break
continue 
range
for

while vs for

funcs ?

"""


num = 10

while num > 0:
    print(num, end=" ")

    num -= 1

print("")

print("---while num > 0:---")
num = 10
while num > 0:

    if num == 2:
        break

    print(num, end=" ")
    num -= 1

print("")
print("---while True:---")









num = 0
while True: # ter cuidado
    # print(num) # opt1 -> 0 ate ao 121
    num += 1
    print(num) # 1 ate ao 122

    if num == 122:
        break


"""

peça ao utilizado 15 números inteiros positivos. <- Done
termine o loop se o utilizador inserir um numero negativo
e indique:
    o maior 
    o menor
    a media  

"""

total = 15
i = 0
maior = 0
menor = 0
media = 0
sum = 0

while i < total:
    i += 1

    num = int(input(f"digite o {i} numero: "))

    if num < 0:
        print("numero negativo, o programa vai terminar")
        i -= 1
        break

    sum += num

    if i == 1:
        maior = num
        menor = num

    if num > maior:
        print("numero maior")
        maior = num

    if num < menor:
        print("numero menor")
        menor = num


print(f"maior = {maior}")
print(f"menor = {menor}")
print(f"total de num = {i}")
print(f"soma = {sum}")
avg = sum / i
print(f"avg = {avg}")


"""
n = 10
max = 10
min = 10

n= 15
max = 15
min = 10

n=4
max= 15
min=4



"""


