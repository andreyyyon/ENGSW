# Questão 5: O programa DivisorProprio recebe da entrada de dados um número inteiro fornecido pelo 
# usuário e mostra, na tela, um dos divisores próprios desse número. Os divisores próprios de um 
# número são aqueles diferentes de 1 e do próprio número. Por exemplo, os divisores próprios de 6 são 
# 2 e 3. O número 5 não tem divisor próprio. O programa descrito abaixo foi desenvolvido para retornar 
# o divisor próprio de um número utilizando a estrutura de repetição while
# num = int(input('Digite um número inteiro maior que zero'))
# divisor = 0
# i = 2
# while i < num - 1:
# if (num%i) == 0:
# divisor = i
# i = i + 1
# if divisor != 0:
# print( divisor,' é um divisor próprio de ', num)
# else:
# print( num ,'não tem divisor próprio')
# Reescreva o código acima e substitua a estrutura de repetição while pela estrutura de repetição for

num = int(input('Digite um número inteiro maior que zero'))
divisor = 0
for i in range(2, num):
    if num % i == 0:
        divisor = i
        break
if divisor != 0:
    print(divisor, 'é um divisor próprio de', num)
else:
    print(num, 'não tem divisor próprio')