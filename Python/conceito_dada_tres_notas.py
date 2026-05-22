nota_1 = float(input())
nota_2 = float(input())
nota_3 = float(input())

media = (nota_1 + nota_2 + nota_3) / 3

if 9.0 <= media <= 10.0:
    print ("Ótimo")
elif 7.5 <= media <= 9.0:
    print ("Bom")
elif 6.0 <= media <= 7.5:
    print ("Satisfatório")
else:
    print ("Insuficiente")