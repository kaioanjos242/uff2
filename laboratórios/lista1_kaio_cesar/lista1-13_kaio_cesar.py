# programa destinado a ler a idade de varios indivíduos e escreva a média de idade desse grupo e a porcentagem de pessoas entre 21 e 65 anos.
# Kaio Cesar da Silva Anjos
# 13/11/2024

idade = 1
adultos = 0
contador = 0
soma = 0


# loop para coletar os números 
while idade > 0:
    idade = int(input('Digite um valor para idade: '))
    
    # verifica se a idade é maior que 0
    if idade > 0:
        contador += 1
        soma += idade

        # verifica se é adulto
        if 21 <= idade <= 65:
            adultos += 1
    
# verifica se há valores para tirar a média e a porcentagem    
if adultos > 0:
    porcentagem_de_adultos = adultos / contador * 100
if contador > 0:
    media_idade = soma / contador

print('A media das idades é: ', media_idade)
print('A porcentagem de pessoas entre 21 e 65 é: ', porcentagem_de_adultos, '%')
    

