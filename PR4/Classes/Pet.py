class Pet:

    def __init__(self, pet_id, kind, name, animal_species, gender, size):
        self.id = pet_id
        self.kind = kind
        self.name = name
        self.animal_species = animal_species
        self.gender = gender
        self.size = size

    def __eq__(self, other):
        return self.id == other.id
    def __str__(self):
        return f"""Животное: {self.kind}, 
            Порода - {self.animal_species},
            Зовут - {self.name}, 
            пол - {self.gender}"""


p1 = Pet(pet_id=1, kind="Кот", name="Сэм", animal_species="Британский", gender="М", size="Маленький")
p2 = Pet(pet_id=2, kind="Собака", name="Джек", animal_species="Лайка", gender="М", size="Большая")
p3 = Pet(pet_id=3, kind="Собака", name="Лейла", animal_species="Немецкая овчарка", gender="Ж", size="Большая")
p4 = Pet(pet_id=4, kind="Кот", name="Яся", animal_species="Сфинкс", gender="Ж", size="Маленький")
p5 = Pet(pet_id=5, kind="Собака", name="Лора", animal_species="Йорик", gender="Ж", size="Маленький")
p6 = Pet(pet_id=3, kind="Собака", name="Лейла", animal_species="Немецкая овчарка", gender="Ж", size="Большая")

#print(p1==p3, p3==p6)