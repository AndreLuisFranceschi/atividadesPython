from livro import Livro

livro1 = Livro('"Java: Como Programar"', 'Paul Deitel', 'Informática')
livro2 = Livro('"Engenharia de Software"', 'Ian Sommerville', 'Informática')
livro3 = Livro('"As Aventuras de Toquinho"', 'Michele Lima da Silva', 'Aventura')
livro4 = Livro('"Quincas Borba"', 'Machado de Assis', 'Romance')
livro5 = Livro('"As Crônicas de Nárnia"', 'C.S. Lewis', 'Fantasia')
livro6 = Livro('"2001: Uma Odisseia no Espaço"', 'Arthur C. Clarke', 'Ficção')
livro7 = Livro('"Em Busca de Sentido"', 'Viktor E. Frankl', 'Psicologia')
livro8 = Livro('"A Garota do Lago"', 'Charlie Donlea', 'Suspense')
livro9 = Livro('"O Desfiladeiro do Medo"', 'Clive Barker', 'Terror')
livro10 = Livro('"As Ruínas"', 'Scott Smith', 'Terror')

livros = [livro1, livro2, livro3, livro4, livro5, livro6, livro7, livro8, livro9, livro10]

print('-='*30)
print(f'{"<<< SOLICITAÇÃO DE LIVROS >>>":^60}')
print('-='*30)
for i, v in enumerate(livros):
    print(f'{i}. {livros[i].nome}, {livros[i].autor}, {livros[i].genero}')
print('-='*30)

nome = str(input('Nome do soliciante: '))
opc = int(input('Escolha o número do livro: '))
print('-='*30)
if opc in range(0, 10):
    print(f'Solicitante: {nome}\nOpção: {opc} - {livros[opc].nome}')
else:
    print('Opção inválida!')
print('-='*30)
