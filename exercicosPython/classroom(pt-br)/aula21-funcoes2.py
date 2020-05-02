"""Interactive Help"""
#Função/método help:
python console -> help()
help() -> Obtém uma ajuda interativa
Depois é só digitar o nome da função/biblioteca desejada etc.
*quit -> sai

#Ou no próprio programa:
help(print)

#Ou imprimir o doc interno dentro de um comando. Ex:
print(input.__doc__)

"""DOCSTRINGS"""
-> String de documentação
help(input) -> Mostra a docstring do comando input
*Ao criar uma doc string para um comando def criado, ela entra na linha abaixo dele
*Basta usar """""" para definir a docstring. #Ex:

def counter(i, f, p):
    """
    -> make a counter and show in the screen
    :param i: Start
    :param f: End
    :param p: Steps
    :return: No return
    """

"""PARÂMETROS OPCIONAIS"""
def somar(a, b, c=0):  ---> Caso o C não seja chamado ele se iniciará com 0 (O C é o parâmetro oficial)

"""ESCOPO DE VARIÁVEL"""
*Escopo -> Local onde variável irá existir e local onde a variável não irá existir
*Existe escopo local e escopo global
*Existem escopos de chamada de biblioteca

#Para alterar uma variável global dentro de um espaço local que tenha nome igual a uma variável local use a palabra global:
def teste(b):  
    global a     ---> Alterará o a=1 que é global
    a = 9

a = 1

"""Retorno de valores"""
#Extra random:
if par(num):  ---> Pode-se fazer isso, pois o if funciona com sentenças True e False
    ...





*g = int(g) --> Usa-se isso pra forçar uma variável g que não seja int a ser int


