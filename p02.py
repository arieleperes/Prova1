a = 80000 * 0.03
b = 200000 * 0.15

soma1 = 0
soma2 = 0
lista = []

while a <= b:
    soma1 = a * 1
    soma2 = b * 1
    a += 1
    lista.append(soma1)

    if soma1 >= soma2:
        break

anos = lista.count(soma1)

print(anos)






