employees = 10

def calcINSS(salary,porcent=9):
  return (salary*porcent/100)

def cacLiq(salary, inss):
  return salary - inss

def main():
  salarys = []
  list_inss = []
  net_wages = []
  for i in range(0, employees):
    salary = int(input(f'Digite o Salario do {i+1} Funcionarios'))
    value_inss = calcINSS(salary)
    liquid = cacLiq(salary,value_inss)
    
    salarys.append(salary)
    list_inss.append(value_inss)
    net_wages.append(liquid)
    
    print('Salario', salarys[i])
    print('Desconto Inss:', list_inss[i])
    print('Salario Liquido',net_wages[i])
    print("="*15)
    print("")
    
main()
  