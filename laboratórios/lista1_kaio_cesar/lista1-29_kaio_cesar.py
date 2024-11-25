# programa para calcular o MDC e a quantidade de divisores entre as váriaveis A e B fornecidas pelo usuário. 
# Kaio Cesar da Silva Anjos
# data de criação 17/11/24

a = int(input('Digite um número inteiro: '))
b = int(input('Digite um número inteiro: '))
contador_divisores = 0 


# calculo do mdc
while b != 0:
    a = b 
    b = a % b

mdc = a

# verifica quantos divisores comuns há
for i in range(1, mdc + 1):
    if mdc % i == 0:
        contador_divisores += 1

print('0 MDC é: ', mdc)
print('A quantidade de divisores comuns: ', contador_divisores)