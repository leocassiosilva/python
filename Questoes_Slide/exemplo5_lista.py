alunos = []
qtdAlunos = int(input("Informe a quantidade de alunos: "))

i=0

while i < qtdAlunos:
    nome = input("Informe o nomer do aluno %d: " %(i+1))
    alunos.append(nome)
    i = i+1

print("\n\n========== Lista ==========")
j = 0

while j < qtdAlunos:
    print("Aluno %d:  %s" %(j+1, alunos[j]))
    j=j+1