import math

pontos1 = input("Digite com espaco as duas primeiras coordenadas, sendo X e Y:").split()
pontos2 = input("Digite com espaco as duas segundas coordenadas, sendo X e Y:").split()
x1 = float(pontos1[0])
x2 = float(pontos2[0])
y1 = float(pontos1[1])
y2 = float(pontos2[1])

x = (x1 - x2)**2
y = (y1 - y2)**2
calc3 = (x + y) ** 0.5

print(f"A distancia entre o ponto X e Y é: {calc3}")
