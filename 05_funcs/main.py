"""
if - conduções
for - loops
etc etc

def - funções


"""


def ola_mundo():# c -> void ola_mundo(){printf("Ola Mundo2")}
    print("Ola Mundo")


print("Linha 1")

ola_mundo()
ola_mundo()
ola_mundo()
print("Linha 2")



def ola_mundo2(nome):
    print(f"Ola Mundo, {nome}")


ola_mundo2("Rita")
ola_mundo2("Carlos")
ola_mundo2("Pedro")


"""

Crie uma função que receber um numero e diga se ele e par ou impar 

"""



def par_ou_impar(numero):

    if numero % 2 == 0:
        print(f"O número {numero} é par.")
    else:
        print(f"O número {numero} é ímpar.")




num = int(input("insira o primeiro numero: "))

par_ou_impar(num)
par_ou_impar(31)
par_ou_impar(40)



def ola_mundo3(nome, ano):
    print(f"Ola Mundo, {nome} no ano de {ano}")


ola_mundo3("Rita", 2020)


"""

crie uma função que receba dois números e 
mostre todos os valores inteiros entre esses dois valores  

"""