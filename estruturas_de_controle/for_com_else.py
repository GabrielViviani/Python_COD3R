PALAVRAS_PROIBIDAS = ('futebol', 'política', 'religião')

textos = [
    'João gosta de futebol e política',
    'A praia estava divertida'
]

for texto in textos:
    for palavra in texto.lower().split():
        if palavra in PALAVRAS_PROIBIDAS:
            print('Texto possui ao menos uma palavra proibida:',palavra)
            found = True
            break
    else:
        print('Texto autorizado',texto)