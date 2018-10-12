# Calcule o tempo de uma viagem de carro. 
# Pergunte a distância a percorrer e a velocidade média esperada para a viagem.

distancia = float(input('Qual a distância (KM) a percorrer?  '))
velocidadeMedia = float(input('Qual a velocidade (KM/h) média esperada?  '))

tempoDeViagem = distancia / velocidadeMedia

print('Você irá levar %.2f ' %tempoDeViagem + ' hora(s) para concluir sua viagem.')

