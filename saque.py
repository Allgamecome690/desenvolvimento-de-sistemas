saldo = 500
saque = int(input("Digite o valor do saque:"))
if saque <= saldo:
    print("Saque realizado com sucesso!")
else:
    print("Saldo insuficiente!")