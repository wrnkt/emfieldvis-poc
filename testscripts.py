import numpy as np

muo = 4*np.pi*10**(-7)

def FieldfromCurrentRadius(current, radius):
    b = (muo*current)/(2*np.pi*radius)
    return b

def RadiusfromCurrentAndField(current, b):
    radius = (muo*current)/(2*np.pi*b)
    return radius

def CurrentfromRadiusAndField(radius, field):
    current = (2*np.pi*field*radius)/(muo)
    return current

calclist = np.array([(0.9144, 0.1e-6), # Refrigerator
                    (0.22, 3e-6), # Computer
                    (0.15, 3e-6), # Laptop
                    (0.10, 2e-6), # Landline
                    (0.10, 3e-6), # Cellphone
                    (0.70, 100e-6), # Television
                    (0.30, 2.5e-6), # Oven
                    (0.60, 30e-6), # Dishwasher
                    (0.76, 20e-6), # Microwave
                    (0.40, 2e-6), # Washing Machine
                    (0.40, 40e-6), # Dryer
                    (0.60, 381e-6), # Air Conditioner
                    (0.20, 20e-6), # Heater
                    (1.00, 1e-6), # Fan
                    (0.25, 0.4e-6), # Gaming Console
                    (0.30, 0.002e-6), # Light
                    (0.20, 30e-6), # Vacuum
                    (1.0, 0.01e-6)]) # Iron


#print(CurrentfromRadiusAndField(0.70, 100e-6))

#print(calclist[0,0])

#for i in range(0,len(calclist)):
#    print(CurrentfromRadiusAndField(calclist[i,0],calclist[i,1]))

print(RadiusfromCurrentAndField(3.7500000000000004, 2.5e-6))