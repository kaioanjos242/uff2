# Faça um programa que leia um número inteiro x e calcule o fatorial de x.

x = int(input('Digite um valor: '))
for i in range(x+1, 1, -1):
    num = i - 1
    soma = num + (num - 1)
    print(f"Resultado da soma de {num} = {soma}")
    resultado = soma + (soma - 1)
    print(resultado)