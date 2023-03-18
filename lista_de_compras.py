import os
import subprocess

ERROR_MESSAGE = "Opção inválida. tente novamente."


def get_option():
    while True:
        try:
            choice = int(input("Escolha (1|2|3|4): "))
            if choice in [1, 2, 3, 4]:
                return choice
        except ValueError:
            print(ERROR_MESSAGE)


def show_shopping_list(shopping_list):
    if len(shopping_list) == 0:
        print("Lista de compras vazia...")
    else:
        print("Lista de compras:")
        for i, item in enumerate(shopping_list):
            print(f"{i + 1} - {item}")


def add_item(shopping_list):
    while True:
        item = input("Qual item deseja adicionar ('sair' para sair) ? ")
        item = item.lower()
        if item == "sair":
            return
        else:
            shopping_list.append(item)
            print(f"O item '{item}' foi adicionado na lista de compras!\n")


def remove_item(shopping_list):
    while True:
        show_shopping_list(shopping_list)
        item = input("Qual item deseja remover ('sair' para sair) ? ")
        item = item.lower()
        if item == "sair":
            break
        elif item in shopping_list:
            shopping_list.remove(item)
            print(f"O item '{item}' foi removido da lista de compras!\n")
        else:
            print(ERROR_MESSAGE)


def apagar_console():
    """
    Limpa o console do sistema operacional atual.
    """
    sistema = os.name
    if sistema == "nt":
        subprocess.call("cls", shell=True)
    else:
        subprocess.call("clear", shell=True)


def show_options():
    print(
        """=-=-=-=LISTA DE COMPRAS=-=-=-=
1 - Inserir um item na Lista.
2 - Remover item da Lista
3 - Ver lista de compras.
4 - Sair
"""
    )


def main():
    shopping_list = []
    while True:
        show_options()
        user_option = get_option()
        apagar_console()
        if user_option == 1:
            add_item(shopping_list)
        elif user_option == 2:
            remove_item(shopping_list)
        elif user_option == 3:
            show_shopping_list(shopping_list)
            while True:
                exit = input("Digite '1' para voltar: ")
                if exit.lower() == "1":
                    break
                else:
                    print(ERROR_MESSAGE)
        else:
            print("Fechando. Até mais!")
            return
        apagar_console()


if __name__ == "__main__":
    main()
