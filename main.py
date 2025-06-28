from typing import Literal


class Prison:
    def __init__(self, name: str):
        self.name = name
        self.guards = []
        self.prisoners = []

    def add_prisoner(self, prisoner):
        self.prisoners.append(prisoner)

    def get_prisoners(self):
        for prisoner in self.prisoners:
            prisoner.get_info()

    def add_guard(self, guard):
        self.guards.append(guard)

    def get_guards(self):
        for guard in self.guards:
            guard.get_info()


class Person:
    def __init__(self, name: str, surname: str, sex: Literal["male", "female"], age: int):
        self.name = name
        self.surname = surname
        self.sex = sex
        self.age = age

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

    def get_info(self):
        print(
            f"name: {self.name}\n"
            f"surname: {self.surname}\n"
            f"sex: {self.sex}\n"
            f"age: {self.age}\n"
            f"prisoner_id: {self.prisoner_id}\n"
            f"sentence_years: {self.sentence_years}\n"
            f"commited_crime: {self.commited_crime}\n"
        )

    def work(self):
        print(f"Prisoner {self.name} is doing prison work.")


class Guard(Person):
    def __init__(self, name: str, surname: str, sex: Literal["male", "female"], age: int, guard_id: int, rank: Literal["Officer", "Sergeant", "Lieutenant", "Captain", "Warden"]):
        super().__init__(name, surname, sex, age)
        self.guard_id = guard_id
        self.rank = rank

    def get_info(self):
        print(
            f"name: {self.name}\n"
            f"surname: {self.surname}\n"
            f"sex: {self.sex}\n"
            f"age: {self.age}\n"
            f"guard_id: {self.guard_id}\n"
            f"rank: {self.rank}\n"
        )

    def work(self):
        print(f"Guard {self.name} is patrolling the prison.")


person1 = Person("Edil", "Smith", "male", 12)
prisoner2 = Prisoner("John", "Biedronka", "male", 30, 1, 5, "Robbery")
guard1 = Guard("Mike", "Lidl", "male", 40, 101, "Warden")

person1.get_info()
prisoner2.get_info()
guard1.get_info()
prisoner2.work()
guard1.work()

shawshank = Prison("Shawshank")
shawshank.add_prisoner(prisoner2)
shawshank.add_guard(guard1)
shawshank.get_prisoners()
shawshank.get_guards()
