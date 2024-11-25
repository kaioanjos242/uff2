# Programa destinado a calcular os primeiros 4 numeros perfeitos.
# Kaio Cesar da Silva Anjos
# data de criação

contador = 0
num = 1

while contador < 4:
    # Calcula a soma dos divisores próprios do numero
    soma_div = 0  # armazena a soma dos divisores
    i = 1
    while i < num:
        if num % i == 0:
            soma_div += i
        i += 1

    # descobrindo se o número é perfeito
    if soma_div == num:
        print(num)
        contador += 1

    soma_div += 1