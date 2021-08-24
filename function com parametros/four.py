def calcularAumento(preco, porcentagem): # Parametros
  aumento = preco + (preco * porcentagem / 100)
  print(f"O preço do Produto apos o aumento é {aumento:.0f}") 
  
def main():
  preco_produto = float(input("Informe o Preço do Produto: "))
  porcentagem_produto = float(input("Informe a Porcentagem do Produto: ")) 
  calcularAumento(preco_produto, porcentagem_produto) # Argumento
main()
