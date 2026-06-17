def get_user_int(msg: str) -> int:
    """
    This function prints the given message and waits for the user to enter an integer.

    :param msg: A message to be printed before prompting the user for an input
    :return: The integer the user entered.
    """
    while True:
        user_input = input(msg)
        try:
            user_input = int(user_input)
            break
        except ValueError:
            print("That is not an integer. Try again...")

    return user_input