from GeoPoint import *

class Geograph(object):
    def __init__(self):
        self.geopoint = GeoPoint(0, 0)
        
    def RandomInit(self):
        self.geopoint.InitGeo()
        self.geopoint.InitChara()