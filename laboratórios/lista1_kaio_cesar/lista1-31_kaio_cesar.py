# programa destinado a calcular a raiz inteira de um número N, fornecido pelo usuário.
# Kaio Cesar da Silva Anjos
# Data de criação 01/11/2024

n = int(input('Digite um número inteiro: '))  # número inteiro fornecido pelo usuário

raiz = (n **  0.5)//1 # cálculo da raiz do número recebido do pelo usuário

print('A raiz inteira de', n, 'é igual a', int(raiz))