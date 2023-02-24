PALAVRAS_PROIBIDAS = {'futebol', 'política', 'religião'}
textos = [
    'João gosta de futebol e política',
    'A praia estava divertida'
]

for texto in textos:
    intersecao = PALAVRAS_PROIBIDAS.intersection(set(texto.lower().split()))
    if intersecao:
        print('Texto possui palavras proibidas:', intersecao)
    else:
        print('texto autorizado:', texto)