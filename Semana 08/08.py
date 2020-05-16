# Curso "Introdução à Programação Python” do IFSP – Câmpus Sertãozinho.

# Semana 8 - 29 de Abril a 6 de Maio de 2020

# ----------------------------------------------

# Funções

# ----------------------------------------------


# def NOME (PARÂMETROS):
#     COMANDOS

# Faça um algoritmo que solicite ao usuário números e os armazene
# em um vetor de 10 posições.
# crie uma função que receba o vetor preenchido e substitua todas as ocorrências
# de valores positivos por 1 e os valores negativos por 0

def troca(vet):
    for i in range(10):
        if vet[i] >= 0:
            vet[i] = 1
        else:
            vet[i] = 0
    return vet

#construindo o vetor

vet = [0] * 10
for i in range(10):
    vet[i] = int(input('Digite um valor: '))
print(vet)


troca(vet)
print(vet)


# ----------------------------------------------

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial (n-1)

numero = int(input('Informe o número: '))

print(fatorial(numero))

# ----------------------------------------------

def fibonacci(num):
    if num <= 1:
        return num
    else:
        return fibonacci(num-1) + fibonacci(num-2)

pos = int(input('Informe a posição do Fibonacci: '))

resultado = fibonacci(pos)

print('O Fibonacci é %d' %(resultado))

# ----------------------------------------------

# Fazer uma função que irá retornar os resultados de operações entre dois números:
# retornar se o primeiro número é par
# retornar a multiplicação do primeiro pelo segundo número


def calcular(x, y):
    return x % 2 == 0, x * y

num1 = int(input('Informe o primeiro número: '))
num2 = int(input('Informe o segundo número: '))

print(calcular(num1, num2))





# ----------------------------------------------


# Faça uma uma função que calcule a área de um círculo

import math

def calculo(r):
    area = math.pi * r**2
    return area


raio = int(input('Informe o raio do círculo em metros: '))

print(calculo(raio))