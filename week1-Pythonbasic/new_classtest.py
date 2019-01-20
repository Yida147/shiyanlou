#!/usr/bin/env python3

class UserData(object):
    def __init__(self, id, name):
        self.id = id
        self.name = name
    def __repr__(self):
        return 'ID:{} Name:{}'.format(self.id, self.name)

class NewUser(UserData):
    group = 'shiyanlou-louplus'
    def get_name(self, name):
        return super().__init__(name)
    def get_id(self, id):
        return super().__init__(id)
    def set_name(self, value):
        self.name = value
    @classmethod
    def get_group(cls):
        return cls.group
    @staticmethod
    def format_userdata(id, name):
        return "{}'s id is {}".format(name,id)

if __name__ == '__main__':
    print(NewUser.get_group())
    print(NewUser.format_userdata(109,'Lucy'))
