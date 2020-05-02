                          """Funções""" ---> 'Rotina'
#Exemplos de funções que já vem no python:
print() len() input() int() float()
No python 'def' -> definição de função
#Ex de função:
def mostraLinha():
    print('---'*20)
*Python pede 2 linhas vazias entre o def e o resto do código

#É possível alterar os parâmetros dessa forma:
def mensagem(msg):
    print('-=' * 30)
    print(msg)
    print('-=' * 30)
mensagem('No meio dos -=')

#Outro exemplo:
def sumnums(num1, num2):
    print(num1+num2)
sumnums(num2=7, num1=30)  ---> Definindo o num2 no primeiro parâmetro e o num1 no segundo (Trocou a ordem)-> Se for explicitar um deve explicitar o outro

                    """Empacotamento de Parâmetros"""
---> Toda passagem de parâmetros em python é por referência e não por valores (Os parâmetros podem se referir a basicamente qualquer coisa sem precisar se especificar)
                    
def cont(*num): * -> Representa o "desempacotamento" se a pessoa colocar 1 parâmetro jogue para num, se ela colocar 10 jogue para num
  *(Cria tuplas)*
*Logo dá pra fazer tudo que se pode fazer em tuplas!!

