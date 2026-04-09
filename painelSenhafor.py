clientes = ["Alice", "João", "Maria", "Roberto"]

print("--- ORDEM DE ATENDIMENTO ---")
for posicao, nome in enumerate(clientes, start=1):
    print(f"Senha nº{posicao}: Favor dirigir-se ao caixa, {nome}.")