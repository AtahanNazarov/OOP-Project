import unittest
from main import Person, Prisoner, Guard


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
        person = Person("Tom", "Ford", "male", 40)
        person.age = 63
        self.assertEqual(person.age, 63)

    def test_sex_literal(self):
        person = Person("Charlie", "Day", "male", 30)
        self.assertIn(person.sex, ["male", "female"])


class TestPrisoner(unittest.TestCase):
    def test_prisoner_creation(self):
        prisoner = Prisoner("Walter", "White", "male", 50, 101, 50, "Drugs")
        self.assertEqual(prisoner.name, "Walter")
        self.assertEqual(prisoner.sentence_years, 5)
        self.assertEqual(prisoner.commited_crime, "Drugs")


class TestGuard(unittest.TestCase):
    def test_guard_creation(self):
        guard = Guard("Alan", "Turing", "male", 41, 201, "Warden")
        self.assertEqual(guard.rank, "Warden")

    def test_guard_id(self):
        guard = Guard("Jane", "Doe", "female", 45, 201, "Warden")
        self.assertEqual(guard.guard_id, 201)


if __name__ == "__main__":
    unittest.main()
