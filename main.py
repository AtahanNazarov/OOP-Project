from typing import Literal
import random


class Prison:
    def __init__(self, name: str):
        self.name = name
        self.guards = []
        self.prisoners = []

    def add_prisoner(self, prisoner):
        self.prisoners.append(prisoner)

    def remove_prisoner(self, prisoner):
        if prisoner in self.prisoners:
            self.prisoners.remove(prisoner)
            print(
                f"Prisoner {prisoner.name} {prisoner.surname} has been removed from {self.name}.")
        else:
            print(
                f"Prisoner {prisoner.name} {prisoner.surname} not found in {self.name}.")

    def get_prisoners(self):
        for prisoner in self.prisoners:
            prisoner.get_info()

    def add_guard(self, guard):
        self.guards.append(guard)

    def get_guards(self):
        for guard in self.guards:
            guard.get_info()

    def summary(self):
        print(f"Prison: {self.name}")
        print(f"Total prisoners: {len(self.prisoners)}")
        print(f"Total guards: {len(self.guards)}")

    def year_passed_all(self):
        for prisoner in self.prisoners:
            prisoner.year_passed(self)


class Person:
    def __init__(self, name: str, surname: str, sex: Literal["male", "female"], age: int):
        self.name = name
        self.surname = surname
        self.sex = sex
        self.__age = None
        self.age = age  # use setter for validation

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if 0 <= value <= 150:
            self.__age = value
        else:
            print("Age must be between 0 and 150. Value not set.")

    def get_info(self):
        print(
            f"name: {self.name}\n"
            f"surname: {self.surname}\n"
            f"sex: {self.sex}\n"
            f"age: {self.age}\n"
        )


class Prisoner(Person):
    def __init__(self, name: str, surname: str, sex: Literal["male", "female"], age: int, prisoner_id: int, sentence_years: int, commited_crime: Literal["Murder", "Robbery", "Burglary", "Fraud", "Drugs"],):
        super().__init__(name, surname, sex, age)
        self.prisoner_id = prisoner_id
        self.sentence_years = sentence_years
        self.commited_crime = commited_crime
        self.years_served = 0

    def get_info(self):
        super().get_info()
        print(
            f"prisoner_id: {self.prisoner_id}\n"
            f"sentence_years: {self.sentence_years}\n"
            f"commited_crime: {self.commited_crime}\n"
            f"years_served: {self.years_served}\n"
        )

    def work(self):
        print(f"Prisoner {self.name} is doing prison work.")

    def year_passed(self, prison=None):
        if self.years_served < self.sentence_years:
            self.years_served += 1
            years_left = self.sentence_years - self.years_served
            if years_left > 0:
                print(
                    f"Congrats! Only {years_left} year(s) left to go for {self.name} {self.surname}.")
            else:
                print(f"{self.name} {self.surname} is now free!")
                if prison is not None:
                    prison.remove_prisoner(self)

    def try_escape(self, prison=None):
        chance = random.random()
        if chance < 0.1:
            print(f"{self.name} {self.surname} has escaped from prison!!")
            if prison is not None:
                prison.remove_prisoner(self)
        else:
            self.sentence_years += 3
            print(f"{self.name} {self.surname} failed to escape! 3 years added to sentence. New sentence: {self.sentence_years} years.")


class Guard(Person):
    def __init__(self, name: str, surname: str, sex: Literal["male", "female"], age: int, guard_id: int, rank: Literal["Officer", "Sergeant", "Lieutenant", "Captain", "Warden"]):
        super().__init__(name, surname, sex, age)
        self.guard_id = guard_id
        self.rank = rank

    def get_info(self):
        super().get_info()
        print(
            f"guard_id: {self.guard_id}\n"
            f"rank: {self.rank}\n"
        )

    def work(self):
        print(f"Guard {self.name} is patrolling the prison.")

    def promote(self):
        ranks = ["Officer", "Sergeant", "Lieutenant", "Captain", "Warden"]
        current_index = ranks.index(self.rank)
        if current_index < len(ranks) - 1:
            self.rank = ranks[current_index + 1]
            print(
                f"Congrats! {self.name} {self.surname} has been promoted to {self.rank}!")
        else:
            print(f"{self.name} {self.surname} is already at the highest rank!")


# example usage
shawshank = Prison("Shawshank")
shawshank.summary()


person1 = Person("Michal", "Zabka", "male", 120)
person1.get_info()


prisoner1 = Prisoner("John", "Biedronka", "male", 30, 1, 5, "Robbery")
prisoner2 = Prisoner("Shawn", "Auchan", "male", 25, 2, 3, "Burglary")
prisoner3 = Prisoner("Sarah", "Carrefour", "female", 28, 3, 4, "Fraud")
prisoner2.get_info()


guard1 = Guard("Mike", "Lidl", "male", 40, 101, "Warden")
guard2 = Guard("Sarah", "Netto", "female", 35, 102, "Captain")
guard3 = Guard("Emma", "Aldi", "female", 30, 103, "Lieutenant")
guard1.get_info()


shawshank.add_prisoner(prisoner1)
shawshank.add_prisoner(prisoner2)
shawshank.add_prisoner(prisoner3)
shawshank.get_prisoners()

shawshank.add_guard(guard1)
shawshank.add_guard(guard2)
shawshank.add_guard(guard3)
shawshank.get_guards()


shawshank.summary()


prisoner2.work()
guard1.work()

guard2.promote()
guard2.get_info()

prisoner2.try_escape(shawshank)
prisoner2.get_info()


shawshank.remove_prisoner(prisoner2)
shawshank.year_passed_all()


shawshank.summary()
