# -*- coding: utf-8 -*-

"""this is the base clasee"""
class BaseClass:
    def __init__(self, name):
        self.name=name
        print('init name=%s' % name)

    def who(self):
        print('in base class')
        print(self.name)

"""this is the diver clasee"""
class DiverClass(BaseClass):
    def __init__(self, name):
        self.name = name
        print('init name=%s' % name)
        print('in diver init')

    def __enter__(self):
        print('in diver enter')

    def __exit__(self):
        print('in diver exit')

    def __str__(self):
        return 'str'

    def __repr__(self):
        return "repr"



if(__name__ == "__main__"):
    b = BaseClass("base")
    d = DiverClass("drive")


    b.who()
    d.who()
    print(d)
    print("%r" % d)


