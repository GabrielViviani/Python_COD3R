with open(r'C:\Users\pwnag\OneDrive\Desktop\Cod3r-Python\manipulando_arquivos\pessoas.csv') as arquivo:
    for registro in arquivo:
        print('Nome: {}, Idade: {}'.format(*registro.strip().split(',')))

if arquivo.closed:
    print('Arquivo já foi fechado')