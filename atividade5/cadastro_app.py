from cadastro import Aluno, Professor, Curso

a1 = Aluno('Bruno', 28)
a2 = Aluno('Ana', 30)
a3 = Aluno('Bruno', 53)
p1 = Professor('Marcos', 13)
p2 = Professor('Evandro', 18)
p3 = Professor('Simone', 15)
c1 = Curso('Medicina', 3)
c2 = Curso('Zootecnia', 6)
c3 = Curso('Administração', 5)

alunos = {a1.matricula, a2.matricula, a3.matricula}
professores = {p1.registro, p2.registro, p3.registro}
cursos = {c1.id, c2.id, c3.id}

print(f'Alunos cadastrados: {alunos}')
print(f'Professores cadastrados: {professores}')
print(f'Cursos cadastrados: {cursos}')
