import Student


class Student2(Student.Student):
    height = None

    def __init__(self, _name="", _gender=None, _age=None, _height=None):
        self.name = _name
        self.gender = _gender
        self.age = _age
        self.height = _height

    def setHeight(self, _height: int):
        self.height = _height

    def getHeight(self):
        return self.getHeight


stu1 = Student2()
stu1.name = "asd"
print(stu1.say())
print(stu1.say1("asdakdjs"))

stu2 = Student2("ccc", "2", 11)
print(stu2.say())
print(stu2)
