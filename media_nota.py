nome = (input('Digite seu nome: '))
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))


media = (n1 + n2) / 2

if media >= 7:
    print(f'{nome}, aprovado com a média {media:.1f}')
else:
    print(f'{nome}, reprovado com a média{media:.1f}')
