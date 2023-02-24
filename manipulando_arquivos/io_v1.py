arquivo = open(r'C:\Users\pwnag\OneDrive\Desktop\Cod3r-Python\manipulando_arquivos\pessoas.csv')
dados = arquivo.read()
arquivo.close()
for registro in dados.splitlines():
    print('Nome: {}, Idade: {}'.format(*registro.split(',')))