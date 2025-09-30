"""
S1 -

var
tipos de dados
    int
    float
    str
    bool
in/out
    print
    input

conversão de dados

"""

"""
Hoje -

Condições
    if
    elif
    else
        
    match
    case
    
"""


"""

1
2
3
4
 A       B
5.1     5.2
6.1     6.2
7.1     7.2
8

"""

"""
1 and 1 -> 1
1 and 0 -> 0

1 or 0 -> 1
1 or 1 -> 1

1 xor 0 -> 1
1 xor 1 -> 0

"""



"""

>  - maior 
<  - menor 
>= - maior ou igual
<= - menor ou igual
== -> igual 
!= -> diferente 

"""
idade = 10

print("fora do if")
#if condição:
if idade >= 18:
    print("dentro do if")
    print("Adulto")
    print("ainda dentro do if")

print("Já fora do if")



print("-------")


idade = 10

if idade >= 18:
    print("dentro do 2º if")
    print("Adulto")
    print("ainda dentro do 2º if")
else:
    print("Menor")


"""

Faça um programa que pede uma nota ao utilizador e indique se esta aprovado(nota maior que 10) ou reprovado

"""

nota = int(input("Digite sua nota: "))

if nota > 10:
    print("Aprovado")
else:
    print("Reprovado")


# X % 2  = 0 -> par |  X % 2  diferente de 0 -> impar

"""

Faça um programa que pede uma um valor,    
    se for par o programa deve pedir a idade e mostra a idade menos o valor pedido
    se for impar o programa deve perguntar o nome ao utilizador e dizer: "Ola [nome] o valor é [valor]"
    
"""
print("----------- Ex 2 --------------")

valor = int(input("Digite um valor: "))

if valor % 2 == 0:
    idade = int(input("Digite sua idade: "))
    aux = idade - valor
    print(aux)
else:
    nome = input("Digite seu nome: ")
    print(f"Ola {nome} o valor é {valor}")


"""

Faça um programa que peça ao utilizador 4 notas, e calcule a media dessas notas.
caso a media seja positiva deve indicar que foi aprovado e a media
caso a media seja negativa deve indicar que foi reprovado e a media

"""
print("----------- Ex 3 --------------")

nota = int(input("Digite sua nota 1: "))
nota2 = int(input("Digite sua nota 2: "))
nota3 = int(input("Digite sua nota 3: "))
nota4 = int(input("Digite sua nota 4: "))

media = (nota + nota2 + nota3 + nota4) / 4

if media >= 10:
    print(f"Aprovado com {media}")
else:
    print(f"Reprovado com {media}")


"""

Peça ao utilizador para introduzir 4 notas (valores numéricos).
Calcule a média aritmética dessas notas.
Apresente o resultado da seguinte forma:
    Se a média for igual ou superior a 10, deve indicar que o aluno está aprovado.
    Se a média for inferior a 10, verifica-se a seguinte condição:
        Se a média for igual ou superior a 8, o programa deve indicar que o aluno tem direito a recuperação.
        Se a média for inferior a 8, o programa deve indicar que o aluno está reprovado.

"""
print("----------- Ex 4 --------------")

nota = int(input("Digite sua nota 1: "))
nota2 = int(input("Digite sua nota 2: "))
nota3 = int(input("Digite sua nota 3: "))
nota4 = int(input("Digite sua nota 4: "))

media = (nota + nota2 + nota3 + nota4) / 4

media = int(input("media: "))

if media >= 10:
    print(f"Aprovado com {media}")
else:
    # sei q a media é < 10
    if media >= 8: # media esta entre 8 e 10
        print(f"tem direito a recuperação com {media}")
    else:
        print(f"reprovado com {media}")
