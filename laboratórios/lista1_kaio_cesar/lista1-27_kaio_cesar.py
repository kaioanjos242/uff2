# programa para converter um número com quaisquer digitos em base numerica de ordem < 10 para um número na base decimal. 
# Kaio Cesar da Silva Anjos
# data de criação 17/11/2024


# dados recebidos do usuário
numero = input('Digite o número a ser convertido: ')
base = int(input('Digite a base (abaixo de 10: 2, 3, 8): '))


decimal = 0 # variavel para armazenar o número convertido para decimal
pot = 0


# percorre o número inversamente para fazer o calculo
for x in numero[::-1]:
    decimal += int(x) * (base**pot)
    pot += 1


print('O número ', numero, ' na base ', base,  ' corresponde a ', decimal, ' na base decimal.')
