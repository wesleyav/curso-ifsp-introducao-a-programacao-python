# Curso "Introdução à Programação Python” do IFSP – Câmpus Sertãozinho.

# Semana 6 de 15 a 22 de Abril de 2020

# #----------------------------------------------

# Estrutura de Repetição – WHILE

# Faça uma aplicação que recebea um número e mostre os próximos três números

numero = int(input('Informe um número: '))

contador = 1

print('O número informado foi: ' +str(numero))

while (contador <= 3):
    numero+=1
    print('Próximo: ' +str(numero))
    contador+=1
print('Fim da aplicação')

# #----------------------------------------------

# Faça uma aplicação que receba o nome e o sexo de uma pessoa.
# Sendo no sexo o valor M para masculino e F para feminino.
# Ao final apresente o nome e o sexo da pessoa.


nome = input('Informe o seu nome: ')
sexo = input('Informe o seu sexo(M/F): ')

while sexo.upper() != 'F' and sexo.upper() != 'M':
    sexo = input('Sexo Incorreto. Informe M ou F: ')

print('A pessoa de nome: ' + nome + ' é do sexo ' + sexo.upper())

# #----------------------------------------------

# Faça uma aplicação que tenha uma estrutura de repetição que fique solicitando uma
# palavra ao usuário até que o usuário informe que o programa deve encerrar.
# Após a finalização da aplicação apresente ao usuário o número de palavras que 
# ele inseriu no sistema.


qtPalavras = 0
continuar = input('Deseja informar uma palavra? (S/N): ')

while continuar.upper() != 'S' and continuar.upper() != 'N':
    continuar = input('Opção inválida! Informe (S/N): ')

while continuar.upper() == 'S':
    qtPalavras+=1
    palavra = input('Informe uma palavra: ')
    continuar = input('Deseja continuar? (S/N)')
    while continuar.upper() != 'S' and continuar.upper() != 'N':
        continuar = input('Opção inválida! Informe (S/N): ')

print('Você informou ' +str(qtPalavras) + ' palavra(s) ao sistema')

# #----------------------------------------------


# Escreva um progrma que solicite 10 números ao usuário através de um laço while,
# e ao final mostre:
# qual destes números é o maior
# qual destes números é o menor
# qual é a média dos números


quantidade = 1
somatorio = 0

while quantidade < 11:
    numero = int(input('Informe um número: '))
    if quantidade == 1:
        maior = numero
        menor = numero
    elif (numero > maior):
        maior = numero
    elif (numero < menor):
        menor = numero

    somatorio += numero
    quantidade +=1
else:
    media = somatorio / 10

print('O maior valor é: ' +str(maior))
print('O menor valor é: ' +str(menor))
print('A média é: ' +str(media))

# #----------------------------------------------

# Estrutura de Repetição – FOR

# Utilizando o conceito de FOR faça uma aplicação que mostre os números
# pares na sequência de 1 a 20

for valor in range(1,21):
    if valor % 2 == 0:
        print(valor)
print('Fim da aplicação')

# #----------------------------------------------

# Utilizando o conceito de FOR faça uma aplicação que mostre 
# a sequência numérica iniciando em 3 até 100 com intervalos de 5 em 5


for  valor in range(3,100,5): # 1º (número inicial), 2º (número final), 3º (passo)
    print(valor)
print('Fim da aplicação')

# #----------------------------------------------

# Utilizando o conceito de FOR, elabore uma aplicação que percorra uma lista de nomes
# e apresente os nomes da lista


listaNomes = ['João', 'José', 'Maria', 'Camilo' ]

for nome in listaNomes:
    print(nome)
else:
    print('A lista foi apresentada com sucesso!')

# #----------------------------------------------

# Escreva um programa que pergunte ao usuário quantos alunos ele tem em sua sala.
# Em seguida, através de um laço FOR, peça ao usuário para que entre com as notas de
# todos os alunos da sala, um por vez.
# Por fim, o programa deve mostrar a média aritmética da turma.



qt = int(input('Quantos alunos você possui? '))
somaNota = 0
media = 0

for qtAluno in range (qt):
    nota = int(input('Informe a nota: '))
    somaNota += nota
else:
    media = somaNota / qt

print ('A média da turma foi: ' +str(media))

# #----------------------------------------------