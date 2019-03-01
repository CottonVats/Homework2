class Animal:
    class_voice = "Неизвестен"
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
    def feed(self):
        print("Вы покормили", self.name)
    def differ(self):
        print(self.name, "звучит", self.class_voice, ".", self.name, "это", self.__class__.__name__)
class Dairy(Animal):
    def milk(self):
        print("Вы подоили",self.name)
class Cow(Dairy):
    class_voice = "Мy-у"
class Goat(Dairy):
    class_voice = "Ме"
class Sheep(Animal):
    class_voice = "Бе"
    def cut(self):
        print("Вы постригли", self.name)
class Bird(Animal):
    def collect_eggs(self):
        print("Вы собрали яйца", self.name)
class Chicken(Bird):
    class_voice = "Ко"
class Duck(Bird):
    class_voice = "Кря"
class Goose(Bird):
    class_voice = "Га"
goose1 = Goose("Серый", 3)
goose2 = Goose("Белый", 4)
cow1 = Cow("Манька", 456)
sheep1 = Sheep("Барашек", 129)
sheep2 = Sheep("Кудрявый", 154)
chicken1 = Chicken("Ко-ко", 1)
chicken2 = Chicken("Кукареку", 2)
goat1 = Goat("Рога", 73)
goat2 = Goat("Копыта", 87)
duck1 = Duck("Кряква", 2)
every_animal_list = [goose1, goose2, cow1, sheep1, sheep2, chicken1, chicken2, goat1, goat2, duck1]
for animal in every_animal_list:
    animal.feed()
    animal.differ()
    if issubclass(animal.__class__, Dairy):
        animal.milk()
    elif issubclass(animal.__class__, Bird):
        animal.collect_eggs()
    elif animal.__class__ == Sheep:
        animal.cut()
weight = 0
for animal in every_animal_list:
    weight += animal.weight
print("Общий вес:", weight, "кг")
weights_list = []
names_list = []
for animal in every_animal_list:
    weights_list.append(animal.weight)
    names_list.append(animal.name)
animals_list = list(zip(weights_list, names_list))
for tuples in animals_list:
    if tuples[0] == max(weights_list):
        print("Больше всех весит", tuples[1])



    





    









    



    
