class Dog:
    """ Simple dog class """
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print('Woof!')

class Cat:
    """ Simple cat class """
    def __init__(self, name):
        self.name = name

    def speak (self):
        print('Meow!')

def get_pet(pet="dog"):
    """ The factory method """
    pets = dict(dog=Dog('Hope'), cat=Cat('Peace'))
    return pets[pet]

dog_variable = get_pet("dog")
print(dog_variable.speak())

cat_variable = get_pet('cat')
print(cat_variable.speak())