# coding: utf-8

class Cat(object):
    def say(self):
        print('i am a cat')


class Dog(object):
    def say(self):
        print('i am a dog')


class Duck(object):
    def say(self):
        print('i am a duck')

    def __init__(self):
        self.name = ['dog', 'cat', 'duck']

    def __getitem__(self, item):
        return self.name[item]

animal_list = [Cat, Dog, Duck]
for animal in animal_list:
    animal().say()

duck = Duck()
a = ['bobby1', 'bobby2']
b = ['bobby2', 'bobby1']
name_tuple = ['bobby3', 'bobby4']
name_set = set()
name_set.add('bobby5')
name_set.add('bobby6')
a.extend(duck)
print(a)