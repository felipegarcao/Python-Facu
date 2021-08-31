def funcao():
    numero_maior = numero_menor = 0
    for i in range(5):
        n = int(input("informe o numero: "))
        if i == 0 :
            numero_maior = numero_menor = n
        
        elif n > numero_maior:
            numero_maior = n
        
        elif n < numero_menor:
            numero_menor = n
    print(f"o numero maior digitado é {numero_maior}, já o numero menor{numero_menor} ")

def main():
    funcao()

main()
