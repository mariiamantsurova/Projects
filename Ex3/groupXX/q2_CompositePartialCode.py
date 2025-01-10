# Component: Base class for both Leaf and Composite
class PackageComponent:

    def get_price(self):
        pass

    def show_details(self, indent=0):
        pass


# Leaf: Individual items
class Item(PackageComponent):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_price(self):
        return self.price

    def show_details(self, indent=0):
        print(f"Item: {self.name}, Price: {self.price}")


# Composite: Packages containing items or other packages
class Package(PackageComponent):
    pass


if __name__ == '__main__':

    # Create Items
    item1 = Item("Laptop", 1200)
    item2 = Item("Mouse", 25)
    item3 = Item("Keyboard", 75)
    item4 = Item("Monitor", 200)

    # Create a package and add items
    package1 = Package("Office Essentials")
    package1.add_component(item2)
    package1.add_component(item3)

    # Create another package and add items/packages
    main_package = Package("Workstation Setup")
    main_package.add_component(item1)
    main_package.add_component(item4)
    main_package.add_component(package1)

    # Show details and total price
    main_package.show_details()
    print(f"Total Price of Workstation Setup: {main_package.get_price()}")
