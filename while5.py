opcao=True
while opcao==True:
    print("1- Iniciar o programa")
    print("2- Sair do programa")
    escolha=int(input("Digite a opção desejada: "))
    if escolha==1:
        print("Programa iniciado!")
    elif escolha==2:
        print("Saindo do programa...")
        opcao=False
    else:
        print("Opção inválida. Tente novamente.")