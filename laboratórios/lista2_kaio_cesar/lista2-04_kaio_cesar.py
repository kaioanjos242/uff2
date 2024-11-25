# programa para ler um vetor de 30 posições e depois ler um número inteiro x, e imprimir a quantidade de ocorrência do número x no vetor
# kaio cesar da silva anjos
# data de criação 25/11/2024


numeros = [] # armazena os números que serão lidos

# repetição para receber os valores do vetor
for n in range(30):
    num = int(input('digite um número: '))
    numeros.append(num)

# recebe o número que será verificado a quantidade de ocorrências
x = int(input('Digite o número que deseja verificar a quantidade de ocorrências: '))

# conta na lista as ocorrências de acordo com x
ocorrencias = numeros.count(x)
print(ocorrencias)
