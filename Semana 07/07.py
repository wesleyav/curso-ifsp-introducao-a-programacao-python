# Curso "Introdução à Programação Python” do IFSP – Câmpus Sertãozinho.

# Semana 7 - 22 a 29 de Abril de 2020

# ----------------------------------------------

# Estruturas de Repetição Aninhadas

# ----------------------------------------------

# Desenvolva uma aplicação para o cadastro de doadores de sangue.
# Neste projeto a etapa que iremos solicitar o número total de pessoas 
# que serão cadastradas.
# Considerar para a pessoa estar apta a doação de sangue é não 
# ter tido resfriado nos últimos 7 dias ao final devemos apresentar
# a quantidade total de pssoas aptas a doação de sangue
# apresentar a quantidade de pessoas do sexo masculino aptas para doação e
#  também do sexo feminino.

quantidade = int(input('Informe o total de cadastros: '))
totM = 0
totF = 0

for qt in range(quantidade):
    sexo = input('Informe o sexo (M/F): ')
    while sexo.upper() != 'M' and sexo.upper() != 'F':
        print('Sexo inválido!')
        sexo = input('Informe o sexo (M/F): ')

    resfriado = input('Algum sintoma de resfriado nos últimos 7 dias? (S/N): ')
    while resfriado.upper() != 'S' and resfriado.upper() != 'N':
        print('Responda S (SIM) ou N (NÂO)')
        resfriado = input('Algum sintoma de resfriado nos últimos 7 dias? (S/N): ')

    if sexo.upper() == 'M' and resfriado.upper() == 'N':
        totM += 1
    elif sexo.upper() == 'F' and resfriado.upper() == 'N':
        totF += 1
    print ('***** Proximo Registro *****')
else:
    print ('***** RESULTADO FINAL *****')


print ('Total de Mulheres aptas a doação: ' +str(totF))
print ('Total de Homens aptas a doação: ' +str(totM))
print ('Total Geral de doadores apto: ' +str(totF + totM))

# #----------------------------------------------

# Desenvolva uma aplicação que faça o cadastro de pessoaspara um sistem de RH.
# O cadastro deverá responder se sabe utilizar o computador e seu nível no idioma inglês
# Ao final deverá apresentar quantidade de pessoas que sabem utilizar
# o computador, quantidade de pessoas com nível básico do idioma ingles
# quantidade de pessoas com nível intermediário do idioma ingles
# quantidade de pessoas com nível avançado do idioma ingles
# quantidade de pessoas com nível avançado do idioma ingles que sabem utilizar o computador

usoComputador = 0
basico = 0
intermediario = 0
avancado = 0
compIdioma = 0

cadastro = input('Deseja efetuar o cadastro? (S/N): ')
while cadastro.upper() != 'S' and cadastro.upper() != 'N':
    print('Responda S(SIM ou N(NÃO)')
    cadastro = input('Deseja efetuar o cadastro? (S/N): ')

while cadastro.upper() == 'S' :
    print('*****************************')
    print('Iniciar Cadastro')
    print('*****************************')
    comp = input('Sabe utilizar o computador? (S/N): ')
    while comp.upper() != 'S' and comp.upper() != 'N':
        print('Responda S(SIM) ou N(NÂO)')
        comp = input('Sabe utilizar o computador? (S/N): ')
    
    ingles = input('Nível do idioma (B-básico, I-Intermediário, A-avançado): ')
    while ingles.upper() != 'B' and ingles.upper() != 'I' and ingles.upper() != 'A':
        print('Responda B(básico) ou I(Intermediário) ou A(Avançado): ')
        ingles = input('Nível do idioma (B-básico, I-Intermediário, A-avançado): ')

    if comp.upper() == 'S':
        usoComputador += 1

    if ingles.upper() == 'B':
        basico += 1
    elif ingles.upper() == 'I':
        intermediario += 1
    else:
        avancado += 1

    if comp.upper() == 'S' and ingles.upper() == 'A':
        compIdioma += 1

    cadastro = input('Deseja efetuar o cadastro? (S/N): ')
    while cadastro.upper() != 'S' and cadastro.upper() != 'N':
        print('Responda S(SIM ou N(NÃO)')
        cadastro = input('Deseja efetuar o cadastro? (S/N): ')
else:
    print('***** FIM DOS CADASTRADOS *****')


print('Total de pessoas que sabem utilizar o computador: ' +str(usoComputador))
print('Total de pessoas com nível básico de inglês: ' +str(basico))
print('Total de pessoas com nível intermediario de inglês: ' +str(intermediario))
print('Total de pessoas com nível avançado de inglês: ' +str(avancado))
print('Total de pessoas que sabem utilizar o computador com nível avançado de inglês: ' +str(compIdioma))

# #----------------------------------------------

# desenvolva um aplicação que repita a inserção de dados de alunos (nome, nota1, nota2 e nota3)
# até que o usuário peça para parar a aplicação.
# as notas para serem consideradas válidas devem estar entre 0 e 10.
# apresente ao final:
# qtd de alunos aprovados (media>=7)
# qtd de alunos reprovados (media<4)
# qtd de alunos de exame final (media >= 4 e media <= 7)


aprovados = 0
exame = 0
reprovados = 0

cadastrar = input('Deseja iniciar lançamentos? (S/N): ')
while cadastrar.upper() != 'S' and cadastrar.upper() != 'N':
    cadastrar = input('Opção inválida. Informe (S/N): ')

while cadastrar.upper() == 'S':
    nome = input('Informe o nome do aluno: ')
    for cont in range (1,4):
        if cont == 1:
            nota1 = int(input('Informe N1: '))
            while nota1 < 0 or nota1 > 10:
                nota1 = int(input('N1 inválido, valor deve ser entre 0 e 10: '))
        elif cont == 2:
            nota2 = int(input('Informe N2: '))
            while nota2 < 0 or nota2 > 10:
                nota2 = int(input('N2 inválido, valor deve ser entre 0 e 10: '))
        else:
            nota3 = int(input('Informe N3: '))
            while nota3 < 0 or nota3 > 10:
                nota3 = int(input('N3 inválido, valor deve ser entre 0 e 10: '))
    
    #calcular média e verificar status  do aluno

    media = (nota1 + nota2 + nota3 ) /3
    print(str(media))

    if media >= 7:
        aprovados += 1
    elif media >= 4:
        exame += 1
    else:
        reprovados += 1

    cadastrar = input('Deseja efetuar outro lançamento? (S/N): ')
    while cadastrar.upper() != 'S' and cadastrar.upper() != 'N':
        cadastrar = input('Opção inválida. Informe (S/N): ')

else:
    print('Lançamentos finalizados.')

print('Total de alunos aprovados: ' +str(aprovados))
print('Total de alunos de exame: ' +str(exame))
print('Total de alunos reprovados: ' +str(reprovados))



# #----------------------------------------------