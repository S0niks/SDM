import sys
sys.path.append('C:\Users\Софья\Desktop\6 семак\Методологии разработки ПО\PR3')
from Classes.Aviary import Aviary

class AviaryRepository:

    def __init__(self):
        self.aviaries = []
    
    def add_aviary(self, aviary:Aviary):
        self.aviaries.append(aviary)

    def del_aviary(self, aviary:Aviary):
        self.aviaries.remove(aviary)

    def find_aviary(self, aviary_id):
        for a in self.aviaries:
            if (a.aviary_id == aviary_id):
                return a
            
    def show_aviaries(self):
        for a in self.aviaries:
            print(f"{a.aviary_id}, {a.size}, {a.availability_of_walking}, {a.pets_id}")



