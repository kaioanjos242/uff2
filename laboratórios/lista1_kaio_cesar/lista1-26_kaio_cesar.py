# progrma que recebe os coeficientes a, b, c, e d do usuário e verifica a existencia de uma raiz no intervalo definido. 
# Kaio Cesar Da Silva Anjos
# data de 17/11/2024


# coeficientes
a = float(input('Digite o coeficiente A: '))
b = float(input('Digite o coeficiente B: '))
c = float(input('Digite o coeficiente C: '))
d = float(input('Digite o coeficiente D: '))


# intervalo
minimo = -1000
maximo = 1000


# calcula o valor inicial
anterior = a * minimo**3 + b * minimo**2 + c * minimo + d

raiz = False


# calcula a raiz entre o intervalo estabelecido 
for x in range(minimo + 1, maximo + 1):
    valor = a * x**3 + b * x**2 + c * x + d

    if anterior * valor < 0:
        raiz = True
    
    anterior = valor

# verifica se há a raiz
if raiz:
    print('Existe ao menos uma raiz no intervalo analisado.')
else:
    print('Não existe raiz no intervalo analisado.')

