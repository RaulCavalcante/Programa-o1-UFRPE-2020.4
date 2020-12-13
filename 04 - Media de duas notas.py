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
