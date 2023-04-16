def check_if_integer(number: float) -> bool:
    """Checks if number is integer of fractional"""

    if int(number) == number:
        return True
    return False


def check_parts_equality(number: float) -> bool:
    """Checks if the inger part is equal to the second part"""

    parts = str(number).split('.')
    if parts[0] == parts[1]:
        return True
    return False


if __name__ == '__main__':
    users_number = float(input('Your number: '))
    if check_if_integer(users_number):
        print("It's integer!")
    else:
        print("It's fractional!")
        print(check_parts_equality(users_number))
