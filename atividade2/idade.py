def maioridade(idade):
    if idade < 18:
        return True
    else:
        return False

idade = int(input('Qual a sua idade? '))

if maioridade(idade):
    print('MENOR DE IDADE')
else:
    print('MAIOR DE IDADE')
