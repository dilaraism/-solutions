import types 

class Dog(object):
    def __init__(self, name, breed, sex, age):
        self.name  = name
        self.breed = breed
        self.sex   = sex
        self.age   = age


def attach(target):
    def bark(target):
        return "Woof!"
    target.bark = types.MethodType(bark,target)

attach(Dog)