altura = float(input("Insira sua altura: "))
genero = int(input("Voce e homem ou mulher?\n Insira 1 para homem e 0 para mulher: "))
if genero == 0 :
    peso_ideal = (72.7*altura) - 58
elif genero == 1 :
    peso_ideal = (62.1*altura) - 44.7
else :
    print("Erro")



"""
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7
"""