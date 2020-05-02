pessoas.append(dados[:])  --> Lista dentro da lista [:] = cópia
# Outro exemplo criando tudo em uma lista:
pessoas = [['Alexandre', 18], ['Rodrigo', 10], ['Henrique', 10]]
print(pessoas[0][0]) ---> Alexandre
print(pessoas[1]) ---> ['Rodrigo', 10]

pessoa.append(lista[:])
lista.clear() --> Deleta a lista, resetando seus dados para usar depois
