valor = float(input("digite valor da compra: "))
if valor >=500:
    desconto = valor * 0.20
    valorfinal= valor - desconto
    print("desconto de 20%")
    print("Valor final", valorfinal)

elif valor >=200:
    desconto = valor * 0.10
    valorfinal= valor - desconto
    print("desconto 10%") 
    print("valor final", valorfinal)
else: 
    print("sem desconto")