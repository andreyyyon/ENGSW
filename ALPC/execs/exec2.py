# Questão 2: Considere o seguinte segmento de código: 
# count = 5
# while count > 1: 
#   print(count, end = " ")
#   count = count - 1
# Reescreva o código acima e substitua o loop while pelo loop for

count = 5
# do 5 ao 1 reduzindo 1 -> range(start, stop, step)
for count in range(5, 1, -1):
    print(count, end=" ")
