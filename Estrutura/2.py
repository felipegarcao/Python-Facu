# Elabore uma estrutura para representar um produto (código, nome, preço). Cadastre 5 produtos, use vetor/lista. Aplique 10% de aumento no preço do produto e apresente todos os dados do preço.
class TipoProduto:
    codigo = 0
    nome = ''
    preco = 0.0


def main():
    vet_produto = []
    for i in range(3):
        p = TipoProduto()
        p.codigo = int(input('Cadastre o Codigo do Produto'))
        p.nome = input('Cadastre o nome do Produto')
        p.preco = float(input('Cadastre o Preço do Produto '))
        p.preco = p.preco + p.preco * 10 / 100
        vet_produto.append(p)
    for i in range(len(vet_produto)):
        print(
            f'Codigo: {vet_produto[i].codigo} \tNome: {vet_produto[i].nome} \tPreço: {vet_produto[i].preco:.2f}')


main()
