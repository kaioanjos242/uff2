# programa para ler uma quantidade n de numeros e escrever a quantidade de números impares e pares
# e a média dos números pares
# kaio cesar da silva anjos
# data de criação 07/11/2024

nums_pares = 0
nums_impares = 0
soma_pares = 0
numero = -1

# recebendo dado do usuário
while numero != 0:
    numero = int(input('Digite um número ou 0 para sair: '))

    # verifica se é diferente da condição de parada
    if numero != 0:

        # verfica se é par ou impar
        if numero % 2 == 0:
            nums_pares += 1
            soma_pares += numero
        else:
            nums_impares += 1

# verifica se há numeros pares e caso haja calcula a média deles
if nums_pares > 0:
    media_pares = soma_pares // nums_pares
    print('A média de números pares = ', media_pares)

if nums_pares > 0:
    print('A quantidade de números pares é: ', nums_pares)

if nums_impares > 0:
    print('A quantidade de números impares é: ', nums_impares)