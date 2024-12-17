class FruitItem:
    # global variable
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
        return f"Fruit Name: {self.name}, Price: {float(self.price)}, Shelf time: {self.shelf_time_in_hours} hours"


class FruitBasket:
    def __init__(self):
        self.fruit_list = []

    def AddFruitItem(self, fruit):
        self.fruit_list.append(fruit)


    ## to ask if the function need to return the self.fruit_list or return a message if not found or return none?
    def DefFruitItem(self, fruit):
        for f in self.fruit_list:
            if f.name == fruit.name and f.price == fruit.price:
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
        self.holiday_greeting = holiday_greeting




##########################
"""
Banana = FruitItem("Banana", 25, 10)
Apple = FruitItem("Apple", 2.5, 11)
Fruit_Basket = FruitBasket()
print(Fruit_Basket.BasketPrice())
print(Fruit_Basket.BasketShelfTime())
Fruit_Basket.AddFruitItem(Apple)
Fruit_Basket.AddFruitItem(Banana)
Apple = FruitItem("Apple", 2.5, 11)
Fruit_Basket.AddFruitItem(Apple)
print(Fruit_Basket)
Fruit_Basket.DefFruitItem(Apple)
print(Fruit_Basket)
Fruit_Basket.DefFruitItem(Apple)
print(Fruit_Basket)
Fruit_Basket.DefFruitItem(Apple)
print(Fruit_Basket)
Fruit_Basket.DefFruitItem(Banana)
print(Fruit_Basket)
"""

########################

# wanted checks:
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
if(b1):
    print(b1)
