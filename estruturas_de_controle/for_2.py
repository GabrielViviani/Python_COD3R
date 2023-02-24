palavra = 'paralelepipedo'
for letra in palavra:
    print(letra)

lista = ['gabriel', 'laura', 'ian', 'bia', 'gabigui']
for nome in lista:
    print(nome)

for posicao, nome in enumerate(lista):
    print(f'{posicao + 1})', nome)

dias_semana = ('Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado')
for dia in dias_semana:
    print(f'hoje é {dia}')

for numero in {1, 2, 3, 4, 5, 6}:
    print(numero)