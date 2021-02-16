import os


def menu(nome_menu, opcoes_menu,cadastro_extra, limite_op):

    print()
    print('-------------------------------')
    print('           ',nome_menu)
    print('-------------------------------')

    x=0
    for opcao in opcoes_menu:
        
        x+=1
        if cadastro_extra:
            print( x ,' -> ', opcao)
        else:

            print( x ,' -> ', nome_menu , ' de ', opcao)
    print(x + 1 , ' ->  Finalizar Menu',nome_menu)

    valor_retorno = int(input("Digite a opção desejada: "))
    valor_retorno = erro(valor_retorno, limite_op)

    os.system('cls||clear')

    return valor_retorno

def erro(valor_digitado,limite):
    while valor_digitado > limite or valor_digitado <= 0 or valor_digitado == '':
        print('---/---/---/---/---/---/---/---/---/---/---/---/')
        print("Valor escolhido encorreto, digite novamente")
        print('---/---/---/---/---/---/---/---/----/----/----/')
        valor_digitado = int(input("Digite a opção desejada: "))

        if (valor_digitado == limite):
            break

    os.system('cls||clear')

    return valor_digitado

