login_usuario = "fla"
senha_usuario= "123"

tentativas_maximas = 3
tentativas_atuais = 0

print("--- Sistema de Login ---")
while tentativas_atuais < tentativas_maximas:
    usuario = input("Digite o usuário: ")
    senha = input("Digite a senha: ")

    if usuario == login_usuario and senha == senha_usuario:
        print("\nLogin realizado com sucesso! Bem-vindo(a).")
        break
    else:
        tentativas_atuais += 1
        tentativas_restantes = tentativas_maximas - tentativas_atuais
        if tentativas_restantes > 0:
            print(f"\nUsuário ou senha incorretos. Você tem mais {tentativas_restantes} tentativa(s).\n")
        else:
            print("\nNúmero máximo de tentativas atingido. Acesso bloqueado.\n")
