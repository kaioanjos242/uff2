# programa destinado a ler os nomes e os preços de x produtos
# e em seguida dizer qual é o produto mais caro.
# kaio cesar da silva anjos
# data de criação 07/11/2024

produto = ''
preco = 0
preco_mais_caro = 0
produto_mais_caro = ''

# verficação se a condição de parada é verdadeira, se for continua o loop
while produto != 'xxx':
    produto = str(input('Produto: '))

    # pega o preço se a string for diferente de 'xxx'
    if produto != 'xxx':
        preco = float(input('Preco: '))

        # verificação do produto mais caro
        if preco > preco_mais_caro:
            preco_mais_caro = preco
            produto_mais_caro = produto


print('produto mais caro é: ',produto_mais_caro , 'custando R$', preco_mais_caro)
