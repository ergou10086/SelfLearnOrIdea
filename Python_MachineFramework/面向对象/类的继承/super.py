class Person():
    def __init__(self, name):
        print("Initializing Person")
        self.name = name


class EmailPerson(Person):
    def __init__(self, name, email):
        print("Initializing EmailPerson")
        super().__init__(name)
        self.email = email


zhangsan = EmailPerson("zhangsan", "123@aaa.com")
print(zhangsan.name, zhangsan.email)