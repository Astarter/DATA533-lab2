import livestocks.livestock
import livestocks.cow



print(livestocks.livestock)

c1 = livestocks.livestock.Livestock("ben")
c2 = livestocks.cow.Cow("Tim", 200)

c1.intoduce()
c1.display()


c2.display()