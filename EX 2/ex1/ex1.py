class FruitItem:
    default_price = 10
    def __init__(self, name, price, shelf_time_in_hours):
        self.name = name
        self.shelf_time_in_hours = shelf_time_in_hours
        if price < FruitItem.default_price:
            self.price = FruitItem.default_price
        else:
            self.price = price

    def getPrice(self):
        return self.price

    def getShelfTime(self):
        return self.shelf_time_in_hours

    # custom print behavior
    def __str__(self):
        return f"Fruit Name: {self.name}, Price: {float(self.price):.2f}, Shelf time: {self.shelf_time_in_hours} hours"


class FruitBasket:
    def __init__(self):
        self.fruit_list = []

    def AddFruitItem(self, fruit):
        self.fruit_list.append(fruit)

    def DelFruitItem(self, fruit):
        for f in self.fruit_list:
            if f == fruit:
                self.fruit_list.remove(f)

    def BasketPrice(self):
        if not self.fruit_list:  # if the basket is empty
            return 0
        basket_price = 0
        for fruit in self.fruit_list:
            basket_price += fruit.getPrice()
        return basket_price

    def BasketShelfTime(self):
        if not self.fruit_list:  # if the basket is empty
            return -1
        return min(self.fruit_list, key=lambda fruit: fruit.shelf_time_in_hours).getShelfTime()

    def __str__(self):
        if not self.fruit_list:  # if the basket is empty
            return 'The Fruit Basket is empty'

        wanted_string = "Printing fruits in basket:\n"
        for fruit in self.fruit_list:
            wanted_string += str(fruit) + "\n"
        return wanted_string

    def __bool__(self):
        if not self.fruit_list:  # if the basket is empty
            return False
        return True

class HolidayFruitBasket(FruitBasket):
    def __init__(self, holiday_greeting):
        super().__init__()
        self.holiday_greeting = holiday_greeting

    def getPrice(self):
        return super().BasketPrice() * 0.95

    def __str__(self):
        if not self.fruit_list:  # if the basket is empty
            return 'The Fruit Basket is empty'

        wanted_string = self.holiday_greeting + "\n"
        for fruit in self.fruit_list:
            wanted_string += str(fruit) + "\n"
        return wanted_string



print("## Wanted Checks For a: ##")
cut_apples = FruitItem('Cut Apples', 15, 4)
print(cut_apples)

strawberries = FruitItem('Strawberries', 22, 6)
print(strawberries)
b1 = FruitBasket()

b1.AddFruitItem(cut_apples)
b1.AddFruitItem(strawberries)
print(b1)
print(b1.BasketPrice())
print(b1.BasketShelfTime())

print("\n## Wanted Checks For b:##")
if(b1):
    print(b1)

print("\n## Wanted Checks For c:##")
b3 = HolidayFruitBasket("Marry Christmas")
b3.AddFruitItem(cut_apples)
b3.AddFruitItem(strawberries)
b3.AddFruitItem(strawberries)
b3.DelFruitItem(cut_apples)
print(b3)
print(b3.getPrice())
print(b3.BasketShelfTime())
