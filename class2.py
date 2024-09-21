# class Animal:
#         def make_sound(self):
#             pass

# class Dog(Animal):
#         def make_sound(self):
#             print("Woof")

# class Cat(Animal):
#         def make_sound(self):
#             print("Meow")
            
#             def animal_sound(animal):
#                   animal.make_sound()
#                   dog = Dog()
#                   cat = Cat()
                  
#                   animal_sound(dog)  # Output: Woof
#                   animal_sound(cat)  # Output: Meow

class Animal:
        def __init__(self) :
              self.limb = 4
              self.eye = 2
              self.stomach = 1
              self.ear = 2
              
        def make_sound(self):
            pass

class Dog(Animal):
        def make_sound(self):
            print("Woof")
        
  
class Cat(Animal):
        def make_sound(self):
            print(f"Meow {self.limb}")


def animal_sound(animal):
        animal.make_sound()

# dog = Dog()
cat = Cat()
print(cat.limb)
        
# animal_sound(dog)  
# animal_sound(cat)  

