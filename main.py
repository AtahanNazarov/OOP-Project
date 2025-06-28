from typing import Literal

class Person:
    def __init__(self, name: str, surname: str, sex: Literal["male", "female"], age: int):
        self.name = name
        self.surname = surname
        self.age = age
        self.sex = sex
        
    def get_name(self):
        return self.name

p1 = Person("Edil", "Smith", "male", 12)

print(p1.get_name())
