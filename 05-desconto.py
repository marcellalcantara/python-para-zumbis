valor = float(input('Digite o valor da mercadoria: R$  '))
porcentagem = float(input('Digite o valor do desconto: '))

valorDesconto = valor * porcentagem / 100
precoPagar = valor - valorDesconto 

print('Valor de desconto será: R$ ' + str(valorDesconto))
print('O Valor a ser pago será de: R$ ' + str(precoPagar))