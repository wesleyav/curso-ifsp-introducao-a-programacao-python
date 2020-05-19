# Curso "Introdução à Programação Python” do IFSP – Câmpus Sertãozinho.

# Semana 10 -  13 a 20 de Maio de 2020

# ----------------------------------------------
# Ramdom
# ----------------------------------------------

import random

x = random.randint(0,15)
y = random.randint(0,30)

print(x)
print(y)

# ----------------------------------------------

# Criar uma lista de 10 posições com números randomicos limitados a 100.
# import random

lista = []
x = 0
for x in range(10):
    lista.append(random.randrange(100))
print(lista)

# ----------------------------------------------

# Criar uma lista de 20 posições com números randômicos variando entre 1000 e 2000.

import random

list = []
x = 0
for x in range(20):
    list.append(random.randrange(1000,2000))

print(list)

# ----------------------------------------------
# Type
# ----------------------------------------------

print(type('IFSP - Sertãozinho'))
print(type(894))
print(type(9.75))
print(type(True))

# ----------------------------------------------
a = "Bons estudos"
print(type(a))

b = 9.75
print(type(b))

c = ['curso', 'python', 20, 47, 8.5, False]
print(type(c))

# ----------------------------------------------

import random

lista = []
x = 0

for x in range (10):
    lista.append(random.randrange(100))

print(lista)
print(type(lista))









# ----------------------------------------------