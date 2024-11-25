# Exercício n°5
# Programa para fazer a leitura de diversos dados de um determinado produto, a descrição, preço e a
# quantidade. Após isso deve determinar qual é o gasto total, e o produto mais caro.
# Kaio Cesar da Silva Anjos
# Data de modificação 29/10/2024


produto_mais_caro = ""  # variável para armazenar o valor do produto mais caro

preco_mais_caro = 0  # variável para armazenar o preço do produto mais caro

gasto_total = 0  # variável para armazenar o gasto total da empresa


for n in range(10):
    print("Produto ", n + 1)
    descricao_do_produto = input("Digite a descrição do produto: ")
    preco_da_unidade = float(input("digite o valor do preço da unidade : "))
    quantidade = int(input("Digite a quantidade: "))

    # cauculo dos gastos totais
    gasto_total += preco_da_unidade * quantidade

    # Verificar se é o produto mais caro
    if preco_da_unidade > preco_mais_caro:
        preco_mais_caro = preco_da_unidade
        produto_mais_caro = descricao_do_produto

print('O gasto total da empresa foi: ' , gasto_total)
print('Produto mais caro: ', produto_mais_caro, 'R$ ', preco_mais_caro)
