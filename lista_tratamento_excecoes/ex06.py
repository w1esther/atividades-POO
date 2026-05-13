def divisao_segura(a, b):

    try: 
        return a/b
    
    except ZeroDivisionError:
        print('Erro: divisão por 0')
        return None
    
    except TypeError:
        print('Erro: os valores devem ser numéricos')
        return None

print(divisao_segura(16, 8))
print(divisao_segura(20, 0))
print(divisao_segura('oi', 'ola'))