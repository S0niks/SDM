from Classes.Pet import Pet

class Aviary:

    def __init__(self, aviary_id, size, availability_of_walking, pets_id, places):
        self.id = aviary_id
        self.size = size
        self.availability_of_walking = availability_of_walking
        self.pets_id = pets_id
        self.places = places

    def __eq__(self, other):
        return self.id == other.id

    def __str__(self):
        return f"ID {self.id}, Размер: {self.size}, Выгул: {self.availability_of_walking}, Содержит питомцев:{self.pets_id}"
