import unittest
from main import add_aviary_to_animalshelter, add_pet_to_aviary, add_volunteer_to_animalshelter
from Volunteer import Volunteer

class TestFunctions(unittest.TestCase):

    def test_add_aviary_to_animalshelter(self):
        # Тест на проверку наличия вольера в репозитории
        self.assertEqual(add_aviary_to_animalshelter(1, 4), "Вольер отсутствует в репозитории")

        # Тест на проверку наличия приюта в репозитории
        self.assertEqual(add_aviary_to_animalshelter(3, 1), "Приют отсутствует")
        # Тест на проверку наличия вольра в приюте
        self.assertEqual(add_aviary_to_animalshelter(1, 1), "Такой вольер уже существует")
        # Тест на успешное добавление
        self.assertEqual(add_aviary_to_animalshelter(1, 2), "Успешно добавлено")

    def test_add_volunteer_to_animalshelter(self):
        # Тест на наличие волонтёров в других приютах
        self.assertEqual(add_volunteer_to_animalshelter(1, Volunteer("Яковченко Софья Александровна", 89832957532)), "Такой волонтер уже работает в другом приюте")
        # Тест на наличие приюта в репозитории
        self.assertEqual(add_volunteer_to_animalshelter(3, Volunteer("Яковченко Софья Александровна", 89832957532)), "Приют отсутствует")
        # Тест на успешное добавление волонтёра
        self.assertEqual(add_volunteer_to_animalshelter(1, Volunteer("Жихарев Иван Аркадьевич", 89835568900)), "Успешно добавлено")

    def test_add_pet_to_aviary(self):
        # Тест на наличие питомца в репозитории
        self.assertEqual(add_pet_to_aviary(1, 12), "Такой питомец не найден")
        # Тест на наличие питомца в другом вольере
        self.assertEqual(add_pet_to_aviary(1,1), "Такой питомец уже добавлен в вольер")
        # Тест на наличие вольера в репозитории
        self.assertEqual(add_pet_to_aviary(11, 6), "Вольер отсутствует")
        # Тест на соответствие размера питомца и размера вольера
        self.assertEqual(add_pet_to_aviary(2,6), "Размер питомца не соответствует размеру вольера")
        # Тест на проверку кол-ва мест в вольере
        self.assertEqual(add_pet_to_aviary(1,6), "Вольер переполнен")
        # Тест на успешное добавление питомца
        self.assertEqual(add_pet_to_aviary(3,7), "Успешно добавлено")


if __name__ == '__main__':
    unittest.main()