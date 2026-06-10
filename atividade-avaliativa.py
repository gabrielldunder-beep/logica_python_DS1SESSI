cargaTotal = 0
faturamento = 0
print("Qual a quantidade de pacotes?:")
pacotes = int(input())
for contador in range(1, 10 + 1, 1):
    print("Qual o peso do pacote:")
    peso = float(input())
    if peso <= 2:
        custo = 10
        print("Classificação: Leve")
    else:
        if peso <= 10:
            custo = 20
            print("Classificação: Padrão")
        else:
            custo = 30
            print("Classificação: Pesado")
    print("Destino internacional? (1)sim / (2)não")
    destino = input()
    if destino == "1":
        custo = custo * 0.2
    cargaTotal = cargaTotal + peso
    faturamento = faturamento + custo
    ticketMedio = faturamento / 10
print("========== RESULTADO FINAL ==========")
print("Total de pacotes: 10")
print("Carga total acumulada (Kg):")
print(cargaTotal)
print("Faturamento Bruto do Lote: R$")
print(faturamento)
print("Ticket médio por pacote: R$")
print(ticketMedio)
print("====================================")