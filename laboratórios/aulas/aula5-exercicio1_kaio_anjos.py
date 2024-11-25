# Programa destinado a verificar se um aluno é calouro ou veterano, logo apos ler a idade de cada um deles,
# verificar a média das idades dos calouros e dos veteranos, o veterano mais velho e o calouro mais velho
# Kaio Cesar da Silva Anjos
# data de criação 04/11/2024

veteranos = 0
calouros = 0
vet_ou_cal = ''
soma_cal = 0
soma_vet = 0
maior_idade_calouro = 0
maior_idade_veterano = 0

# variaveis para armazenar as médias de idade dos veteranos e calouros respectivamente
media_vet = 0
media_cal = 0


# loop para verificar se é calouro ou veterano
while vet_ou_cal != 'x':
    vet_ou_cal = input('Digite c para calouro ou v para veterano: ')

    if vet_ou_cal == 'c' or vet_ou_cal == 'C':
        idadecalouro = int(input('Digite sua idade: '))
        soma_cal += idadecalouro # soma da idade calouros

        # verificação da maior idade dos calouros
        if idadecalouro > maior_idade_calouro:
            maior_idade_calouro = idadecalouro
        calouros += 1
        media_cal = soma_cal / calouros # calculo da média das idades dos calouros

    elif vet_ou_cal == 'v' or vet_ou_cal == 'V':
        idadeveterano = int(input('Digite sua idade: '))
        soma_vet += idadeveterano  # soma da idade veteranos

        # verificação da maior idade dos veteranos
        if idadeveterano > maior_idade_veterano:
            maior_idade_veterano = idadeveterano
        veteranos += 1
        media_vet = soma_vet / veteranos # calculo da média das idades dos veteranos

print('A média de idade dos alunos veteranos é: ', media_vet * 1)
print('A média de idade dos alunos calouros é: ', media_cal * 1)

print('O calouro mais velho é: ', maior_idade_calouro)
print('O veterano mais velho é: ', maior_idade_veterano)