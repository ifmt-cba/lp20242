nome = 'João' # variável global
# Criando o comando ola
def ola(nome): #variável local
    print(f'Olá {nome}! Seja bem vindo(a)!')

print(f'Olá {nome}!')
ola('João')
ola(input('Digite seu nome: '))
