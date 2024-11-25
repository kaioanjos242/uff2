# programa para ler um número digitado pelo usuário e verificar se esse número é perfeito
# Kaio Cesar Da Silva Anjos
# data de criação 16/11/2024

numero = int(input('Digite um número inteiro: '))
i = 1

while  i < numero:
    # Calcula a soma dos divisores próprios do numero
    soma_div = 0  # armazena a soma dos divisores
    while i < numero:
        if numero % i == 0:
            soma_div += i
        i += 1

    # Verifica se o número é perfeito
    if soma_div == numero:
        print(numero, "é um número perfeito.")
    else:
        print(numero, "não é um número perfeito. ")
