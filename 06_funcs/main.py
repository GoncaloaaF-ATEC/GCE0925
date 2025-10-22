""""
var
tipos de dados
op com var
in/out
condições
    if
    switch-case
range
loops
    for
    while

intro a funcs


hoje (22)
funcs
listas

"""



def ola_mundo():
    print("ola")


# print("ola")

ola_mundo()
ola_mundo()


def soma_org():
    resultado = 10 + 30
    print(f"o resultado da soma é {resultado}")

soma_org()


"""
crie uma função que mostre todos os números inteiros de 0 a 10
"""

def ex1_aula():
    for num in range(0, 11):
        print(num, end=" ")
    print()

ex1_aula()

"""
crie uma função que mostre todos os números par de 0 a 10
"""

def ex2_aula():
    for num in range(0, 11):
        if num % 2 == 0:
            print(num, end=" ")
    print()

ex2_aula()




def soma(val1, val2):
    resultado = val1 + val2
    print(resultado)


soma(val1=1, val2=2)
soma(val1=12, val2=31)

soma(12, 31) # -> soma(12,31) o val1: e val2: é o PyCharm que adiciona



def subtracao(val1, val2):
    resultado = val1 - val2
    print(resultado)

subtracao(1, 2) # -> subtracao(1,2) o val1: e val2: é o PyCharm que adiciona
subtracao(10, 6)


def subtracao2(val1, val2):
    resultado = val2 - val1
    print(resultado)


subtracao2(1, 2)

"""

em py uma func sem param -> def nome_da_func():
em py uma func 1 param -> def nome_da_func(param1):
em py uma func multi param  -> def nome_da_func(param1, param2, ..., paramN):


"""

"""
crie uma função que mostre todos os números inteiros de dois valores recebidos como parametro 

def ex3_aula(menor, maior):

"""

def ex3_aula(menor, maior):
    for num in range(menor, maior+1):
        print(num, end=" ")

print("-----")
ex3_aula(20, 10)

print("-----")

print("--ex4_aula---")

def ex4_aula(val_a, val_b):
    # ver qual dos 2 param é o menor
    if val_a > val_b:
        maior = val_a
        menor = val_b
    else:
        maior = val_b
        menor = val_a


    for num in range(menor, maior+1):
        print(num, end=" ")
    print()

ex4_aula(10, 20)


print("-----")

ex4_aula(20, 10)


print("--- soma_2 ---")

def soma_2(val1, val2):
    resultado = val1 + val2
    return resultado

print("-----")

soma_2(19, 11)

print("-----")
print(soma_2(19, 11))



print("-----")

num = soma_2(11, 11)
print(num)

print("-----")



def subtracao3(val1, val2):
    resultado = val1 - val2
    print(resultado)


subtracao3(soma_2(11, 11), 12)

# (3 * ( 1 * (1 + 4) + 2) - 1 )
# (3 * ( 1 * 5 + 2) - 1 )
# (3 * 7 - 1 )
# (21 - 1 )
# 20

"""
 
crie uma função que receba de três argumentos, e devolva a soma desses três argumentos.

"""
def ex5_aula(val1, val2, val3):
    resultado = val1 + val2 + val3
    return resultado







print("-----")
def soma7():
    resultado = 10 + 30
    print(resultado)

soma7()

print("-----")

def soma8(val1):
    resultado = 10 + val1
    print(resultado)

soma8(13)

soma8(123)

print("-----")

def soma9(val1, val2):
    resultado = val1 + val2
    print(resultado)

soma9(12,14)


"""
crie uma função que receba de um argumento, pode assumir que será inteiro  
A função retorna: 
 - ‘P’, se seu argumento for positivo,
 - ‘N’, se seu argumento for zero ou negativo.

"""

