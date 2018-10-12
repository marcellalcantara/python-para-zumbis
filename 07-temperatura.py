#Converta uma temperatura digitada em Celsius para Fahrenheit. 
#F = 9*C/5 + 32

temperaturaCelsius = float(input('Qual a temperatura em Celsius?  '))

temperaturaFahrenheit = 9 * temperaturaCelsius / 5 +32
print('A temperatura em Fahrenheit será ' + str( temperaturaFahrenheit) + '°F')

