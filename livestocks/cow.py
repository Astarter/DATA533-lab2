from livestocks.livestock import Livestock


class Cow(Livestock):
    def __init__(self, owner, price):
        Livestock.__init__(self, owner)
        self.price = price

    def makeSound(self):
        print("Mooooooooooo!!!")

    def setPrice(self, price):
        self.price = price

    def getPrice(self):
        return self.price

    def display(self):
        print("%s's cow can be sold at %.2f dollars" % (self.owner, self.price))