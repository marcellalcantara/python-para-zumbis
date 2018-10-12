# Qual quantidade de km percorridos por um carro alugado pelo usuário,
# assim como a quantidade de dias pelos quais o carro foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado

kmPercorrido =float(input('Quantos Km percorridos? '))
diasalugado =float(input('Por quantos dias o carro foi alugado? '))

preçoPagar = (kmPercorrido * 0.15) + diasalugado * 60
print('O Valor total do aluguel será R$ %.2f ' %preçoPagar)