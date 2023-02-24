import csv

with open(r'C:\Users\pwnag\OneDrive\Desktop\Cod3r-Python\manipulando_arquivos\pessoas.csv') as entrada:
    for pessoa in csv.reader(entrada):
        print('Nome: {}, Idade: {}'.format(*pessoa))