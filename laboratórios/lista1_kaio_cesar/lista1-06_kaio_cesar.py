# Exercicío n°6
# Programa para realizar a soma dos números compreendidos entre A e B, excluindo A e B da soma
# Kaio Cesar da Silva Anjos
# data de criação 29/10/2024

a = int(input('Digite um valor A: '))  # variável responsável por receber do usuario e armazenar o valor de A
b = int(input('Digite um valor B: '))  # variável responsável por receber do usuario e armazenar o valor de B
soma = 0  # variável responsável por armazenar o valor da soma dos numeros compreendidos

# verificação se A > B
if a > b:
    print('A soma não será realizada')
else:
    # loop para o calculo dos números compreendidos
    for i in range(a+1, b):
        print(i)
        soma += i
    print("A soma dos valores compreendidos entre ", a, 'e', b, 'é:', soma)