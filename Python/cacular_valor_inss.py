salario_bruto = float(input())

if salario_bruto <= 720:
    desconto_inss = salario_bruto*(7.65/100)
elif salario_bruto <= 1200:
    desconto_inss = salario_bruto*(9/100)
elif salario_bruto <= 2400:
    desconto_inss = salario_bruto*(11/100)
else:
    desconto_inss = 2400*(11/100)
    
print (f"{desconto_inss:.2f}")