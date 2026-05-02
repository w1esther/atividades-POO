agenda = {}

def adicionar_contato(agenda, nome, telefone):
    agenda[nome] = telefone
    return 'Contato adicionado/atualizado com sucesso!'

def buscar_telefone(agenda, nome):
    if nome in agenda:
        return f'Telefone de {nome}: {agenda[nome]}'
    else:
        'Contato não encontrado na agenda'

def remover_contato(agenda, nome):
    if nome in agenda:
        del agenda[nome]
        return 'Contato removido com sucesso!'
    else:
        return 'Conato não encontrado!'
    
def listar_contatos(agenda):
    for elemento in sorted(agenda):
        print(f'Nome: {elemento}, Telefone: {agenda[elemento]}')

while True:
    print("\n--- MENU ---")
    print("1 - Adicionar contato")
    print("2 - Buscar telefone")
    print("3 - Remover contato")
    print("4 - Listar contatos")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        adicionar_contato(agenda, nome, telefone)

    elif opcao == "2":
        nome = input("Nome: ")
        print(buscar_telefone(agenda, nome))

    elif opcao == "3":
        nome = input("Nome: ")
        print(remover_contato(agenda, nome))

    elif opcao == "4":
        listar_contatos(agenda)

    elif opcao == "5":
        print("Saindo...")
        break

    else:
        print("Opção inválida!")