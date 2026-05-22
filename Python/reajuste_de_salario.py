salario_atual = float(input())
salario_minimo = float(input())

quantos_salarios_minimos = salario_atual / salario_minimo
teto = salario_minimo * 20
piso = salario_minimo * 1.5

if quantos_salarios_minimos <= 3:
    novo_salario = salario_atual+(salario_atual*0.2)
elif 3 <= quantos_salarios_minimos <= 5:
    novo_salario = salario_atual+(salario_atual*0.15)
else:
    novo_salario = salario_atual+(salario_atual*0.1)

if novo_salario < piso:
    novo_salario = piso
elif novo_salario > teto:
    novo_salario = teto
    
print (f"{novo_salario:.2f}")