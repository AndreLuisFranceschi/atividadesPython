linha = '-='*20
frutas = ['Maçã', 'Banana', 'Laranja', 'Melão']
print(linha)
print(f'{"<<< BEM VINDOS À FRUTEIRA >>>":^40}')
print(linha)
print('Escolha a sua fruta:')
for i in range(0, len(frutas)):
    print(f'{i}. {frutas[i]}')
print(linha)
cliente = str(input('Olá, nobre cliente, digite seu nome: '))
opc = int(input('Digite sua opção: '))
print(linha)
if opc in range(0, len(frutas)):
    print(f'Cliente: {cliente}\nFruta Escolhida: {frutas[opc]}')
else:
    print('Opção inválida!')
