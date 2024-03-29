from PetRepository import PetRepository
from AviaryRepository import AviaryRepository
from AnimalShelterRepository import AnimalShelterRepository
from Animalshelter import AnimalShelter
from Volunteer import Volunteer
from Aviary import Aviary
from Pet import Pet
#Бизнес логика:
# 1)Вольер имеет определенное количество мест
# 2)Большие и маленькие собаки не могут сидеть вместе
# 3)Волонтёр закреплен за одним приютом
# 4)Животное не может числиться в двух вольерах одновременно
# 5)Вольер закреплён за одним приютом

def add_aviary_to_animalshelter(shelter_id, aviary_id):
    if not aviaryrepository.find_aviary(aviary_id):
        return "Вольер отсутствует в репозитории"
    if not animalshelterrepository.find_animalshelter(shelter_id):
        return "Приют отсутствует"
    else:
     for shelter in animalshelterrepository.animalshelters:
          for aviary in shelter.aviaries:
               if aviary == aviary_id:
                    return "Такой вольер уже существует"
     animalshelterrepository.find_animalshelter(shelter_id).aviaries.append(aviary_id)
     return "Успешно добавлено"

def add_volunteer_to_animalshelter(shelter_id, volunteer:Volunteer):
     if not animalshelterrepository.find_animalshelter(shelter_id):
          return "Приют отсутствует"
     else: 
          for shelter in animalshelterrepository.animalshelters:
               for v in shelter.volunteers:
                    if v == volunteer:
                         return "Такой волонтер уже работает в другом приюте"
          animalshelterrepository.find_animalshelter(shelter_id).volunteers.append(volunteer)
          return "Успешно добавлено"

def add_pet_to_aviary(aviary_id, pet_id):
     pet = petrepository.find_pet(pet_id)
     if not pet:
          return "Такой питомец не найден"
     else: 
          for s in animalshelterrepository.animalshelters:
               for a in s.aviaries:
                    for p in aviaryrepository.find_aviary(a).pets_id:
                         if p == pet_id:
                              return "Такой питомец уже добавлен в вольер"
     aviary = aviaryrepository.find_aviary(aviary_id)
     if not aviary:
          return "Вольер отсутствует"
     else: 
          if aviary.size != pet.size:
               return "Размер питомца не соответствует размеру вольера"
          if len(aviary.pets_id) >= aviary.places:
               return "Вольер переполнен"
          aviary.pets_id.append(pet_id)
          return "Успешно добавлено"

aviaryrepository = AviaryRepository()
petrepository = PetRepository()
animalshelterrepository = AnimalShelterRepository()

v = [Volunteer("Яковченко Софья Александровна", 89832957532), 
     Volunteer("Жихарев Иван Аркадьевич", 89835568900),
     Volunteer("Николаев Павел Владимирович", 89833667834)]

petrepository.add_pet(Pet(pet_id=1, kind="Кот", name="Сэм", animal_species="Британский", gender="М", size="Маленький"))
petrepository.add_pet(Pet(pet_id=2, kind="Собака", name="Джек", animal_species="Лайка", gender="М", size="Большой"))
petrepository.add_pet(Pet(pet_id=3, kind="Собака", name="Лейла", animal_species="Немецкая овчарка", gender="Ж", size="Большой"))
petrepository.add_pet(Pet(pet_id=4, kind="Кот", name="Яся", animal_species="Сфинкс", gender="Ж", size="Маленький"))
petrepository.add_pet(Pet(pet_id=5, kind="Собака", name="Лора", animal_species="Йорик", gender="Ж", size="Маленький"))
petrepository.add_pet(Pet(pet_id=6, kind="Собака", name="Лайма", animal_species="Немецкая овчарка", gender="Ж", size="Большой"))
petrepository.add_pet(Pet(pet_id=7, kind="Кот", name="Вася", animal_species="Сибирский", gender="М", size="Маленький"))

aviaryrepository.add_aviary(Aviary(aviary_id=1, size="Большой", availability_of_walking="С выгулом", pets_id=[2, 3], places=2))
aviaryrepository.add_aviary(Aviary(aviary_id=2, size="Маленький", availability_of_walking="Без выгула",  pets_id=[1, 4], places=4))
aviaryrepository.add_aviary(Aviary(aviary_id=3, size="Маленький", availability_of_walking="С выгулом", pets_id=[5], places=2))

animalshelterrepository.add_animalshelter(AnimalShelter(shelter_id=1, name="Мокрый нос", volunteers=[], aviaries=[1]))
animalshelterrepository.add_animalshelter(AnimalShelter(shelter_id=2, name="Сухой нос", volunteers=[v[0]], aviaries=[]))


