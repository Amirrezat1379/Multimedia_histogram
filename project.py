from turtle import title
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def cumulative(lisst):
    length = len(lisst)
    x = 0
    returnList = np.zeros(256, dtype= int)
    for i in range(length):
        x += lisst[i]
        returnList[i] = x
    return returnList

def createNegasht(lisst, width, height):
    returnList = np.zeros(256, dtype= int)
    for i in range(256):
        returnList[i] = round((256 * lisst[i]) / (width * height))
    return returnList

def plotHistogram():
    plt.plot(arr, histarrColor, color='r')
    plt.title("Histogram")
    plt.figure()

def plotCumulative():
    plt.plot(arr, cumulativeColor, color='g')
    plt.title('Cumulative')
    plt.figure()

def plotT():
    plt.plot(arr, TC, color='b')
    plt.title('negasht')

img = Image.open('image.png')
width = img.size[0] 
height = img.size[1] 
histarrColor = np.zeros(256, dtype= int)
arr = list(range(0, 256))
for i in range(0,width):
    for j in range(0,height):
        data = img.getpixel((i,j))
        color = data[0] * 0.2989 + data[1] * 0.5870 + data[2] * 0.1140
        histarrColor[int(data[0])] += 1

plotHistogram()
cumulativeColor = cumulative(histarrColor)
plotCumulative()
TC = createNegasht(cumulativeColor, width, height)
plotT()
plt.show()

for i in range(0,width):
    for j in range(0,height):
        data = img.getpixel((i,j))
        color = data[0] * 0.2989 + data[1] * 0.5870 + data[2] * 0.1140
        img.putpixel((i,j),(TC[int(color)], TC[int(color)], TC[int(color)]))
img.show("result.png")
img.save("result.png")
