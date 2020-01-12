class Dog(object):
    '''定义一个类'''

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return "%r" % self.__dict__

    def sit(self):
        print(self.name.title()+" "+"is sitting!")

my_dog = Dog('whillie',6)
print(my_dog.name)
print(my_dog.age)
print(my_dog)