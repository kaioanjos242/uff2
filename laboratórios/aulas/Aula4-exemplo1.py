# Programa para ler duas notas inseridas pelo usuário e e calcular de acordo com a fórmula da média
# verificando por meio de uma estrutura logica se o resultado é maior que 7 ou não, se for, imprime apenas que o aluno
# foi aprovado
# Kaio Cesar da Silva Anjos
# data de criação: 25/10/2024

# Entrada para que o usuário entre com um número real para a nota da P1
notap1 = float(input('Digite a primeira nota: '))

# Entrada para que o usuário entre com um número real para a nota da P2
notap2 = float(input('Digite a segunda nota: '))

# Variável que calcular a media de acordo com os valores inseridos nas variáveis notap1 e nota2
media = (notap1 + notap2) / 2

# Estrutura condicional para verificar se a a média das notas do aluno é suficiente para a aprovação
if media >= 7:
    print('Aprovado com média', media)