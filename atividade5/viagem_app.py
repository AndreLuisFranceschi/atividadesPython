from viagem import Viagem

print(f'{"<<< CADASTRO DE VIAGENS >>>":^40}')
print('-='*20)
nome = input('Olá, turista, qual o seu nome? ')
print('Caro ', nome, ', qual o seu destino?')

print('-='*20)
cidades = ['Rio de Janeiro', 'Orlando', 'Paris', 'Pequim']
valores = [800.00, 1600.00, 2400.00, 3200.00]
for i in range(0, 4):
    print(f'{i}. {cidades[i]:<18} R$ {valores[i]:>6}')
print('-='*20)

opc = int(input('Qual a sua opção? '))
if opc in range(0, 4):
    viagem1 = Viagem(nome, cidades[opc], valores[opc])
    print(f'Parabéns, {nome}, sua viagem para {cidades[opc]} foi registrada com sucesso!')
else:
    print('Opção inválida!')
