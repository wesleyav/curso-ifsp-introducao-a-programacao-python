# Curso "Introdução à Programação Python” do IFSP – Câmpus Sertãozinho.

# Semana 5 - 08 a 15 de Abril de 2020



# Informe um valor.
# Verificar se o valor é maior que 100.
# em caso verdadeiro, calcule 10%

valor = int(input('Informe um valor: '))

if valor > 100:
    valor = valor * 0.1
print('Valor é: ' +str(valor))

# #----------------------------------------------

# # Solicite ao usuário seu sexo e sua idade.
# # Caso a idade seja maior ou igual a 18
# # e o sexo seja masculino, solicite a carteira de reservista.

idade = int(input('Informe sua idade: '))
sexo = input('Informe o sexo: (M/F): ')

if idade >= 18 and sexo.upper() == 'M' :
    print('Serviço Militar Obrigatório!')
    cartReservista = input('Informe sua carteira de Reservista: ')
    print('Todos os dados coletados!')

print('Fim da aplicação.')

#----------------------------------------------

# Solicitar o tipo sanguineo.
# Caso seja do tipo A ou O a pessoa é um possível doador.

tipoSanguineo = str(input('Informe o seu tipo sanguíneo: '))

if tipoSanguineo.upper() == 'A' or tipoSanguineo.upper() == 'O':
    print('Você é um possível doador!')
print('Tipo sanguineo informado: ' +tipoSanguineo.upper())

#----------------------------------------------

# Solicitar ao usuário 3 notas
# Calcular a média
# Caso media < 6, mensagem de aumentar a dedicação aos estudos
# Caso media >= 6, mensagem de continue assim

nomeAluno = str(input('Informe o nome do aluno: '))
n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))
n3 = float(input('Informe a terceira nota: '))

media = (n1 + n2 + n3) / 3

if media < 6:
    print('Você precisa se dedicar mais!')
else:
    print('Continue assim!')

print('Olá ' +nomeAluno+ ' sua média foi ' +str(media))
print('Fim da aplicação.')

#----------------------------------------------

# Solicitar nome e peso de 2 pessoas.
# Apresentar o nome da pessoa mais pesada.

pessoa1 = str(input('Informe o nome da pessoa 1: '))
peso1 = float(input('Informe o peso da pessoa 1: '))

pessoa2 = str(input('Informe o nome da pessoa 2: '))
peso2 = float(input('Informe o peso da pessoa 2: '))

if peso1 > peso2:
    print('A pessoa mais pesada é: ' +pessoa1)
else:
    print('A pessoa mais pesada e: ' +pessoa2)

print('Fim da aplicação')

#----------------------------------------------

# Solicitar 3 valores e verificar se forma um triângulo equilátero

lado1 = int(input("Informe lado 1: "))
lado2 = int(input("Informe lado 2: "))
lado3 = int(input("Informe lado 3: "))

if lado1 == lado2 and lado1 == lado3:
    print('Forma um triângulo equilátero')
else:
    print('Não forma um triângulo equilátero')

print('Fim da aplicação.')

#----------------------------------------------


valor1 = int(input('Informe o valor 1: '))
valor2 = int(input('Informe o valor 2: '))

valor3 = valor1 ** valor2

resto = valor3 % 2

if resto == 0:
    print('O resultado da potência do valor 1 pelo valor 2 gerou um número PAR.')
else:
    print('O resultado da potência do valor 1 pelo valor 2 gerou um número ÍMPAR.')

print('Fim da aplicação')

#----------------------------------------------

# Ler 3 nomes de pessoas e seus pesos.
# Mostrar os dados (nome e peso) em ordem decrescente de peso.

nome1 = input('Informe o primeiro nome: ')
peso1 = input('Informe o primeiro peso: ')

nome2 = input('Informe o segundo nome: ')
peso2 = input('Informe o segundo peso: ')

nome3 = input('Informe o terceiro nome: ')
peso3 = input('Informe o terceiro peso: ')

if peso1 > peso2 and peso1 > peso3:
    print('O nome do mais pesado é: ' +nome1+ ' e seu peso é ' +peso1)
    if peso2 > peso3:
        print('O nome com peso médio é ' +nome2+ ' e seu peso é ' +peso2)
        print('O nome com peso mais leve é ' +nome3+ ' e seu peso é ' +peso3)
    else:
        print('O nome com peso médio é ' +nome3+ ' e seu peso é ' +peso3)
        print('O nome com peso mais leve é ' +nome2+ ' e seu peso é ' +peso2)
elif peso2 > peso1 and peso2 > peso3:
    print('O nome do mais pesado é: ' +nome2+ ' e seu peso é ' +peso2)
    if peso1 > peso3:
        print('O nome com peso médio é ' +nome1+ ' e seu peso é ' +peso1)
        print('O nome com peso mais leve é ' +nome3+ ' e seu peso é ' +peso3)
    else:
        print('O nome com peso médio é ' +nome3+ ' e seu peso é ' +peso3)
        print('O nome com peso mais leve é ' +nome1+ ' e seu peso é ' +peso1)
else:
    print('O nome do mais pesado é ' +nome3+ ' e seu peso é ' +peso3)
    if peso1 > peso2:
        print('O nome com peso médio é ' +nome1+ ' e seu peso é ' +peso1)
        print('O nome com peso mais leve é ' +nome2+ ' e seu peso é ' +peso2)
    else:
        print('O nome com peso médio é ' +nome2+ ' e seu peso é ' +peso2)
        print('O nome com peso mais leve é ' +nome1+ ' e seu peso é ' +peso1)

print ('****** Fim da aplicação *******')