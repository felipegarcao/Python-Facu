def tabuada(x): 
  for count in range(1,11):
    print(f"{x} X {count} = {x * count}")
  
def main():
  valor_tabuada = int(input("Valor da Tabuada: "))
  tabuada(valor_tabuada,)
main()