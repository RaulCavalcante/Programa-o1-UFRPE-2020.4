'''
Dada uma string fornecida como entrada composta de uma sequência ordenada (ou seja, sempre o '1' virá depois dos '0's) de '0's e '1's, escreva um programa que imprima na tela o índice do primeiro '1' observado na sequência.

caso não encontre nenhum '1' na sequência, imprima '-1'

Entrada:                Saida
000001111               5
'''

entrada = input().strip()
i = 0
nao_Tem = True
while i < len(entrada) :
    if entrada[i] == "1":
        print(i)
        nao_Tem = False
        break
    i += 1
if nao_Tem:
    print("-1") 