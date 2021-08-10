nome = 'Fulano'
idade = 22
grana = 31.32131


print("%s tem %i anos e R$%f no bolso"%(nome, idade, grana))
# Fulano tem 22 anos e R$31 no Bolso

print("%12s tem %5i anos e R$%15.2f no bolso"%(nome, idade, grana))
# Fulano tem 22 anos e R$       31.47 no Bolso  => 15 digitos e duas casas decimais

print("%s tem %04i anos e R$%2f no bolso"%(nome, idade, grana))
# Fulano tem 0022 anos e R$ 31.47 no bolso

print("%-12s tem %-3i anos e R$%9.2f no bolso"%(nome, idade, grana))
# Fulano tem 22 anos 


print(f'{nome} tem {idade} anos e R${grana:.2f} no Bolso')