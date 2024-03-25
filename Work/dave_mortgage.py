# Dave decidiu fazer uma hipoteca de taxa fixa de 30 anos de US$ 500.000 com a empresa Guido’s Mortgage,
# Stock Investment e Bitcoin Trading Corporation. 
# A taxa de juros é de 5% e o pagamento mensal é de $ 2.684,11.

taxa_anos = 30
montante = 5e5
#print(taxa)
taxa_juros = 5/100
pag_mensal = 2684.11 + 1000
total = 0.0

while montante > 0:
  montante = montante * (1+taxa_juros/12)-pag_mensal
  total = total + pag_mensal
print(total) 
