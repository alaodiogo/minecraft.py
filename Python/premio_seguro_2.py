valor_veiculo = float(input())
sexo_cliente = input()
idade_cliente = int(input())

adicional_valor_veiculo = valor_veiculo * (10/100)

if idade_cliente <= 24 and sexo_cliente == 'F':
    adicional_tabela = adicional_valor_veiculo * (5/100)
elif 25 <= idade_cliente <= 33 and sexo_cliente == 'F':
    adicional_tabela = adicional_valor_veiculo * (20/100)
elif sexo_cliente == 'F':
    adicional_tabela = adicional_valor_veiculo * (35/100)
elif 25 <= idade_cliente <= 33 and sexo_cliente == 'M':
    adicional_tabela = adicional_valor_veiculo * (10/100)
elif idade_cliente >= 33 and sexo_cliente == 'M':
    adicional_tabela = adicional_valor_veiculo * (20/100)
else:
    adicional_tabela = 0
    
total_a_pagar = adicional_valor_veiculo - adicional_tabela
        
print (total_a_pagar)
