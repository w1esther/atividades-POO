import random

sorteio = random.sample(range(1, 41), 25)
sorteio.sort()
print('Números Sorteados:')
for numero in sorteio:
    print(numero)