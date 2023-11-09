#Cadastrando dicionário
alunos = {}
alunos[10] = {"Nome":"Ronaldo","Notas":[10,10,9,8]}
alunos[11] = {"Nome":"Arthur","Notas":[10,10,10,9]}
alunos[12] = {"Nome":"Reinaldo","Notas":[5,9,7,6]}
print(alunos)
#Remover
alunos.pop(10)
print(alunos)
#Percorrer dicionário! 
for matricula in alunos:
    print(alunos[matricula]["Nome"])
print('-----------------------------------------------')
for aluno in alunos.values():
    print(aluno["Nome"])
print('-----------------------------------------------')
for matricula,aluno in alunos.items():
    print   (f'{matricula}-{aluno["Nome"]}')
