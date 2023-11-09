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

        
    elif menu == 7:
        break
    else:
        print("Opção inválida!")

