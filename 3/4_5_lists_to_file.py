import os.path
import random


def create_file(file_path: os.path) -> bool:
    if os.path.exists(file_path):
        return False
    with open(file_path, 'w', encoding='utf-8') as f:
        strings = [sym for sym in 'abcd']
        numbers = [number for number in list(range(4))]
        for string, number in zip(strings, numbers):
            if random.choice([0, 1]) == 0:
                f.write(f'{string}{number}\n')
            else:
                f.write(f'{number}{string}\n')
    return True


def read_file(file_path: os.path) -> None:
    with open(file_path, encoding='utf-8') as f:
        for line in f.readlines():
            print(line.strip())


def search_in_file(file_path: os.path, search_string: str,
                   first_only: True, change_to: str = None):

    with open(file_path, encoding='utf-8') as f:
        for line in f.readlines():
            if search_string in line:
                if change_to is not None:
                    line = line.replace(search_string, change_to)
                print(line.strip())
                if first_only:
                    break


if __name__ == '__main__':
    file_path = os.path.join('.', 'test.txt')

    created = create_file(file_path)
    if not created:
        print('File exists!')

    print('Original file:')
    read_file(file_path)

    print('Search results:')
    search_in_file(file_path=file_path, search_string='b',
                   first_only=False, change_to='f')
