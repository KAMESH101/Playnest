-
class student:

    def __init__(self,name,register_no):
        self.name=name
        self.register_no=register_no
    def display(self):
      print("Name:",self.name)
      print("Register No:",self.register_no)

a=student("John",1001)
b=student("Jack",1002)
print("Program.1")
a.display()
b.display()

#Program.2
class Fruit:
    def __init__(self,color):

        self.color=color

    def display(self):
        print("The color of apple is",self.color)
apple=Fruit("red")
print("Program.2")
apple.display()

#Program.3
class teacher:

    def __init__(self,name,register_no):
        self.name=name
        self.register_no=register_no
    def display(self):
      print("Name:",self.name)
      print("Register No:",self.register_no)

t1=teacher("John",1001)
t2=teacher("Jack",1002)
print("Program.3")
t1.display()
t2.display()

#Program.4
class calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        sum=self.a+self.b
        print("Addition:",sum)
    def subtract(self):
        sub=self.a-self.b
        print("Subtraction:",sub)
    def multiply(self):
        mul=self.a*self.b
        print("Multiply:",mul)
    def division(self):
      if self.b!=0:
        div=self.a/self.b
        print("Division:",div)
      else:
         print("Error")
        
cal=calculator(10,5)
print("Program.4")
cal.add()
cal.subtract()
cal.multiply()
cal.division()


