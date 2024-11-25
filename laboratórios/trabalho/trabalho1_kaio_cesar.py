# trabalho 1
# Programa destinado a fazer o cálculo do IMC de um indivíduo, baseando-se em seu peso e altura. Em seguida, pega esses dados e indica através da # tabela para cada determindo sexo e idade em qual dos índicices o resultado se encontra. Os valores estão divididos da seguinte forma para homens # e mulheres acima de 20 anos: abaixo do peso, peso ideal, pré-obesidade, obesidade grau 1, 2 e 3. Já para aqueles abaixo de 20 anos, está 
# dividido entre baixo peso, adequado e sobrepeso.
# Kaio Cesar da Silva Anjos
# data de criação 30/10/2024


# Dados recolhidos do usuário
pessoa = input('Qual seu nome? ')
altura = float(input('Qual a sua altura? (ex: 1.71) '))
peso = float(input('Qual o seu peso? (ex: 86.60) '))
idade = int(input('Qual a sua idade? (ex: 20) '))
imc = 0 # inicializa a variável imc em zero


# verificação se a idade do usuário é maior que 20
# caso seja verdade, calcula o imc de acordo com a tabela
# válida tanto para homens e mulheres.
if idade >= 20:
    imc = peso / (altura ** 2)
    print(pessoa,'seu imc é', imc)
    print('E você se encaixa na categoria: ', end='')
    if imc < 18.5:
        print('Abaixo do peso')
    elif 18.5 <= imc < 25:
        print('Peso ideal')
    elif 25 <= imc < 30:
        print('Pré-obesidade')
    elif 30 <= imc < 35:
        print('Obesidade Grau 1')
    elif 35 <= imc < 40:
        print('Obesidade Grau 2')
    elif imc > 40:
        print('Obesidade Grau 3')
else:
    # se a idade do usuário for menor que 20 é necessário saber se é do sexo
    # masculino ou feminino, pois isso fará diferença no indice em que se
    # encaixará o resultado do cálculo do imc do determinado individuo.
    HomemOuMulher = input('Qual é o seu gênero? (h para homem / m para mulher)')
    if HomemOuMulher == 'h':
        imc = peso / (altura ** 2)
        print(pessoa,'seu imc é', imc)
        print('E você se encaixa na categoria: ', end='')
        if idade == 10:
            if imc < 14.42:
                print('Baixo peso')
            elif 14.42 < imc < 19.60:
                print('Adequado')
            elif imc > 19.60:
                print('sobrepeso')

        elif idade == 11:
            if imc < 14.83:
                print('Baixo peso')
            elif 14.83 < imc < 20.35:
                print('Adequado')
            elif imc > 20.35:
                print('sobrepeso')

        elif idade == 12:
            if imc < 15.24:
                print('Baixo peso')
            elif 15.24 < imc < 21.12:
                print('Adequado')
            elif imc > 21.12:
                print('sobrepeso')

        elif idade == 13:
            if imc < 15.73:
                print('Baixo peso')
            elif 15.73 < imc < 21.93:
                print('Adequado')
            elif imc > 21.93:
                print('sobrepeso')

        elif idade == 14:
            if imc < 16.18:
                print('Baixo peso')
            elif 16.18 < imc < 22.77:
                print('Adequado')
            elif imc > 22.77:
                print('sobrepeso')

        elif idade == 15:
            if imc < 16.59:
                print('Baixo peso')
            elif 16.59 < imc < 23.63:
                print('Adequado')
            elif imc > 23.63:
                print('sobrepeso')

        elif idade == 16:
            if imc < 17.01:
                print('Baixo peso')
            elif 17.01 < imc < 24.45:
                print('Adequado')
            elif imc > 24.45:
                print('sobrepeso')

        elif idade == 17:
            if imc < 17.31:
                print('Baixo peso')
            elif 17.31 < imc < 25.28:
                print('Adequado')
            elif imc > 25.28:
                print('sobrepeso')

        elif idade == 18:
            if imc < 17.54:
                print('Baixo peso')
            elif 17.54 < imc < 25.95:
                print('Adequado')
            elif imc > 25.95:
                print('sobrepeso')

        elif idade == 19:
            if imc < 17.80:
                print('Baixo peso')
            elif 17.80 < imc < 25.95:
                print('Adequado')
            elif imc > 25.95:
                print('sobrepeso')

    elif HomemOuMulher == 'm':
        imc = peso / (altura ** 2)
        print(pessoa,'seu imc é', imc)
        print('E você se encaixa na categoria: ', end='')
        if idade == 10:
            if imc < 14.23:
                print('Baixo peso')
            elif 14.23 < imc < 20.19:
                print('Adequado')
            elif imc > 20.19:
                print('sobrepeso')

        elif idade == 11:
            if imc < 14.60:
                print('Baixo peso')
            elif 14.60 < imc < 21.18:
                print('Adequado')
            elif imc > 21.18:
                print('sobrepeso')

        elif idade == 12:
            if imc < 14.98:
                print('Baixo peso')
            elif 14.98 < imc < 22.17:
                print('Adequado')
            elif imc > 22.17:
                print('sobrepeso')

        elif idade == 13:
            if imc < 15.36:
                print('Baixo peso')
            elif 15.36 < imc < 23.08:
                print('Adequado')
            elif imc > 23.08:
                print('sobrepeso')

        elif idade == 14:
            if imc < 15.67:
                print('Baixo peso')
            elif 15.67 < imc < 23.88:
                print('Adequado')
            elif imc > 23.88:
                print('sobrepeso')

        elif idade == 15:
            if imc < 16.01:
                print('Baixo peso')
            elif 16.01 < imc < 24.29:
                print('Adequado')
            elif imc > 24.29:
                print('sobrepeso')

        elif idade == 16:
            if imc < 16.37:
                print('Baixo peso')
            elif 16.37 < imc < 24.74:
                print('Adequado')
            elif imc > 24.74:
                print('sobrepeso')

        elif idade == 17:
            if imc < 16.59:
                print('Baixo peso')
            elif 16.59 < imc < 25.23:
                print('Adequado')
            elif imc > 25.23:
                print('sobrepeso')

        elif idade == 18:
            if imc < 16.71:
                print('Baixo peso')
            elif 16.71 < imc < 25.56:
                print('Adequado')
            elif imc > 25.56:
                print('sobrepeso')

        elif idade == 19:
            if imc < 16.87:
                print('Baixo peso')
            elif 16.87 < imc < 25.85:
                print('Adequado')
            elif imc > 25.95:
                print('sobrepeso')
