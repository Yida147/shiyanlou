class Animal(object):
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, age):
        super(Dog, self).__init__(name)
        # super().__init__(name)
        # Animal.__init__(self,name)
        self.age = age

if __name__ == '__main__':
    dog = Dog('Wangcai',8)
    print(dog.name)
