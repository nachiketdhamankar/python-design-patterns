class Dog:
	"""One of the objects to be returned"""

	def speak(self):
		return "Woof!"

	def __str__(self):
		return "Dog"


class DogFactory:
	"""Concrete Factory"""
	# This class creates an object of the concrete (basic) class, that is, Dog class. Similar to this, there will be a CatFactory to create an object of of Cat class

	def get_pet(self):
		"""Returns a new Dog object"""
		return Dog()

	def get_food(self):
		"""Returns a Dog Food object"""
		return "Dog Food!"

class Cat:
	"""One of the objects to be returned(other being Dog)"""

	def speak(self):
		return "Meow!"

	def __str__(self):
		return "Cat"


class CatFactory:
	"""The other Concrete Factory"""
	# This is the other CatFactory class mentioned in the DogFactory class

	def get_pet(self):
		"""Returns a new Dog object"""
		return Cat()

	def get_food(self):
		"""Returns a Dog Food object"""
		return "Cat Food"


class PetStore:
	""" PetStore houses our Abstract Factory """
	# This is the abstract factory that is used to dispense out the concrete classes. That is, the client uses this class to create an object of the desired class.

	def __init__(self, pet_factory=None):
		""" pet_factory is our Abstract Factory """
		self._pet_factory = pet_factory


	def show_pet(self):
		""" Utility method to display the details of the objects retured by the DogFactory """
		# The client calls this method to get the instance of the desired object.

		pet = self._pet_factory.get_pet()
		pet_food = self._pet_factory.get_food()

		print("Our pet is '{}'!".format(pet))
		print("Our pet says hello by '{}'".format(pet.speak()))
		print("Its food is '{}'!".format(pet_food))


#Create a Concrete Factory
# dog_factory = DogFactory()
cat_factory = CatFactory()

#Create a pet store housing our Abstract Factory
# shop_dog = PetStore(dog_factory)
shop_cat = PetStore(cat_factory)

#Invoke the utility method to show the details of our pet
# shop_dog.show_pet()
shop_cat.show_pet()
