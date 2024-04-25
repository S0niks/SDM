from Classes.Aviary import Aviary
from Classes.Pet import Pet
from Repositories.XMLrepository import XMLRepository

def save_to_xml(pet_data):
    repository = XMLRepository("base.xml")
    repository.save(pet_data)


def find_pet_by_aviary(aviary):
    pet_repository = XMLRepository("base.xml")
    query = f"//item[aviary='{aviary}']"
    pets = pet_repository.find()
    return pets

if __name__ == "__main__":
    pet_data = {
        'pet_id': 1,
        'kind': "Кот",
        'name': "Сэм",
        'animal_species': "Британский",
        'gender': "М",
        'size': "Маленький"
    }
    pet = Pet(**pet_data)
    save_to_xml(pet)
    pet_data = {
        'pet_id': 2,
        'kind': "Собака",
        'name': "Джек",
        'animal_species': "Лайка",
        'gender': "М",
        'size': "Большой"
    }
    pet = Pet(**pet_data)
    save_to_xml(pet)
    pet = Pet(3, 'Собака', 'Лейла', 'Немецкая овчарка', 'Ж', 'Большой')
    save_to_xml(pet)

    aviary_data = {
        'aviary_id': 2,
        'size': 'Маленький',
        'availability_of_walking': 'Без выгула',
        'pets_id': [1, 4],
        'places': 4
    }
    aviary = Aviary(**aviary_data)
    save_to_xml(aviary)
    aviary_data = {
        'aviary_id': 1,
        'size': 'Большой',
        'availability_of_walking': 'С выгулом',
        'pets_id': [2, 3],
        'places': 2
    }
    aviary = Aviary(**aviary_data)
    save_to_xml(aviary)

    print(find_pet_by_aviary('Сэм'))