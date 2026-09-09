#  Single level inheritance 

class Employee:   #Parent class
    in_time = "9 AM"
    out_time = "5 PM"

class Teacher(Employee): ## Child class which inherits the properties of parent class employee 
    def __init__(self,name,subject):
        self.name = name
        self.subject = subject

    def get_info(self):
        print(f"{self.name} teaches {self.subject} subject. Working time of {self.name} is {self.in_time} to {self.out_time} ")

t1 = Teacher("Swati", "Science")
t1.get_info()

# -----------------------xox-----------------------------xox-------------------------xox--------------------------------------xox--------------------------xox

# Multiple Inheritance
# One child class inherits from TWO parent classes
# Father + Mother → Son

class Father:
    def __init__(self, f_name):
        self.f_name = f_name

class Mother:
    def __init__(self, m_name):
        self.m_name = m_name

class Son(Father, Mother):
    def __init__(self,s_name):
        Father.__init__(self, "Sanjay")
        Mother.__init__(self, "Charu")
        self.s_name = s_name

    def get_info(self):
        print(f"{self.s_name} is the son of {self.f_name} and {self.m_name}")


s1 = Son("Aditya")
s1.get_info()


# Color + Company → Car


class Color:
    def __init__(self, color):
        # Store the color of the car
        self.color = color


class Company:
    def __init__(self, brand):
        # Store the company/brand of the car
        self.brand = brand


# Car inherits from both Color and Company
class Car(Color, Company):

    def __init__(self, model):
        # Store Car's own information
        self.model = model

        # Call Color's __init__() to set the color
        Color.__init__(self, "Red")

        # Call Company's __init__() to set the brand
        Company.__init__(self, "BMW")

    def get_info(self):
        # Use data from Car, Color and Company
        print(f"{self.model} is a {self.color} car of {self.brand} company")


# Create an object of Car
car1 = Car("M5")

# Call the method
car1.get_info()

# Output:
# M5 is a Red car of BMW company


# -------------------------xox--------------------------------------------------xox-------------------------------------------------------xox



