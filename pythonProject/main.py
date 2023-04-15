class Cat:
    isHungry = True

    def __init__(self,name):
        self.name = name

    def play(self,person):
        print('I`m playing with', person.name)
        person.isHappy = True


class Person:
    isHappy = False
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def feed(self, cat):
        if cat.isHungry:
            print(self.name, "is feeding cat named", cat.name)
            cat.isHungry = False
        else:
            print(cat.name)




my_cat = Cat("Barsik")
friend_cat = Cat("Asya")
me = Person("Hlieb", 12)
friend = Person("Venya", 12)

print(me.name, me.age)
print(friend.name, friend.age)

print(me.isHappy)
my_cat.play(me)
print(me.isHappy)
my_cat.play(friend)

me.feed(my_cat)
me.feed(friend_cat)