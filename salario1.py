valor_salario_minimo = 1621.00

salario_usuario = float(input("Digite o valor do seu salário: "))

quantidade_salarios = salario_usuario / valor_salario_minimo

# :.2f formata o número para mostrar apenas 2 casas decimais
print(f"O seu salário equivale a {quantidade_salarios:.2f} salários mínimos.")
