'''
Biblioteca com comandos utilitários personalizados
'''

# pip install getpass4
from getpass4 import getpass

def input_int(mensagem):
    while True:
        try:
            inteiro = int(input(mensagem))
        except ValueError:
            print('Valor digitado não é um inteiro! Digite novamente.')
        except:
            print('Ocorreu um erro! Tente novamente.')
        else:
            return inteiro

def input_float(mensagem):
    while True:
        try:
            real = float(input(mensagem))
        except ValueError:
            print('Valor digitado não é um número real! Digite novamente.')
        except:
            print('Ocorreu um erro! Tente novamente.')
        else:
            return real

def input_senha(mensagem):
    senha = ''
    while len(senha) < 6:
        senha = getpass(mensagem)
        if len(senha) < 6:
            print('A senha deve ter pelo menos 6 caracteres!')
        else:
            return senha
