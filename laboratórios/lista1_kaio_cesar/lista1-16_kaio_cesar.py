# Programa para ler o sexo e a resposta de 20 entrevistados para saber o numeros de respostas "sim", "não" e o 
# homens que responderam "não"
# Kaio Cesar da Silva Anjos
# data de criação 13/11/2024


# declaração das variáveis
resposta = ''
sexo = ''
contador_sim = 0
contador_nao = 0
contador_homens_não = 0
total = 0


# repetição para coletar as respostas
for i in range(20):
    sexo = input('Digite o sexo ("m" para masculino e "f" para feminino): ')
    print('Digite "s" caso tenha gostado ou "n" caso não tenha gostado ')
    resposta = input('Digite sua resposta: ')
    total += 1    

    # verificação da resposta
    if resposta == 's':
        contador_sim += 1
    
    elif resposta == 'n':
        contador_nao += 1
        if sexo == 'm':
            contador_homens_não += 1


# calculo da porcentagem de homens que responderam não
pct_homens_nao = contador_homens_não / total * 100

print('A quantidade de pessoas que responderam SIM é: ', contador_sim)
print('A quantidade de pessoas que responderam NÂO é: ', contador_nao)
print('A porcentagem de homens que responderam NÃO é: ', pct_homens_nao, '%')

        