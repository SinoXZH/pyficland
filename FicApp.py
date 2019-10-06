from Geograph import *
from Character import *

class FicApp(object):
    def __init__(self):
        self.geograph = Geograph()
        self.charaList = []
        self.currentCharaId = 0

    def RandomInit(self):
        self.geograph.RandomInit()
        
    def Run(self):
        pass

    def CreateChara(self):
        chara = Character(self.currentCharaId)
        self.currentCharaId += 1
        self.charaList.append(chara)
        return chara

app = FicApp()