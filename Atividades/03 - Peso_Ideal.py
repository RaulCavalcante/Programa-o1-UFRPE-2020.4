'''
Tendo como dados de entrada a altura em metros e o sexo de uma pessoa (M ou F),
escreva um programa que calcule seu peso ideal, utilizando as seguintesfórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7 (h = altura)
O seu programa deve receber como entrada o sexo (string), a altura (float) e o peso atual (float) da pessoa. Como saída, informe se seu peso atual em relação ao ideal está:
ideal, acima do peso, abaixo do peso

Entrada: M              Saida: acima do peso
         1.78
         120       

'''
sexo = input()
altura = float(input())
peso = float(input())
if sexo.upper == "M" :
    peso_Ideal = (62.1*altura) - 44.7
else:
    peso_Ideal = (72.7*altura) - 58

if peso_Ideal < peso :
    print("acima do peso")
elif peso_Ideal == peso :
    print("ideal")
else:
    print("abaixo do peso")
