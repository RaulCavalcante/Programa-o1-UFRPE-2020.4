'''
Dado um array e um número k, onde k é menor que o tamanho do array, imprima o k-ésimo menor elemento no array fornecido. 
Considere que todos os elementos do array são inteiros distintos, e serão recebidos como uma string separados por vírgula
(utilize .split(',') para separá-los).

Entrada:                        Saida:
7, 10, 4, 3, 20, 15             7
3
'''
lista = list(map(int,input().split(',')))
k = int(input())
lista_Ordenada = sorted(lista)
print(lista_Ordenada[k-1])
  