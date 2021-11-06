
class TipoProduto:
    codigo = 0
    nome = ''
    preco = 0.0


def Cadastrar(produtos):
    arquivo = open('Arquivo/produto1.txt', 'w')
    print('Cadastrar Produto....')
    for i in range(2):
        cadastro = TipoProduto()
        cadastro.codigo = int(input('Digite o Codigo do Cadastro: '))
        cadastro.nome = input('Nome do Produto: ')
        cadastro.preco = float(input('Preco do Produto: '))
        produtos.append(cadastro)
        arquivo.write("%d%s%.2f\n" %
                      (cadastro.codigo, cadastro.nome, cadastro.preco))
    arquivo.close()
    return produtos


def MostrarDados():
    arquivo = open('Arquivo/produto1.txt', 'r')
    print('Apresentação dos dados do Produtos.....')
    print('Codigo\tNome\tPreço')
    for linha in arquivo.readlines():
      print(linha)
    arquivo.close()


def main():
    op = 1
    while op >= 1 and op <= 2:
        print("*** Cadastrar Produtos COM ARQUIVO")
        print('1-Cadastrar')
        print('2-Mostrar Dados')
        print('3-Sair')
        op = int(input('Digite a opção: '))
        if op == 1:
            vetP = []
            vetP = Cadastrar(vetP)
        elif op == 2:
            MostrarDados()
        else:
            print('Adeus Ate Mais')


main()
