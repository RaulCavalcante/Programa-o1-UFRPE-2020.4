'''
def create(tipo,nome,formacao, monitor):#tipo, nome, campo/formacao, monitores
#criar aluno(participar de monitoria), professor(participar de uma disciplina) e disciplina(adicionar monitor)
'''
from exibicao import *

def validar(tipo_pesquisa,ordem):#qual o valor de pesquisa e qual é a ordem cadastrada
    try:
        valores=[]
        file = open('dados.txt', 'r+')
        file.seek(0,0)
        
        for linha in file:
            linha_separa = linha.split('/')
            if tipo_pesquisa == linha_separa[ordem]:#se aquela tipo especificado esta cadastrado
                valores.append(linha)

        return valores

    except FileNotFoundError or ValueError or IndexError:    
        print("nenhum valor encontrado")


def criar(tipo, nome, formacao, monitor):
 
    #verificar se o nome e campo ja existe(search)
    dados = '{}/{}/{}/{}\n'.format(tipo ,nome ,formacao,monitor)

    nome_existe = validar(nome,1)#verificar se o nome ja é cadastrado
    if nome_existe and dados in nome_existe: #Se esse valor guardado é igual a outro

        print("Esse Valor já esta cadastrado")

    else:

        with open('dados.txt', 'a+') as file:
            file.write(dados)
            file.close()
        print('\nCadastro Feito Com Sucesso!')


def valores(texto_tipo, texto_nome, texto_curso, monitor):#monitor define se não é valores da monitoria para cadastro
    tipo= texto_tipo

    while True:
        nome = str(input(texto_nome)).lower().capitalize()
        formacao = str(input(texto_curso)).lower().capitalize()

        if nome != '' and formacao != '': 
            break
        else:
            print('Você não pode guarda a informação vazia')

    if monitor:
        monitorias = validar('Monitoria', 0)
                
        if not monitorias:
            print("Nenhuma monitoria encontrada para cadastro")
            monitoria = "Sem Cadastro"
        else:
            monitoria = menu('Deseja participar de alguma monitoria ?',['Sim', 'Não'], True, 3)
            if monitoria == 1:
                monitor = menu("Digite o numero da monitoria", monitorias, True, len(monitorias) + 1)
                monitoria = monitorias[monitor - 1]

            else:   
                monitoria = "Sem Cadastro"
    else:
       # professores = validar("Prof(a)", 0)
        monitoria = "Sem Professor"
    
    return tipo,nome,formacao,monitoria


def listar(tipo_pesquisa):
    
    valores= validar(tipo_pesquisa, 0)
    
    if valores:
        print(tipo_pesquisa,'             - Nome  -             Cadastro')
        print('----------------------------------------------------')
        for valor in valores:
            organizado = valor.split('/')
            print(organizado[1], ' \t \t \t', organizado[2], ' \t \t \t', organizado[3])
    else:    
        print("Ainda não há cadastros")


def pesquisar(tipo_pesquisa,objetivo_pesquisa):
    nome = ''
    formacao = ''
    monitoria = ''

    valores= validar(tipo_pesquisa, 0)

    if objetivo_pesquisa == 1:
        nome = str(input('Nome:').lower().capitalize())
    elif objetivo_pesquisa == 2:
        formacao = str(input('Formação:').lower().capitalize())
    else:
        monitoria = str(input('Monitoria:').lower().capitalize())
    
    
    if valores:
        for valor in valores:
            organizado = valor.split('/')
            if organizado[1] == nome or organizado[2] == formacao or organizado[3] == monitoria:
                print(organizado[1], ' \t \t \t', organizado[2], ' \t \t \t', organizado[3])
    else:    
        print("Ainda não há cadastros")

def deletar(tipo_pesquisa,objetivo_pesquisa):
    nome = ''
    monitoria = ''

    valores= validar(tipo_pesquisa, 0)

    if objetivo_pesquisa == 1:
        nome = str(input('Nome:').lower().capitalize())
    else:
        monitoria = str(input('Monitoria:').lower().capitalize())
        
    if valores:
        for valor in valores:
            organizado = valor.split('/')
            if organizado[1] == nome or organizado[3] == monitoria:
                print(organizado[1], ' \t \t \t', organizado[2], ' \t \t \t', organizado[3])
    else:    
        print("Ainda não há cadastros")
    