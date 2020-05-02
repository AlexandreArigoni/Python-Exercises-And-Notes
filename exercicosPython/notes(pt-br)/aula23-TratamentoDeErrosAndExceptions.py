"""Tratamentos de Erros e Exceções"""
*Existem erros de sintaxe
*O que não é erro sintático chama excessao. #Ex:
print(x) ---> mas a variável x NÃO foi inicializada
*Toda excessão no Python é filho duma classe maior chamada 'Exception'

#Estruturas para lidar com exceções:
try: Operação: *Problemas que normalmente acontecem*
except: Falhou: *Se tentar e falhar acontecerá isso*
---> Podem existir vários excepts, um pra cada situação
else: Deu certo: *O que ocorrerá caso o try dê certo*
finally: Será realizado independete do resultado do try

except Exception as erro:
    print(f'The problem was: {erro.__class__}')
    ---> Demonstrar qual foi o erro

#Lidando com várias except:
except (ValueError, TypeError):
    print('Problems with the type or value')
except ZeroDivisionError:
    print('Problem with 0 division')
except KeyboardInterrupt:
    print('The user need to inform the data')
