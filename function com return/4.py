def squareCalc():
  lado = int(input('Digite a medida do lado do quadrado: '))
  area = lado**2
  return area
def main():
  x = squareCalc()
  print(f'O Resultado da Area do quadrado é {x}')
main()