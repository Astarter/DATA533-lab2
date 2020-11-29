# Documentation

### class **pet(name=None)**
Class for pet animals, which should have the following parameters and methods:

**Parameteres**: 
**name**: string value
Contains the name of the pet 

**Methods**:
Method | Desription |
--- | --- |
**intro()** | Returns pet introduction
**display()** | Returns pet information

### class **cat(name=None)**	
**cat** class inherits from **pet** class. 
Class for cats, which should have the following parameters and methods:

**Parameteres**: 
**Name**: string value
Contains the name of the pet 

**Methods**:
Method | Desription |
--- | --- |
**sound()**: | Returns cat sound
**describe(adj)**: | Returns cat’s activity with adjective labels on string adj

### class **livestock(owner=None)**	
Class for livestock animals, which should have the following parameters and methods:

**Parameteres**: 
**owner**: string value
Contains the owner of the livestock 

**Methods**:
Method | Desription |
--- | --- |
**introduce()**: | Returns livestock introduction
**display()**: | Returns livestock information

### class **cow(owner=None, price=None)**	
**cow** class inherits from **livestock** class. 
Class for cow, which should have the following parameters and methods:

**Parameteres**: 
**owner**: string value
Contains the owner of the livestock

**price**: float value
Contains the purchased price of the livestock 

**Methods**:
Method | Desription |
--- | --- |
**makeSound()**: | Returns cow sound
**setPrice(price)**: | Sets the cow’s purchased price
**getPrice(price)**: | Gets the cow’s purchased price
**display()**: | Returns cow information
