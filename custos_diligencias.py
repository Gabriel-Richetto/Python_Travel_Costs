def calcular_custo_viagem(distancia_km, consumo_km_l, preco_combustivel, pedagios=0.0, despesas_adicionais=0.0):
    litros_necessarios = distancia_km / consumo_km_l
    custo_combustivel = litros_necessarios * preco_combustivel
    custo_total = custo_combustivel + pedagios + despesas_adicionais
    return custo_total

def ler_float(mensagem, valor_padrao=0.0, obrigatorio=True):
    while True:
        entrada = input(mensagem)
        if not entrada and not obrigatorio:
            return valor_padrao
        try:
            valor = float(entrada)
            if valor < 0:
                print("Por favor, insira um valor positivo.")
                continue
            return valor
        except ValueError:
            print("Entrada inválida. Tente novamente com um número válido.")

def main():
    print("=== Calculadora de Custo de Viagem ===")

    distancia = ler_float("Informe a distância da viagem (km): ")
    consumo = ler_float("Informe o consumo do veículo (km/l): ")
    preco = ler_float("Informe o preço do combustível (R$/litro): ")
    pedagios = ler_float("Informe o total gasto com pedágios (opcional, R$): ", valor_padrao=0.0, obrigatorio=False)
    adicionais = ler_float("Informe outras despesas (alimentação, hospedagem, etc.) (opcional, R$): ", valor_padrao=0.0, obrigatorio=False)

    custo = calcular_custo_viagem(distancia, consumo, preco, pedagios, adicionais)
    print(f"\nCusto total estimado da viagem: R$ {custo:.2f}")

if __name__ == "__main__":
    main()