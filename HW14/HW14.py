class Person():

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__friends = []

    def know(self, new_person):
        if new_person in self.__friends:
            return
        self.__friends.append(new_person)
        new_person.know(self)


    def is_known(self, new_person):
        if new_person in self.__friends:
            return True
        return False

pers_1 = Person('Kate', 21)
pers_2 = Person('Alex', 25)
pers_3 = Person('David', 31)

pers_1.know(pers_2)
pers_2.know(pers_3)

print(pers_1.is_known(pers_2))
print(pers_2.is_known(pers_1))
print(pers_1.is_known(pers_3))