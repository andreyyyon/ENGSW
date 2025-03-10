x = float(input("Digite a altura? "))
y = float(input("Digite o raio? "))

metros = 2 * 3.14 * (y**2) + 2 * 3.14 * y * x 
latas = metros/3
custo = latas * 20

print(f"Vao ser necessarios {latas:.0f} latas de tinta que custam R${custo:.2f} para pintar o tanque")
