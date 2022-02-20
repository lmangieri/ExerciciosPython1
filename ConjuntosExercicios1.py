def exerc1():
    print('Informe Nome, CPF e Idade')
    nome = input()
    cpf = input()
    idade = input()

    print('Confirmação de cadastro:')
    print(f'Nome:{nome}')
    print(f'CPF:{cpf}')
    print(f'Idade:{idade}')

def exerc2():
    string = 'Umxpratoxdextrigoxparaxtrêsxtigresxtristes'
    print(string.replace('x',' '))

def exerc3Func(x,y):
    print(f'Soma: {x} + {y} = {(x+y)}')
    print(f'Diferença: {x} - {y} = {(x - y)}')

def exerc3():
    print('Informe X')
    x = int(input())
    print('Informe Y')
    y = int(input())
    exerc3Func(x,y)

def exerc4Func(idade):
    if idade <= 1964:
        print('Baby Boomer')
    elif idade <= 1979:
        print('Geração X')
    elif idade <= 1994:
        print('Geração Y')
    else:
        print('Geração Z')

def exerc4():
    print('Informe uma idade')
    idade = int(input())
    exerc4Func(idade)

#exerc1()
#exerc2()
#exerc3()
#exerc4()