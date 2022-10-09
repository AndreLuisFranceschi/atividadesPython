class Local:
    def __init__(self, nome, logradouro, cep):
        self.nome = nome
        self.logradouro = logradouro
        self.cep = cep

class Agenda:
    def __init__(self, nome, local, dia, hora, minuto):
        self.nome = nome
        self.local = local
        self.dia = dia
        self.hora = hora
        self.minuto = minuto

    def mostra_compromisso(self):
        print(f'Compromisso: {self.nome} | Local: {self.local.nome:<20}\nDia: {self.dia} às {self.hora}:{self.minuto}h')
