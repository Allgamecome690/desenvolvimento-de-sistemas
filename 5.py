def calcular_trabalho(forca: float, deslocamento: float) -> float:
    """
    Calcula o trabalho realizado.
    
    :param forca: Força aplicada (em Newtons)
    :param deslocamento: Deslocamento (em metros)
    :return: Trabalho (em Joules)
    """
    return forca * deslocamento

def main():
    try:
        # Entrada de dados com validação
        forca = float(input("Digite a força (N): ").strip())
        deslocamento = float(input("Digite o deslocamento (m): ").strip())

        # Cálculo
        trabalho = calcular_trabalho(forca, deslocamento)

        # Saída formatada
        print(f"Trabalho realizado: {trabalho:.2f} Joules")

    except ValueError:
        print("Erro: Digite apenas valores numéricos.")

if __name__ == "__main__":
    main()