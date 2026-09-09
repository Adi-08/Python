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