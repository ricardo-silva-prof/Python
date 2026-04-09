numero = int(input("Digite um número para ver a tabuada: "))
if 1 <=numero<=10:
    print(f"Tabuada do {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
else:
    print("Por favor, digite um número entre 1 e 10.")