from Pet import Pet

class PetRepository:

    def __init__(self):
        self.pets = []

    def add_pet(self, pet:Pet):
        self.pets.append(pet)

    def del_pet(self, pet:Pet):
        self.pets.remove(pet)

    def find_pet(self, pet_id):
        for p in self.pets:
            if (p.pet_id == pet_id):
                return p
            
    def show_pets(self):
        for p in self.pets:
            print(f"{p.name}, {p.kind}, {p.gender}")
