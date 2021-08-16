# (Função sem retorno sem parâmetro) Faça uma função/método que receba três números inteiros a, b, c que sejam divisíveis por a. O valores b e c representam o intervalo da estrutura de repetição. Apresente a quantidade e os números divisíveis. Não pode usar vetor e função pronta da linguagem Python.

def somathree():
    a = int(input('Digite o valor de a: '))
    b = int(input('Digite o valor de b: '))
    c = int(input('Digite o valor de C: '))
    qtde = 2
    if a % qtde == 0:
      print(f'O Numero {a} É divisel por 2')
    if b % qtde == 0:
      print(f'O Numero {b} É divisel por 2')
    if c % qtde == 0:
      print(f'O Numero {c} É divisel por 2')

somathree()
