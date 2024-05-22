import sys
#sys.path.append('C:\Users\Софья\Desktop\6 семак\Методологии разработки ПО\PR3')
from Classes.Animalshelter import AnimalShelter


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


