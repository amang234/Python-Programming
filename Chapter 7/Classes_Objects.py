class Student:
    def set_name(self,name):
        self.name = name # Class Attribute

    def get_name(self):
        return self.name
        
Student1 = Student()
Student1.set_name("Aman")
Student1.eng_marks  = 95 # Instance attribute
print(Student1.name)
print(Student1.get_name())
print(Student1.eng_marks)

Student2 = Student()
Student2.set_name("Ravi")
print(Student2.get_name())
