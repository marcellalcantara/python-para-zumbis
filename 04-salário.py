salario = float(input('Digite o valor do salário: R$  '))
porcentagem = float(input('Digite o valor da porcentagem: '))

aumentoSalario = salario * porcentagem / 100
novoSalario = salario + aumentoSalario

print('O aumento de salário será de: R$ ' + str(aumentoSalario))
print('Totalizando: R$ ' + str(novoSalario))