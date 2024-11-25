# Programa destinado a receber um número N do usuário e calcular o somatório até N
# Kaio Cesar da Silva Anjos
# data de criação 15/11/2024


n = int(input('Digite um número inteiro: '))
somatorio = 0
div = 0

# loop para calcular o somatório
for num in range(1, n+1):
    div = 1/num
    print(div)
    somatorio += div

print('O somatório é ', somatorio)
