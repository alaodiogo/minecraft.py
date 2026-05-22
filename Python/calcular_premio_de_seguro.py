valor_veiculo = float(input())
classe_desconto = input()
procedencia_veiculo = input() #Para saber se o veiculo e nacional ou importado
idade_segurado = int(input())

desconto_tabela = 0
veiculo_nacional = 0.1
veiculo_importado = 0.15

if procedencia_veiculo == 'nacional':
    porcentagem_valor_veiculo = valor_veiculo * veiculo_nacional #Desconto de 10% encima do valor total do veiculo
else:
    porcentagem_valor_veiculo = valor_veiculo * veiculo_importado #Desconto de 15% encima do valor total do veiculo
    
match classe_desconto:
    case 'A':
        desconto_tabela = porcentagem_valor_veiculo * 0.3
    case 'B':
        desconto_tabela = porcentagem_valor_veiculo * 0.2
    case 'C':
        desconto_tabela = porcentagem_valor_veiculo * 0.1
    case 'D':
        desconto_tabela = porcentagem_valor_veiculo * 0.05

if idade_segurado > 24:
    desconto_idade = porcentagem_valor_veiculo * 0.1
    total_a_receber = porcentagem_valor_veiculo - desconto_tabela - desconto_idade
else:
    total_a_receber = porcentagem_valor_veiculo - desconto_tabela
        
print (f"{total_a_receber:.2f}")