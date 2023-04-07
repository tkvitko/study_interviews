
class NoProductForRequestedSum(Exception):
    pass


class NoProductForRequestedTime(Exception):
    pass


def create_deposit(sum: float, months: int, regular_replenishment: float = None) -> float:
    """
    Function to calculate bank account earnings
    :param sum: summary of account
    :param months: deposit interval
    :param regular_replenishment: amount of regular replenishment (optional)
    :return: final amount on deposit at the end of interval
    """

    if sum < 1000 or sum > 1000000:
        raise NoProductForRequestedSum
    if months not in [6, 12, 24]:
        raise NoProductForRequestedTime

    products = [
        {'begin_sum': 1000, 'end_sum': 10000, 6: 5, 12: 6, 24: 5},
        {'begin_sum': 10000, 'end_sum': 100000, 6: 6, 12: 7, 24: 6.5},
        {'begin_sum': 100000, 'end_sum': 1000000, 6: 7, 12: 8, 24: 7.5}
    ]

    customer_product, customer_percent = None, None
    for product in products:
        if product['begin_sum'] <= sum < product['end_sum']:
            customer_product = product
    if customer_product:
        customer_percent = customer_product[months]
    if customer_percent:

        total = sum + sum * customer_percent / 100 * months / 12

        if not regular_replenishment:
            return total

        else:
            increase_for_replenishment = regular_replenishment * (1 + customer_percent / 100 / 12)
            replenishments_number = months - 2
            return total + increase_for_replenishment * replenishments_number


if __name__ == '__main__':
    print(create_deposit(sum=100000, months=6, regular_replenishment=1000))
