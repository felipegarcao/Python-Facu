# (Função sem retorno sem parâmetro) Faça uma função/método que leia um único valor representado em segundos, converta-o e apresente o resultado em horas, minutos e segundos.

def converterHours():
  segundos_str = int(input('Por favor, entre com o Numeros de Segundos que Deseja Converter: '))


  horas = segundos_str // 3600
  dias = horas // 86400


  segs_restantes = segundos_str % 3600
  minutos = segs_restantes // 60
  segs_restantes_final = segs_restantes % 60

  if (horas >= 24):
    dias = int(horas / 24)
    horas = int(horas % 24)

  print(dias,"dias,",horas,"horas,",minutos,"minutos e",segs_restantes_final,"segundos.")

converterHours()