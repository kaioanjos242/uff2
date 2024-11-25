# Programa destinado a calcular os N primeiros números de uma Progressão Aritmética
# Kaio Cesar da Silva Anjos
# data de criação 1/11/2024


a1 = int(input('Digite o primeiro termo da pa: '))  # primeiro termo da PA
r = int(input('Digite a razão: '))  # Razão da PA
n = int(input('Digite n: '))  # Quantidade de termos da PA


for i in range(n):
    termo = a1 + i * r
    numero = i + 1  # Determina qual é termo da PA
    print('a', numero, " ", termo)