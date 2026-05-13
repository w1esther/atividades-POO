class SenhaCurtaError(Exception):
    pass

def cadastrar_senha(senha: str):
    try:
        if len(senha) < 8:
            raise SenhaCurtaError('Sua senha tem menos de 8 caracteres')
        print('Senha cadastrada com sucesso!')
    
    except SenhaCurtaError as erro:
        print(f'Erro: {erro}')

cadastrar_senha('12345678')
cadastrar_senha('1234567')