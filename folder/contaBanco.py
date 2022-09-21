# atividadesPython
atividades feitas na disciplina de Programação 2 no curso de ADS do IFRS Campus Sertão
class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print('Iniciando uma conta...')
        self.numero = numero
        self.titular = titular
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
