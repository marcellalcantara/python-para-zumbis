dias = int(input('Digite uma quantidade de dias: '))
horas = int(input('Digite uma quantidade de horas: '))
minutos = int(input('Digite uma quantidade de minutos: '))
segundos = int(input('Digite uma quantidade de segundos: '))

diasEmSegundos = dias * 24 * 60 * 60
horasEmSegundos = horas * 60 * 60
minutosEmSegundos = minutos * 60

print(str(diasEmSegundos + horasEmSegundos + minutosEmSegundos + segundos) + 'segundos')