from conta import Conta

contaAna = Conta('738-1', 'Ana Vitória', 600.0, 1000.0)
contaJoao = Conta('489-3', 'João da Silva', 300.0, 1000.0)
print('Conta Ana: ', vars(contaAna))
print('Conta João: ', vars(contaJoao))

contaAna.transfere_para(contaJoao, float(input('Valor para transferência: ')))
print('Conta Ana: ', vars(contaAna))
print('Conta João: ', vars(contaJoao))
