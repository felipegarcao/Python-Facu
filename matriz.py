print('Exemplo de Vetor')
v = []
for i in range(4):
  v.append(int(input('Informe o Valor')))
print(v)


print('Exemplo de Matriz')
m = []
for l in range(2): #Duas Linhas
  linha_com_colunas = []
  for c in range(3): #Tres Colunas
    linha_com_colunas.append(int(input('Informe o valor: ')))
  m.append(linha_com_colunas)
print(m)
for l in range(len(m)): # len de m, mostra a quantidade de Linhas
  for c in range(len([0])): # len de m[0], mostra a qtde de colunas
    print(m[l][c],end=' ')
print()# Faz Pular Linhas
