from typing import Literal

# class Prison:
#     def __init__(self, name: str, capacity: int):
#         self.name = name
#         self.capacity = capacity

#     def add_prisoner(self, prisoner_: str):
#         self.prisoner_name = prisoner_name

# def get_name(self):
# return self.name


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


p1 = Person("Edil", "Smith", "male", 12)
p2 = Prisoner("John", "Biedronka", "male", 30, 1, 5, "Robbery")

p1.get_info()
p2.get_info()
