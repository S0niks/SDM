import Volunteer
import Aviary


class AnimalShelter:

    def __init__(self, shelter_id, name:str, volunteers:list, aviaries:list):
        self.id = shelter_id
        self.name = name
        self.volunteers = volunteers
        self.aviaries = aviaries

    def __eq__(self, other):
        return self.id == other.id
    
    def __str__(self):
        return f"{self.id}, название - '{self.name}', Волонтеры - {self.volunteers}, Вольеры - {self.aviaries} "
