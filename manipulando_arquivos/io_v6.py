with open(r'C:\Users\pwnag\OneDrive\Desktop\Cod3r-Python\manipulando_arquivos\pessoas.csv') as arquivo:
    with open(r'C:\Users\pwnag\OneDrive\Desktop\Cod3r-Python\manipulando_arquivos\pessoas.txt', 'w') as saida:
        for registro in arquivo:
            pessoa = registro.strip().split(',')
            print('Nome: {}, Idade: {}'.format(*pessoa), file = saida)

if arquivo.closed:
    print('Arquivo já foi fechado')

if saida.closed:
    print('Arquivo de saída já foi fechado')