def cadastraralunos(alunos,matricula,nome):
    alunos[matricula] = {'nome': nome}

def imprimiralunos(alunos):
   for matricula, aluno in alunos.items():
        print(f"{matricula} - {aluno['nome']}")