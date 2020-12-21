'''
O triângulo de Pascal é uma matriz triangular dos coeficientes binomiais. Escreva uma função que recebe 
um valor inteiro n como entrada e imprime as primeirasn linhas do triângulo de Pascal. 
A seguir estão as primeiras 6 linhas do Triângulo de Pascal.

Entrada:                Saida:
3                       1
                        1  1
                        1  2  1
'''
def calculo(n,p):
    x = 0
    if p == 0 :
        x = 1
    elif p == 1 :
        x = n 
    elif (p+1) == n:
        x = n
    elif n == p:
        x = 1
    else:
        x = fatorial(n) / (fatorial(p) * fatorial(n-p))
    return x

def fatorial (x):
    num = x
    while x - 1 > 1 :
        num = num * (x - 1)
        x -= 1    
    return num

linha = int(input())
n = 0
p = 0
i = 0
while n < linha :
    if n == 0:
        print(calculo(n,p))
    else:
        while p <= i:
            print(int(calculo(n,p)),end=" ")
            p += 1
        print()         
    n += 1
    i += 1
    p = 0 