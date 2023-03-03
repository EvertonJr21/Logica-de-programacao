#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês
#Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê: salário bruto. quanto pagou ao INSS. quanto pagou ao sindicato. o salário líquido. calcule os descontos e o salário líquido, conforme a tabela abaixo:
#+ Salário Bruto : R$
#- IR (11%) : R$
#- INSS (8%) : R$
#- Sindicato ( 5%) : R$
#= Salário Liquido : R$

sal_hr = float(input('Quanto você ganha por hora trabalhada? '))
hr_trab = int(input('Quantas horas você trabalha no mês? '))
sal_bruto = sal_hr * hr_trab
print(f'Seu salário bruto é de: R${sal_bruto:.2f}')
ir = sal_bruto * 0.11 
print(f'Você está pagando R${ir:.2f} de imposto de renda')
inss = sal_bruto * 0.08
print(f'Você está pagando R${inss:.2f} de INSS')
sindicato = sal_bruto * 0.05
print(f'Você está pagando RS${sindicato:.2f} de sindicato')
sal_liquido = sal_bruto - ir - inss - sindicato
print(f'Seu salário depois dos descontos é de: R${sal_liquido:.2f}')