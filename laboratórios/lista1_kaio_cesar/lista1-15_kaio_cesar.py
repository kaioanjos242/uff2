# Programa destinado a ler a altura das idades das moças inscritas em um concurso de beleza e imprimir as duas maiores alturas.
# Kaio Cesar da Silva Anjos
# data de criação 13/11/2024


# declaração das variáveis
nome = ''
altura = 0
maior_altura = 0
segunda_maior_altura = 0
soma = 0 
contador_maior_altura = 0 
contador_segunda_maior_altura = 0 


# repetição para receber os dados das candidatas
while nome != 'maria':
    nome = input('Digite o nome ou digite maria para sair: ')
    altura = float(input('Digite a altura: '))

    # verifica a maior altura e quantas candidatas as possuem
    if altura > maior_altura:
        segunda_maior_altura = maior_altura
        contador_segunda_maior_altura = contador_maior_altura
        maior_altura = altura
        contador_maior_altura = 1
    elif altura == maior_altura:
        contador_maior_altura += 1
    elif altura > segunda_maior_altura:
        segunda_maior_altura = altura
        contador_segunda_maior_altura = 1
    elif altura == segunda_maior_altura:
        contador_segunda_maior_altura += 1


# soma de todas as candidatas que possuem a maior e a segunda maior altura
soma = contador_maior_altura + contador_segunda_maior_altura    
    
print('Maior altura é: ', maior_altura)
print('A segunda maior altura é: ', segunda_maior_altura)
print('E quantidade de moças com essas alturas é: ', soma)
