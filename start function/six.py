# (Função sem retorno sem parâmetro) Faça uma função/método que leia um valor inteiro entre 1 e 9 e mostre a seguinte tabela de multiplicação

def tabuada():
  valorTabu = int(input('Digite o Numero que Deseja ver A tabuada: '))
  
  for count in range(11):
    print(valorTabu, 'X' ,count, '=', valorTabu * count)

tabuada()