#!/usr/bin/env python3

class UserData(object):
    def __init__(self, id, name):
        self.id = id
        self._name = name

    def __repr__(self):
        return 'ID:{} Name:{}'.format(self.id, self._name)


class NewUser(object):
    group = 'shiyanlou-louplus'

    def __init__(self, id, name):
        self.id = id
        self._name = name

    def __call__(self):
        return print(self.format_userdata(self.id,self.name))

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if len(value) > 3:
            self._name = value
        else:
            print('Error')

    @classmethod
    def get_group(cls):
        return cls.group

    @staticmethod
    def format_userdata(id, name):
        return "{}'s id is {}".format(name, id)


if __name__ == '__main__':
    user = NewUser(101, 'Jack')
    user()

