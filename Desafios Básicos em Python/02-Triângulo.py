"""Leia 3 valores reais (A, B e C) e verifique se eles formam ou não um triângulo. Em caso positivo,
calcule o perímetro do triângulo (soma de todos os lados) e apresente a mensagem"""

lados = [float(x) for x in input().split()]

a = lados[0];
b = lados[1];
c = lados[2];
perimetro = a + b + c
area = ((a+b)* c) / 2
if a + b > c and a + c > b and b + c > a:
    print(f"Perimetro = { perimetro   :.1f}")
else:
    print(f"Area = { area   :.1f}")