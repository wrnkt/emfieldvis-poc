from tkinter import *
from PIL import ImageTk,Image  
import numpy as np
import matplotlib.pyplot as plt
import pandas
import os
import csv
import magpylib as mgpy
from magpylib.source.magnet import Box,Cylinder
from magpylib import Collection, displaySystem

imagedir = "../content/floorplans/floorplan1.jpg"
imagepil = Image.open(imagedir) # open floorplan (PIL)
imagew = imagepil.width 
imageh = imagepil.height

#xl = np.linspace(0,imagew,(imagew*2))
#yl = np.linspace(0,imageh,(imageh*2))

xl = imagew//2
yl = imageh//2

xlist = np.linspace(0,imagew,xl)
ylist = np.linspace(0,imageh,yl)

collection = mgpy.Collection()

with open('../content/applianceslist/applistoutputTEST.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    i = 0
    for row in reader:
        #c.addSources(Cylinder(mag=(0,0,600), dim=(3,3), pos=((imageh-int(row[1])),row[2],0)))
        cylinder = Cylinder(mag=(0,0,600), dim=(10,10), pos=(row[1],row[2],0))
        collection.addSources(cylinder)
        i += 1
    print(f'Read {i} lines.')

print(collection.getB([900,900,0])[2])

#POS = np.array([(x,y,(collection.getB([x,y,0])[2])) for y in ylist for x in xlist])

#B = collection.getB(POS).reshape(imagew//2,imageh//2,-1)

Bs = np.zeros(shape=(imagew*2,imageh*2))

for x in range(0,imagew,2):
    for y in range(0,imageh,2):
        Bs[x,y] = collection.getB([x,y,0])[2]

#X,Y = np.meshgrid(xlist,ylist)

#print(collection.getB([1,1,1])[0])

#B = collection.getB([xl,yl,0])[0]

fig, ax = plt.subplots()


c = ax.pcolormesh(Bs, cmap='RdBu', vmin=1000, vmax=1000)


#data = np.zeros(((xl),(yl)))


#for x in range(xl):
#    for y in range(yl):
 #       data[x,y] = c.getB([x,y,0])[2]


#plt.imshow(data, cmap='viridis')



#fig, plot1 = plt.subplots()
#plot1.plot([1,2],[1,2])
#plot1.set_xlim([0, imagew])
#plot1.set_ylim([imageh, 0])

#X,Y = np.meshgrid(xl,yl)
#U,V = B[:,:,0], B[:,:,2]
#plot1.streamplot(X, Y, U, V, color=np.log(U**2+V**2))



#cf = ax2.contourf(x,y,z,51,vmin=-1,vmax=1,cmap='viridis')


#B = c.getB(POS).reshape(33,33,3)


plt.show()

