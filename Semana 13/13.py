# Curso "Introdução à Programação Python” do IFSP – Câmpus Sertãozinho.

# Semana 13 - 03 a 10 de Junho de 2020

# ----------------------------------------------
# Format
# ----------------------------------------------
print('Olá {0}, seja bem vindo ao curso de {1}'.format('aluno','Python!'))

print('Vamos definir apenas duas casas decimais. {0:5.2f}'.format(7.4356))

msg = 'Programação {} com {}.'
print(msg.format('Python', 'IFSP'))

var = 'Formataçaõ de Strings'
print(var.center(50,'*'))
print(var.ljust(50,'<'))
print(var.rjust(50,'>'))

print('Linguagens {0}, {1}, e {outra}'.format('Python', 'C#', outra='PHP'))

# ----------------------------------------------
# Trabalhando com posicionamento
print('Alunos %d, Python %5.2f' %(237, 9.42745))

print('Programação: {string}, Total Alunos: {t:2d}'.format(string='teste', t=4))

# ----------------------------------------------
# Possuir no mínimo dez centímetros em cada mecha;
# Ter atenção para ue os fios cortados não toquem o chão;
# Não ter nenhuma doença capilar;
# Guardar os fios secos elimpos em um saco plástico;

continuar = input('Deseja iniciar o sistema (S/N)? ').upper()
while (continuar != 'S' and continuar != 'N'):
    print('Opção inválida')
    continuar = input('Informe S-Sim ou N-Não').upper()

totalDoadores = 0
totalMasculino = 0
totalFeminino = 0
doacoesPerdidas = 0

while(continuar == 'S'):
    totalDoadores += 1
    nome = input('Informe o seu nome: ')

    sexo = input('Qual o sexo (M/F): ').upper()
    while (sexo != 'M' and sexo != 'F'):
        print('Opção inválida')
        sexo = input('Informe M-Masculino ou F-Feminino: ').upper()
        
    #Doadores por sexo
    if(sexo == 'M'):
        totalMasculino += 1
    else:
        totalFeminino += 1
    
    tamanhoMecha = int(input('Qual o tamanho da mecha em centímetros? '))
    #teste tamanho mecha
    if (tamanhoMecha < 10):
        print('Para doação a mecha deve possuir no mínimo 10 cm.')
        print('Deixe o seu cabelo crescer mais um pouco.')
        doacoesPerdidas += 1
    else:
        tocouChao = input('Durante o processo os cabelos tocaram no chão (S/N)? ').upper()
        while(tocouChao != 'S' and tocouChao != 'N'):
            print('Opção inválida')
            tocouChao = input('Informe S-Sim ou N-Não: ').upper()
        
        #teste se a mecha tocou no chão
        if(tocouChao == 'S'):
            print('Para doação a mecha não pode ter tocado no chão.')
            doacoesPerdidas += 1

        else:
            doencaCapilar = input('Possui alguma doença capilar (S/N)? ').upper()
            while(doencaCapilar != 'S' and doencaCapilar != 'N'):
                print('Opção inválida')
                doencaCapilar = input('Informe S-Sim ou N-Não: ').upper()

            #teste de doença capilar
            if(doencaCapilar == 'S'):
                print('Para doação os cabelos devem estar saudáveis.')
                doacoesPerdidas += 1

            else:
                armazenamento = input('Os fios foram guardados adequadamente (S/N)? ').upper()
                while(armazenamento != 'S' and armazenamento != 'N'):
                    print('Opção inválida')
                    armazenamento = input('Informe S-Sim ou N-Não').upper()

                #teste do armazenamento
                if(armazenamento == 'N'):
                    print('Para doação os cabelos devem ser armazenados limps e secos em um saco plástico.')
                    doacoesPerdidas += 1
    
    continuar = input('Deseja continuar no sistema (S/N)? ').upper()
    while(continuar != 'S' and continuar != 'N'):
        print('Opção inválida')
        continuar = input('Informe S-Sim ou N-Não: ').upper()
else:
    print('\n\nApresentar os resultados finais\n\n')

print('Total de doações: ', totalDoadores)
print('Total de doações perdidas: ', doacoesPerdidas)
print('Total de doações válidas: ', totalDoadores - doacoesPerdidas)
print('Porcentagem de participantes do sexo Feminino: ', (totalFeminino * 100) / totalDoadores, '%')
print('Porcentagem de participantes do sexo Masculino: ', (totalMasculino * 100) / totalDoadores, '%')





# ----------------------------------------------
