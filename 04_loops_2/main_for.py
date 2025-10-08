
# while


for i in range(10):
    print(i, end=" ")

print("")


for i in range(10):
    if i == 5:
        break

    print(i, end=" ")

print("")


for i in range(10):
    if i == 5:
        continue

    print(i, end=" ")

print("")

"""
Faça um porgrama que calcule a tabuada, 
deve perguntar ao utilzador que tabuada que quer ver 

"""
"""
num = int(input("digite um numero: "))
print(f"tabuada: {num}")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

"""


"""
adapte o ex antetior de forma a repetir o processo 
até o utilizador indicar que quer ver uma tabuada negativa 

qts num vão ser pedidos ?
"""


"""
while ?
for   ?

"""

while True:
    num = int(input("digite um numero: "))
    if num < 0:
        print("o utilizador terminou o programa")
        break

    print(f"tabuada: {num}")
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")



