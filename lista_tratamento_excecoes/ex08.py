def abrir_arquivo():
    print('Abrindo arquivo...')
    try:
        resultado = 10/0
    except ZeroDivisionError:
        print('Erro: não é possível realizar uma divisão por 0')
    finally:
        print('Fechando arquivo...')
    
print(abrir_arquivo())