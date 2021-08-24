def calcularMedia(p1,p2):

  media = (p1 + p2) / 2

  if media >= 6:
    print('Aluno Aprovado')
  else: 
    print('Aluno Reprovado')
    
def main():
  nota1 = float(input("Digite o valor Da Primeira Nota: "))
  nota2 = float(input("Digite o valor da Segunda Nota: "))
  calcularMedia(nota1, nota2)
main()