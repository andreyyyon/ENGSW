A = int(input('Digite um valor A: '))
B = int(input('Digite um valor B: '))
calc = A % B
N = int(input('Quantas vezes você quer ver o resultado? '))
print('-='*15)
print('Letra a)')
for c in range(0,10):
    print(calc)

print('-='*15)
print('Letra b)')
for c in range(0,0):
    print(calc)

print('-='*15)
print('Letra c)')
for c in range (0, N):
    print(calc)