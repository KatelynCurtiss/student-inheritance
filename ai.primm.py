<<<<<<< HEAD
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

    def analyze(self):
        print(f"AI is analyzing data.")
        # print(AI.analyze)

        # AI.analyze()


class Robot(Human):
    def __init__(self, name, age, occupation, color):
        self.color = color 
        super().__init__(name, age, occupation)
    
    def think(self):
        print(f"The robot is thinking about its future.")

    def communicate(self):
        print("The robot is communicating digitally with a human.")

    def learn(self):
        print("The robot is learning and improving its capabilities.")



my_ai = AI("Athena", 5, "Virtual Assistant", 9.8)
# print(my_ai.name)
# print(my_ai.age)
# print(my_ai.occupation)
# print(my_ai.intelligence_level)
# my_ai.think()
# my_ai.communicate()
# my_ai.learn()
my_ai.analyze()

# print()
# my_robot = Robot("Samuel",2, "Cleaning Robot", "Purple")
# print(f"The name of my new robot is {my_robot.name}.")
# print(f"The job title of my new robot is {my_robot.occupation}.")
# Use the think ( ) method with our new robot
# my_robot.think()
=======
# Katelyn Curtiss
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

def analyze(self):
        print(f"AI is analyzing data.")
        print(AI.analyze)

        AI.analyze()


class Robot(Human):
    def __init__(self, name, age, occupation, color):
        self.color = color 
        super().__init__(name, age, occupation)
    
    def think(self):
        print(f"The robot is `perform_task()`.")

    def communicate(self):
        print("The robot is communicating digitally with a human.")

    def learn(self):
        print("The robot is learning and improving its capabilities.")




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

### I(nvestigate)

Answer these questions about the code snippet:

1. What is the relationship between the Human and AI classes?
   They are parent and child classes.
2. How does the `__init__()` method in the AI class use the `super()` function?
   It uses it to take the methods fromt the parent classes.
3. How does the output of the `think()` and `communicate()` methods differ between the Human and AI instances?
   They differ on the input that is given to the user. 
4. Which attributes will the AI class get/grab from the Human class?
    Self, name, age, and occupation.
5. Which attribute belongs specifically to the AI class?
    Intelligence_level
6. How many attributes **total** will an instance of the AI class have?
    5
---
>>>>>>> add8b1b4472b33879cb5d6d2cee8bcea9e1db316
