import random
class Vehicle:
    def __init__(self, p, l):
        self.price = p
        self.length = l
    def get_price(self):
        return self.price
    def is_more_expensive(self, v):
        return (self.price > v.price)

class Car(Vehicle):
    passengers = 4
    def get_passengers(self):
        return self.passengers
    def get_color(self):
        colors=["red","orange","green","yellow","blue","brown","gold","grey","black"]
        blank=random.choice(colors)
        self.colour=blank
        return self.colour


x = Vehicle(1000, 5)
y = Vehicle(2000, 6)
print(x.is_more_expensive(y))

z = Car(10000, 5)
print(z.get_passengers())
v = Car(12,23)
print(v.get_color())