from csv import DictReader
from random import choice, uniform, randint


class Item:
    all = []       # variable to store all created instances (aka objects)
    discount = .9  # .1% discount
    def __init__(self, name: str, price: float, quantity: int) -> None:
        # validate received arguments
        assert price >= 0, f'Price is expected to be positive. {price} given.'
        assert quantity >= 0, f'Quantity is expected to be positive. {quantity} given.'

        # assing to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # add object to list
        Item.all.append(self)

    @classmethod
    def instantiate_from_db(cls) -> None:
        with open("items.csv", "r") as f:
            reader = DictReader(f)    # or we could have done
            items = list(reader)      # items = list(DictReader(f))

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
                )

    def getFinalPrice(self) -> float:
        return self.price * self.quantity * self.discount

    def __repr__(self) -> str:
        return f'Item("{self.name}", {self.price}, {self.quantity})'

"""
item1 = Item("Iphone 14", 1099.99, 1)
amount1 = item1.getFinalPrice()
print(round(amount1, 2))

item2 = Item("Pixel 7", 1099.99, 1)
item2.discount = .85    # we modify the "discount" attribute but only for the actual instance
amount2 = item2.getFinalPrice()
print(round(amount2, 2))

for _ in range(4):
    item = Item(choice(["A", "B", "C", "D", "E", "F"]), 
                round(uniform(199.99, 499.99), 2), randint(1, 5))

print(Item.all)    # prints out representation of the instances
                        # we can alter this behaviour by implementing
                        # the __repr__ magic method in our class definition

# show the name of every instance created
for instance in Item.all:
    print(instance.name)
# then for example we could use the filter method to filter the list out
# under custom defined criterias
"""

# now we gonna instantiante from a database (CSV file)
# and to do so we call the class with the correct class method
Item.instantiate_from_db()

# if we check on the list
print(Item.all) # at this moment in time it contains 0 objects because
                # all we have done is showing the items from the db
# another thing to remark here is the reader assumes all the content 
# as str even the price and quantity ones, so we'll have to change that

