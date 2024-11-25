# programa para ler a idade, o sexo e o salário e calcular a média salarial, e o maior salário.
# kaio cesar da silva anjos
# data de criação 07/11/2024

cont_mulheres = 0 # conta quantas mulheres
cont_homens = 0 # conta quantos homens
homem_ou_mulher = ''
soma_s_m = 0 # soma do salário das mulheres
soma_s_h = 0 # soma do salário dos homens
idade =  1  # inicializando idade em 1 para que o loop funcione
maior_s_abaixo_30 = 0 # maior salário até 30 anos



while idade > 0:
    idade = int(input('digite a idade ou digite um número negativo para sair: '))
    if idade > 0:
        homem_ou_mulher = input('digite "m" para mulher e "h" para homen: ')
        salario = float(input('digite o salário: '))

        if homem_ou_mulher == 'm':
            cont_mulheres += 1
            soma_s_m += salario

        elif homem_ou_mulher == 'h':
            cont_homens += 1
            soma_s_h += salario

        if idade < 30:
            if salario > maior_s_abaixo_30:
                maior_s_abaixo_30 = salario

    idade = int(input('digite a idade ou digite um número negativo para sair: '))


if cont_homens > 0:
    media_s_homens = soma_s_h / cont_homens  # média dos salários dos homens
    print('A média salarial dos homens é: ', media_s_homens)

if cont_mulheres > 0:
    media_s_mulheres = soma_s_m / cont_mulheres  # média dos salários das mulheres
    print('A média salarial das mulheres é: ', media_s_mulheres)

if maior_s_abaixo_30 > 0:
    print('O maior salário entre as pessoas abaixo dos 30 anos é: ', maior_s_abaixo_30)
