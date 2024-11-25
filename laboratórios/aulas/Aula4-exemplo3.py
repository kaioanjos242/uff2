# Programa para definir qual entre dois números é o maior, atráves de uma estrutura condicional que
# pega o primeiro número e comprara com o segundo através de um operador comparativo e imprime o resultado da expressão.
# Kaio Cesar da Silva Anjos
# data de criação 25/10/2024

# Entrada para que o usuário digite um valor que será atribuido ao numero 1
num1 = int(input('Digite o primeiro valor: '))

# Entrada para que o usuário digite um valor que será atribuido ao numero 2
num2 = int(input('Digite um segundo valor: '))

# Estrutura condicional para comparar os dois valores digitados
if num1 > num2: # Aqui testa através do operador comparativo (>) se o primeiro é maior que o segundo
    print('O primeiro é maior que o segundo') # caso a expressão seja verdadeira, imprime está linha, caso contrario
    # parte para próxima condição
elif num2 > num1: # Aqui testa através do operador comparativo (>) se o segundo é maior que o primeiro
    print('O segundo é maior que o primeiro') # caso a expressão seja verdadeira, imprime está linha, caso contrario
    # parte para próxima condição
else:
    print('Os dois são iguais') # Nesta linha imprime caso uma das condições anteriores não tenha sido atendida