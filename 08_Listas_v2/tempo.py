import time

lst = []

ti = time.time()
for i in range(50_000):
    lst.append(i) ## so add no fim
tf = time.time()

tdelta = tf-ti
print(f"append(i) - {tdelta}")

lst = []

ti = time.time()
for i in range(50_000):
    lst.insert(0, i)  ##  add na pos indicada

tf = time.time()

tdelta = tf-ti
print(f"lst.insert(0, i) - {tdelta}")

lst = [23,1,4,1,2,4,1,2,4,1,6]

# append -> add valor
# insert -> se Necessário move a todos os elementos da lista
# #      -> quando a pos estiver vazia add o valor

lst = [6,8, 19, 21]

lst = [6,8, 9999 ,19 ,21]