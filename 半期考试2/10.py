class Animal(object):
    def __init__(self, name):
        self.__name = name

    def speak(self):
        print("I am an animal.")

class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.__species = 'Dog'
        self.name = name
        

    def speak(self):
        print("I am a Dog.")

    def play(self):
       print(f"Dog {self.name} is playing.")

class Cat(Animal):
    def __init__(self, name):
        super(Cat, self).__init__(name)
        self.__species = 'Cat'
        self.name = name 

    def speak(self):
       print("I am a Cat.")

    def play(self):
        print(f"Cat {self.name} is playing.")

class PetShop(object):
    def __init__(self):
        self.item = []
    

    def add_pet(self, pet):
        self.item.append(pet)


    def show_pets(self):
        for animal in self.item :
          
            print(f"{animal.name} is {animal.__class__.__name__}.")
        


def testing_PetShop(pet_dict):
    pet_shop = PetShop()
    for species, name in pet_dict.items():
        species = species.split("_")
        if species[0] == "Dog":
            dog = Dog(name)
            dog.speak()
            dog.play()
            pet_shop.add_pet(dog)
        elif species[0] == "Cat":
            cat = Cat(name)
            cat.speak()
            cat.play()
            pet_shop.add_pet(cat)
        else:
            print("Incorrect dict keys!")
    pet_shop.show_pets()



testing_PetShop({"Dog_1":"Tom", "Dog_2":"Bob", "Cat":"Lucy"})
