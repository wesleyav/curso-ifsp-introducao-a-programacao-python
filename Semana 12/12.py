# Curso "Introdução à Programação Python” do IFSP – Câmpus Sertãozinho.

# Semana 12 - 27 de Maio a 03 de Junho de 2020

# ----------------------------------------------
# Find
# ----------------------------------------------
msg = 'Olá seja bem-vindo!'
resultado = msg.find('seja') # encontra a primeira ocorrência
print(resultado)

msg2 = 'Trabalhando com strings'
resultado2 = msg2.find('python') #retorna -1 quando não encontra
print(resultado2)

msg3 = "Vamos em frente com Python"
resultado3 = msg3.find('e')
print(resultado3)

frase = 'Python uma das 10 linguagens mais utilizadas do mundo!'
busca = input('Informe uma palavra que deseja localizar: ')
result = frase.find(busca)
print(result)
# ----------------------------------------------
frase2 = 'Indicar o ponto de início da busca'
palavra = 'Indicar'
result = frase2.find(palavra, 10) #pesquisar a partir da 10ª posição
print(result)

frase3 = 'Passando o parâmetro de início e fim'
busca = input('Qual a palavra deseja buscar? ')
inicio = int(input('Informe a posição inicial: '))
fim = int(input('Informe a posição final: '))
resultado = frase3.find(busca, inicio, fim)
print(resultado)

# ----------------------------------------------
# Split
# ----------------------------------------------
texto = 'Aplicando a função split no Python'
print(texto)

texto = texto.split() #converte string e listas, separando as palavras
print(texto)

frase = 'João foi para a escola hoje, e voltará pas 12:00 horas.'
resultado = frase.split(',')
print(resultado)

equipamentos = 'mouse#teclado#monitor#webcam#hd#memoria'
result = equipamentos.split('#', 2)
print(result)

# ----------------------------------------------
#Partition
# ----------------------------------------------
mensagem = 'Continuando os estudos para aperfeiçoar'
resultado = mensagem.partition('estudos') #O método partition() procura uma string especificada e divide a string em uma tupla contendo três elementos.
print(resultado)

texto = 'Curso de Python com o Instituto Federal de São Paulo'
busca = texto.partition('sertãozinho')
print(busca)

# ----------------------------------------------
