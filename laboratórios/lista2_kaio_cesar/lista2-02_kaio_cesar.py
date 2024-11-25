# programa para verificar quantos números pares há em uma determinada lista
# kaio cesar da silva anjos
# data de criação 25/11/2024

numeros = [] # armazena os numeros coletados do usuário
numeros_pares = [] # armazena os numeros pares dentre os números coletados do usuário

# repetição para coletar os números do usuário
for n in range(40):
    n = int(input('Digite um número:'))
    numeros.append(n) # adiciona na lista de numeros

    # verificação se o número é par
    if n % 2 == 0:
        numeros_pares.append(n) # adiciona na lista de pares

print('A quantidade de número pares é: ', len(numeros_pares))
