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