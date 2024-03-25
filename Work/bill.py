# Certa manhã, você sai e coloca uma nota de um dólar na calçada perto da torre Sears,
# em Chicago. A cada dia seguinte, você sai com o dobro do número de contas. 
# Quanto tempo leva para a pilha de notas ultrapassar a altura da torre?


nota_metros = 0.11 * 0.001
altura_torre = 442
dia = 1
num_notas = 1
while num_notas*nota_metros < altura_torre:
  print(dia,num_notas)
  dia = dia +1
  num_notas = num_notas*2
print(dia)