from contaBanco2 import Estudante, Conta

estudante1 = Estudante('Lucas', 'Lima', 'Medicina')
conta1 = Conta('456-2', estudante1, 250.0, 1000.0)
print(conta1.titular.nome)
print(conta1.titular.curso)
