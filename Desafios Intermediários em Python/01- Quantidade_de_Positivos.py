"""Crie um programa que leia 6 valores, os quais poderão ser negativos e/ou positivos. Em seguida,
apresente a quantidade de valores positivos digitados"""
counter = 0
for i in range(6):
    number = float(input())
    if number > 0:
        counter += 1

print(f"{counter} valores positivos")