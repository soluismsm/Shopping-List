from os import system

MENSAGEM_DE_ERRO = "Opção inválida. tente novamente."


def tela_inicial():
    print("Selecione uma opção")
    print("1 - Inserir item na lista")
    print("2 - Apagar tem da lista")
    print("3 - Ver lista de compras")
    print("4 - Sair")
    while True:
        try:
            escolha = int(input("Escolha (1|2|3|4): "))
            if escolha == 1:
                return 1
            elif escolha == 2:
                return 2
            elif escolha == 3:
                return 3
            elif escolha == 4:
                return 4
            else:
                raise ValueError(MENSAGEM_DE_ERRO)
        except ValueError:
            print(MENSAGEM_DE_ERRO)


def mostrar_lista_de_compras():
    if len(lista_de_compras) == 0:
        print("Lista de compras vazia...")
    else:
        print("Lista de compras:")
        for índice, item in enumerate(lista_de_compras):
            print(f"{índice + 1} - {item}")


def adicionar_item():
    while True:
        item = input("Qual item deseja adicionar ('sair' para sair) ? ")
        item = item.lower()
        if item == "sair":
            return
        else:
            lista_de_compras.append(item)
            print(f"O item '{item}' foi adicionado na lista de compras!\n")


def remover_item():
    while True:
        mostrar_lista_de_compras()
        item = input("Qual item deseja remover ('sair' para sair) ? ")
        item = item.lower()
        if item == "sair":
            break
        elif item in lista_de_compras:
            lista_de_compras.remove(item)
            print(f"O item '{item}' foi removido da lista de compras!\n")
        else:
            print(MENSAGEM_DE_ERRO)


def programa_lista_de_compras():
    while True:
        system("cls")
        escolha = tela_inicial()
        system("cls")
        if escolha == 1:
            adicionar_item()
        elif escolha == 2:
            remover_item()
        elif escolha == 3:
            mostrar_lista_de_compras()
            while True:
                voltar = input("Digite '1' para voltar: ")
                if voltar.lower() == "1":
                    return
                else:
                    print(MENSAGEM_DE_ERRO)
        else:
            print("Fechando. Até mais!")
            return


lista_de_compras = []
programa_lista_de_compras()
