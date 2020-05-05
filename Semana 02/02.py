# Curso "Introdução à Programação Python” do IFSP – Câmpus Sertãozinho.

# Semana 2 - 18 a 25 de Março de 2020

# Declaração de variáveis

# Variáveis não podem ter nomes iniciados com números ou caracteres especiais!

mensagem = 'Olá Mundo'
numero = 520
numeroPi = 3.141592
teste = True

print (mensagem)
print (numero)
print (numeroPi)
print (teste)

print (type(mensagem)) # str - string
print (type(numero)) # int - inteiro
print (type(numeroPi)) # float - decimal
print (type(teste)) # bool - booleano

# Alterando variável

numero = 520.1
print (numero)
print (type(numero))

# Variáveis fortemente tipadas
#----------------------------------------------

# Operadores aritiméticos e relacionais

# Operadores aritiméticos

# + - adição
# - - subtração
# * - multiplicação
# / - divisão
# ** - potenciação
# % - resto da divisão (mod)

# Operadores relacionais (True ou False)

# == - igualdade
# != - diferença
# < - menor que
# > - maior que
# <= - menor ou igual
# >= - maior ou igual

print (4 + 5)
print (6 - 3)
print (7 * 8)
print (12 / 4)
print (63 % 10)
print (5 ** 3)

soma = 45 + 7
print (soma)
subtracao = 30 - 15
multiplicacao = 5 * 22
divisao = 93 /7
resto = 5 % 2
potenciação = 7 ** 3

#----------------------------------------------

# Operadores relacionais

print (9 == 10) # False
print (9 != 10 )# True
print (8 >= 6)# True
print (8 >= 8)# True

print (divisao != potenciação) # True - é diferente!
print (subtracao < resto) # Falso - valor da variável subtração é maior que o valor da variável resto.
print (multiplicacao > potenciação) # Falso

# Precedências

result = 7 + 2 * 3
print (result)

result = (7 + 2) * 3
print (result)

