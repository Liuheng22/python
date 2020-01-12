class Dog():
    '''定义一个类'''

    def _init_(self,name,age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title()+" "+"is sitting!")
