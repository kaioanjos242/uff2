# programa para receber um número N do usuário e imprimir os primeiros N números primos que façam parte da série de Fibonacci.
# Kaio Cesar Da Silva Anjos
# data de criação 16/11/2024


n = int(input('Digite um número inteiro: '))
a = 0
b = 1
cont = 0
        

print('Os primeiros ', n, ' números primos da sequência de fibonacci são:')


# Loop para encontrar números primos na sequência de Fibonacci
while cont < n:
    # Verifica se o número atual da sequência é primo
    if a > 1:  # Apenas verifica se for maior que 1
        primo = True
        i = 2
        while i <= int(a**0.5):
            if a % i == 0:
                primo = False
            i += 1
                
        if primo:
            print(a)  # número primo
            cont += 1
            
    # próximo da sequência de Fibonacci
    a, b = b, a + b