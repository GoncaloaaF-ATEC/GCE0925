#isto é um comentário e vai ser ignorado
#
#
# O CÓDIGO TEM DE ESTAR ALINHADO
#
#

"""
cmt
multi
linha
"""



# Var, tipos de dados e print (out), concat Str

print("Ola Mundo") # o print() mostra uma a msg que esta ( ) na consola

nome = "Gonçalo" # String (str) -> Texto, "esta sempre entre aspas"
ano = 2025       # int -> representa números inteiros

# nome = 123 # -> funciona mas devem evitar que um var mude o tipo de dados

altura = 1.76   # float -> representa números decimais
aprovado = True # bool -> representa True ou False

print("Ola Mundo", nome) # estou a "juntar" a str "Ola Mundo" com a var nome -> funciona apenas no print

print(f"Ola Mundo {nome}") # estou a criar uma f-string que me permite colocar var dentro de Strings
                          # e fazer o seu print

msg = f"Ola Mundo {nome}"# estou a criar uma f-string que me permite colocar var dentro de Strings e
                         # a colocar o seu var na var msg

print(msg) # mostrar a var msg


#"Estanos no ano de [2025]. O [Gonçalo] tem [1.76]m"
print("Estanos no ano de 2025. O Gonçalo tem 1.76m  <-- Objetivo")
print("Estanos no ano de", ano, ". O", nome, "tem", altura, "m")
print(f"Estanos no ano de {ano}. O {nome} tem {altura}m")
# print(nome)
# print(ano)

# op var - 1 tipo

num1 = 10
num2 = 20

soma = num1 + num2
print(f"{num1} + {num2} = {soma}")


sub1 = num1 - num2
print(f"{num1} - {num2} = {sub1}")

sub2 = num2 - num1
print(f"{num2} - {num1} = {sub2}")

multip = num1 * num2
print(f"{num1} x {num2} = {multip}")

div = num1 / num2
print(f"{num1} / {num2} = {div}")



"""

7 % 3 -> 1

7 Mod 3 

0 1 2 3 4 5 6 7
0 1 2 0 1 2 0 1

7 Mod 4

0 1 2 3 4 5 6 7
0 1 2 3 0 1 2 3

"""

num1 = 7
num2 = 2

mod = num1 % num2 # % -> modulo ->  num1 Mod num2 -> Resto da div
print(f"{num1} % {num2} = {mod}")

div_int = num1 // num2 # // -> div inteira
print(f"{num1} // {num2} = {div_int}")


num1 = 7.5
num2 = 2.25

mod = num1 % num2 # % -> modulo ->  num1 Mod num2 -> Resto da div
print(f"{num1} % {num2} = {mod}")

div_int = num1 // num2 # // -> div inteira
print(f"{num1} // {num2} = {div_int}")

# op multi tipos

num1 = 7.5
num2 = 2

soma2 = num1 + num2
print(soma2)

num1 = 7.5
num2 = 2
div3 = num1 / num2
print(div3)


num1 = 8
num2 = 2
div3 = num1 / num2 # a div devolve sp um float
print(div3)


# op com str


print("str1" + "str2")

# print("str1" + 19) # o op + "so" func com num +, -, /  num ou str + str

print(" str1 " * 3) # devolve ->  str1  str1  str1


# input

nome = input("Digite seu nome: ") # receber dados do utilizado, mostra a msg q esta ()
                                  # o valor recebido e sempre String

print(f"o nome inserido foi: {nome}")


ano_curr = 2025
idade = int(input("Digite sua idade: ")) # int(), converte para int o que esta (), se não for possível -> Erro
ano_nasc = ano_curr - idade
print(ano_nasc)