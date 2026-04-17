def main():
    print("--- DEMONSTRAÇÃO DE FUNÇÕES DE LISTAS EM PYTHON ---\n")

    # Criando nossa lista inicial vazia (o nosso "cadastro")
    cadastro_nomes = []
    print(f"Lista inicial: {cadastro_nomes}")

    # 1. append(x)
    # Adiciona um item ao final da lista.
    print("\n1. append() - Adicionando nomes 1 por 1:")
    cadastro_nomes.append("Carlos")
    cadastro_nomes.append("Ana")
    cadastro_nomes.append("Beatriz")
    print(f"Depois do append: {cadastro_nomes}")

    # 2. insert(i, x)
    # Insere um item em uma posição específica (índice).
    print("\n2. insert() - Inserindo 'João' na posição 1 (segundo elemento):")
    cadastro_nomes.insert(1, "João") 
    print(f"Depois do insert: {cadastro_nomes}")

    # 3. extend(iterable)
    # Estende a lista adicionando todos os itens de outra lista (ou iterável).
    print("\n3. extend() - Adicionando vários nomes de uma vez:")
    novos_nomes = ["Maria", "Pedro", "Carlos"]
    cadastro_nomes.extend(novos_nomes)
    print(f"Depois do extend: {cadastro_nomes}")
    
    # 4. count(x)
    # Retorna o número de vezes que 'x' aparece na lista.
    print("\n4. count() - Contando quantas vezes 'Carlos' aparece:")
    qtd_carlos = cadastro_nomes.count("Carlos")
    print(f"'Carlos' aparece {qtd_carlos} vezes.")

    # 5. index(x)
    # Retorna o índice (posição) da primeira ocorrência do elemento 'x'.
    print("\n5. index() - Descobrindo a posição da 'Ana':")
    posicao_ana = cadastro_nomes.index("Ana")
    print(f"A 'Ana' está na posição: {posicao_ana} (lembre-se que começa em 0)")

    # 6. copy()
    # Retorna uma cópia rasa (shallow copy) da lista.
    print("\n6. copy() - Criando um backup do cadastro:")
    backup_cadastro = cadastro_nomes.copy()
    print(f"Backup feito: {backup_cadastro}")

    # 7. remove(x)
    # Remove o primeiro item encontrado na lista com o valor 'x'.
    print("\n7. remove() - Removendo a primeira ocorrência de 'Carlos':")
    cadastro_nomes.remove("Carlos")
    print(f"Depois do remove: {cadastro_nomes}")

    # 8. pop([i])
    # Remove o item na posição dada e o retorna. Se nenhum índice for passado, remove e retorna o último.
    print("\n8. pop() - Removendo e retornando um item:")
    removido_ultimo = cadastro_nomes.pop() # sem índice remove o último ("Carlos")
    removido_pos_0 = cadastro_nomes.pop(0) # com índice remove o primeiro ("João" porque Carlos havia sido removido)
    print(f"Itens removidos com pop: {removido_ultimo} (final) e {removido_pos_0} (início)")
    print(f"Depois do pop: {cadastro_nomes}")

    # 9. sort()
    # Ordena os itens da lista in-place (diretamente na própria lista).
    print("\n9. sort() - Ordenando a lista em ordem alfabética:")
    cadastro_nomes.sort()
    print(f"Depois do sort (alfabética): {cadastro_nomes}")
    
    # sort(reverse=True) também é possível
    print("   sort(reverse=True) - Ordenando em ordem reversa:")
    cadastro_nomes.sort(reverse=True)
    print(f"   Ordem decrescente: {cadastro_nomes}")

    # 10. reverse()
    # Inverte a ordem dos itens da lista (não interage com valor, apenas vira de trás para frente).
    print("\n10. reverse() - Invertendo a ordem atual da lista:")
    cadastro_nomes.reverse()
    print(f"Depois do reverse: {cadastro_nomes}")

    # 11. clear()
    # Remove todos os itens da lista.
    print("\n11. clear() - Limpando toda a lista principal:")
    cadastro_nomes.clear()
    print(f"Depois do clear: {cadastro_nomes}")
    
    print(f"\nGraças à função copy(), nosso backup contínua intacto: {backup_cadastro}")

if __name__ == "__main__":
    main()
