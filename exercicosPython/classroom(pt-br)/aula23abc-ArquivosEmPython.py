"""Arquivos em Python"""

#Tentando ler e criando um arquivo de texto:
try:
    a = open(name, 'rt') ---> Tentando abrir um arquivo de texto 'rt': read text
    a.close() ---> Tentando fechar

def createArchive(name):
    try:
        a = open(name, 'wt+')  ---> 'wt': Escreve um arquivo de texto '+': se não existir cria 
        a.close()

#Lendo arquivos de texto:
        print(a.read()) ou print(a.readlines())

#Escrevendo no arquivo de texto:
    a = open(arc, 'at') ---> 'at': append text
