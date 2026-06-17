import user_input

def print_menu() -> None:
    print("Menu   ")
    print("\t1] TODO")
    print("\t2] TODO")
    print("\t0] Exit")

def main() -> None:
    """
    This function holds the main loop of the program.

    :return: None - Function does not return anything
    """
    print("Entering main loop...")

    running = True
    while running:
        print_menu()
        menu = user_input.get_user_int("Enter your menu choice: ")

        if menu == 1:
            print("Option 1 not implemented...")
        elif menu == 2:
            print("Option 2 not implemented...")
        elif menu == 0:
            print("Thank you for using PassGo!")
            running = False

if __name__ == '__main__':
    main()
