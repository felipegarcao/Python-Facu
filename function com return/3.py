def calculoTriangulo():
  base = int(input('Digite o Valor da Base do Triangulo: '))
  altura = int(input('Digite o Valor da altura do Triangulo: '))
  resultado = (base * altura) / 2
  return resultado
def main():
  x = calculoTriangulo()
  print(f'o Resultado do Calculo do Triangulo é {x}')
main()