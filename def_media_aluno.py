def situacao(media):
    if media >= 7:
        return 'Aprovado'
    elif media >= 5:
        return 'Recuperação'
    else:
        return'Reprovado'

aprovados = 0
recuperacao = 0
reprovados = 0
for i in range(5):
    nome = input('Nome do aluno: ')
    nota1 = float(input('Primeira nota do aluno: '))
    nota2 = float(input('Segunda nota do aluno: '))
    media = (nota1 + nota2) /2
    resultado = situacao(media)
    if resultado == 'Aprovado':
        aprovados += 1
    elif resultado == 'Recuperação':
        recuperacao += 1
    elif resultado == 'Reprovado':
        reprovados += 1
    print(f'{nome} - Média: {media:.1f} - {resultado}')

print('Aprovados: ', aprovados)
print('Recuperação: ', recuperacao)
print('Reprovados: ', reprovados)
    