import os


def get_file_name(file_path: str) -> str:
    """Returns name of file without it's extensions"""

    return os.path.split(file_path)[-1].split('.')[0]


if __name__ == '__main__':
    print(get_file_name('/home/tkvitko/test_name.tar.gz'))
