def media(lista):
    
    return sum(lista) / len(lista)

numeros = []

for i in range(5):
    n = int(input('Digite um número: '))
    numeros.append(n)

resultado = media(numeros)
print('Media: ', resultado)


