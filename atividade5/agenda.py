class Agenda:

    def __init__(self, nome, sobrenome, telefone):
        self.nome = nome
        self.sobrenome = sobrenome
        self.telefone = telefone

    def mostra_registro(self):
        print(f'Nome: {self.nome:<20} Fone: {self.telefone}')
