# Solicita que o usuário insira um número inteiro
numero_inteiro = int(input("Digite um número inteiro: "))

# Calcula o antecessor (número - 1)
antecessor = numero_inteiro - 1

# Calcula o sucessor (número + 1)
sucessor = numero_inteiro + 1

# Exibe os resultados na tela
print(f"O antecessor de {numero_inteiro} é {antecessor}")
print(f"O sucessor de {numero_inteiro} é {sucessor}")

# f antes das aspas significa f-string 
# (ou formatted string literal), um recurso 
# introduzido no Python 3.6 para facilitar a 
# formatação de textos.

#Para que serve?
#Ele permite que você coloque variáveis e expressões Python diretamente dentro do texto, entre chaves { }.