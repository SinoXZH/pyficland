import FicApp
from Building import *

class Settlement(object):
    def __init__(self, parent):
        self.parent = parent
        self.charaList = []
        self.houseList = []

    def InitChara(self):
        pass

class City(Settlement):
    def InitGeo(self):
        self.lordHouse = LordHouse()
        self.lordHouse.InitGeo()

        self.government = Government()
        self.government.InitGeo()

        self.shop = Shop()
        self.shop.InitGeo()

        self.tarvern = Tarvern()
        self.tarvern.InitGeo()

    def InitChara(self):
        self.lordHouse.InitChara()
        self.government.InitChara()
        self.shop.InitChara()
        self.tarvern.InitChara()


class Village(Settlement):
    def InitGeo(self):
        self.lordHouse = LordHouse()
        self.lordHouse.InitGeo()

    def InitChara(self):
        self.lordHouse.InitChara()


class Fb(Settlement):
    def InitGeo(self):
        pass