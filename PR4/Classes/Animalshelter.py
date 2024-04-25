import Volunteer
import Aviary


class AnimalShelter:

    def __init__(self, shelter_id, name:str, volunteers:list, aviaries:list):
        self.shelter_id = shelter_id
        self.name = name
        self.volunteers = volunteers
        self.aviaries = aviaries

    def __eq__(self, other):
        return self.shelter_id == other.shelter_id
    
    def __str__(self):
        return f"{self.shelter_id}, название - '{self.name}', Волонтеры - {self.volunteers}, Вольеры - {self.aviaries} "
