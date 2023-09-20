class Student:
    def __init__(self, name, rollNo):
        self.name = name
        self.rollNo = rollNo
        self.lap = self.Laptop()

    def show(self):
        print(self.name, self.rollNo)
        self.lap.show()

    class Laptop:
        def __init__(self):
            self.brand = "Lenovo"
            self.cpu = "i5"
            self.ram = 16

        def show(self):
            print(self.brand, self.cpu, self.ram)

s1 = Student("Shaheer", 286021)
s2 = Student("Hamza", 290951)

s1.show()

lap1 = s1.lap
lap2 = s2.lap
