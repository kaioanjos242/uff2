# programa para calcular a quantidade de dias compreendidos entre duas datas fornecidas pelo usuário.
# Kaio Cesar Da Silva Anjos
# data de criação 17/11/2024


# data 1
D1 = int(input("Digite o dia da data 1: "))
M1 = int(input("Digite o mês da data 1: "))
A1 = int(input("Digite o ano da data 1: "))

# data 2
D2 = int(input("Digite o dia da data 2: "))
M2 = int(input("Digite o mês da data 2: "))
A2 = int(input("Digite o ano da data 2: "))

cont_ano_bissexto = 0
soma_dias = 0

# percorre os anos entre A1 e A2 para saber se tem algum ano bissexto compreendido entre eles
for i in range(A1, A2+1):

    if i % 4 == 0:
        cont_ano_bissexto += 1


# converte para dias
dias_data1 = A1 * 365 + M1 * 30 + D1
dias_data2 = A2 * 365 + M2 * 30 + D2


# calcula a quantidade de dias compreendidos entre a data 1 e a data 2
qtd_dias = dias_data2 - dias_data1

# se houver algum ano bissexto adiciona ao total de dias a quantidade de dias para cada ano bissexto
if cont_ano_bissexto > 0:
    soma_dias += cont_ano_bissexto
    qtd_dias += soma_dias
    print('A quantidade de dias entre as datas é:', qtd_dias)
else:
    print('A quantidade de dias entre as datas é:', qtd_dias)
