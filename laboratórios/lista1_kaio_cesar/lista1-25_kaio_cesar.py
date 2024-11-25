# faça um programa que receba n números inteiros e verifique se é possível formar um poligono. 
# Kaio Cesar Da Silva Anjos
# data de criação 16/11/2024

lado = 1  # lado inicia em 1 para o loop funcionar
maior_lado = 0
quantidade_de_lados = 0  # conta os lados do poligono 
soma_lados = 0  # soma os lados do polígono

# recebe os lados do polígono
while lado != 0:
    lado = int(input('Digite um número inteiro e positivo ou digite 0 para sair: '))
    soma_lados += lado
    quantidade_de_lados += 1

    # verifica o maior lado
    if lado > maior_lado:
        maior_lado = lado

# separando o maior lado dos demais lados
soma_dos_demais_lados = soma_lados - maior_lado

# verifica se as condições de existência de um polígono são atendidas ou não
if quantidade_de_lados > 3:
    if maior_lado < soma_dos_demais_lados:
        print('É possível formar um polígono com os lados fornecidos.')
    else:
        print('Não é possível formar um polígono com os lados fornecidos.')
else:
    print('Não é possível formar um polígono com a quantidade de lados fornecidos.')
    
