# 是指子类可以对从父类中继承过来的方法进行重新定义，
# 从而使得子类对象可以表现出与父类对象不同的行为。

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        print("姓名:", self.name)
        print("年龄:", self.age)

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def get_info(self):
        super().get_info()
        print("成绩:", self.grade)


def print_info(person):  # 定义普通函数print_info
    print("print_info 函数的输出结果：")
    person.get_info() # 通过person调用get_info方法

p = Person("张三", 17) # 创建 Person 类对象
stu = Student("张三", 17, 80)   # 创建 Student 类对象
p.get_info()
stu.get_info()
print_info(p)
print_info(stu)