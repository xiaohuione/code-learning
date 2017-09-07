# encoding: utf-8
from random import randint

class Person:
    def __init__(self, name, money):
        self.name = name
        self.money = money

    def print_property(self):
        print("{0}'s money is {1}".format(self.name, self.money))

    def money_out(self):
        if self.money == 0:
            return 0
        self.money -= 1
        #self.print_property()
        return 1

    def money_in(self, money):
        self.money += money


class Game:
    def __init__(self, person_total, init_money, times):
        self.persons = [Person("player-{0}".format(i), init_money) for i in range(100)]
        self.times = times

    def play_one_time(self):
        for person in self.persons:
            money_out = person.money_out()
            others = list(filter(lambda x: x != person, self.persons))
            luckey_person = others[randint(0, len(self.persons) -2)]
            luckey_person.money_in(money_out)

    def plays(self):
        for i in range(self.times):
            self.play_one_time()
            #money_list = [person.money for person in self.persons ]
            #print("{0}: {1}".format(i, money_list))

    def result(self):
        print("--" * 20)
        print("duang, game result is bellow")
        print("--" * 20)
        money = 0
        for person in self.persons:
            money += person.money
            person.print_property()
        print("total money is {0}".format(money))

if __name__ == '__main__':
    game = Game(100, 100, 10000)
    game.plays()
    game.result()
