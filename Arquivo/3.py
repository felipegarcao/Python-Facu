"""
3. Elabore uma estrutura para representar e armazenar 10 alunos (matricula, nome, telefone). Utilize os recursos de arquivo para armazenar estes dados permanentemente. O nome do arquivo deve ser o mesmo da estrutura. Construa um menu com as seguintes opções, cada uma delas deve ter uma função e a main para chamar todas elas.
Menu de opções:
Cadastrar alunos
Visualizar todos os dados
Sair
"""


# pip install tabulate
from tabulate import tabulate

class AlunoCadastro:
    matricula: int
    telefone: str
    nome: str


def Cadastro():
    try:
        with open('Arquivo/alunosCadastrados.txt', 'r', encoding="utf-8") as arquivo:
            totalAlunosCadastro = len(arquivo.readlines())
    except:
        totalAlunosCadastro = 0

    irCadastrar = True
    while irCadastrar:
      if totalAlunosCadastro == 10:
        print('10 alunos ja Cadastrados !!')
        irCadastrar = False
      with open('aArquivo/alunosCadastrados.txt', "a+", encoding="utf-8") as arquivo:
        newAluno = AlunoCadastro()
        newAluno.matricula = int(input('Digite a matricula do aluno: '))
        newAluno.nome = input('Digite o nome do Aluno: ')
        newAluno.telefone = input('Digite o telefone do Aluno: ')

        arquivo.write(str(newAluno.matricula) + '/' +
                      newAluno.nome + '/' + newAluno.telefone + '\n')

      totalAlunosCadastro += 1

      perguntaContinue = input('Desja Cadastrar um novo aluno ? [S/N]: ').upper()
      if perguntaContinue != "S":
        irCadastrar = False

    article()
  
def verAlunos():
  try:
    with open("Arquivo/alunosCadastrados.txt", 'r', enconding="utf-8") as arquivo:
      
      tabelaAluno = []
      for line in arquivo.readlines():
        info = line.split('/')
        aluno = AlunoCadastro()
        aluno.matricula = info[0]
        aluno.nome = info[1]
        aluno.telefone = info[2]
        tabelaAluno.append([aluno.matricula, aluno.nome, aluno.telefone])
      
      print(tabulate(tabelaAluno, headers=["Matricula", "Name", "Phone"]))
      article()
  except:
    # Caso o Arquivo não exista
    article()

def article():
  print("="*20)
  print('1. Cadastrar Aluno')
  print('2. Visualizar todos os dados dos alunos')
  print('3. Cair Fora')
  print("="*20)
  operation = input('Digite a operação Desejada:  ')
  if operation in ['1', '2', '3']:
    operation = int(operation)
    if operation == 1:
      Cadastro()
    elif operation == 2:
      verAlunos()
    elif operation == 3:
      quit('Aplicação Finalizada com Sucesso !!!')
    else:
      print('Operação Não encontrada - Status code 404')
      
def main():
  article()
  
main()
