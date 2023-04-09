import os


def show_directory(path: str) -> None:
    """
    Prints directory files listing include subdirectories
    :param path: directory to print
    :return:
    """

    for file in os.listdir(path):
        file = os.path.join(path, file)
        if os.path.isfile(file):
            print(file)
        else:
            show_directory(file)


if __name__ == '__main__':
    show_directory('../')
