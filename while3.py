total = 0
while total < 20:
    moeda = float(input("Qual o valor da moeda depositada? "))
    total += moeda
    print(f"Saldo atual: R$ {total:.2f}")
print(f"Cofre cheio! Total: R$ {total:.2f}")