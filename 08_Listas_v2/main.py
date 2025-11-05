"""

tipos de dados
var
    criar
    usar
    mudar valor de uma var
op mat com var

in/out
    input
    print

condições
    if - elif - else
    match - case

range

loops
    while
    for

Func (def)

listas


hoje:
    rever listas
    tuplos
    usar multiplos files
    classes

Trabalho - incluir tudo

"""


nomes = ["Rui", "Joao", "Carlos", "Rita", "Maria", "Joana", "Diana"]

print(nomes)

print(nomes[0])

print(nomes[3])

# print(nomes[99])

print(len(nomes)) # len() -> num de elm na lista

nomes.append("Luis")

print(nomes)
print(len(nomes))

nomes.insert(0, "Pedro")
print(nomes)
print(len(nomes))



nomes.insert(4, "Gonçalo")
print(nomes)
print(len(nomes))


print("---------")
"""

Cria uma lista com 5 nomes
mostre o numero de elementos na lista
peça ao utilizador 3 nomes
    o 1º adicione ao final da lista
    o 2º adicione ao inicio da lista
    o 3º adicione ao no meio da lista (não tem de ser exatamente na pos central )
mostre novamente o numero de elementos na lista

"""
"""
nomes = ["Rui", "Joao", "Carlos", "Rita", "Maria"]
print(f"a lista inicial tem {len(nomes)} elementos")

nome1 = input("informe o nome do primeiro nome: ")
nome2 = input("informe o nome do segundo nome: ")
nome3 = input("informe o nome do terceiro nome: ")

print(nome1)
print(nome2)
print(nome3)

nomes.append(nome1) # adicionar sempre no final
nomes.insert(0, nome2)
nomes.insert(3, nome3)# adicionar no index indicado

"""
print(nomes)


print(f"a lista final tem {len(nomes)} elementos")

nomes.insert(8999999999, "novo Nome")
print(nomes)




"""
Listas 
    num de elementos
    criamos
    add elem
    acedemos a ele 
"""
print("----- Remover -----")
# Remover
nomes = ["Rui", "Joao", "Carlos", "Rita", "Maria", "Joana", "Diana"]
print(nomes)
# pelo idx

nomes.pop() # se vazio -> remove o ultimo elm
print(nomes)


nomes.pop(3) # se indicar valor  -> remove o elm no idx indicado
print(nomes)


"""

Cria uma lista com 5 nomes
mostre a lista inicial 
    
    remova um elemento do meio da lisra
    remova o  1º elm  da lista
    remova o ultimo  elm  da lista
    
mostre a lista final

Quando estiver terminado -> levantar a mão

"""
print("---------")
nomes = ["Rui", "Joao", "Carlos", "Rita", "Maria"]

print(nomes)

nomes.pop(2)
print(nomes)

nomes.pop(0)
print(nomes)

nomes.pop()
print(nomes)

# pelo valor

print("---------")
nomes = ["Rui", "Joao", "Carlos", "Rita", "Maria", "Joana", "Diana"]
print(nomes)

nomes.remove("Joao")
print(nomes)

print("---------")
nomes = ["Rui", "Joao", "Carlos", "Rita","Joao", "Maria", "Joana", "Diana", "Joao"]
print(nomes)

nomes.remove("Joao")
# print(nomes.index("Joao", 5))

print("---------")

"""
Listas 
    num de elementos
    criamos
    add elem
    acedemos a ele 
    remove elem
        idx
        valor
    percorrer a lista  
"""
print("---------")

nomes = ["Rui", "Joao", "CarlOs", "RIta","JoAo", "Maria", "JoAna", "diana", "Joao"]
print(nomes)
print("--")
for elemento in nomes:
    print(f"o nome é {elemento.capitalize()}")

print("---------")



# num = input("informe um numero: ") # -> recebe um str -> txt

# num = int(input("informe um numero: ")) # -> recebe um str e converte para int

"""
crie uma lista com 2 valores inteiros 
Peça ao utilzador números ate ser intruduzido um valor negativo 
adicione esse numero no fim da lista 

mostre a lista
"""

lista1 = [1 ,2]
print("---- Aqui ----")
while True:
    num = int(input("informe um numero: "))

    if num < 0:
        break

    lista1.append(num)



print(lista1)

"""

tendo a lista [1,12,34,134,1241,4123]

peça ao utilziador um num e adcione a lista na pos correcta de forma a que a liste fique sempre ordenada 

"""
print("---- Aqui2 ----")
lista = [1,12,34,134,1241,4123]
num = int(input("informe um numero: "))


for i in range(0,len(lista)):
    if lista[i] > num:
        lista.insert(i, num)
        break


print(lista)

"""
Ex2:

crie uma lista com 2 valores inteiros, ordenados 
Peça ao utilzador um número indeterminado de valores inteiros 
    (quando for inserido um valor negativo o loop deve terminar)
adicione o numero fornecido na posição correta para que a lista fique ordenada 

"""
print("---- Aqui3 ----")


print("---- Aqui4 ----")
lista1 = [1 ,2]
print(lista1)
while True:
    num = int(input("informe um numero: "))

    if num < 0:
        break

    if num > lista1[-1]:
        lista1.append(num)
        continue

    for i in range(0, len(lista1)):
        if lista1[i] > num:
            lista1.insert(i, num)
            break


    print(lista1)
