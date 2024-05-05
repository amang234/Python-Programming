class Animal:
    def speaks(self):
        pass

class Dog(Animal):
    def speaks(self):
        print("Barks")

class Cat(Animal):
    def speaks(self):
        print("Meow")

class Lion(Animal):
    def speaks(self):
        print("Roars")

dog = Dog()
cat = Cat()
lion = Lion()

dog.speaks()
cat.speaks()
lion.speaks()