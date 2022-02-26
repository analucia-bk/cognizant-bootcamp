"""Você recebeu o desafio de ler um valor e criar um programa que coloque o valor lido na primeira
posição de um vetor N[10]. Em cada posição subsequente, coloque o dobro do valor da posição anterior.
Por exemplo, se o valor lido for 1, os valores do vetor devem ser 1,2,4,8 e assim
sucessivamente. Mostre o vetor em seguida."""

x = int(input("Digite um número "))
n = list()

for i in range(10):
    n.append(x)
    x = (x * 2)
    print(" N[{}] = ".format(i), n[i])