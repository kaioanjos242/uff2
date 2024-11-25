# 1 


# lista = []
# num = 1
# while num != 0:
#     num = int(input('Digite um número inteiro e positivo: '))
#     if num != 0:
#         lista.append(num)
    
#     if len(lista) == 5:
#         print(lista)
#         lista.clear()
#     else:
#         print(lista)


# 2 

listaA = []
listaB = []

numA = 0
numB = 0

while numA != -1:
    numA = int(input('Digite um número ou digite \'-1\' para sair '))
    if numA != -1:
        listaA.append(numA)

print('Lista A', listaA)

while numB != -1:
    numB = int(input('Digite um número ou digite \'-1\' para sair '))
    if numB != -1:
        listaB.append(numB)

print('Lista B', listaB)

soma = listaA + listaB

for i in range(len(soma)):
    if soma[i] > soma[i+1]:
        soma[i], soma[i+1] = soma[i+1], soma[i]
    
print(soma)