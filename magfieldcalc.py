from tkinter import *
from PIL import ImageTk,Image  
import numpy as np
import matplotlib.pyplot as plt
import pandas
import os
import csv
import tkinter as tk
from tkinter import filedialog
from tkinter import simpledialog

muo = np.pi*4e-7
acceptablemag = 0.1e-6 # microTeslas

# MATH
def FieldfromCurrentRadius(current, radius):
    b = (muo*current)/(2*np.pi*radius)
    return b

def RadiusfromCurrentAndField(current, b):
    radius = (muo*current)/(2*np.pi*b)
    return radius

def CurrentfromRadiusAndField(radius, field):
    current = (2*np.pi*field*radius)/(muo)
    return current

def calculate():
    with open('/Users/niko/Documents/emfvisualizer/applianceslist/applistoutput.csv') as csvfile:
        reader = csv.reader(csvfile)
        numsources = 0
        for row in reader:
            numsources += 1

    xarr = np.zeros(numsources)
    yarr = np.zeros(numsources)
    currentfactor = np.zeros(numsources)
    colorsetterlist = np.zeros(numsources)

    with open('/Users/niko/Documents/emfvisualizer/applianceslist/applistoutput.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        i = 0
        for row in reader: # populates x and y data from csv
            xarr[i] = row[1]
            yarr[i] = row[2]
            currentfactor[i] = row[3]
            i += 1
        print(f'Read {i} lines.')

    plt.figure()
    axes = plt.gca()
    for x,y,i,colorsetter in zip(xarr,yarr,currentfactor,colorsetterlist):
        radius = RadiusfromCurrentAndField(i, acceptablemag)*1000*pixelspercm # radius in meters > cm > pixels radius
        print(radius)
        #radius = (muo*i)/(2*np.pi*acceptablemag)*10000*pixelspercm
        #print(radius)
        #print((muo*i)/(2*np.pi*0.0000025)*10000*pixelspercm)
        circle = plt.Circle(((x),(y-50)),radius,facecolor='r',alpha=0.1)
        axes.add_artist(circle)

    axes.imshow(imagepil)
    plt.xlim([0,w])
    plt.ylim([h, 0])
    axes.axis('off')
    plt.title(str(acceptablemag)+' T Field')
    #plt.grid()
    plt.show()