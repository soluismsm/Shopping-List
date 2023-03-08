from os import system

ERROR_MESSAGE = "Opção inválida. tente novamente."


def get_option():
    print("Selecione uma opção")
    print("1 - Inserir item na lista")
    print("2 - Apagar tem da lista")
    print("3 - Ver lista de compras")
    print("4 - Sair")
    while True:
        try:
            choice = int(input("Escolha (1|2|3|4): "))
            if choice == 1:
                return 1
            elif choice == 2:
                return 2
            elif choice == 3:
                return 3
            elif choice == 4:
                return 4
            else:
                raise ValueError(ERROR_MESSAGE)
        except ValueError:
            print(ERROR_MESSAGE)


def show_shopping_list():
    if len(shopping_list) == 0:
        print("Lista de compras vazia...")
    else:
        print("Lista de compras:")
        for i, item in enumerate(shopping_list):
            print(f"{i + 1} - {item}")


def add_item():
    while True:
        item = input("Qual item deseja adicionar ('sair' para sair) ? ")
        item = item.lower()
        if item == "sair":
            return
        else:
            shopping_list.append(item)
            print(f"O item '{item}' foi adicionado na lista de compras!\n")


def remove_item():
    while True:
        show_shopping_list()
        item = input("Qual item deseja remover ('sair' para sair) ? ")
        item = item.lower()
        if item == "sair":
            break
        elif item in shopping_list:
            shopping_list.remove(item)
            print(f"O item '{item}' foi removido da lista de compras!\n")
        else:
            print(ERROR_MESSAGE)


def main():
    while True:
        system("cls")
        user_option = get_option()
        system("cls")
        if user_option == 1:
            add_item()
        elif user_option == 2:
            remove_item()
        elif user_option == 3:
            show_shopping_list()
            while True:
                exit = input("Digite '1' para voltar: ")
                if exit.lower() == "1":
                    break
                else:
                    print(ERROR_MESSAGE)
        else:
            print("Fechando. Até mais!")
            return


shopping_list = []
main()
