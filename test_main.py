import unittest
import random
from main import Prison, Person, Prisoner, Guard


class TestPerson(unittest.TestCase):
    def test_person_creation(self):
        person1 = Person("Jakub", "Dino", "male", 57)
        self.assertEqual(person1.age, 57)  # this should pass

    def test_person_creation_fail(self):
        person1 = Person("Jakub", "Dino", "male", 57)
        self.assertEqual(person1.age, 58)  # this should fail, age is 57

    def test_invalid_age(self):
        person = Person("Anna", "Stokrotka", "female", 600)
        # this should pass, age cannot be 600
        self.assertNotEqual(person.age, 600)

    def test_invalid_age_fail(self):
        person = Person("Anna", "Stokrotka", "female", 600)
        # this should fail, age not set to 600
        self.assertEqual(person.age, 600)

    def test_set_age(self):
        person = Person("Tom", "Ford", "male", 40)
        person.age = 63
        self.assertEqual(person.age, 63)  # this should pass

    def test_set_age_fail(self):
        person = Person("Tom", "Ford", "male", 40)
        person.age = 600
        self.assertEqual(person.age, 63)  # this should fail, age remains 40

    def test_sex_literal(self):
        person = Person("Charlie", "Day", "male", 30)
        self.assertIn(person.sex, ["male", "female"])  # this should pass

    def test_sex_literal_fail(self):
        person = Person("Charlie", "Day", "male", 30)
        self.assertIn(person.sex, ["female"])  # this should fail, sex is male


class TestPrisoner(unittest.TestCase):
    def test_prisoner_creation(self):
        prisoner = Prisoner("Walter", "White", "male", 50, 101, 50, "Drugs")
        self.assertEqual(prisoner.commited_crime, "Drugs")  # this should pass

    def test_prisoner_creation_fail(self):
        prisoner = Prisoner("Walter", "White", "male", 50, 101, 50, "Drugs")
        # this should fail, crime is Drugs
        self.assertEqual(prisoner.commited_crime, "Robbery")

    def test_prisoner_creation_not_equal(self):
        prisoner = Prisoner("Walter", "White", "male", 50, 101, 50, "Drugs")
        # this should pass, crime is Drugs
        self.assertNotEqual(prisoner.commited_crime, "Robbery")

    def test_try_escape_success_or_fail(self):
        prisoner = Prisoner("Walter", "White", "male", 50, 101, 10, "Drugs")
        prison = Prison("Test Prison")
        prison.add_prisoner(prisoner)
        # Patch random.random to always return 0.05 (escape succeeds)

        def always_escape():
            return 0.05

        def always_fail():
            return 0.5

        # Use them in your test:
        original_random = random.random
        random.random = always_escape
        prisoner.try_escape(prison)
        # Should be removed from prison
        self.assertNotIn(prisoner, prison.prisoners)

        # Patch random.random to always return 0.5 (escape fails)
        prison.add_prisoner(prisoner)
        random.random = always_fail
        prisoner.try_escape(prison)
        self.assertIn(prisoner, prison.prisoners)  # Should still be in prison
        self.assertEqual(prisoner.sentence_years, 13)  # 3 years added

        # Restore original random
        random.random = original_random


class TestGuard(unittest.TestCase):
    def test_guard_creation(self):
        guard = Guard("Alan", "Turing", "male", 41, 201, "Warden")
        self.assertEqual(guard.rank, "Warden")  # this should pass

    def test_guard_creation_fail(self):
        guard = Guard("Alan", "Turing", "male", 41, 201, "Warden")
        # this should fail, rank is Warden
        self.assertEqual(guard.rank, "Officer")

    def test_guard_id(self):
        guard = Guard("Jane", "Doe", "female", 45, 201, "Warden")
        self.assertEqual(guard.guard_id, 201)  # this should pass

    def test_guard_id_fail(self):
        guard = Guard("Jane", "Doe", "female", 45, 201, "Warden")
        self.assertEqual(guard.guard_id, 202)  # this should fail, id is 201


if __name__ == "__main__":
    unittest.main()
