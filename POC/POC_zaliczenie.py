
# coding: utf-8

# In[61]:


import numpy as np
import matplotlib.pyplot as plt
from skimage import io, exposure
from skimage.color import rgb2gray
from skimage import filters
from scipy import ndimage as ndi
import skimage
from skimage.morphology import square
from skimage.morphology import binary_erosion
from scipy.spatial import distance
import math

#środek ciężkości
def cog2(points):
    mx=0
    my=0
    for (y,x) in points:
        mx = mx + x
        my = my + y
    mx = mx/len(points)
    my = my/len(points)
    mx = round(mx, 2)
    my = round(my, 2)
    
    return [my, mx]


def getFigure(labelledImage, objNumber):
    
    points = []
    for y in range(labelledImage.shape[0]):
        for x in range(labelledImage.shape[1]):
            if labelledImage[y,x] == objNumber:
                points.append((y,x))

    return points

def computeBB(points):
    
    s = len(points)
    my,mx = cog2(pts)
    
    r = 0
    for point in points:
         r = r + distance.euclidean(point,(my,mx))**2
            
    return s/(math.sqrt(2*math.pi*r))


def computeFeret(points):
    
    px = [x for (y,x) in points]
    py = [y for (y,x) in points]
    
    fx = max(px) - min(px)
    fy = max(py) - min(py)
    
    return float(fy)/float(fx) 


path = 'zdjecia/'
for z in range(1, 19):
                        #Wczytywanie zdjec, przerabianie ich na skale szarosci
    image = io.imread(path + 'z{}.jpg'.format(z))
    image = rgb2gray(image)

   # plt.imshow(image, cmap='gray')
   # plt.axis('on')
   # plt.suptitle('Analizowany obraz')
   # plt.show()
    
                                    #----Histogram
    #print('Histogram')
   # hist, bins = exposure.histogram(image)
    #print(hist.shape, hist.dtype)
    #plt.figure()
   # plt.plot(hist, color="black")
   # plt.show()
    
                                    #----Binaryzacja
    #print('Obraz po binaryzacji')
    th = filters.threshold_otsu(image)
    erosion = binary = image > th
  
   # plt.imshow(binary, cmap='binary')
   # plt.axis('on')
   # plt.show()
    
                                    #----Erozja
   # print("Po erozji")

    square = np.array([[1, 1, 1],
                       [1, 1, 1], 
                       [1, 1, 1]], dtype=np.uint8)
    
    for i in range(5):
        erosion = binary_erosion(erosion, square)
    
   # plt.imshow(erosion, cmap="gray")
   # plt.axis('off')
   # plt.show()
    
                                    #---Wyliczanie obiektow na obrazie
    #print('Obiekty na obrazie')
    label_objects, nb_labels = ndi.label(erosion)
    
    #plt.imshow(label_objects, cmap="hot")
    #plt.axis('on')
    #plt.show()
    
    
    values, counts = np.unique(binary, return_counts=True)
    T=counts[1]
    F=counts[0]
    full = (T/(T+F))*100
    full = round(full, 2)
    
    print("Ilosc obiektów na zdjęciu {}: ".format(z) + str(nb_labels))  
    print("Obiekty zajmuja: {}".format(full) +"% obszaru zdjęcia")

    for i in range(nb_labels):
        pts = getFigure(label_objects, i+1)
        bb = computeBB(pts)
        bb = round(bb, 4)
        feret = computeFeret(pts)
        feret = round(feret, 4)
        
        print('Srodek ciezkosci: ', cog2(pts))
        print('Współczynnik Blair-Bliss\'a: ', bb)
        print('Współczynnik Feret\'a: ',feret)
        print('\n')
    print('\n\n')

