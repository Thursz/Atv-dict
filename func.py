def cadastraralunos(alunos,matricula,nome):
    alunos[matricula] = {'nome': nome}

def imprimiralunos(alunos):
   for matricula, aluno in alunos.items():
        print(f"{matricula} - {aluno['nome']}")

def informarnotas (alunos,matricula,nota1, nota2, nota3, nota4):
    alunos[matricula]['notas'] = [nota1, nota2, nota3, nota4]

def calcularMedia(notas):
    media = sum(notas)/len(notas)
    return media
    
def situcacaoAluno(media):
    if media >= 7:
        return 'Aprovado'
    else:
        return 'Reprovado'

def pesquisaraluno (alunos,nome):
    for matricula, aluno in alunos.items():
         if nome in aluno['nome']:
             media = calcularMedia(aluno['notas'])
             situacao = situcacaoAluno(media)
             print("Matrícula: ", matricula)
             print("Nome: ", aluno['nome'])
             print("Notas: ", aluno['notas'])
             print("Média: ", media)
             print("Situação: ", situacao)

def excluirAluno(alunos, matricula):
    if matricula in alunos:
        del alunos[matricula]
        return 'Aluno excluído com sucesso.'

def relatorioFinal(alunos):
    for matricula, aluno in alunos.items():
        if len(aluno['notas']) == 4:
            media = calcularMedia(aluno['notas'])
            situacao = situcacaoAluno(media)
            print(f"{matricula} - {aluno['nome']} | Média: {media} | {situacao}")



