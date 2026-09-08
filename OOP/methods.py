class Student:
    clg = "KSE"

    #### Instance Method
    def __init__(self, name):
        self.name= name

    def introduce(self):
        print("Welcome:",self.name)

    ##### class Method

    @classmethod
    def intro_clg(cls):
        print("To", cls.clg, "!!")

s1 = Student("Aditya")
s1.introduce()
s1.intro_clg()