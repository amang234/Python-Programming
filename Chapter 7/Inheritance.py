class Parent:
    def __init__(self):
        self.super_attribute = True
        print("this is a super class")
class Child(Parent):
    def __init__(self):
        super().__init__()
        print("This is a child class")
        print(self.super_attribute)

Child1 = Child()