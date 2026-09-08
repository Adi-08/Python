class Students:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def avg(self):
        sum = 0
        for i in self.marks:
            sum +=i
        print("Average marks of", self.name, "is:", sum/3)

s1 = Students("Aditya", [90, 80, 70])
s1.avg()