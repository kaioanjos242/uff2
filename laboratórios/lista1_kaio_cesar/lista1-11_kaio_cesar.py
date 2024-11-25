# Programa destinado a fazer o cálculo dos primeiros n números inteiros, impares e positivos
# Kaio Cesar da Silva Anjos
# data de criação 1/11/2024


n = int(input('Digite um número: ')) # recebe do usuário o valor até qual número será feito o cálculo
impares = 0  # variável que mostra os numeros impares
soma = 0  # variável que mostra a soma dos números pares

# verifica se o valor é maior que 0, ou seja, positivo
if n < 0:
    print('Número inválido')
else:
     
    for i in range(n+1):
        if i % 2 != 0:
            impares = i
            soma += i
            print(impares)
    print('A soma dos primeiros números impares até', n, 'é', soma)
