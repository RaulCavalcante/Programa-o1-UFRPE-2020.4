'''
Escreva um programa que imprime um padrão na tela. O programa deve receber um valor inteiro 'n',
que determina o número de colunas e linhas que o padrão terá.

Entrada: 5          Saida:000
                          X00
                          XX0
                          XXX
'''

x = int(input())
y = 0
lista = []
for i in range(x):
    lista.append(0)     #Adiciona um intem a lista
for i in range(x+1):
    for i in lista[0:x]:    #Ira printa a lista ate a posição desejada
        print(i,end="")
    print()
    lista.insert(y,"X")     #Caso quise-se excluir os itens a mais da lista teria que inseir elementos vazio [] na posição dele
    y += 1
    
    

    
