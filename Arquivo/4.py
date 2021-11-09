

# pip install tabulate
from tabulate import tabulate


def get():
  with open("Arquivo/futebol.txt", 'r', encoding='utf-8') as file:
    tabela = []
    interaction = 0
    for line in file.readlines():
      interaction += 1
      data = line.split(",")

      position = data[0]
      height = float(data[1])
      weight = float(data[2])
      imc = weight / (height ** 2)
      if imc < 18.5:
        classification = "Abaixo do peso"
      elif imc >= 18.5 and imc <= 24.9:
        classification = "Peso normal"
      elif imc >= 25 and imc <= 29.9:
        classification = "Sobrepeso"
      elif imc >= 30:
        classification = "Obesidade"
        
      with open('Arquivo/newFutebol.txt', "a+", encoding='utf-8') as newFutebol:
        newFutebol.write(str(position) + ","+ str(height) + "," + str(weight) + "," + str(imc) + "," + classification + "\n")
      tabela.append([interaction, weight, height, imc, classification])
    print(tabulate(tabela, headers=["Player", "position", "height", "weight", "IMC", "Classification"]))
    
def main():
  get()
  
main()