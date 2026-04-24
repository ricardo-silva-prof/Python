cadastro=[]
a=1
while a==1:
    print("1.para cadastrar uma pessoa")
    print("2.excluir uma pessoa")
    print("3.buscar uma pessoa")
    print("4.atualizar um cadastro")
    print("5.sair")
    print("6.listar pessoas cadastradas")
    opcao=int(input("escolha uma opção: "))
    if opcao==1:
        nome=input("digite o nome: ")
        email=input("digite o email: ")
        telefone=input("digite o telefone: ")
        pessoa={"nome":nome,"email":email,"telefone":telefone}
        cadastro.append(pessoa)
        print(f"Pessoa '{nome}' cadastrada com sucesso!")
    elif opcao==2:
        excluir=input("digite o nome da pessoa que deseja excluir: ")
        encontrado=False
        for i, pessoa in enumerate(cadastro):
            if pessoa["nome"].lower()==excluir.lower():
                del cadastro[i]
                print(f"Pessoa '{excluir}' excluída com sucesso!")
                encontrado=True
                break
            if not encontrado:
                print("Pessoa não encontrada no cadastro!")
    elif opcao==3:
        buscar=input("digite o nome da pessoa que deseja buscar: ")
        encontrado=False
        for pessoa in cadastro:
            if pessoa["nome"].lower()==buscar.lower():
                print("\n--- Dados da Pessoa ---")
                print(f"Nome: {pessoa['nome']}")
                print(f"Email: {pessoa['email']}")
                print(f"Telefone: {pessoa['telefone']}")
                encontrado=True
                break
        if not encontrado:
            print("Pessoa não encontrada no cadastro!")
    elif opcao==4:
        atualizar=input("digite o nome da pessoa que deseja atualizar: ")
        encontrado=False
        for pessoa in cadastro:
            if pessoa["nome"].lower()==atualizar.lower():
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
                encontrado=True
                break
    elif opcao==5:
        print("Saindo do programa")
        a=0
    elif opcao==6:
        if len(cadastro)==0:
            print("O cadastro está vazio.")
        else:
            print("--- Lista de Pessoas Cadastradas ---")
            for i, pessoa in enumerate(cadastro):
                print(f"{i+1}. Nome: {pessoa['nome']} | Email: {pessoa['email']} | Telefone: {pessoa['telefone']}")
    else:
        print("Opção inválida, vai de novo cabra safado")