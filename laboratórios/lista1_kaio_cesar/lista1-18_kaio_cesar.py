# Programa que recebe um número N do usuário, e imprime os primeiros números primos até n.
# Kaio Cesar da Silva Anjos
# data de criação 15/11/24


n = int(input('Digite um número inteiro para n: '))
primos = 0
num = 2

# verificação se o número é primo
while primos < n:
    divisor = 0

    for i in range(2, num):
        if num % i == 0:
            divisor += 1

    if divisor == 0:
        print("Número primo: ", num)
        primos += 1
    num += 1


    
