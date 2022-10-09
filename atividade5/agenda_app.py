from agenda import Local, Agenda

local1 = Local('IFRS Sertão', 'Eng Luiz Englert', 99170000)
local2 = Local('Salão Paroquial', 'Av Brasil', 99170000)
local3 = Local('Centro Cultural', 'Av Getúlio Vargas', 99170000)

a1 = Agenda('Aula Prog 2 com Iuri', local1, 11, 11, 0)
a2 = Agenda('Futsalzinho', local2, 14, 21, 0)
a3 = Agenda('Formatura Joãozinho', local3, 27, 13, 30)

a1.mostra_compromisso()
a2.mostra_compromisso()
a3.mostra_compromisso()
