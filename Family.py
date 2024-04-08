class Anna:
    def __init__(self,name):
        self.name = name
    def get_name(self):
        return self.name

class Baba(Anna):
    def __init__(self,name,age):
        Anna.__init__(self,name)
        self.age = age
    def get_age(self):
        return self.age

class Vishwajit(Baba):
    def __init__(self,name,age,address):
        Baba.__init__(self,name,age)
        self.address =address
    def get_address(self):
        return self.address

a = Anna("Vijaysingh")
print(a.get_name())

b = Baba("Amarsingh", 53)
print(b.get_name())
print(b.get_age())

v = Vishwajit("Vishwajit", 21, "Kodoli")
print(v.get_name())
print(v.get_age())
print(v.get_address())