class Computer:

    def config(self):
        print("i5, 16GB, 450GB")

# x = 9
#print(type(x))

#a = '8'

#print(type(a))

com1 = Computer()
com2 = Computer()

#print(type(com1))

Computer.config(com1)
Computer.config(com2)

com1.config()
com2.config()