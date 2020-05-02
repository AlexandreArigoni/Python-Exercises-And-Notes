                 """        Dicionários{}          """
dados = dict()
dados = {}
dados = {'nome': 'Pedro', 'idade': 25} --> Python chama esses elementos (ex: 'idade') de 'chaves/keys'
'' são tipo posições
*dados['sexo'] = 'M'  ---> Já acrescenta no final
del dados['idade']  ---> Deleta
print(dados['nome'])
                 """Chamando os valores/chaves/itens"""
print(filme.values()) ---> 25
print(filme.keys())   ---> 'idade'
print(filme.items())  ---> Os dois

#Exemplo de for:
for k,v in filme.items(){   k -> key / v -> value
   print(f'O {k} é {n}')
}
 ...
 print(locadora[0]['ano'])
 print(f'{pessoas["nome"]}{pessoas["idade"]}') ---> usar "" no print formato com ''
 dict_items([('nome', 'Alexandre'), ('sexo', 'M'), ('idade', 18)])---> tuplas dentro de listas 

""" IMPORTANTISSIMO """
.Em dicionários não se pode usar o fatiamento[:] para copiar
Se usa o .copy()   EXEMPLO:
    brasil.append(estado.copy())

#É possível colocar listas dentro de tuplas ou dicionários e etc
#.append não funciona
#É possível ter índices literais, personalizar os índices

""" PRINTANDO EM ORDEM: """
from operator import itemgetter
for k, v in sorted(gamers.items(), key=itemgetter(1), reverse=True):

key=itemgetter(0) ---> key
key=itemgetter(1) ---> value 


for c in tudo:
    if c['age'] > mean/len(tudo):
        print(c['name'])     ---> tudo é uma lista mas mesmo assim pode-se usar c['name'] q acessa o valor desse espaço de memória
