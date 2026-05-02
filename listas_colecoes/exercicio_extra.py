dicionario = {}

while True:

    idade = input('Digite a Idade ou Enter para parar: ')

    if idade == '':
        break

    else:
        idade = int(idade)
        if idade in dicionario:
            dicionario[idade] += 1
        else:
            dicionario[idade] = 1

for idade in sorted(dicionario):
    print(f'Idade: {idade}\nQuantidade de Pessoas: {dicionario[idade]}')