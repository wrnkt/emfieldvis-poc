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
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.figure import Figure

# definitions

muo = np.pi*4e-7
acceptablemag = 1e-6 # microTeslas

defaultwidth = 500

appliances = []

applistoutput="/Users/niko/Documents/emfvisualizer/applianceslist/applistoutput.csv"

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

def clearFile(fpath): # clear output file
    if os.path.exists(fpath):
        f = open(applistoutput, "w+")
        f.close()

# functions handling dragging widgets on screen

def dragstart(event):
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y

def dragmotion(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y
    widget.place(x=x,y=y)

def enableDrag(self): # bind click and drag to functions
    self.bind("<Button-1>",dragstart)
    self.bind("<B1-Motion>",dragmotion)

def createAppliance(applianceselection):
    print(applianceselection)
    placeholderimage = Image.open('/Users/niko/Documents/emfvisualizer/appliancepics/circle1.png')
    print(appdata._get_value(appdata[appdata['appliance']==applianceselection].index.values[0], 'current'))
    placeholderimage = placeholderimage.resize((int(25*pixelspercm),int(25*pixelspercm)), Image.ANTIALIAS)
    i = ImageTk.PhotoImage(placeholderimage)
    #count = len(root.winfo_children())
    currentapp = Label(leftFrame, text=applianceselection,background="#ffffe0",pady=0, padx=0, borderwidth=0, highlightthickness = 0)
    currentapp["compound"] = tk.LEFT
    currentapp["image"] = i
    currentapp.image = i
    currentapp.place(bordermode=INSIDE,x=w/2,y=h/2)
    appliances.append(currentapp)
    enableDrag(currentapp)
    #label = Label(leftFrame, text=applianceselection, justify=LEFT,background="#ffffe0", relief=SOLID, borderwidth=1,font=("tahoma", "12", "normal"))

def deleteLast():
    appliances.pop().destroy()

def loadData():
    clearFile(applistoutput)
    for a in appliances:
        with open(applistoutput,'a', newline='') as fd:
            current = appdata._get_value(appdata[appdata['appliance']==a.cget("text")].index.values[0], 'current')
            print(current)
            fd.write(a.cget("text")+","+str(a.winfo_rootx())+","+str(a.winfo_rooty())+","+str(current)+"\n")

def calculate():

    with open('/Users/niko/Documents/emfvisualizer/applianceslist/applistoutput.csv') as csvfile:
        reader = csv.reader(csvfile)
        numsources = 0
        for row in reader:
            numsources += 1

    xarr = np.zeros(numsources)
    yarr = np.zeros(numsources)
    currentfactor = np.zeros(numsources)
    colorsetterlist = np.zeros(numsources) # unused

    with open('/Users/niko/Documents/emfvisualizer/applianceslist/applistoutput.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        i = 0
        for row in reader: # populates x and y data from csv
            xarr[i] = row[1]
            yarr[i] = row[2]
            currentfactor[i] = row[3]
            i += 1
        print(f'Read {i} lines.')

    fig = Figure()
    plt.get_current_fig_manager().canvas.set_window_title("Magnetic Field Intensity Visualizer")
    axes = plt.gca()
    plt.cla()
    for x,y,i,colorsetter in zip(xarr,yarr,currentfactor,colorsetterlist):
        radius = RadiusfromCurrentAndField(i, acceptablemag)*defaultwidth*pixelspercm # radius in meters > cm > pixels radius
        print(radius)
        circle = plt.Circle(((x),(y-50)),radius,facecolor='r',alpha=0.1)
        axes.add_artist(circle)

    axes.imshow(imagepil)
    plt.xlim([0,w])
    plt.ylim([h, 0])
    axes.axis('off')
    plt.title(str(acceptablemag)+' T Field')
    plt.show()

def quitprogram():
    root.quit()     # stops mainloop
    root.destroy()

columnnames = ['appliance', 'xcm', 'ycm','current','radius']

appdata = pandas.read_csv('/Users/niko/Documents/emfvisualizer/applianceslist/applist.csv', names=columnnames)
sourcenames = appdata.appliance.tolist()

root = Tk()
root.title("Appliance Arranger")

leftFrame = Frame(root)
leftFrame.pack(side = LEFT)

imagedir = filedialog.askopenfilename()

imagepil = Image.open(imagedir)
heighttowidth = imagepil.height/imagepil.width
imagepil = imagepil.resize((defaultwidth, int(defaultwidth*heighttowidth)), Image.ANTIALIAS)
w = imagepil.width 
h = imagepil.height
img = ImageTk.PhotoImage(imagepil)

# estimate pixel to meter ratio (scaling factor)
estimatedwidth = simpledialog.askfloat("Input", "What is the width of this floorplan (meters)?", parent=root,minvalue=0.0, maxvalue=100.0)
estimatedlength = simpledialog.askfloat("Input", "What is the length of this floorplan (meters)?", parent=root,minvalue=0.0, maxvalue=100.0)
pixelspercm = ((w/(estimatedwidth*100)) + (h/(estimatedlength*100)))/2
print(w)
print(h)
print(pixelspercm)

piccanvas = Canvas(leftFrame, width = w, height = h) # set canvas size based on floorplan size
piccanvas.pack()
piccanvas.create_image(0, 0, anchor=NW, image=img)

rightFrame = Frame(root, width = 500, height = h, highlightbackground="black", highlightthickness=2, background="light grey")
rightFrame.pack(expand=True, fill=BOTH)

promptlabel = Label(rightFrame,text="Select an appliance: ")
promptlabel.grid(row=1, sticky="NESW")

optionchoice = StringVar(rightFrame)
optionchoice.set(sourcenames[0]) # default value
dropdown = OptionMenu(rightFrame, optionchoice, *sourcenames)
dropdown.config(width=20)
dropdown.grid(row=2)

placebutton = Button(rightFrame, command = lambda : createAppliance(optionchoice.get()), text="Place", width="10", height="5")
placebutton.grid(row=3, sticky="NEW")

deletebutton = Button(rightFrame, command = deleteLast, text="Delete Last Appliance", width="10", height="5")
deletebutton.grid(row=4, sticky="NEW")

donebutton = Button(rightFrame, command = loadData, text="Confirm Arrangement", width="10", height="5")
donebutton.grid(row=5, sticky="NEW")

exitbutton = Button(rightFrame, command = calculate, text="Calculate", width="10", height="5")
exitbutton.grid(row=6, sticky="NEW")

closebutton = Button(rightFrame, command = quitprogram, text="Quit", width="10", height="5")
closebutton.grid(row=7, sticky="NEW")

root.mainloop()
