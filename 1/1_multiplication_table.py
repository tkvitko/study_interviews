
# external lambda to convert list to string
list_to_string = lambda lst: '\t'.join(lst)


def create_table(multiplier_left: int, multiplier_right: int) -> None:
    """
    Prints multiplication table based on miltipliers
    :param multiplier_left: left multiplier
    :param multiplier_right: right multiplier
    :return: None
    """

    for i in range(1, multiplier_left + 1):
        line_results = list()
        for j in range(1, multiplier_right + 1):
            line_results.append(str(i * j))
        print(list_to_string(line_results))


if __name__ == '__main__':
    create_table(3, 5)
