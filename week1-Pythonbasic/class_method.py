class Animal(object):
    owner = 'jack'
    def __init__(self, name):
        self._name = name
    @classmethod
    def get_owner(cls):
        return print(cls.owner)
    @classmethod
    def set_owner(cls, name):
        cls.owner = name
    @staticmethod
    def order_animal_food():
        print('ordering...')
        print('ok')

Animal.order_animal_food()
