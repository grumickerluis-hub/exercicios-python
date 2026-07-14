n = int(input('Digite um valor: '))

for i in range(1, 11):
    print(f'{n} x {i} = {n * i}')

for j in range(2, 21, 2):
    print(j)
s = 0
for k in range(1, n + 1):
    s += k
print(s)