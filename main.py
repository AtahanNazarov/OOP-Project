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

p1 = Person("Edil", "Smith", "male", 12)

p1.get_info()
