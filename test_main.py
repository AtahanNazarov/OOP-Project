import unittest
from main import Person


class TestPerson(unittest.TestCase):
    def test_person_creation(self):
        person1 = Person("Jakub", "Dino", "male", 57)
        self.assertEqual(person1.name, "Jakub")
        self.assertEqual(person1.surname, "Dino")
        self.assertEqual(person1.sex, "male")
        self.assertEqual(person1.age, 57)

    def test_person_creation_fail(self):
        person1 = Person("Jakub", "Dino", "male", 57)
        self.assertEqual(person1.age, 58)  # this should fail

    def test_invalid_age(self):
        person = Person("Anna", "Stokrotka", "female", 600)
        self.assertNotEqual(person.age, 600)

    def test_set_age(self):
        person = Person("Tom", "Ford", "male", 63)
        person.age = 40
        self.assertEqual(person.age, 64)


if __name__ == "__main__":
    unittest.main()
