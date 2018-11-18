def sep():
    print(30*'-')


class Animal:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def speak(self):
        print("{}: Hello to you!".format(self.name))
        print("{}: I'm a little fat, now weigh {} pounds".format(self.name, self.weight))
        sep()

    def action(self, user):
        print("{}: Let's drink some beer, {}...gulp-gulp".format(self.name, user))
        sep()

    def eat(self):
        print("{} eating".format(self.name))
        sep()


class Me:
    name = '$_Script user_$'

    def say_hello(self,obj):
        print('I: Hello, {}, how are you?'.format(obj.name))
        obj.speak()

    def ask_action(self, obj):
        print('I: Do some action, {}!'.format(obj.name))
        obj.action(self.name)

    def want_eggs(self, obj):

        print("I: Give me some eggs, {}".format(obj.name))

        if type(obj) == Goose or type(obj) == Chicken or type(obj) == Duck:
            obj.give_eggs(self.name)
        else:
            print("Sorry, but {} can`t do eggs".format(obj.name))

    def feed(self, obj):
        print('Here some food, {}'.format(obj.name))
        obj.eat()

    def ask_heaviest_animal(self, *animals):
        animals_list = []

        for animal in animals:
            animals_list.append([animal.name, animal.weight])

        animals_list.sort(key=lambda i: i[1], reverse=True)

        for i in animals_list:
            print("%20s: %1d" % (i[0], i[1]) + ' kilo')

        sep()

        print('The most heaviest animal is: {}'.format(animals_list[0][0]))


class Goose(Animal):
    def speak(self):
        print('Awww, shit, i`m a goose, my name is {}! Ga-ga-ga'.format(self.name))
        sep()

    def action(self, user):
        print('The {} eating scrumble eggs'.format(self.name))
        sep()

    def give_eggs(self, user):
        print("Now, {} have few eggs from {}".format(user, self.name))


class Cow(Animal):
    def speak(self):
        print('Moooooooooo, my name is {}! Moooooooooo'.format(self.name))
        sep()

    def action(self, user):
        print('The {} gives milk'.format(self.name))
        sep()


class Goat(Cow, Animal):
    def speak(self):
        print('Buaaaaa, buaa, my name is {}! I am goat!'.format(self.name))
        sep()


class Sheep(Animal):
    def speak(self):
        print('Be-e-e, be-e-e-e my name is {}! I`m sheep!'.format(self.name))
        sep()

    def action(self, user):
        print('{} shears a {}, now we have some wool'.format(user, self.name))
        sep()


class Chicken(Goose, Animal):
    def speak(self):
        print('Ko-ko-ko, my name is {}! I am chicken!'.format(self.name))
        sep()


class Duck(Goose, Animal):
    def speak(self):
        print('Quark-Quark, my name is {}! I am duck!'.format(self.name))
        sep()


human = Animal('Uncle Joe', 80)
gray_goose = Goose('Gray', 5)
white_goose = Goose('White', 7)
cow = Cow('Manya', 300)
goat_horns = Goat('Horns', 10)
goat_hooves = Goat('Hooves', 9)
sheep_barry = Sheep('Barry', 17)
sheep_curvy = Sheep('Curvy', 15)
chicken_koko = Chicken('Koko', 2)
chicken_kuku = Chicken('Kuku', 2.5)
krya_duck = Duck('Krya', 3)

i = Me()

i.say_hello(human)
i.ask_action(human)
i.feed(human)

sep()

i.say_hello(gray_goose)
i.ask_action(gray_goose)
i.want_eggs(gray_goose)
i.feed(gray_goose)

sep()

i.say_hello(white_goose)
i.ask_action(white_goose)
i.want_eggs(white_goose)

sep()

i.say_hello(cow)
i.ask_action(cow)
i.want_eggs(cow)

sep()

i.say_hello(goat_horns)
i.ask_action(goat_horns)
i.want_eggs(goat_horns)

sep()

i.say_hello(goat_hooves)
i.ask_action(goat_hooves)
i.feed(goat_hooves)

i.ask_heaviest_animal(human, gray_goose, white_goose, cow, goat_horns, goat_hooves, sheep_barry, sheep_curvy, chicken_koko, chicken_kuku, krya_duck)