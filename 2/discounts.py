class ItemDiscount:
    def __init__(self, name: str, price: float):
        """Private properties"""
        self.__name = name
        self.__price = price

    def get_name(self):
        """Getter for private property"""
        return self.__name

    def get_price(self):
        """Getter for private property"""
        return self.__price

    def set_price(self, price):
        """Setter for private property"""
        self.__price = price


class ItemDiscountReport(ItemDiscount):
    def __init__(self, name, price, discount: int = 0):
        """Init with properties of parent class and property of current class"""
        super().__init__(name=name, price=price)
        self.discount = discount

    def __str__(self):
        """Overriding str method"""
        return str(self.get_price() * (1 - self.discount / 100))

    def get_parent_data(self):
        """Getting private properties from parent class"""
        return f'{self.get_name()}: {self.get_price()}'


# Polymorphism
class ItemDiscountReportPrice(ItemDiscount):
    def get_info(self):
        return self.get_price()


class ItemDiscountReportName(ItemDiscount):
    def get_info(self):
        return self.get_name()


if __name__ == '__main__':

    # Demo:
    item_1 = ItemDiscount(name='Audi', price=100)
    item_2_report = ItemDiscountReport(name='Mercedes', price=200)
    print(item_2_report.get_parent_data())

    item_2_report.set_price(300)
    print(item_2_report.get_parent_data())

    item_3_report = ItemDiscountReport(name='BMW', price=1000, discount=20)
    print(item_3_report)

    item_4_report = ItemDiscountReportName(name='Opel', price=200)
    print(item_4_report.get_info())
    item_5_report = ItemDiscountReportPrice(name='Skoda', price=300)
    print(item_5_report.get_info())
