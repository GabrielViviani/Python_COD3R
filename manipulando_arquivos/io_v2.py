arquivo = open(r'C:\Users\pwnag\OneDrive\Desktop\Cod3r-Python\manipulando_arquivos\pessoas.csv')
for registro in arquivo:
    print('Nome: {}, Idade: {}'.format(*registro.split(',')))
arquivo.close()