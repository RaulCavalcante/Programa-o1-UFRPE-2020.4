'''
Faça um programa que leia 3 números inteiros e os imprima em ordem crescente.
Ex: Entrada: 111    Saida: 111
             444           222
             222           444
            
'''

x=int(input())
y=int(input())
z=int(input())
if x > y :
    a = x
    x = y
    y = a
if y > z :
    a = y
    y = z
    z = a
print(x,y,z,sep="\n")
