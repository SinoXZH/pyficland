import FicApp

class Building(object):
    def __init__(self, parent):
        self.leader = None
        self.charaList = []
        self.parent = parent

    def InitChara(self):
        pass


class LordHouse(Building):
    def __init__(self):
        pass

    def InitGeo(self):
        pass


class Government(Building):
    def __init__(self):
        pass

    def InitGeo(self):
        pass


class Shop(Building):
    def __init__(self):
        pass

    def InitGeo(self):
        pass


class Tarvern(Building):
    def __init__(self):
        pass

    def InitGeo(self):
        pass


class House(Building):
    def __init__(self):
        pass

    def InitGeo(self):
        pass