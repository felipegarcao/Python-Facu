# Elabore uma estrutura para representar um produto (código, nome, preço). Aplique 10% de aumento no preço do produto e apresente.

class TipoProduto:
    codigo = 0
    nome = ''
    preco = 0.0

def main():
    p1 = TipoProduto
    p1.codigo = int(input('Cadastre o Codigo do Produto: '))
    p1.nome = input('Cadastre o nome do Produto: ')
    p1.preco = float(input('Cadastre o Preço do Produto R$: '))
    p1.preco = p1.preco + p1.preco * 10 / 100
    print(f'Codigo: {p1.codigo} \tNome: {p1.nome} \tPreço R$ {p1.preco:.2f}')
main()