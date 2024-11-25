# programa para converter um número decimal com qualquer número de digitos fornecido pelo usuário e converter para base hexadecimal. 
# Kaio Cesar Da Silva Anjos
# data de criação 17/11/2024

numero = int(input('Digite um número: '))
numero_hexadecimal = ''  # variavel para armazenar o número convertido para hexadecimal

# 
digitos_hexadecimais = '0123456789ABCDEF'

# conversão do número para hexadecimal
while numero > 0:
    resto = numero % 16
    numero_hexadecimal = digitos_hexadecimais[resto] + numero_hexadecimal
    numero //= 16 


print('O número digitado convertido para base hexadecimal é', numero_hexadecimal)