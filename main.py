from func import *
alunos = {}
while True:
    print('''
    1 - Cadastrar aluno
    2 - Imprimir alunos
    3 - Informar notas
    4 - Pesquisar aluno
    5 - Excluir aluno
    6 - Relatório final
    7 - Sair
    ''')
    menu = int(input("Escolha a opção desejada: "))
    if menu == 1:
        nome = input('Digite o nome do aluno:')
        matricula = int(input(('Digite a matricula do aluno:')))
        alunos[matricula] = {"nome": nome}
        print('Aluno cadastrado com sucesso!')

    elif menu == 2:
        imprimiralunos(alunos)

    elif menu == 3:
        matricula = int(input('Digite a matrícula do aluno:'))
        nota1 = float(input('Digite a nota do primeiro bimestre:'))
        nota2 = float(input('Digite a nota do segundo bimestre:'))
        nota3 = float(input('Digite a nota do terceiro bimestre:'))
        nota4 = float(input('Digite a nota do quarto bimestre:'))
        informarnotas(alunos,matricula,nota1, nota2, nota3, nota4)

    elif menu == 4:
        nome = input('Digite o nome do aluno:')
        pesquisaraluno(alunos,nome)

    elif menu == 5:
        matricula = int(input('Digite a matricula do aluno:'))
        excluirAluno(alunos,matricula)
    
    elif menu == 6:
        relatorioFinal(alunos)




    elif menu == 7:
        break
    else:
        print("Opção inválida!")

