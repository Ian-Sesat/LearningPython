
class Animal():
    def __init__(self,habitat):
        self.habitat=habitat
    def print_habitat(self):
        print('The habitat of the animal is {}'.format(self.habitat)) 
    def animalFood(self):
        food='Some animal food'
        print('The animal eats: {}'.format(food))
class Dog(Animal):
    def __init__(self):
        super().__init__('Kennel')
    def animalFood(self):
        food='Bones'
        print('The animal eats: {}'.format(food))
    
dog=Dog()
dog.print_habitat()
dog.animalFood()

