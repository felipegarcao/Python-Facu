def produtoReajuste(x):
  aumento = x + (x * 9 / 100)
  print(f"O Valor do Produto Informado foi Reajustado e o Novo valor é  R${aumento}")
  
def main():
  preco_produto = float(input('Digite o valor do Produto, Para de ser Reajustado: R$ '))
  produtoReajuste(preco_produto)
main()