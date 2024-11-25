"""1 saber se um determinado ano é bisexto"""

# ano = int(input('Digite um ano: '))
#
# if ano % 4 == 0:
#     if ano % 100 == 0:
#         if ano % 400 == 0:
#             print(f'O ano {ano} é bissexto')
#         else:
#             print(f'O ano {ano} não é bissexto')
#     else:
#         print(f'O ano {ano} é bissexto')
# else:
#     print(f'o ano {ano} não é bissexto')


# '''2) Construa um algoritmo que receba do usuário dois números inteiros A e B. Em
# seguida, o programa deve informar se A é múltiplo de B ou não. Faça uma segunda
# versão desse exercício no qual o programa deve informar se o maior valor digitado é
# múltiplo do menor valor.'''
#
# A = int(input('Digite o valor de A: '))
# B = int(input('Digite o valor de B: '))
#
# if A % B == 0:
#     print(f'{A} é um multiplo de {B}')
# else:
#     print(f'{A} não é um multiplo de {B}')

"""Em uma determinada faculdade, a médias dos alunos é calculada a partir de 3 notas,
sendo que a menor das 3 é descartada. Faça um programa que peça ao aluno suas
duas primeiras notas e informe quanto ele precisa tirar na 3ª prova para passar. Se o
aluno já possuir média suficiente (nota 6 ou superior) com as duas primeiras notas, o
programa deve informar que ele não precisa realizar a última prova."""

#algoritmo_notas
nota_necessaria = 6
nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))
nota3 = 0
notafinal = 0

# if (nota1 + nota2 / 2) < 6:
#     print(f'Você precisa ralizar a última prova!')

    # nova = int(input("Digite a terceira nota: "))
    # nota3 = nova
    # if nota1 > nota2 > nota3:
    #     notafinal = (nota1 + nota2) / 2
    # elif nota1 > nota2 < nota3:
    #     notafinal = (nota1 + nota3) / 2
    # elif nota1 < nota2 < nota3:
    #     notafinal = (nota2 + nota3) / 2
    #
    # if notafinal >= 6:
    #     print("APROVADO!")
    # else:
    #     print("REPROVADO!")
# else:
#     print('Você está aprovado')

