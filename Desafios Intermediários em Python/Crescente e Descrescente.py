"""Leia uma quantidade indeterminada de duplas de valores inteiros X e Y. Para cada X e Y,
escreva uma mensagem para indicar se tais valores foram digitados em ordem crescente ou decrescente."""

X, Y = map(int, input().split())
while ( X != Y ):
    floor = min(X, Y)
    top = max(X, Y)
    if (X < Y):
        print("Crescente")
    elif ( X > Y       ):
        print("Decrescente")
    X, Y = map(int, input().split())