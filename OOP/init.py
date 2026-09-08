class Student:
    def __init__(self, name, age =18):
        self.name = name
        self.age = age

s1 = Student("Aditya")
s2 = Student("Akash", 20)
print(s1.name, s1.age)
print(s2.name, s2.age)