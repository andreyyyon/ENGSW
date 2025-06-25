N = int(input('Digite um número inteiro positivo: '))
A = N
div = 1
if N <= 0:
    print('Digite um número diferente de zero.')
else:
    for c in range (1,N):
        N -= 1
        div += 1
        A += N/div
print(A)