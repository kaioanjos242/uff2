# Faça um programa que lista o número de indentificação e o peso do boi e escreve número do boi mais pesado e o boi mais magro. além disso mostra se há dois ou mais bois com o mesmo peso.
# Kaio Cesar da Silva Anjos
# data de criação 13/11/2024


bois = 5 
numero_id = ''  # identificação do boi
peso = 0

numero_do_mais_pesado = ''  # armazena a identificação do boi mais pesado
mais_pesado = 0

numero_do_mais_magro = ''  # armazena a identificação do boi mais magro
mais_magro = 10000

# repetição para coletar as informações necessárias
for i in range(bois):
    peso = int(input('Digite o peso do boi: '))
    numero_id = int(input('digite o número de indentificação: '))
    
    # verifica o boi mais pesado
    if peso > mais_pesado:
        mais_pesado = peso
        numero_do_mais_pesado = numero_id

    # verifica o boi mais magro
    if peso < mais_magro:
        mais_magro = peso
        numero_do_mais_magro = numero_id


print('O boi mais pesado é o número',numero_do_mais_pesado, 'pesando: ' , mais_pesado)
print('O boi mais magro é o número',numero_do_mais_magro, 'pesando: ' , mais_magro)

# Supondo que seja digitado dois ou mais pesos iguais, e estes forem maiores que todos os demais, 
# a váriavel mais_pesado que diz respeito ao peso do boi mais pesado não mudára, pois ela armazena apenas um valor
# e uma vez que seja digitado outro valor que seja igual ao anterior, o novo valor será ignorado e 
# permanecerá o valor que já estava atribuido a variável, até que seja digitado um valor maior.
