from menu import(
    Menu,
)


def run():

    Menu().print_start()

    choose = input("Введите выбор: ")

    while choose != "5":
        Menu().choose(choose)
        Menu().print_start()

        choose = input("Введите выбор: ")

run()