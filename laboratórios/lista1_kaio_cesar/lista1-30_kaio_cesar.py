# programa destinado a imprimir os fatores da fatoração de um número recebido do usuário.
# Kaio Cesar da Silva Anjos
# data de criação 15/11/24


# declaração de variáveis
numero = int(input('Digite o número inteiro que deseja fatorar: '))
divisor = 2
contador_de_divisores = 0

# loop para inicializar a fatoração
print('Fatoração de ', numero)
while numero > 1:
    contador_de_divisores = 0

    # loop para dividir o numero pelo divisor enquando o resto for 0, se não for passa pro próximo divisor
    while numero % divisor == 0:
        numero //= divisor
        contador_de_divisores += 1
    
    # verifica se o divisor dividiu o número
    if contador_de_divisores > 0:
        print(divisor, '^', contador_de_divisores)


    divisor += 1


