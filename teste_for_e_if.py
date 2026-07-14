s = 0
p = 0
for i in range(5):
    n = int(input('Digite um número: '))
    s += n
    if n % 2 == 0:
        p += 1

print(f'Quantidade de pares: {p}')
print(f'Soma total dos números: {s}')

