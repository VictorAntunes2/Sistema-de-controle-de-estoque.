estoque = []

while True:

    print("\n=== CONTROLE DE ESTOQUE ===")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Atualizar estoque")
    print("4 - Remover produto")
    print("5 - Buscar produto")
    print("6 - Sair")

    opcao = input("Escolha uma opção: ")

    # CADASTRAR PRODUTO
    if opcao == "1":

        nome = input("Nome do produto: ").strip().title()
        preco = float(input("Preço: R$ "))
        quantidade = int(input("Quantidade: "))

        produto = {
            "nome": nome,
            "preco": preco,
            "quantidade": quantidade
        }

        estoque.append(produto)

        print("✅ Produto cadastrado com sucesso!")

    # LISTAR PRODUTOS
    elif opcao == "2":

        if not estoque:
            print("Nenhum produto cadastrado.")

        else:
            print("\n=== PRODUTOS CADASTRADOS ===")

            for produto in estoque:
                print(f"Nome: {produto['nome']}")
                print(f"Preço: R$ {produto['preco']:.2f}")
                print(f"Quantidade: {produto['quantidade']}")
                print("-" * 20)

    # ATUALIZAR ESTOQUE
    elif opcao == "3":

        nome_produto = input("Digite o nome do produto: ")

        encontrado = False

        for produto in estoque:

            if produto["nome"].lower() == nome_produto.lower():

                nova_quantidade = int(
                    input("Digite a nova quantidade: ")
                )

                produto["quantidade"] = nova_quantidade

                print("✅ Estoque atualizado com sucesso!")

                encontrado = True
                break

        if not encontrado:
            print("❌ Produto não encontrado.")

    # REMOVER PRODUTO
    elif opcao == "4":

        nome_produto = input("Digite o nome do produto que deseja remover: ")

        encontrado = False

        for produto in estoque:

            if produto["nome"].lower() == nome_produto.lower():

                estoque.remove(produto)

                print("✅ Produto removido com sucesso!")

                encontrado = True
                break

        if not encontrado:
            print("❌ Produto não encontrado.")

    # BUSCAR PRODUTO
    elif opcao == "5":

        busca = input("Digite o nome do produto: ")

        encontrado = False

        for produto in estoque:

            if produto["nome"].lower() == busca.lower():

                print("\n=== PRODUTO ENCONTRADO ===")
                print(f"Nome: {produto['nome']}")
                print(f"Preço: R$ {produto['preco']:.2f}")
                print(f"Quantidade: {produto['quantidade']}")

                encontrado = True
                break

        if not encontrado:
            print("❌ Produto não encontrado.")

    # SAIR
    elif opcao == "6":

        print("Encerrando sistema...")
        break

    # OPÇÃO INVÁLIDA
    else:
        print("❌ Opção inválida. Tente novamente.")