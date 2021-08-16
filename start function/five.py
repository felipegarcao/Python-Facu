#  (Função sem retorno sem parâmetro) Faça uma função/método que receba o preço antigo e atual de um produto, determine o percentual de acréscimo entre esses valores e apresente-o.

def comparadorPreco():
  preco_antigo = float(input('Digite o Valor Antigo Do Produto: '))
  preco_novo = float(input('Digite o Valor Novo Do Produto: '))
  
  r = (100 * preco_novo - 100 * preco_antigo) / preco_antigo
  
  print(f'Porcentaul de Acrescimo entre esses valores: {r:.0f}%')

comparadorPreco()