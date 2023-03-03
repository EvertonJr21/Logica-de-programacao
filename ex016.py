'''Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.

Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.

Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.'''


cob_tinta = 3
tam_lata = 18 
preco_lata = 80

tam_metros = float(input('Qual o tamanho em metros quadradas da área a ser pintada? '))

litros = tam_metros / cob_tinta
latas_inteiras = int(litros/tam_lata)
if(litros % tam_lata !=0 ):
    latas_inteiras += 1
    
valor_total = latas_inteiras * preco_lata

print(f'É necessário {litros:.2f} litros de tinta')
print(f'É necessário {latas_inteiras} de latas de tintas ')
print(f'O preço total foi de R${valor_total}')

