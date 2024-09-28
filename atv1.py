#calculador de nota de aluno.
nota1 = int(input("nota1: ")) # entrada da nota 1
nota2 = int(input("nota2: ")) # entrada da nota 2
nota3 = int(input("nota3: ")) # entrada da nota 3
media = (nota1 + nota2 + nota3)/3 # calculo da media
print(media)
if media >= 7: # defini resposta em relação a nota do aluno.
  print("aprovado")
else:
  print("reprovado")