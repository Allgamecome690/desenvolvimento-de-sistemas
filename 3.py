def calcular_velocidade_media(espaco, tempo):
    """
    Calcula a velocidade média.
    :param espaco: Distância percorrida (em metros ou km)
    :param tempo: Tempo gasto (em segundos, minutos ou horas)
    :return: Velocidade média
    """
    if tempo <= 0:
        raise ValueError("O tempo deve ser maior que zero para evitar divisão por zero.")
    return espaco / tempo


if __name__ == "__main__":
    try:
        # Entrada de dados
        espaco = float(input("Digite o espaço percorrido: "))
        tempo = float(input("Digite o tempo gasto: "))

        # Cálculo
        velocidademedia = calcular_velocidade_media(espaco, tempo)

        # Saída formatada
        print(f"Velocidade média: {velocidademedia:.2f} unidades por unidade de tempo")

    except ValueError as e:
        print(f"Erro: {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")