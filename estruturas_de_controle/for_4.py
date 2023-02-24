from random import randint

def sortear():
    return randint(1, 6)

for x in range(1, 7):
    if x % 2 == 1:
        continue

    elif sortear() == x:
        print('Acertou!', x)
        break

else:
    print('Não acertou o número!')