class Animal:
    zoo_name = "Eram Zoo"

    def __init__(self, name, species, age, sound):
        self.name = name
        self.species = species
        self.age = age
        self.sound = sound

    def make_sound(self):
        print(f"{self.name} sings: {self.sound}")

    def info(self):
        print(str(self))

    def __str__(self):
        return f"Name: {self.name}\nSpecies: {self.species}\nAge: {self.age}\nSound: {self.sound}\nZoo: {Animal.zoo_name}"


class Bird(Animal):
    def __init__(self, name, species, age, sound, wing_span):
        Animal.__init__(self,name, species, age, sound)
        self.wing_span = wing_span

    def make_sound(self):
        print(f"\n--->  bird sound \n{self.name} sings: {self.sound}")

    def __str__(self):
        base_info = Animal.__str__(self)    #super().__str__()
        return f"{base_info}\nWing Span: {self.wing_span} cm"

#test animal
lion = Animal("Lion", "Shir", 2, "Haaay")
print("=== Animal Test ===")
lion.info()
lion.make_sound()

#test bird
parrot = Bird("Parrot", "Toti", 5, "Tweet tweet", 25)
print("\n\n=== Bird Test ===")
parrot.info()
parrot.make_sound()