"""Módulos e Pacotes"""
# Modularização -> Construir módulos
-> Dividir um programa grande

*Para fazer o acesso entre módulos basta dar um improt. #Ex:
import class22functions
*Chamando a função:
class22functions.fatorial(num)

# Pacotes (Algumas linguagens chamam de bibliotecas)
-> Junção de módulos em uma pasta (Separadas por assuntos)
Pra importar um pacote basta fazer:
import NomeDoPacote

__init__.py  # ---> Esse arquivo sempre deve ser criado dentro de uma pasta

from functions import numbers  ---> numbers é uma pasta, pode-se importar diretamente uma pasta e usar suas funções
