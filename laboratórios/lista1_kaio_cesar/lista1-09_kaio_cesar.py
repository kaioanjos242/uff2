# Programa destinado a calcular a porcentagem de satisfação dos consumidores de uma determinada
# marca
# Kaio Cesar da Silva Anjos
# data de criação 08/11/2024

resposta = ''  # variavel responsável por armazenar a resposta do usuário
satisfeitos = 0  # total de clientes satisfeitos
nao_satisfeitos = 0  # total de clientes insatisfeitos
pct_satisfeitos = 0  # porcentagem de consumidores satisfeitos
pct_naosatisfeitos = 0  # porcentagem de consumidores insatisfeitos
total = 0  # total de respostas


# loop para receber a resposta do usuário enquanto a entrada não for "f"
while resposta != 'f' and resposta != 'F':
    resposta = input('Digite S para satisfeito e N para não satisfeito, ou digite f para sair: ')

    # verificação se a resposta é diferente de "f"
    # se for incrementa 1 a variavel "total"
    if resposta != 'f':
        total += 1

        # verificação se a resposta é 's' para sim ou 'n' para não
        if resposta == 'S' or resposta == 's':
            satisfeitos += 1

        elif resposta == 'N' or resposta == 'n':
            nao_satisfeitos += 1

pct_satisfeitos = satisfeitos / total * 100
pct_naosatisfeitos = nao_satisfeitos / total * 100

print('os clientes satisfeitos representam ', pct_satisfeitos, '% de', total)
print('os clientes não satisfeitos representam ', pct_naosatisfeitos, '% de', total)
