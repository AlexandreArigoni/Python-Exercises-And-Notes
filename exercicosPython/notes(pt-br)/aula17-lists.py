"""LISTAS"""
Adcionar ->

.append -> lanche.append('cookie') adciona item extra no final
.insert -> lanche.insert(0,'hotdog') coloca item na posição e empurra o resto

Apagar ->
del lanche[3]
lanche.pop(3) ---> (Deleta posição 3) Normalmente usado no final sem nenhum parâmetro
lanche.remove('cookie') ---> Deleta pelo nome doq está na posição (primeiro)
if 'pizza' in lanche:
    lanche.remove('pizza')

"""Exemplo da função list"""
valores = list(range(4,11)) lista com posições d 0 - 6 com os valores de 4 - 10
valores = [2,4,7,4,5,6]
valores.sort() ---> Ordena os valores
valores.sort(reverse = True) ---> Ordena os valores ao contrário

#IMPORTANTE:
a = [1, 2, 3, 4]
b = a
b[2] = 8         ---> Muda o A tb pois em python é criada uma ligação entre as listas não uma cópia

b = a[:] # Fatiamento completo -> cria uma cópia
