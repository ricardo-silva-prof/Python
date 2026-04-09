# Definição de variáveis do tipo String (texto) e Integer (inteiro)
nome = "Ricardo"
idade = 39
cidade = "Limoeiro"
escola = "ETE Limoeiro"

# Exibição dos dados na tela usando f-string (format string)
# O 'f' antes das aspas permite inserir variáveis diretamente dentro das chaves {}
print(f"Olá meu nome é: {nome} minha idade é: {idade} Sou professor na Escola: {escola} na cidade de: {cidade}")

# Outra forma de fazer o mesmo print (Concatenação Clássica)
# Note que precisamos usar str(idade) para transformar o número em texto
# print("Olá meu nome é: " + nome + " minha idade é: " + str(idade) + " Sou professor na Escola: " + escola + " na cidade de: " + cidade)