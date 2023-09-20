class A:

    def feature1(self):
        print("Feature 1 working...")

    def feature2(self):
        print("Feature 2 working...")

class B:

    def feature3(self):
        print("Feature 3 Working...")

    def feature4(self):
        print("Feature 4 Working...")

class C(A, B):

    def feature5(self):
        print("Feature 5 Working...")




a1 = A()

a1.feature1()
a1.feature2()

b1 = B()
b1.feature3()

c1 = C()
c1.feature5()