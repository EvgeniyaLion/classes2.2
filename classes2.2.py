class animal:
    """Вид животного"""

    def __init__(self, name, weight):
        """Имя и вес"""
        self.name = name
        self.weight = weight

    def feed(self):
        """Кормление"""
        print(self.name.title() + " накормлен")

    def __repr__(self):
        return "имя — " + self.name + ", вес — " + str(self.weight) + "кг."


class bird(animal):
    """Птица"""

    def pick_eggs(self):
        """Сбор яиц"""
        print("У " + self.name.title() + " собраны яйца")


class goose(bird):
    """Гусь"""

    def voice(self):
        """Гусь гогочет"""
        print(self.name.title() + " гогочет")


class chicken(bird):
    """Курица"""

    def voice(self):
        """Курица кудахчет"""
        print(self.name.title() + " кудахчет")


class duck(bird):
    """Утка"""

    def voice(self):
        """Утка крякает"""
        print(self.name.title() + " крякает")


class cow(animal):
    """Корова"""

    def milk(self):
        """Доение"""
        print(self.name.title() + " подоена")

    def voice(self):
        """Корова мычит"""
        print(self.name.title() + " мычит")


class goat(animal):
    """Коза"""

    def milk(self):
        """Доение"""
        print(self.name.title() + " подоена")

    def voice(self):
        """Коза мекает"""
        print(self.name.title() + " мекает")


class sheep(animal):
    """Овца"""

    def cut(self):
        """Стрижка"""
        print(self.name.title() + " подстрижен")

    def voice(self):
        """Овца бекает"""
        print(self.name.title() + " бекает")


all_animals = {"Серый": goose("Серый", 6)}
all_animals.get("Серый").voice()
all_animals.get("Серый").feed()
all_animals.get("Серый").pick_eggs()

all_animals["Белый"] = goose("Белый", 5)
all_animals.get("Белый").voice()
all_animals.get("Белый").feed()
all_animals.get("Белый").pick_eggs()

all_animals["Ко-ко"] = chicken("Ко-ко", 2)
all_animals.get("Ко-ко").voice()
all_animals.get("Ко-ко").feed()
all_animals.get("Ко-ко").pick_eggs()

all_animals["Кукареку"] = chicken("Кукареку", 3)
all_animals.get("Кукареку").voice()
all_animals.get("Кукареку").feed()
all_animals.get("Кукареку").pick_eggs()

all_animals["Кряква"] = duck("Кряква", 1)
all_animals.get("Кряква").voice()
all_animals.get("Кряква").feed()
all_animals.get("Кряква").pick_eggs()

all_animals["Манька"] = cow("Манька", 300)
all_animals.get("Манька").voice()
all_animals.get("Манька").feed()
all_animals.get("Манька").milk()

all_animals["Рога"] = goat("Рога", 100)
all_animals.get("Рога").voice()
all_animals.get("Рога").feed()
all_animals.get("Рога").milk()

all_animals["Копыта"] = goat("Копыта", 110)
all_animals.get("Копыта").voice()
all_animals.get("Копыта").feed()
all_animals.get("Копыта").milk()

all_animals["Барашек"] = sheep("Барашек", 140)
all_animals.get("Барашек").voice()
all_animals.get("Барашек").feed()
all_animals.get("Барашек").cut()

all_animals["Кудрявый"] = sheep("Кудрявый", 150)
all_animals.get("Кудрявый").voice()
all_animals.get("Кудрявый").feed()
all_animals.get("Кудрявый").cut()

overall_weight = 0
for beast in all_animals.values():
    overall_weight += beast.weight
print(f'\nОбщий вес всех животных — {overall_weight} кг.')

fattest_animal = ""
fattest_animal_weight = 0
for beast in all_animals.values():
    if fattest_animal_weight < beast.weight:
        fattest_animal = beast.name
        fattest_animal_weight = beast.weight
print(f'\nСамое тяжелое животное — {fattest_animal}\n')

print(all_animals)
