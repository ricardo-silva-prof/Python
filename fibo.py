# Solicita o número de termos ao usuário
n_termos = int(input("Quantos termos da sequência de Fibonacci você deseja ver? "))

# Inicializa os dois primeiros termos
termo1 = 0
termo2 = 1

print("\nSequência de Fibonacci:")

# O laço for controla a iteração até o número solicitado
for i in range(n_termos):
    print(termo1, end=" ")
    
    # Lógica de atualização (incremento dos termos)
    proximo = termo1 + termo2
    termo1 = termo2
    termo2 = proximo

print("\n\nFim da sequência.")