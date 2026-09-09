def calcular_forca(massa: float, aceleracao: float) -> float:
    """
    Calcula a força resultante.
    :param massa: massa em quilogramas (kg)
    :param aceleracao: aceleração em metros por segundo ao quadrado (m/s²)
    :return: força em Newtons (N)
    """
    return massa * aceleracao


def entrada_float(mensagem: str) -> float:
    """Lê um número float do usuário com validação."""
    while True:
        try:
            valor = float(input(mensagem))
            return valor
        except ValueError:
            print("❌ Entrada inválida. Digite um número válido.")


if __name__ == "__main__":
    print("=== Cálculo da Força (F = m * a) ===")

    # Entrada de dados com validação
    massa = entrada_float("Informe a massa (kg): ")
    aceleracao = entrada_float("Informe a aceleração (m/s²): ")

    # Cálculo
    forca = calcular_forca(massa, aceleracao)

    # Exibição do resultado
    print(f"\nA força resultante é: {forca:.2f} N")