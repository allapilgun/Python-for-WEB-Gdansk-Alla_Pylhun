f = open('zadanie_4_triangle_big.txt', 'r')
suma = 0

for line in f:
    lines = line.split()
    try:
        suma += int(max(lines))
    except ValueError:
        pass

f.close()

print("Największa suma elementów w trójkącie: {}".format(suma))
