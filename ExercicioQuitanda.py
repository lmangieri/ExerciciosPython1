import os

clear = lambda: os.system('cls')

opcoesQuitanda = [(1,'Banana',3.5),(2,'Melancia',7.5),(3,'Morango',5.0)]
carrinho = {}

def getFruitName(opc):
    for item in opcoesQuitanda:
        if item[0] == opc:
            return item[1]
    return 'Invalido'

def getFruitPrice(opc):
    for item in opcoesQuitanda:
        if item[0] == opc:
            return item[2]
    return 0.0


def addCarrinho(opc):
    if opc in carrinho.keys():
        carrinho[opc] += 1
    else:
        carrinho[opc] = 1
    print(f'{getFruitName(opc)} adicionada com sucesso!')
    print('Digite algo para continuar')
    c = input()

def verCesta():
    clear()
    for key in carrinho:
        print(f'O carrinho tem {getFruitName(key)} {carrinho[key]} itens')
    print('Digite algo para continuar')
    c = input()

def menuDeFrutas():
    while True:
        clear()
        print('------------------')
        print('Menu de frutas:\n')
        print('Escolha fruta desejada:')
        for obj in opcoesQuitanda:
            print(f'{obj[0]} - {obj[1]}')
        print('Digite a opção desejada:')
        try:
            opc = int(input())
            if (opc-1) not in range(len(opcoesQuitanda)):
                print('Esta Opcao é inválida')
            addCarrinho(opc)
            break
        except ValueError:
            print('Esta Opção não é um número')

def checkOut():
    clear()
    tot = 0.0
    listaCompras = ''
    for key in carrinho:
        quantidadeItens = carrinho[key]
        tot = tot + (quantidadeItens * getFruitPrice(key))
        if(listaCompras == ''):
            listaCompras = listaCompras + getFruitName(key)
        else:
            listaCompras = listaCompras + ', ' + getFruitName(key)
    print(f'Total de compras: {tot}')
    print('Cesta de compras: '+listaCompras)
    print('Digite algo para continuar')
    c = input()

while True:
    clear()
    print('------------------')
    print('Quitanda\n')
    print('1: Ver cesta')
    print('2: Adicionar Frutas')
    print('3: Checkout\n')
    print('4: Sair\n')
    print('Digite a opção desejada:')
    try:
        opc = int(input())
        if (opc-1) not in range(4):
            print('Esta Opcao é inválida')
        if opc == 1:
            verCesta()
        elif opc == 2:
            menuDeFrutas()
        elif opc == 3:
            checkOut()
        elif opc == 4:
            exit(1)
    except ValueError:
        print('Esta Opção não é um número')

