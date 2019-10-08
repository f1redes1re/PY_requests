# Вы приехали помогать на ферму Дядюшки Джо и видите вокруг себя множество разных животных:
# гусей "Серый" и "Белый"
# корову "Маньку"
# овец "Барашек" и "Кудрявый"
# кур "Ко-Ко" и "Кукареку"
# коз "Рога" и "Копыта"
# и утку "Кряква"
# Со всеми животными вам необходимо как-то взаимодействовать:
# кормить
# корову и коз доить
# овец стричь
# собирать яйца у кур, утки и гусей
# различать по голосам(коровы мычат, утки крякают и т.д.)


class Animal:
    feed = 0
    weight = 0
    max_weight = 0
    voice = 'Some voice'
    name = 'Some name'
    kind = 'Some animal'
    condition = 'Some condition'

    def __init__(self, kind, name):
        self.kind = kind
        self.name = name

    def eat(self, value):
        self.feed += value
        if self.feed > 1:
            self.condition = 'full'
            print("{}'s named {} condition - {}".format(self.kind, self.name, self.condition))
        else:
            self.condition = 'hungry'
            print("{}'s named {} condition - {}".format(self.kind, self.name, self.condition))

    def voices(self):
        print("{}'s named {} voice - {}".format(self.kind, self.name, self.voice))

    def info(self):
        print("{} named {}, {} kg".format(self.kind, self.name, self.weight))

    # def intro(self, **data):
    #     for key, value in data.items():
    #         print("{} is {}".format(key, value))

    def weight_sum(self, *all_weight):
        sum_weight = 0
        for n in all_weight:
            sum_weight += n
        print("Total animal weight is {} kg's".format(sum_weight))

    def weight_top(self, *all_weight):
        top_weight = max(all_weight)
        print("Top animal weight is {} kg's".format(top_weight))


class Cow(Animal):
    weight = 300    # kg
    voice = 'Moo!'

    def __init__(self, kind, name):
        super().__init__(kind, name)

    def give_milk(self):
        if self.condition == 'full':
            print("Collected 1 {}'s litres from {}".format(self.kind, self.name))
        else:
            print('{} named {} need more feed'.format(self.kind, self.name))


class Sheep(Animal):
    weight = 20     # kg
    voice = 'Be-e-e!'

    def __init__(self, kind, name):
        super().__init__(kind, name)

    def give_wool(self):
        if self.condition == 'full':
            print("Collected 1 kg of {}'s wool from {}".format(self.kind, self.name))
        else:
            print('{} named {} need more feed'.format(self.kind, self.name))


class Chickens(Animal):
    weight = 3
    voice = 'Co-co-co!'

    def __init__(self, kind, name):
        super().__init__(kind, name)

    def give_eggs(self):
        if self.condition == 'full':
            print("Collected 1 {}'s egg from {}".format(self.kind, self.name))
        else:
            print('{} named {} need more feed'.format(self.kind, self.name))


class Goose(Animal):
    weight = 7
    voice = 'Ga-ga-ga!'

    def __init__(self, kind, name):
        super().__init__(kind, name)

    def give_eggs(self):
        if self.condition == 'full':
            print("Collected 1 {}'s egg from {}".format(self.kind, self.name))
        else:
            print('{} named {} need more feed'.format(self.kind, self.name))


class Goat(Animal):
    weight = 30
    voice = 'Bebw!'

    def __init__(self, kind, name):
        super().__init__(kind, name)

    def give_milk(self):
        if self.condition == 'full':
            print("Collected 1 {}'s litres from {}".format(self.kind, self.name))
        else:
            print('{} named {} need more feed'.format(self.kind, self.name))


class Duck(Animal):
    weight = 4
    voice = 'Krya!'

    def __init__(self, kind, name):
        super().__init__(kind, name)

    def give_eggs(self):
        if self.condition == 'full':
            print("Collected 1 {}'s egg from {}".format(self.kind, self.name))
        else:
            print('{} named {} need more feed'.format(self.kind, self.name))


goose_1 = Goose('Goose', 'Серый')
goose_2 = Goose('Goose', 'Белый')
goose_1.info()
goose_2.info()
goose_1.eat(2)
goose_2.eat(2)
goose_1.give_eggs()
goose_2.give_eggs()
goose_1.voices()
goose_2.voices()
print('\n')

cow_1 = Cow('Cow', 'Манька')
cow_1.info()
cow_1.eat(2)
cow_1.give_milk()
cow_1.voices()
print('\n')

sheep_1 = Sheep('Sheep', 'Барашек')
sheep_2 = Sheep('Sheep', 'Кудрявый')
sheep_1.info()
sheep_2.info()
sheep_1.eat(2)
sheep_2.eat(2)
sheep_1.give_wool()
sheep_2.give_wool()
sheep_1.voices()
sheep_2.voices()
print('\n')

chick_1 = Chickens('Chicken', 'Ко-Ко')
chick_2 = Chickens('Chicken', 'Кукареку')
chick_1.info()
chick_2.info()
chick_1.eat(2)
chick_2.eat(2)
chick_1.give_eggs()
chick_2.give_eggs()
chick_1.voices()
chick_2.voices()
print('\n')

goat_1 = Goat('Goat', 'Рога')
goat_2 = Goat('Goat', 'Копыта')
goat_1.info()
goat_2.info()
goat_1.eat(2)
goat_2.eat(2)
goat_1.give_milk()
goat_2.give_milk()
goat_1.voices()
goat_2.voices()
print('\n')

duck_1 = Duck('Duck', 'Кряква')
duck_1.info()
duck_1.eat(2)
duck_1.give_eggs()
duck_1.voices()
print('\n')

Animal.weight_sum(goose_1.weight, goose_2.weight, cow_1.weight, sheep_1.weight, sheep_2.weight, chick_1.weight, chick_2.weight, goat_1.weight, goat_2.weight, duck_1.weight)
Animal.weight_top(goose_1.weight, goose_2.weight, cow_1.weight, sheep_1.weight, sheep_2.weight, chick_1.weight, chick_2.weight, goat_1.weight, goat_2.weight, duck_1.weight)