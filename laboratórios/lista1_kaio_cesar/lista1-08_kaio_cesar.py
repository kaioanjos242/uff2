# programa destinado a apurar os votos de uma eleição ficticia, mostrando
# quantos votos cada candidato recebeu e a quantidade de votos nulos e brancos
# nota: testei o programa com um range de 10, para não precisar digitar 20.000 votos
# kaio cesar da silva anjos
# data de criação 07/11/2024


eleitores = 20000

# variáveis de contagem de votos para cada candidato
joao = 0
jose = 0
maria = 0
pedro = 0
brancos = 0
nulos = 0

# candidatos possíveis
print('Os candidatos são: '
      '1 - João da Silva; '
      '2 - José Ramalho; '
      '3 - Maria Mattos; '
      '4 - Pedro Américo; '
      '0 - Branco; '
      'Qualquer outro número - Nulo')

# loop para receber a quantidade de votos necessários
for i in range(1, eleitores+1):
    voto = int(input('Digite o candidato que deseja votar: '))

    # verificação para qual dos candidatos foi o voto do usuáro
    if voto == 1:
        joao += 1

    elif voto == 2:
        jose += 1

    elif voto == 3:
        maria += 1

    elif voto == 4:
        pedro += 1

    elif voto == 0:
        brancos += 1

    else:
        nulos += 1


print('João da Silva recebeu', joao, 'votos')
print('José recebeu', jose, 'votos')
print('Maria Mattos recebeu', maria, 'votos')
print('Pedro Américo recebeu', pedro, 'votos')
print('O total de votos em branco foi', brancos)
print('O total de votos nulos foi', nulos)
