

from tabulate import tabulate


class Tipo_Cliente:
    cliente_id: int
    nome: str


class Tipo_Venda:
    cod_venda: int
    dia: int
    total: float
    client: int


clientes = []
vendas = []


def registrationClient():
    advance = "S"
    while advance == "S":
        client = Tipo_Cliente()
        client.client = int(input("Consumer Code: "))
        client.nome = input("Name: ")

        clientes.append(client)

        advance = input("wish to advance? (S/N): ").upper()

    menu()


def listClient():
    matriz = []
    for client in clientes:
        matriz.append([client.cliente_id, client.nome])
    print(tabulate(matriz, headers=["Consumer Code", "name"]))

    menu()


def registerSales():
    registration = "S"
    while registration == "S":
        if len(vendas) != 5:
            v = Tipo_Venda()
            v.cod_venda = int(input("sales code: "))
            v.dia = int(input("code day: "))
            v.total = float(input("sale value: "))
            v.cliente = int(input("customer code: "))
            vendas.append(v)

            registration = input("do you wish to continue? (S/N): ").upper()
        else:
            print("limit reached!")
            registration = "N"

    menu()


def listSales():
    matriz = []
    for v in vendas:
        matriz.append([v.cod_venda, v.dia, v.total, v.cliente])
    print(tabulate(matriz, headers=[
          "sale code", "sale day", "value", "customer code"]))

    menu()


def list_sales_day():
    day = int(input("enter the day: "))
    if day > 0 and day < 32:
        matriz = []
        for v in vendas:
            if v.dia == dia:
                matriz.append([v.cod_venda, v.dia,
                              v.total, v.cliente])
        print(tabulate(matriz, headers=[
              "sale code", "sale day", "value", "customer code"]))
    else:
        print("invalid day!")
    menu()


def storeSales():
    with open("vendas.txt", "a+", encoding="utf-8") as file:
        for v in vendas:
            file.write(str(v.cod_venda) + "," + str(v.dia) +
                       "," + str(v.total) + "," + str(v.cliente) + "\n")
    menu()


def toIntroduce():
    with open("vendas.txt", "r", encoding="utf-8") as file:
        table = []
        for line in file.readlines():
            v = line.split(",")
            table.append([v[0], v[1], v[2], v[3]])
        print(tabulate(table, headers=[
              "sale code", "sale day", "value", "customer code"]))
    menu()


def menu():
    print("="*20)
    print("1. Cadastrar clientes")
    print("2. Mostrar todos os clientes")
    print("3. Cadastrar vendas")
    print("4. Mostrar todas as vendas")
    print("5. Mostrar o total de vendas de um determinado dia")
    print("6. Armazenar todos os campos da venda em um arquivo")
    print("7. Apresentar o conteúdo do arquivo")
    print("8. Sair")
    print("="*20)

    operation = input("Digite a operação: ")

    if operation == "1":
        registrationClient()
      elif operation == "2":
         listClient()
      elif operation == "3":
        registerSales()
        elif operation == "4":
          listSales()
        elif operation == "5":
          list_sales_day()
        elif operation == "6":
          storeSales()
        elif operation == "7":
          toIntroduce()
        elif operation == "8":
          quit("Bye Bye")
    else:
        menu()


def main():
    menu()


main()
