emprestimo = float(input("Digite o valor do empréstimo: ")) 
salario = float(input("Digite o valor do salário: "))
parcelas = int(input("Digite a quantidade de parcelas: "))
emprestimo = emprestimo / parcelas

if emprestimo > salario * 0.3:
    print("Empréstimo não concedido.")
else:
    print("Empréstimo concedido.")