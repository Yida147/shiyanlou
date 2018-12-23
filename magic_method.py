class Animal(object):
    def __new__(cls,name):
        print('__new__')
        return super(Animal,cls).__new__(cls)
    def __init__(self,name):
        print('__init__')
        self.name = name
    def __del__(self):
        print('__del__')

cat = Animal('tom')
print(cat.name)
del cat
