total = 5
i = 0
maior = 0
menor = 0

while i < total:
    i += 1

    num = int(input(f"digite o {i} numero: "))

    if num > maior:
        print("numero maior")
        maior = num
        continue # -> reinicia o loop

    print("açao pos validade se num > maior ")

    if num < menor:
        print("numero menor")
        menor = num
        continue # -> reinicia o loop

    print("açao pos validade se num > menor ")
