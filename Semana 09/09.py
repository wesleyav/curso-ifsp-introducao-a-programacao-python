# Curso "Introdução à Programação Python” do IFSP – Câmpus Sertãozinho.

# Semana 9 - 06 a 13 de Maio de 2020

# ----------------------------------------------
# Funções LAMBDA (Funções anônimas)
# ----------------------------------------------

# Como usar as funções lambda no Python?


# Uma função lambda em python possui a seguinte sintaxe.

# argumentos lambda: expressão

# Lambdas são funções de uma linha. Eles também são conhecidos como funções anônimas em alguns outros idiomas. 
# Você pode querer usar lambdas quando não quiser usar uma função duas vezes em um programa. 
# Eles são como funções normais e até se comportam como eles.

# A estrutura da Função Lambda
# 1. Definimos a função com a palavra lambda
# 2. Após definir a função os parâmetros devem ser inseridos
# 3. Colocamos  :  (dois pontos) após os parâmetros
# 4. Inserimos a lógica da função
# 5. Podemos definir uma variável para a função lambda (opcional)

# ----------------------------------------------

# Aplicação utilizando função e expressão lambda para comparação de sintaxe.

# função normal
def subtrai(num1, num2):
    return num1-num2


# função lambda
sub = lambda a,b: a-b

valor1 = int(input('Informe o Valor 1: '))
valor2 = int(input('Informe o Valor 2: '))

# Utilizando a expressão lambda
print('Expressão Lambda')
print(sub(valor1,valor2))

# Utilizando a função DEF
print('Função DEF')
print(subtrai(valor1,valor2))

# ----------------------------------------------

# Expressão lambda para efetuar a soma de 2 números.

soma = lambda num1, num2:num1+num2

vl1 = int(input('Informe o num1: '))
vl2 = int(input('Informe o num2: '))

print(soma(vl1,vl2))

# ----------------------------------------------

# Iremos percorrer os valores de uma lista e elevá-los ao quadrado.
# Assim é retornado o dobro deles com a operação: x*2, e com a 
# operação irá nos retornar um map object utilizarmos o método list para voltar a ter um array.

lista = [2,5,3,7,9]

elev = list(map(lambda x: x**2, lista))
print(elev)

# ----------------------------------------------

# Programa para filtrar apenas os itens pares de uma lista.

lista = [1,4,7,3,9,12,44,30]
lista_par = list(filter(lambda x: (x%2 == 0), lista))

print(lista_par)

# ----------------------------------------------

# Combine o primeiro nome e o sobrenome da pessoa

completa = lambda nome, sobrenome: nome.strip().title() + " " +sobrenome.strip().title()

primeiro = str(input('Informe o primeiro nome: '))
segundo = str(input('Informe o segundo nome: '))

print(completa(primeiro,segundo))


# ----------------------------------------------

# Faça uma lista que retorne outra lista de números pares maiores que 10

a = [12,33,26,14,8,39,0,244]

result = list(filter(lambda x:x % 2 == 0 and x > 10, a))

print(result)


