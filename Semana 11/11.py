# Curso "Introdução à Programação Python” do IFSP – Câmpus Sertãozinho.

# Semana 11 - 20 a 28 de Maio de 2020

# ----------------------------------------------
# Strings
# ----------------------------------------------

curso1 = 'Aprendendo Python'
print(curso1)

curso2 = "Aprendendo Strings com Python"
print(curso2)

mensagem = 'Trabalhando com Strings'
print(mensagem[0])
print(mensagem[1])
print(mensagem[2])
print(mensagem[3])
print(mensagem[4])
print(mensagem[5])
print(mensagem[6])
print(mensagem[7])
print(mensagem[8])
print(mensagem[9])
print(mensagem[10])
print(mensagem[11])
print(mensagem[12])

# ----------------------------------------------

local = 'Sertãozinho'

for item in local:
    print(item)
# ----------------------------------------------
frase = 'Estudando as Funcionalidades de pyThon'
print(frase.lower())

frase2 = 'grupO dE EstuDoS'
print(frase2.upper())

frase3 = 'Dedicação e SuceSSo'
print(frase3.title())



# ----------------------------------------------

endereco = 'Av. Paulista'
print(endereco.isalpha()) # verifica se a string possui apenas letras

endereco2 = 'Av. Paulista, 427'
print(endereco2.isalpha())

sobrenome = 'Machado'
print(sobrenome.isalpha())

sobrenome2 = "6"
print(sobrenome2.isalpha())

# ----------------------------------------------
msg = '       Remover Espaços à esquerda'
print(msg.strip())

msg2 = 'Remover Espaços à direita        '
print(msg2.strip())

# ----------------------------------------------
unir = 'IFSP'
print('-'. join(unir))

# ----------------------------------------------

frase = 'Python com VSCode'
print(len(frase))

msg = 'Olá'
print(len(msg))












