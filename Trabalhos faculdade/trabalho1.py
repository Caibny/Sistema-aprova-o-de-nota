def calcular_situacao(n1, n2, frequencia):
    media = (n1 + n2) / 2

    if frequencia < 75:
        return media, "Reprovado"
    
    if media >= 7:
        return media, "Aprovado"
    elif media >= 5:
        return media, "Recuperação"
    else:
        return media, "Reprovado"


try:
    n1 = float(input("Digite a nota N1: "))
    n2 = float(input("Digite a nota N2: "))
    frequencia = float(input("Digite a frequência (%): "))

    # Validação de valores
    if not (0 <= n1 <= 10 and 0 <= n2 <= 10):
        print("Erro: as notas devem estar entre 0 e 10.")
    elif not (0 <= frequencia <= 100):
        print("Erro: a frequência deve estar entre 0 e 100.")
    else:
        media, situacao = calcular_situacao(n1, n2, frequencia)

        print(f"\nMédia final: {media:.2f}")
        print(f"Situação: {situacao}")

except ValueError:
    print("\nErro: digite apenas números válidos.")