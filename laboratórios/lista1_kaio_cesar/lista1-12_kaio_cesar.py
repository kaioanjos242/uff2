# programa para calcular a área de um triangulo sendo fornecidos pelo usuário 
# Kaio cesar da silva anjos
# data de criação 10/11/2024

lado1 = 0
lado2 = 0
lado3 = 0


# loops para garantir que o usuário digite um valor válido
while lado1 <= 0:
    lado1 = float(input('Digite o valor do lado 1 do triângulo: '))

while lado2 <= 0:
    lado2 = float(input('Digite o valor do lado 2 do triângulo: ')) 

while lado3 <= 0:
    lado3 = float(input('Digite o valor do lado 3 do triângulo: '))


# calculando a área do triangulo pela fórmula de Herão, onde são conhecidos os lados

# s = semiperimetro
s = (lado1 + lado2 + lado3) / 2

# multiplicação dos valores 
multi = s * (s - lado1) * (s - lado2) * (s - lado3)

# area do triangulo
a = (s * (s - lado1) * (s - lado2) * (s - lado3)) ** 0.5

print(multi)
print('A área do triângulo é: ', a)


