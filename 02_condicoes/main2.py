""""
if media >= 10:
    print(f"Aprovado com {media}")
else:
    # sei q a media é < 10
    if media >= 8: # media esta entre 8 e 10
        print(f"tem direito a recuperação com {media}")
    else:
        print(f"reprovado com {media}")

"""

"""


se          if 
se não      else

"""

"""

se media > 10 ....
se nao se media > 8 ... -> sei que media < 10
se nao ... -> sei se a meida < 8
"""

media = 10

if media >= 10:
    print(f"Aprovado com {media}")
elif media >= 8:
    print(f"reprovado mas com direito a recuperação com {media}")
elif media >= 6:
    print(f"reprovado com {media} mas se nao tiver faltas pode fazer a recuperação ")
else:
    print(f"reprovado com {media}")

########################################

if media >= 10:
    print(f"Aprovado com {media}")
else:
    if media >= 8:
        print(f"tem direito a recuperação com {media}")
    else:
        if media >= 6:
            print(f"reprovado com {media} mas se nao tiver faltas pode fazer a recuperação ")
        else:
            print(f"reprovado com {media}")

