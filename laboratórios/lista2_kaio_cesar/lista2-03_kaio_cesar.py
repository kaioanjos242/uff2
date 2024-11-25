# programa para ler um frase e imprimir a quantidade de vogais, de espaços em branco e todo o restante.
# kaio cesar da silva anjos
# data de criação 25/11/2024

frase = input('Digite uma frase: ')
frase_min = frase.lower() # transforma todos os caracteres em minusculo para facilitar 


# conta a ocorrência de cada uma das vogais dentro da frase
a = frase_min.count('a')
e = frase_min.count('e')
i = frase_min.count('i')
o = frase_min.count('o')
u = frase_min.count('u')


# conta a ocorrência de espaços em branco
brancos = frase_min.count(' ')


# conta a ocorrencia de tudo
separado = [i for i in frase_min]
total = len(separado)
print(total)

# conta quantidade de caracateres do resto, ou seja, não considerando os espaços em brancos e vogais 
resto = total - a - e - i - o - u - brancos

print(f'A frase tem {a + e + i + o + u} letras vogais')
print(f'A frase tem {brancos} espaços em branco.')
print(f'A quantidade do restante é: {resto}')