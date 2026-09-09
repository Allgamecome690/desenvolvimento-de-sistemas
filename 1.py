def calcular_dobro():
    try:
        # Solicita um número ao usuário
        numero_str = input("Digite um número: ").strip()

        # Verifica se o valor é numérico (aceita inteiros e decimais)
        numero = float(numero_str)

        # Calcula o dobro
        dobro = numero * 2

        # Exibe o resultado
        print(f"O dobro de {numero} é {dobro}")

    except ValueError:
        print("Erro: Por favor, digite um valor numérico válido.")

if __name__ == "__main__":
    calcular_dobro()