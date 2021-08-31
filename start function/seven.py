def funcao():
    n1 = float(input("informe a primeira nota: "))
    n2 = float(input("informe a segunda nota: "))
    n3 = float(input("informe a terceira nota: "))
    l = input("infome a Letra:[A]ou[p] ").upper()
    if l == "A":
        media = (n1 + n2 + n3) /3
        print(f"media arimética é {media}")
    
    elif l == "P":
        media_ponderada = ((n1 * 5 + n2 * 3 + n3 * 2 ) / (5 + 3 + 2))
        print(f"a média ponderada é:{media_ponderada}")

def main():
    funcao()

main()