# Lista que irá armazenar os dicionários com os dados das pessoas
cadastro = []

while True:
    print("\n--- Sistema de Cadastro de Pessoas ---")
    print("1. Inserir pessoa")
    print("2. Alterar dados")
    print("3. Listar todas as pessoas")
    print("4. Excluir pessoa")
    print("5. Buscar pessoa pelo nome (Listar individual)")
    print("6. Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        nome = input("Digite o nome: ")
        email = input("Digite o email: ")
        telefone = input("Digite o telefone: ")
        
        pessoa = {
            "nome": nome,
            "email": email,
            "telefone": telefone
        }
        cadastro.append(pessoa)
        print(f"Pessoa '{nome}' cadastrada com sucesso!")

    elif opcao == '2':
        nome_busca = input("Digite o nome da pessoa que deseja alterar: ")
        encontrado = False
        for pessoa in cadastro:
            if pessoa["nome"].lower() == nome_busca.lower():
                print(f"\nDados atuais -> Nome: {pessoa['nome']} | Email: {pessoa['email']} | Telefone: {pessoa['telefone']}")
                print("Deixe em branco (aperte Enter) caso não queira alterar um campo específico.")
                
                novo_nome = input(f"Novo nome [{pessoa['nome']}]: ")
                novo_email = input(f"Novo email [{pessoa['email']}]: ")
                novo_telefone = input(f"Novo telefone [{pessoa['telefone']}]: ")
                
                if novo_nome.strip():
                    pessoa["nome"] = novo_nome
                if novo_email.strip():
                    pessoa["email"] = novo_email
                if novo_telefone.strip():
                    pessoa["telefone"] = novo_telefone
                    
                print("Dados alterados com sucesso!")
                encontrado = True
                break
        
        if not encontrado:
            print("Pessoa não encontrada no cadastro!")

    elif opcao == '3':
        if len(cadastro) == 0:
            print("O cadastro está vazio.")
        else:
            print("\n--- Lista de Pessoas Cadastradas ---")
            for i, pessoa in enumerate(cadastro):
                print(f"{i+1}. Nome: {pessoa['nome']} | Email: {pessoa['email']} | Telefone: {pessoa['telefone']}")

    elif opcao == '4':
        nome_busca = input("Digite o nome da pessoa que deseja excluir: ")
        encontrado = False
        for i, pessoa in enumerate(cadastro):
            if pessoa["nome"].lower() == nome_busca.lower():
                del cadastro[i]
                print(f"Pessoa '{nome_busca}' excluída com sucesso!")
                encontrado = True
                break
        
        if not encontrado:
            print("Pessoa não encontrada no cadastro!")

    elif opcao == '5':
        nome_busca = input("Digite o nome da pessoa que deseja buscar: ")
        encontrado = False
        for pessoa in cadastro:
            if pessoa["nome"].lower() == nome_busca.lower():
                print("\n--- Dados da Pessoa ---")
                print(f"Nome: {pessoa['nome']}")
                print(f"Email: {pessoa['email']}")
                print(f"Telefone: {pessoa['telefone']}")
                encontrado = True
                break
        
        if not encontrado:
            print("Pessoa não encontrada no cadastro!")

    elif opcao == '6':
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida. Tente novamente.")