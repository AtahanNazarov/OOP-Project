import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        return math.dist([self.x, self.y], [other.x, other.y])


def dist(points):
    sum = 0
    for i in range(len(points)-1):
        sum += points[i].distance(points[i+1])
    return sum


class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def length(self):
        return self.p1.distance(self.p2)


# tests
p1 = Point(1, 2)
p2 = Point(4, 6)
p3 = Point(2, 8)

print(p1.x, p1.y)
print("distance of p1 and p2:", p1.distance(p2))

points = [p1, p2, p3]
print("sum of distances:", dist(points))

line = Line(p1, p2)
print("length:", line.length())


class Age:
    def __init__(self):
        self.age = 0

    # setter
    def set_age(self, age):
        if 0 <= age <= 150:
            self.age = age
        else:
            print("error! invalid age")

    # getter
    def get_age(self):
        return self.age

    def birthday(self):
        self.age+= 1
        print(
            f"Happy birthday!"
            f"You are now aged {self.age}!"
        )


# age test
old_guy = Age()

print(old_guy.get_age())

old_guy.set_age(140)
print(old_guy.get_age())

old_guy.birthday()
print(old_guy.get_age())

old_guy.set_age(151)


class Person:
    def __init__(self, name: str, surname: str, age: Age):
        self.name = name
        self.surname = surname
        self.age = age
        
     # getter
    def get_age(self):
        return self.age

atakhan_age = Age()  
atakhan_age.set_age(21)
 
atakhan = Person("Atakhan", "Nazarov", atakhan_age)

print("Atakhan's age:", atakhan.get_age().get_age())
