# crie um programa que leia um número n e verifique se ele é primo
# Kaio Cesar da Silva Anjos
# data de criação 13/11/2024

n = int(input('Digite um número: '))
sinal = False  # variável para sinalizar se a divisão de algum dos numeros no for é exata

# verifica se a divisão dos números até n é exata, se for, gera um sinal que significa que 
# não é um número primo, pois os  números primos só são divisíveis por 1 e ele mesmo 
for num in range(2, n):
    if n % num == 0:
        sinal = True
        
# verifica se há um sinal, se houver não é primo
if sinal == True:
    print(n, 'não é primo')
elif sinal == False:
    print(n, 'é um número primo')
