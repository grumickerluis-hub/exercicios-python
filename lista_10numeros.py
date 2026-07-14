numeros = []

for i in range(10):
    n = int(input('Digite um número: '))
    numeros.append(n)

q = 0
for j in numeros:
    if j > 10:
        q += 1    

soma = sum(numeros)
total = len(numeros)
media = soma / total
print(f'Soma: {soma}')
print(f'Média: {media:.2f}')
print('Quantiade de números maiores que 10: ', q)
