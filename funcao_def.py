def maior(a, b):
    if a >= b:
        return a
    else:
        return b

x = int(input('Digite um número: '))
y = int(input('Digite outro número: '))

print(maior(x, y))