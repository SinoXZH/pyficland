from Settlement import *
import FicApp

class GeoPoint(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.mainSettlement = None
        self.villageList = []
        self.fbList = []
        self.charaList = []

    def InitGeo(self):
        self.mainSettlement = City(self)
        self.mainSettlement.InitGeo()

        for i in range(0, 10):
            village = Village(self)
            village.InitGeo()
            self.villageList.append(village)

        for i in range(0, 30):
            fb = Fb(self)
            fb.InitGeo()
            self.fbList.append(fb)

    def InitChara(self):
        self.mainSettlement.InitChara()
        self.charaList.extend(self.mainSettlement.charaList)


        for village in self.villageList:
            village.InitChara()
            self.charaList.extend(village.charaList)



