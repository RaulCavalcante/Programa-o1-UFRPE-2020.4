from operacoes import *
from exibicao import *
from modelos import *

def main():

    #delete aq
    info=['Cadastrar', 'Editar', 'Pesquisar', 'Excluir', 'Mostrar Lista']
    opcoes_principais=['Aluno(a)', 'Prof(a)', 'Monitoria']
    opcoes_secundarias=['Nome','Formação','Monitoria']
    
    
    while True:

        escolha_usuario = menu('Menu', info, False, 6)

        try:

            if escolha_usuario == 1: #Criar
                while True:
                    cadastro_escolha = menu('Menu Cadastro', opcoes_principais, False, 4)
            
                    if cadastro_escolha == 1:      # Cadastra Aluno
                        texto_tipo= opcoes_principais[0]
                        texto_nome= 'Informe seu primeiro nome: '
                        texto_curso='Informe a sigla do seu curso ou matrícula: '
                        monitoria = True
                    
                    elif cadastro_escolha == 2:    # cadastra Professor 
                        texto_tipo= opcoes_principais[1]
                        texto_nome= 'Informe seu primeiro nome: '
                        texto_curso='Informe sua matrícula do curso: '
                        monitoria = True
                    
                    elif cadastro_escolha == 3:    # Cadastra monitoria e adiciona algum professor
                        texto_tipo= opcoes_principais[2]
                        texto_nome= 'Informe o nome da monitoria: '
                        texto_curso= 'Informe a sigla da matéria: '
                        monitoria = False

                    elif cadastro_escolha == 4:    #volta para o menu principal finalizando o programa 
                        break

                    valores_cadastro = valores(texto_tipo, texto_nome, texto_curso, monitoria)
                    cadastro = Pessoa(valores_cadastro[0],valores_cadastro[1],valores_cadastro[2],valores_cadastro[3])
                    criar(cadastro.getTipo(), cadastro.getNome(), cadastro.getFormacao(), cadastro.getMonitoria())
            
            elif escolha_usuario == 2: #Editar
                pass
            elif escolha_usuario == 3: #Pesquisar
                
                while True:
                    
                    escolha_pesquisa = menu('Menu Pesquisa', opcoes_principais, False, 4)
                
                    if 1 <= escolha_pesquisa <= 3:
                        tipo_pesquisa = menu('Menu Pesquisa',opcoes_secundarias,False, 4)
                        pesquisar(opcoes_principais[escolha_pesquisa - 1],tipo_pesquisa)
                    else:
                        os.system('cls||clear')
                        break

            elif escolha_usuario == 4: #Exluir
                deletar()
                
            elif escolha_usuario == 5: #Mostrar Lista  
     
                while True:
                    escolha_lista = menu('Menu Listagem', opcoes_principais, False, 4)
                
                    if 1 <= escolha_lista <= 3:
                        listar(opcoes_principais[escolha_lista - 1])
                    else:
                        os.system('cls||clear')
                        break

            elif escolha_usuario == 6:
                os.system('cls||clear')
                print('---/---/---/---/---/---/---/---/---/---/---/---/')
                print("              Programa Finalizado               ")
                print('---/---/---/---/---/---/---/---/----/----/----/')
                break

        except ValueError:
            escolha_usuario = erro(escolha_usuario, 5)  

            #menu('Menu Inicial', info, False, 6)