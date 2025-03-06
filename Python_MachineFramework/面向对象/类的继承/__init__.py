class A():
    def foo(self):
        print('A.foo')

    def zoo(self):
        print('A.zoo')


class B(A):  # B 类将继承 A 类的所有属性和方法。
    def fooo(self):
        super().foo()  # 使用 super() 函数调用父类 A 的 foo方法。
        print('B.foo')

    def bar(self):
        print('B.bar')


a = A()
b = B()
b.bar()



