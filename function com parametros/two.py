def sub(x,y):
  resultado = x - y
  print(f"O Resultado do seu Calculo é {resultado}")
  
def main():
  number1 = float(input('Primeiro Numero que Deseja Subtrair: '))
  number2 = float(input('Segundo Numero que Deseja Subtrair: '))
  sub(number1, number2)
main()