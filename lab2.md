# DATA 533: Collaborative Software Development

# Assignment 2

## Collabrators:
- Vicens Paneque Fernandez, 85493799
- Bohan Gao, 25611161

## Overall goal
In this lab, you will work collaboratively in a group of two to develop a Python package. Your package could contain functions that are entirely new to the Python ecosystem, improve upon pre-existing functions or re-implement existing code/functions that you wish to deepen your understanding of (e.g., a linear regression package from scratch). 

## Step 1: Group formation
~~ Students are required to work in a group for this lab. Please form a group (maximum two students) and upload the group information to Canvas by November 25, 2020 at 8.00pm. ~~

## Step 2: Package topic selection (4 marks)
~~ Each group is required to select a topic (i.e., a set of functions) to develop the package. Students need to write a brief description of the package and functions (max 1000 characters, with spaces) that they are planning to implement and upload it to Canvas by November 27, 2020 at 8.00 pm. ~~

### Our topic: Animals

## Step 3: Working on the Package (16 marks)
Now it's time to start developing the package. Specific expectations for this step are:
- Set-up an appropriate directory structure (file and folder organization) for your package [2 marks].
- Use Python to write the package that contains at least four useful functions. These are the functions you proposed in the previous step. [8 marks].
    - Create a package with two subpackages. Each subpackage must have at least two modules and each module should have at least three methods/functions. Each member of the group is expected to do one of the subpackages. 
    - One module must use inheritance.
    - The person who did not write a particular subpackage must write the documentation for the package as well as create a test Python file demonstrating how to use the package.

## Package structure:

```
Just some initial ideas: 

├── package: Animals
│   ├── sub-package1 : pet_animals
|       └── module 1 (at least 2 methods) pet
            └──method __init__: 1 attribute: name(str). 
            └──method 1: makeSound() (print("Hi, I am your pet"))
            └──method 2: display() (like what we did in lab1, just print all attributes.)
|       └── module 2 (at least 2 methods) cat (cat class inherit pet class)
            └──method __init__: 1 additional attribute: name, color. 
            └──method 1: makeSound() (like print("Hi, I am your cat"))
            └──method 2: display()
│   ├── sub-package2 : livestocks
│       └── module 1 (at least 2 methods) livestock
            └──method __init__: 1 attribute: owner(str). (Not all livestock have a name, but they always have an owner) 
            └──method 1: makeSound() (like print("Hi, I am your livestock"))
            └──method 2: display()
|       └── module 2 (at least 2 methods) cow (cow class inherit livestock class)
            └──method __init__: 1 additional attribute: owner(str), price(float).  
            └──method 1: makeSound() (print("Hi, I am your cow"))
            └──method 2: display()
```

- Write a .md file explaining the function details and how they work. Create a test Python file demonstrating how to use the package [2 marks].
- Use version control features to collaborate with your team members. Have a Git history to demonstrates that the group members contributed equally [4 marks]. 

## Submission instructions: 

Please upload the following information (one submission from a group is good enough)
- Step 1: Directly write the information in Canvas lab 2.
- Step 2: Upload a PDF file. Please include both students' information in the file. 
- Step 3: Submit the GitHub classroom link. 

## Resources
- [Python Modules and Packages](https://docs.python.org/3/tutorial/modules.html)
- [Understanding the GitHub flow](https://guides.github.com/introduction/flow/)
