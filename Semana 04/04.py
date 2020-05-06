# Curso "Introdução à Programação Python” do IFSP – Câmpus Sertãozinho.

# Semana 4 - 01 a 08 de Abril de 2020


#----------------------------------------------
# Input de dados

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

print('Seu nome é ' +nome+ ' e sua idade é ' +idade)

estudar = ('Informe o próximo conteúdo de estudos: ')
print('A próxima matéria de estudos é: ' +estudar)

print('A variável ESTUDAR contém ' +str(len(estudar))+ ' caracteres.')
print(estudar[0:6])

# Desenvolva uma aplicação que solicite ao usuário o seu nome.
# Verifique se o nome do usuário começa com Maria.

nomeUsuario = input('Informe o seu nome: ')
print(nomeUsuario[:5].upper() == 'MARIA')
#----------------------------------------------

# Solicite ao usuário que informe o seu nome.
# Verifique se existe a palavra José em qualquer parte do nome.

nomeUsuario2 = input('Informe o seu nome: ')
print('jose' in nomeUsuario2.lower())
#----------------------------------------------

# Solicite ao usuário que informe uma frase.
# mostrar a frase em maiúsculo.
# mostrar a frase em minúsculo.
# mostrar a quantidade de caracteres, sem considerar os espaços.

frase = input('Informe uma frase: ')
print ('Frase em maiúsculo: ' +frase.upper())
print ('Frase em maiúsculo: ' +frase.lower())
print ('Quantidade de caracteres da frase: ' +str(len(frase) - frase.count(' ')))
#----------------------------------------------
