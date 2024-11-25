# Programa destinado a ler os valores de temperaturas em celsius armazenados em uma determinada lista e converter os valores para fahrenheit
# e calcular a média das temperaturas em celsius e fahrenheit e depois imprimir as temperaturas que ficaram acima da média em fahrenheit
# kaio cesar da silva anjos
# data de criação 25/11/24

temperaturas_em_celsius = [] # lista para armazenar as temperaturas em celsius
temperaturas_em_fahrenheit = [] # lista para armazenar as temperaturas em fahrenheit 
soma_t_em_c = 0
soma_t_em_f = 0


# repetição para que o usuário entre com as temperaturas que serão convertidas
for i in range(50):
    temp = int(input('digite uma temperatura em graus celsius: '))
    soma_t_em_c += temp
    temperaturas_em_celsius.append(temp)


# repetição que pega as temperaturas recebidas em celsius e transforma em fahrenheit
for t in temperaturas_em_celsius:
    conv = t * 1.8 + 32
    soma_t_em_f += conv
    temperaturas_em_fahrenheit.append(conv)


# média das temperaturas em celsius
media_t_em_c = soma_t_em_c / len(temperaturas_em_celsius)
print('A média das temperaturas em celsius é:', media_t_em_c)


# média das temperaturas em fahrenheit
media_t_em_f = soma_t_em_f / len(temperaturas_em_fahrenheit) 
print('A média das temperaturas em fahrenheit é:', media_t_em_f)


# verificando temperaturas acima da média em fahrenheit  
temp_acima_da_media = []
for x in temperaturas_em_fahrenheit:
    if x > media_t_em_f:
        temp_acima_da_media.append(x)

print('A quantidade de temperaturas em fahrenheit acima da média das temperaturas em fahrenheit é:', len(temp_acima_da_media), 'e são elas: ', temp_acima_da_media)
