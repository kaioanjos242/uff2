# Programa para ler um número inserido pelo usuário e definir se o mesmo é impar ou par pegando o resto (%) da
# divisão por 2 e verificando se é igual a 0, caso seja, o número é par, caso contrário é impar.
# Kaio Cesar da Silva Anjos
# data de criação: 25/10/2024

# Entrada para o usuário digitar um número inteiro
numero = int(input('Digite um número inteiro: '))

# Estrutura condicional para verificiar se o número passado é impar ou par
if numero % 2 == 0: # o número que quando dividido por 2 dá resto 0 é par
# impressão de um dos possíveis resultados da expressão lógica
    print('O número é par!')
else:
    print('O número é impar!')