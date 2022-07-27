import numpy as np

class MagFieldCalculatorO:

    def __init__(self):
        self.muo = np.pi*4e-7


    def FieldfromCurrentRadius(self, current, radius):
        b = (self.muo*current)/(2*np.pi*radius)
        return b

    def RadiusfromCurrentAndField(self, current, b):
        radius = (self.muo*current)/(2*np.pi*b)
        return radius

    def CurrentfromRadiusAndField(self, radius, field):
        current = (2*np.pi*field*radius)/(self.muo)
        return current
