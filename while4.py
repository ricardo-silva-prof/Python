nota = float(input("Digite a nota (0-10): "))
while nota < 0 or nota > 10:
    print("Nota inválida!")
    nota = float(input("Digite novamente (0-10): "))
print(f"Nota {nota} registrada!")