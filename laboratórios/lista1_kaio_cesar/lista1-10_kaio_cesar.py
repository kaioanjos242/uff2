# Exercício n°10
# Programa para calcular através de um loop for a soma dos primeiros 20 numeros pares, usando um range.
# Kaio Cesar Da Silva Anjos
# Data de modificação 29/10/2024

soma = 0  # varível soma, responsável por armazenar a soma dos números pares

for numero in range(1, 41): # estrutura de repetição responsável por percorrer usando um
    # range os primeiros 20 números pares

    if numero % 2 == 0: # estrutura condicional que verifica paridade de numero;
        # se for par faz o cálculo e atribui a variável soma.
        print(numero)
        soma += numero

print('A soma dos primeiros 20 números pares é: ', soma)
''