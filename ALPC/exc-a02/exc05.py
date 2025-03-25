valhora = float(input("Digite o valor da hora: "))
hrs = int(input("Digite a quantidade de horas trabalhadas: "))
inss = float(input("Digite o valor do INSS: "))
salariobruto = valhora * hrs
inss = inss / 100
liquido = salariobruto - (salariobruto * inss)
print(f"O salário líquido é de R${liquido:.2f}.")