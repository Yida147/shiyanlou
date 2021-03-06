class Animal(object):
    def __init__(self):
        self.__age = 3
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,value):
        if isinstance(value ,int):
            self.__age = value
        else:
            raise ValueError
    @age.deleter
    def age(self):
        print('delete age')
        del self.__age

if __name__ == '__main__':
    cat = Animal()
    print(cat.age)
    cat.age = 6
    print(cat.age)
    del cat.age
    print(cat.age)
