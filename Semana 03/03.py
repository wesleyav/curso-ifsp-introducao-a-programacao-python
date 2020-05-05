# Curso "Introdução à Programação Python” do IFSP – Câmpus Sertãozinho.

# Semana 3 - 25 de Março a 01 de Abril de 2020

# Variáveis

# Definindo um nome para uma variável

# nome = valor - CERTO
# _nome = valor - CERTO
# 1nome = valor - ERRADO

a = 3
b = 7
print(a+b)


string1 = "Olá Mundo!"
print (string1)

string2 = 'Python - IFSP'
print (string2)

# Padrão adotado pela comunidade python - uso de aspas simples ('')

# Tratamento de Strings

nome = 'Maria José da Silva'
print (nome)

# String -> 0 ao infinito
# Posição dos caracteres inicia em 0

print (nome[0])

# No exemplo seria:
#   0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18
#   M   A   R   I   A       J   O   S   É       D   A       S   I   L   V   A

print (nome[2:5])   # Exibe os caracteres (-1) - RIA
print (nome[2:7])   # Eixibe os caracteres (-1) - RIA J
print (nome[4:8:2]) # Inicia na 4ª posição até a última -1 (-1) de 2 em 2 - AJ
print (nome[:5])    # Início não definido até a quinta -1 (-1) - MARIA
print (nome[8:])    # Início na 8ª posição até a última -1 (-1) - SÉ DA SILVA
print (nome[2::3])  # Início na 2ª posição até a última -1 (-1) de 3 em 3 - R SDSV

#----------------------------------------------

# PYTHON é case sensitive!

frase = 'Aprendendo Python com o IFSP'

print(len(frase)) # Calcula o número de caracteres dentro da viariável

frase = frase.replace('IFSP', 'Instituto Federal') # Reescreve.
print (frase)

print (frase.count('r')) # Conta quantas letras "r minúsculo" tem na variável

print (frase.find('r'))         # Localiza a posição do elemento buscado. No caso a letra 'r'.
print (frase.find('Instituto')) # Localiza a posição da primeira letra. No caso a letra 'L'.
print (frase.find('instituto')) # Localiza a posição da primeira letra. No caso a letra 'l'. Como não existe, exibe -1.


print (frase.split()) # Pegou o espaços e dividou a frase em palavras, dentro d eum array.

print (frase.upper())       # Altera as letras para maiúsculo
print (frase.lower())       # Altera as letras para minúsculo
print (frase.capitalize())  # Altera a 1ª letra para maiúsculo.
print (frase.title())       # Altera a 1ª letra de cada palavra para maiúsculo.
print (frase.swapcase())    # Realiza a troca, faz o oposto.

#----------------------------------------------

frase2 = '   Aprendendo Python   '
print (frase2)
print (len(frase2))

frase2 = frase2.strip() # Remove os espaços no início e no final
print (len(frase2))
frase2 = frase2.rstrip() # Remove os espaços à direita
frase2 = frase2.lstrip() # Remove os espaços à esquerda


# Concatenação

nome2 = 'Maria'
sobrenome = 'Silva'

nomeCompleto = nome2 + ' ' +sobrenome # Concatenação de espao em branco entre as variáveis.
print (nomeCompleto)

# Escapando caracteres
# Escapar significa: inserir em uma string caracteres que tenham algum significado especial, como uma nova
# linha, um caracter de tabulação (TAB) ou as aspas simples ou duplas.

string_frase = '''Olá. Esta é uma string. Vou utilizar " ou ' para o armazenamento de strings.'''
# Com 3 aspas simples exibe as aspas normalmente, seja simples ou dupla. "escaping".
print (string_frase)

cantora = "A cantora Sinnead O'Connor" # Com 2 aspas duplas, só exibe a aspa simples dentro, se digitar aspas duplas não escapa.
print (cantora)

curso = 'Tenham bastante atenção ao estudar "Python"' # Com 2 aspas simples, só exibe a aspa dupla dentro, se digitar aspas simples não escapa.
print (curso)

curso = "Tenham bastante atenção ao estudar \"Python\"" # Escapando com barras
print (curso)

barra = "Escapando com \\" # Escapando com \ para exibir também a barra (\).
print (barra)

#  Sequência   |     Escapada Significado
#     \\       |        Contrabarra
#     \’       |        Aspas simples
#     \”       |        Aspas duplas
#     \a       |        Caracter de controle ASCII Bell (BEL)
#     \b       |        Caracter ASCII Backspace (BS)
#     \f       |        Caracter ASCII Formfeed (FF)
#     \n       |        Caracter ASCII Linefeed (LF) - este cria uma nova linha no output
#     \r       |        Caracter ASCII Carriage Return (CR)
#     \t       |        Caracter ASCII Tab Horizontal (TAB)
#     \v       |        Caracter ASCII Tab Vertical (VT)
#     \ooo     |        Caracter ASCII com valor octal “ooo”
#     \xhh     |        Caracter ASCII com valor hex de “hh”


nome3 = 'Fernando'
idade = 27

print('O nome informado é %s '%nome3) # Insere o valor da variável na exibição.
print('Com idade de %d anos' %idade)

print('O nome informado é ' +nome3+ ' e ele possui ' +str(idade)+ ' anos.') # Utilizando concatenação e casting.

valor = 503.78987
print("O valor é " + str(valor))

print ("O valor é " + format(valor, '.2f'))

# A função print não faz a conversão de um número inteiro para uma string
# automaticamente. Desta forma, para incluir esta variável, precisamos converter o
# número inteiro para uma string usando a função str, e passando dentro do
# parênteses o valor a ser convertido.


raio = 30.46257
print ('Formatando decimais: %f' %raio)
print ('Formatando decimais: %.2f' %raio) # Exibe o número com 2 casas decimais.
print ('Formatando decimais: %.3f' %raio) # Exibe o número com 3 casas decimais.



# Raw String Literals
# A string é exibida exatamente como ela foi definida, e não substituindo caracteres escapados por
# seus significados no output. 

string3 = r'Utilizamos \n para inserir uma nova linha na string'
print (string3)

# Funções para strings

nome4 = input('Olá, qual seu nome?\n') #  utilizada para captar informações enviadas pelo usuário.
print (nome4)

palavra = "Olá, eu sou uma string." # Centraliza o conteúdo da string no total de caracteres informados.
print(palavra.center(50, "*"))

palavra = "Olá, eu sou uma string." # Alinha a esquerda o conteúdo da string no total de caracteres informados.
print(palavra.ljust(50, "*"))

palavra = "Olá, eu sou uma string." # Alinha a direita o conteúdo da string no total de caracteres informados.
print(palavra.rjust(50, "*"))

# isalnum() - totalmente formada por caracteres alfanuméricos
# isalpha() - alfabéticos (só contem letras)
# isnumeric() - numéricos

# Se as strings tiverem pelo menos um caracter que invalide cada condição, estas
# funções retornarão “False”. Vale notar que espaço em branco na string torna uma
# string inválida para qualquer uma destas funções.

soletras = "palavra"
print(soletras.isalpha())
print(soletras.isnumeric())
print(soletras.isalnum())

sonumeros = '123456789'
print(sonumeros.isalpha())
print(soletras.isnumeric())
print(sonumeros.isalnum())

letrasenumeros = '1234abcd'
print(letrasenumeros.isalpha())
print(letrasenumeros.isnumeric())
print(letrasenumeros.isalnum())

