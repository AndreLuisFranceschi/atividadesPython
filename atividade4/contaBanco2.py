class Estudante:
    def __init__(self, nome, sobrenome, curso):
        self.nome = nome
        self.sobrenome = sobrenome
        self.curso = curso

class Conta:
    def __init__(self, numero, estudante, saldo, limite):
        print('Iniciando uma conta...')
        self.numero = numero
        self.titular = estudante
        self.saldo = saldo
        self.limite = limite

    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        if (self.saldo < valor):
            print('Impossível sacar')
        else:
            self.saldo -= valor
            return True

    def extrato(self):
        print('Titular: {}\nSaldo: {}'.format(self.titular, self.saldo))
