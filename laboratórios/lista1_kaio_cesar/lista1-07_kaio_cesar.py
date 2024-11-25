
a = int(input('Digite um valor A: '))  # variável responsável por receber do usuario e armazenar o valor de A
b = int(input('Digite um valor B: '))  # variável responsável por receber do usuario e armazenar o valor de B
soma = 0  # variável responsável por armazenar o valor da soma dos numeros compreendidos

# verificação se A > B
if a > b:
    print('A soma não será realizada')
else:
    # loop para o calculo dos números multiplos de 4 compreendidos
    for i in range(a+1, b):
        print(i)
        # verifica se o resto da divisão por 4 é 0, se for é multiplo de 4
        if i % 4 == 0:
            soma += i
    print('A soma dos números multiplos de 4 compreendidos entre ',a, 'e', b, 'é', soma)
