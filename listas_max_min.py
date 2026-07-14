numeros = []

for i in range(5):
    n = int(input('Digite um número: '))
    numeros.append(n)

maior_numero = max(numeros)
menor_numero = min(numeros)

for j in numeros:
    print(j)

print('Maior número:', maior_numero)
print('Menor número:', menor_numero)