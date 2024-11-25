# programa para simular um caixa eletrônico e ler um valor digitado pelo usuário e entregar esse valor no menor número de notas possíveis.
# Kaio Cesar Da Silva Anjos
# data de criação 16/11/2024
  
#declaração das variáveis
valor = int(input('Digite o valor que deseja retirar: '))
resto = 0

# contadores das notas
cont_50 = 0
cont_20 = 0
cont_10 = 0
cont_5 = 0
cont_1 = 0

print('Valor solicitado: ', valor)  


# verifica se o valor é maior que 50, se for, pega a quantidade de notas de 50 que dá pra retirar
if valor > 50:
    cont_50 = valor // 50
    resto = valor % 50
    valor = resto

# verifica se o valor é maior que 20, se for, pega a quantidade de notas de 20 que dá pra retirar
if valor > 20:
    cont_20 = valor // 20
    resto = valor % 20
    valor = resto

# verifica se o valor é maior que 10, se for, pega a quantidade de notas de 10 que dá pra retirar
if valor > 10:
    cont_10 = valor // 10
    resto = valor % 10
    valor = resto


# verifica se o valor é maior que 5, se for, pega a quantidade de notas de 5 que dá pra retirar
if valor > 5:
    cont_5 = valor // 5
    resto = valor % 5
    valor = resto


# verifica se o valor é maior que 1, se for, pega a quantidade de notas de 1 que dá pra retirar
if valor > 1:
    cont_1 = valor // 1
    resto = valor % 1
    valor = resto
        

print('Entregando: ')
print(cont_50, 'nota(s) de $50; ')
print(cont_20, 'nota(s) de $20; ')
print(cont_10, 'nota(s) de $10; ')
print(cont_5, 'nota(s) de $5; ')
print(cont_1, 'nota(s) de $1')