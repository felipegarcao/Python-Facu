

class TipoFuncionario:
    matricula = 0
    nome = ""
    salario = 0.0


def Cadastrar(vetFuncionario):
    arquivo = open('Arquivo/arq_funcionario.txt', 'w')
    print('Cadastro de Funcionarios.............')
    for i in range(3):
        f = TipoFuncionario()
        f.matricula = int(input('Digite a Matricula: '))
        f.nome = input("Digite o Nome")
        f.salario = float(input('Salario: '))
        vetFuncionario.append(f)
        arquivo.write(f'{f.matricula} {f.nome} {f.salario:.2f}\n')
        # ou
        arquivo.write("%d %s %.2f\n" % (f.matricula, f.nome, f.salario))
    arquivo.close()
    return vetFuncionario
  
def Mostrar():
  arquivo = open('Arquivo/arq_funcionario.txt', "r")
  print('Aprensentação dos dados dos Funcionarios')
  for linha in arquivo.readlines():
    mat, nome, sal = linha.strip().split(' ')
    print(mat, '\t\t', nome, '\t', sal )
  arquivo.close()
def main():
  op = 1
  while op >= 1 and op <= 2:
    print("*** Gerenciamento de Funcionarios COM ARQUIVO ***")
    print('1-Cadastrar')
    print('2-Mostrar')
    print('3-Sair')
    op = int(input("Digite a opção: "))
    if op == 1:
      vetF = []
      vetF = Cadastrar(vetF)
    elif op == 2:
      Mostrar()
main()
