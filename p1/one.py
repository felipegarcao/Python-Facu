def f(email):
  ta = 0
  tp = 0
  for i in range(0,len(email)):
    letra = email[i]
    if letra == ".":
      tp+=1
    elif letra == "@":
      ta+=1
  if ta == 1 and tp >= 1:
    return print('Email É Valido',True)
  else:
    return print('Email Invalido',False)

def main():
  isValidEmail = str(input('Digite um Email: '))
  f(isValidEmail)
main() 