n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))

media = (n1 + n2 + n3) / 3

if media >= 9:
    print(f'Nota {media:.1f} -> Excelente!')
elif media >= 7:
    print(f'Nota {media:.1f} -> Aprovado!')
elif media >= 5:
    print(f'Nota {media:.1f} -> Recuperação!')
else:
    print(f'Nota {media:.1f} -> Reprovado!')