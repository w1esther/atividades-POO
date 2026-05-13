def adicionar_valor(inicial, adicional):
    
    if adicional <= 0:
        raise ValueError(
            'Somente valores positivos devem ser adicionados ao valor inicial'
        )
    
    return inicial + adicional

try:
    resultado = adicionar_valor(10, 5)
    print(f'Resultado: {resultado}')

except ValueError as erro:
    print(f'Erro: {erro}')


try:
    resultado = adicionar_valor(10, -5)
    print(f'Resultado: {resultado}')

except ValueError as erro:
    print(f'Erro: {erro}')

# obs: Em Python, exceções são situações de erro ou comportamentos inesperados que interrompem o fluxo normal de execução do programa. Elas acontecem quando o programa encontra uma operação inválida, como por exemplo uma divisão por zero ou a tentativa de converter um texto inválido para número.

# O tratamento de exceções é importante porque evita que o programa encerre abruptamente (“quebre”), permitindo que o erro seja tratado de forma controlada. Além disso, ele melhora a experiência do usuário ao fornecer mensagens claras sobre o problema e ajuda a preservar a integridade dos dados e do sistema, evitando comportamentos incorretos ou perda de informações.