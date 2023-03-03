reg_pesca = 50
multa_por_quilo = 4
peso_peixe = float(input('Indique quantos pesos há no momento: '))
if peso_peixe > reg_pesca:
    excesso = peso_peixe - reg_pesca
    multa = excesso * multa_por_quilo
    print(f'Está pesando {peso_peixe:.0f}Kg. Será multado em {multa:.2f}R$ pelo excesso de {excesso:.0f}Kg ')
else:
    print(f'Está pesando {peso_peixe:.0f}Kg. Você não excedeu o limite definido, Não será multado. ')   