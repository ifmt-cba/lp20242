'''
Biblioteca com comandos utilitários personalizados
'''

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