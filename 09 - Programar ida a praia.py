'''
O ano novo começou, e como meta desse novo período da sua vida, você quer programar sair mais vezes para ir a praia. 
Crie um programa que lhe informe o melhor dia do ano, que seja um final de semana, para sair num passeio para a praia, ou seja,
o dia em que a chance de chover é a menor, sempre priorizando a data mais próxima ao começo do ano!A entrada consiste em 12 linhas 
(Janeiro-Dezembro), com 8 elementos em cada (Todos os elementos possuem ponto flutuante), representando a chance de chuva nos sábados
 e domingos, respectivamente (e.g., S1 D1 S2 D2 S3 D3 S4 D4).

Entrada:                                                Saida:
0.47 0.11 0.32 0.12 0.67 0.41 0.76 0.86                 O melhor dia e no Primeiro Sabado de Janeiro
0.91 0.98 0.34 0.12 0.54 0.36 0.53 0.67
0.66 0.19 0.55 0.91 0.08 0.85 0.65 0.16
0.78 0.49 0.01 0.32 0.11 0.87 0.18 0.16
0.05 0.83 0.64 0.51 0.12 0.32 0.38 0.66
0.50 0.29 0.03 0.40 0.71 0.49 0.10 0.67
0.61 0.29 0.62 0.72 0.27 0.43 0.01 0.57
0.22 0.45 0.59 0.49 0.72 0.90 0.76 0.50
0.69 0.51 0.79 0.56 0.67 0.22 0.65 0.88
0.32 0.20 0.87 0.01 0.18 0.39 0.48 0.23
0.67 0.07 0.27 0.09 0.86 0.26 0.44 0.91
'''


def melhor_Dia ( i ):
    if i % 2 != 0:
        dia = "Domingo"
    else:
        dia = "Sabado"
    return dia
def melhor_Semana ( i ):
    if 0 <= i <= 1:
        semana = "Primeiro"
    elif 2 <= i <= 3:
        semana = "Segundo"
    elif 4 <= i <= 5:
        semana = "Terceiro"
    elif 6 <= i <= 7:      
        semana = "Quarto"
    return semana

listaJ = list(map(float,input().split(' ')))
listaF = list(map(float,input().split(' ')))
listaM = list(map(float,input().split(' ')))
listaA = list(map(float,input().split(' ')))
listaMA = list(map(float,input().split(' ')))
listaJN = list(map(float,input().split(' ')))
listaJL = list(map(float,input().split(' ')))
listaAG = list(map(float,input().split(' ')))
listaS = list(map(float,input().split(' ')))
listaO = list(map(float,input().split(' ')))
listaN = list(map(float,input().split(' ')))
listaD = list(map(float,input().split(' ')))

melhor = listaJ[0]
dia = "Sabado"
semana = "Primeiro"
mes = "Janeiro"

for j in range(len(listaJ)):   
    if melhor > listaJ[j]: 
        mes = "Janeiro"
        dia = melhor_Dia(j)
        semana = melhor_Semana(j)
for j in range(len(listaF)):   
    if melhor > listaF[j]: 
        mes = "Fevereiro"
        dia = melhor_Dia(j)
        semana = melhor_Semana(j)
for j in range(len(listaM)):   
    if melhor > listaM[j]: 
        mes = "Março"
        dia = melhor_Dia(j)
        semana = melhor_Semana(j)
for j in range(len(listaA)):   
    if melhor > listaA[j]: 
        mes = "Abril"
        dia = melhor_Dia(j)
        semana = melhor_Semana(j)
for j in range(len(listaMA)):   
    if melhor > listaMA[j]: 
        mes = "Maio"
        dia = melhor_Dia(j)
        semana = melhor_Semana(j)
for j in range(len(listaJN)):   
    if melhor > listaJ[j]: 
        mes = "Junho"
        dia = melhor_Dia(j)
        semana = melhor_Semana(j)
for j in range(len(listaJL)):   
    if melhor > listaJL[j]: 
        mes = "Julho"
        dia = melhor_Dia(j)
        semana = melhor_Semana(j)
for j in range(len(listaAG)):   
    if melhor > listaAG[j]: 
        mes = "Agosto"
        dia = melhor_Dia(j)
        semana = melhor_Semana(j)
for j in range(len(listaS)):   
    if melhor > listaS[j]: 
        mes = "Setembro"
        dia = melhor_Dia(j)
        semana = melhor_Semana(j)
for j in range(len(listaO)):   
    if melhor > listaO[j]: 
        mes = "Outubro"
        dia = melhor_Dia(j)
        semana = melhor_Semana(j)
for j in range(len(listaN)):   
    if melhor > listaN[j]: 
        mes = "Novembro"
        dia = melhor_Dia(j)
        semana = melhor_Semana(j)
for j in range(len(listaD)):   
    if melhor > listaD[j]: 
        mes = "Dezembro"
        dia = melhor_Dia(j)
        semana = melhor_Semana(j)
                         
print('O melhor dia e no {} {} de {}'.format(semana,dia,mes))
