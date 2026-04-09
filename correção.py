def main():
    nome = input("Digite seu nome: ")
    ano_nascimento = int(input("Digite seu ano de nascimento: "))
    ano_atual = int(input("Digite o ano atual: "))

    idade = ano_atual - ano_nascimento

    print(f"\nOlá, {nome}!")
    print(f"Neste ano de {ano_atual}, você tem ou fará {idade} anos.")

    if idade >= 18:
        print("Você é maior de idade.")
    else:
        print("Você é menor de idade.")

if __name__ == "__main__":
    main()