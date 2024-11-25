# programa para receber do usuário as taxas de juros (r), o valor das parcelas (pmt), o número de parcelas (n) e calcular 
# o valor do financiamento.
# Kaio Cesar Da Silva Anjos
# data de criação 16/11/24

r_pct = float(input('Digite a taxa de juros em porcentagem: '))  # taxa de juros em porcentagem
pmt = float(input('Digite o valor das parcelas: ')) 
n = int(input('Digite o número de parcelas: ')) 
somatorio = 0

r = r_pct / 100 # transformando a taxa de juros de porcentagem para um número real

# cálculo do financiamento, através do somatório das parcelas
for num in range(1, n+1):
    div = pmt / ((1 + r)**num)
    somatorio += div

print('O valor do financiamento é: ', somatorio)