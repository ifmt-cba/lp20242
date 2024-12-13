'''
PROVA PRÁTICA DE PYTHON
Ao término enviar e-mail conforme modelo:
Para: preti.joao@ifmt.edu.br
Assunto: Prova 1 de Laboratório de Programação 2024/2
Mensagem: Coloque seu nome completo na mensagem do e-mail
Anexo: p1.py
'''

#1. Faça um programa que leia o valor unitário de um produto,
#   a quantidade desejada e imprima o valor total a pagar. (2,5pt)
def q1():
    valor = float(input('Valor R$: '))
    qtde = int(input('Qtde: '))
    print(f'Total: R$ {valor * qtde}')

#2. Faça um programa que permita entrar com o nome, a nota da prova 1 e a nota
#   da prova 2 de um aluno. O programa deve imprimir o nome, a nota da prova 1,
#   a nota da prova 2, a média das notas e uma das mensagens: "Aprovado",
#   "Reprovado" ou "em Prova Final"(a média é 7 para aprovação, menor que 3 para
#   reprovação e as demais em prova final). (2,5pt)
def q2():
    nome = input('Nome: ')
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2)/2
    print(nome)
    print(n1)
    print(n2)
    print(media)
    if media >= 7:
        print('Aprovado')
    elif media >= 3:
        print('Em Prova Final')
    else:
        print('Reprovado')

#3. Faça um programa que apresente um menu com 4 opções:
#   [1] - Cadastrar
#   [2] - Excluir
#   [3] - Pesquisar
#   [0] - Sair
#   O usuário deve escolher uma opção e o programa deve imprimir uma mensagem 
#   ao entrar em cada opção do menu. O programa só deve encerrar quando a opção
#   escolhida for zero (0). (2,5pt)
def q3():
    menu = '''
[1] - Cadastrar
[2] - Excluir
[3] - Pesquisar
[0] - Sair

Digite a opção desejada:
    '''
    opcao = -1
    while opcao != 0:
        opcao = int(input(menu))
        match(opcao):
            case 1:
                print('Cadastrando...')
            case 2:
                print('Excluindo...')
            case 3:
                print('Pesquisando...')
            case 0:
                print('Saindo...')
            case _:
                print('Opção Inválida!')

#4. Faça um programa que calcule o retorno de um investimento. (2,5pt)
#   O programa deve solicitar do usuário o:
#   - valor que será investido;
#   - prazo do investimento (meses);
#   - juros mensal (juros composto).'''
def q4():
    valor = float(input('Valor R$: '))
    prazo = int(input('Meses: '))
    juros = float(input('Juros %: '))
    juros = juros/100
    for _ in range(prazo):
        valor += valor*juros
    print(f'Valor final: R$ {valor}')

q4()