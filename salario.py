salario = float(input("digite o salario: "))

if salario >=3000:
    bonus = salario * 0.10
elif salario >= 2000:
    bonus = salario * 0.05
else:
    bonus = salario * 0.02
salario_final = salario + bonus
print("salario final:", salario_final)