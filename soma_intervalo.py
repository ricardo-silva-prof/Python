inicio = int(input("Início: "))
fim = int(input("Fim: "))

soma = 0
# Somamos +1 no fim para incluir o último número digitado
for n in range(inicio, fim + 1):
    soma = soma + n

print(f"A soma de todos os números entre {inicio} e {fim} é: {soma}")