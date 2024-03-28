class Base:
    def __init__(self, name):
        self.name = name
    def get_name(self):
        return self.name
class Child_1(Base):
    def __init__(self,name,age):
        Base.__init__(self,name)
        self.age = age
    def get_age(self):
        return self.age
class Grand_child(Child_1):
    def __init__(self,name, age, address):
        Child_1.__init__(self, name,age)
        self.address = address
    def get_address(self):
        return self.address

#obj_1 = Base("Vishwajit")
#print(obj_1.name)

#obj_2 = Child_1("Vishwait", 21)
#print(obj_2.get_name(), obj_2.get_age())

obj_3 = Grand_child("Vishwait", 23, "Kodoli")
print(obj_3.get_name(), obj_3.get_age(), obj_3.get_address())