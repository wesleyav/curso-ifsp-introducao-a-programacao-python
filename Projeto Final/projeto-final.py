lancar = input('Deseja iniciar o lançamento de notas (S/N)? ').upper()
while (lancar != 'S' and lancar != 'N'):
    print('Opção inválida')
    lancar = input('Informe S-Sim ou N-Não: ').upper()

totalAlunos = 0
totalMasculino = 0
totalFeminino = 0
totalAprovadosMasculino = 0
totalAprovadosFeminino = 0
totalExameMasculino = 0
totalExameFeminino = 0
totalReprovadosMasculino = 0
totalReprovadosFeminino = 0
totalAprovados = 0
totalReprovados = 0
totalExame = 0

while (lancar == 'S'):
    totalAlunos += 1
    nomeAluno = input('Informe o nome do aluno: ')

    sexo = input('Qual o sexo (M/F): ').upper()
    while (sexo != 'M' and sexo != 'F'):
        print('Opção inválida')
        sexo = input('Informe M-Masculino ou F-Feminino: ').upper()
        
    # total alunos por sexo
    if (sexo == 'M'):
        totalMasculino += 1
    else:
        totalFeminino += 1
    
    # laço do tipo for validando notas entre (0 e 10)
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
        
    # calculando a média
    media = (nota1 + nota2 + nota3 ) / 3
   
    # Calculando as médias, identificando sexo e condição de aprovação
    if media > 7 and sexo == 'M':
        totalAprovados += 1
        totalAprovadosMasculino += 1
    elif media > 7 and sexo == 'F':
        totalAprovados += 1
        totalAprovadosFeminino =+ 1
    elif media >= 4 and sexo == 'M':
        totalExame += 1
        totalExameMasculino += 1
    elif media >= 4 and sexo == 'F':
        totalExame += 1
        totalExameFeminino =+ 1
    elif media < 4 and sexo == 'M':
        totalReprovados += 1
        totalReprovadosMasculino += 1
    elif media < 4 and sexo == 'F':
        totalReprovados += 1
        totalReprovadosFeminino =+ 1
    

    # Questiona se deseja cadastrar um novo aluno ou finalizar e exibir o relatório
    lancar = input('Deseja continuar no sistema (S/N)? ').upper()
    while(lancar != 'S' and lancar != 'N'):
        print('Opção inválida')
        lancar = input('Informe S-Sim ou N-Não: ').upper()
else:
    print('\n\nApresentando os resultados finais\n\n')

# Total 
print('Total de alunos cadastrados: ', totalAlunos)

# Porcentagem
print('Quantidade porcentual de alunos aprovados: ', (totalAprovados * 100) / totalAlunos, '%')
print('Quantidade porcentual de alunos de exame: ', (totalExame * 100) / totalAlunos, '%')
print('Quantidade porcentual de alunos reprovados: ', (totalReprovados * 100) / totalAlunos, '%')

# Valores absolutos
# print('Total de alunos aprovados: ', totalAprovados)
print('Quantidade de pessoas do sexo feminino aprovadas: ', totalAprovadosFeminino)
print('Quantidade de pessoas do sexo masculino aprovadas: ', totalAprovadosMasculino)
print('Quantidade de pessoas do sexo feminino de exame: ', totalExameFeminino)
print('Quantidade de pessoas do sexo masculino de exame: ', totalExameMasculino)
print('Quantidade de pessoas do sexo feminino reprovadas: ', totalReprovadosFeminino)
print('Quantidade de pessoas do sexo masculino reprovadas: ', totalReprovadosMasculino)


