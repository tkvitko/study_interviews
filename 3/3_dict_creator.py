from itertools import zip_longest


def create_dict(keys: list, values: list) -> dict:
    """
    Returns dict based on 2 lists.
    If keys > values, last keys will have None value;
    if keys < values, last values will not being used.
    """

    return {key: value for key, value in zip_longest(keys, values) if key}


if __name__ == '__main__':
    print(create_dict([1, 2, 3], [4, 5]))
    print(create_dict([1, 2, 3], [4, 5, 6, 7]))
