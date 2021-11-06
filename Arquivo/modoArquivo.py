

# o modo "w" apaga o arquivo existente ou cria um novo arquivo

# arquivo = open('Arquivo/numeros.txt', 'w')
# for linha in range(1005, 1101):
#     arquivo.write('Bom dia! %d\n' % linha)
# arquivo.close()

# o modo "a" (append) cria um arquivo para escrever, mas preserva o que ja existe nele

# arquivo = open('Arquivo/numeros.txt', 'a')
# for linha in range(112, 1006):
#     arquivo.write('Bom dia! %d\n' % linha)
# arquivo.close()

# o modo "r" abre o arquivo para somente leitura
# o Metodo/função readlines, gera uma lista de cada elemento é uma linha do Arquivo

# arquivo = open('Arquivo/numeros.txt', 'r')

# for x in arquivo.readlines():
#     print(x)
# arquivo.close()


# Trabalhando com dois arquivos

# Gravação de numeros pares e impares em arquivos diferentes

impares = open('Arquivo/impares.txt', "a")
pares = open('Arquivo/pares.txt', "a")

for n in range(1, 51):
    if n % 2 == 0:
      pares.write("%d\n" % n)
    else:
      impares.write("%d\n" % n)
impares.close()
pares.close()
