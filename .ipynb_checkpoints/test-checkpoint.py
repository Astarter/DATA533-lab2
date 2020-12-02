from Animals.livestocks.cow import *
from Animals.pet_animals.cat import *

# Test for subpackage 1:
print("This is a test for subpackage1:")
Garfield = Cat("Garfield", "orange")
Garfield.display()
Garfield.sound()
Garfield.intro()
Garfield.sound()
Garfield.describe("lazy")

print("\n")

# Test for subpackage 2:
print("This is a test for subpackage1:")
c1 = Livestock("ben")
c2 = Cow("Tim", 200)

print("Livestock c1:")
c1.intoduce()
c1.display()

print("\n")

print("Cow c2:")
c2.intoduce()
c2.makeSound()
print("The price for c2 is %.2f" % c2.getPrice())
c2.setPrice(1000)
c2.display()


