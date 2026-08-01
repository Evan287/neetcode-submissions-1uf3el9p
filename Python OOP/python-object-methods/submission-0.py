class Pet:
    def __init__(self, name: str):
        self.name = name
        self.hunger = 5

    def feed(self):
        # TODO: Implement this method
        # It should decrease the pet's hunger by 1
        self.hunger -= 1
        print("Fluffy has been fed.")
        print(f"Fluffy's hunger level: {self.hunger}")
        # and print a message about feeding the pet


# Create a pet
my_pet = Pet("Fluffy")

# TODO: Feed the pet three times
my_pet.feed()
my_pet.feed()
my_pet.feed()