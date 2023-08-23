class Student:
    name = ""
    gender = None
    age = None

    def __init__(self, _name="", _gender=None, _age=None):
        self.name = _name
        self.gender = _gender
        self.age = _age

    def say(self):
        print(f"hello {self.name}")

    def say1(self, others: str):
        print(f"hello {self.name}, {others}")

    def __str__(self) -> str:
        return f"{self.name} 是 {self.gender}, 目前{self.age}岁"


stu1 = Student()
stu1.name = "asd"
print(stu1.say())
print(stu1.say1("asdakdjs"))

stu2 = Student("ccc", "2", 11)
print(stu2.say())
print(stu2)
