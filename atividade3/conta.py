class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        if valor > self.saldo:
            print('\033[1;31mValor indiponível. Saque não realizado!\033[m')
            return False
        else:
            self.saldo -= valor
            print('\033[1;32mSaque realizado com sucesso!\033[m')
            return True

    def transfere_para(self, destino, valor):
        saque = self.saca(valor)
        if saque:
            destino.deposita(valor)
            print('\033[1;32mTransferência concluída!\033[m')
            return True
        else:
            print('\033[1;31mTransferência inválida!\033[m')
            return False

    def extrato(self):
        print('Titular: {} \nSaldo: {}'. format(self.titular, self.saldo))
