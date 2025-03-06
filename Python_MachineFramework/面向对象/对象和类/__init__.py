# 在Python中通常使用`class`语句来定义一个类（类对象）
# `class`定义的对象（类）可以用于产生新的对象（实例）。

class Person():
    pass

someone = Person()
print(id(someone), type(someone))

# 类中的属性对应前面所学习的变量，而类中的方法对应前面所学习的函数。
# 通过类，可以把数据和操作封装在一起，从而使得程序结构更加清晰，
# 这也就是所谓的类的封装性。
# 在类的内部，使用`def`关键字可以为类定义一个方法，
# 与一般函数定义不同，方法必须包含参数`self`，且为第一个参数。

class Person():
    name = 'TZ'
    sex = 'F'
    def jump(self):
        print('Jumping!')


# 对象的初始化方法__init__
# 也就是构造方法
class Person():
    def __init__(self, name):
        self.name = name

someone = Person('小明')
print(someone)
print(someone.name)  # 访问类属性