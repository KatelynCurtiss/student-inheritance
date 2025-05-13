## Inheritance in Python
### PRIMM Activity 

### Objective

Learn how to use the `super()` function in a Python child class to access the attributes and methods found in a parent class.

---

### P(redict)

Predict what the following code snippet will do:
```py
class Human:
    def __init__(self, name, age, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation

    def think(self):
        print("The human is thinking deeply.")

    def communicate(self):
        print("The human is communicating clearly.")

class AI(Human):
    def __init__(self, name, age, occupation, intelligence_level):
        self.intelligence_level = intelligence_level
        super().__init__(name, age, occupation)

    def think(self):
        print("The A`perform_task()` online.")

    def communicate(self):
        print("The AI is communicating digitally with its human.")

    def learn(self):
        print("The AI is learning and improving its capabilities.")

my_ai = AI("Athena", 5, "Virtual Assistant", 9.8)
print(my_ai.name)
print(my_ai.age)
print(my_ai.occupation)
print(my_ai.intelligence_level)
my_ai.think()
my_ai.communicate()
my_ai.learn()
```
---
### R(un)

Copy and paste the previous code snippet into in a file named `ai-primm.py`.

Run the script.  Did your predictions match the output?  Why or why not?

---

### I(nvestigate)

Answer these questions about the code snippet:

1. What is the relationship between the Human and AI classes?
   It is a Parent and Child class.
2. How does the `__init__()` method in the AI class use the `super()` function?
   It uses it by calling the methods from the parents class.
3. What is the purpose of the `think()` and `communicate()` methods in both the Human and AI classes?
   The 'think' method is used to represent a humans thoughts and the 'communication' method is used to represent the expression of thoughts.  
4. How does the output of the `think()` and `communicate()` methods differ between the Human and AI instances?
   They differ by the message given to the user.
5. What is the purpose of the `learn()` method in the AI class?
   It is the method that makes Ai update to the new data given and adjust its behavoir. 
6. Which attributes will the AI class get/grab from the Human class?
   Self, name, age, and occupation.
7. Which attribute belongs specifically to the AI class?
   Intelligence Level.
8. How many attributes **total** will an instance of the AI class have?
   5

---

### M(odify)

- Modify the AI class by adding a new method called `analyze()` that uses an f-string to print a message about the AI analyzing data
- Create a new AI instance named `ai1` and use dot notation to call the `analyze()` method for `ai1`

---

### M(ake)

- Create your own `Robot` class that inherits from the `Human` class
- Your `Robot` class should have its own `__init__()` method that uses the `super()` function to access/borrow the attributes and methods contained in the `Human` class
- In your `Robot` class, define a method `perform_task()`
- The `perform_task()` method should print -- using an f-string -- a short message about the robot performing a specific task

---
