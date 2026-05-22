lado_1 = int(input())
lado_2 = int(input())
lado_3 = int(input())

if lado_1 == lado_2 == lado_3:
    print ("equilátero")
elif lado_1 != lado_2 and lado_2 != lado_3 and \
     lado_3 != lado_1:
    print ("escaleno")
else:
    print ("isósceles")