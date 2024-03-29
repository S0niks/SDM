from Animalshelter import AnimalShelter

class AnimalShelterRepository:

    def __init__(self):
        self.animalshelters = []
    
    def add_animalshelter(self, animalshelter:AnimalShelter):
        self.animalshelters.append(animalshelter)

    def del_animalshelter(self, animalshelter:AnimalShelter):
        self.animalshelters.remove(animalshelter)

    def find_animalshelter(self, animalshelter_id):
        for a in self.animalshelters:
            if (a.shelter_id == animalshelter_id):
                return a
            
    def show_animalshelters(self):
        for a in self.animalshelters:
            print(a)


