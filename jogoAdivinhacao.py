import random #importa a biblioteca random para gerar números aleatórios

numero_secreto = random.randint(1, 10) #   gera um número aleatório entre 1 e 10 e o armazena na variável numero_secreto
tentativas = 0
opcao=True
print("Adivinhe o número entre 1 e 10!")

while opcao==True:
    palpite = input("Seu palpite: ")
    
    # Verifica se a entrada contém apenas dígitos
    if palpite.isdigit(): # Verifica se a entrada do usuário é um número válido (apenas dígitos)
        palpite = int(palpite)# Converte a entrada do usuário para um número inteiro
        tentativas = tentativas + 1 # Incrementa o número de tentativas
        
        if palpite < numero_secreto:
            print("Muito baixo!")
        elif palpite > numero_secreto:
            print("Muito alto!")
        else:
            print(f"Parabéns! Você acertou em {tentativas} tentativas!")
            opcao=False
    else:
        print("Digite um número válido!")

print("Fim do jogo!")