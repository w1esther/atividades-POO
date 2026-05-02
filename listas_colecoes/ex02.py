contagem = {}

while True:
    entrada = input("Digite o ano de nascimento (ou pressione Enter para finalizar): ")
    
    if entrada == "":
        break

    else:
        ano = int(entrada)
        
        if ano in contagem:
            contagem[ano] += 1
        else:
            contagem[ano] = 1

print("\nRelatório de anos de nascimento:")
for ano in sorted(contagem):
    print(f"Ano {ano}: {contagem[ano]} pessoa(s)")