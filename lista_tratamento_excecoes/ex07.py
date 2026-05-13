def verificar_nota(nota):
    if nota < 0 or nota > 10:
        raise ValueError(
            'Nota inválida: deve estar entre 0 e 10'
        )
    
    return nota

print(verificar_nota(8))
print(verificar_nota(-3))
print(verificar_nota(15))