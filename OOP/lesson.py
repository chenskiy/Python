class Person:

    def can_breathe(self):
        print('Я могу дышать')

    def can_walk(self):
        print('Я могу ходить')

class Doctor(Person):

    def can_cure(self):
        print('Я мгу лечить')

class Architect(Person):

    def can_build(self):
        print('Я могу построить')

d = Doctor()
d.can_cure()
d.can_walk()
d.can_breathe()

a = Architect()
a.can_build()
a.can_walk()
a.can_breathe()