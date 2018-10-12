#tempo de vida de um fumante. 
#Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. 
#Considere que um fumante perde 10  minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. 
# Exiba o total de dias.

DIAS_DO_ANO = 365
MINUTOS_PERDIDOS_POR_CADA_CIGARRO = 10
MINUTOS_DE_UM_DIA = 1440

quantidadeCigarros = int(input('Quantos cigarros você fuma por dia? '))
anosFumando = float(input('Quantos anos já fumou? '))

totalCigarros = (anosFumando * DIAS_DO_ANO) * quantidadeCigarros
diasPerdido = (totalCigarros * MINUTOS_PERDIDOS_POR_CADA_CIGARRO) / MINUTOS_DE_UM_DIA

print('Você perdeu ' + str(diasPerdido) + ' dias de vida')