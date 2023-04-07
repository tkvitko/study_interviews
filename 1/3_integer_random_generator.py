import time


def get_random_integer(min: int, max: int):
    """
    Random integer generator based on time.time
    :param min:
    :param max:
    :return:
    """
    difference = max - min
    random = int(time.time() * 1000)
    random %= difference
    random += min
    time.sleep(0.01)
    return random


def create_dict(size: int, min: int, max: int):
    result = dict()
    for step in range(size):
        result[f'elem_{step}'] = get_random_integer(min=min, max=max)
    return result


if __name__ == '__main__':
    print(create_dict(size=10, min=5, max=50))
