'''
Faça um programa para calcular a situação de um aluno. O programa deve calcular a média das duas avaliações do aluno e apresentar:

A média alcançada, arredondada para uma casa decimal (ex., "7.5")
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez.

Entrada: 7             Saida: Média: 7.8
         8.5                  Aprovado
                 
        
'''
nota1 = float(input())
nota2 = float(input())
media = (nota1 + nota2) / 2
print("Média: %.1f" % media)
if media == 10 :
    print("Aprovado com Distinção")
elif media >= 7  :
    print("Aprovado")
else:
    print("Reprovado")
