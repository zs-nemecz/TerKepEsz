# this script assigns lure and foil locations to original coordniates
import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt

def assign_index(raw_i,max_i):
    '''assign index based on direction'''
    if raw_i < 0:
        index = max_i + raw_i
    elif raw_i > max_i:
        index = raw_i - max_i
    else:
        index = raw_i
    return index

orig = 'original_coordinates_121.csv'
coord = pd.read_csv(orig, sep=',', lineterminator='\n')
indeces = np.arange(0, len(coord))
print(coord)

lure1_distance=np.random.randint(3,16,size=indeces.shape)
lure2_distance=np.random.randint(3,16,size=indeces.shape)
foil_distance = np.random.randint(58,63,size=indeces.shape)
lure1_signs =[(-1)**random.randint(0,1) for i in lure1_distance]
lure2_signs =[(-1)**random.randint(0,1) for i in lure2_distance]
lure1_distance = lure1_distance*lure1_signs
lure2_distance = lure2_distance*lure2_signs

#check distances on histogram
plt.hist(lure1_distance)
plt.hist(lure2_distance)
plt.show()

lure1_indexes = []
lure2_indexes = []
foil_indexes = []

xcoordinate_lure1=[]
ycoordinate_lure1=[]
xcoordinate_lure2=[]
ycoordinate_lure2=[]
xcoordinate_foil = []
ycoordinate_foil = []

#assign positions based on distance
max_i = len(coord.index)-1
for i in range(len(coord.index)):
    lure1_index = indeces[i] + lure1_distance[i]
    lure1_index = assign_index(lure1_index, max_i)
    lure1_indexes.append(lure1_index)
    xcoordinate_lure1.append(coord['Xcoordinate'][lure1_index])
    ycoordinate_lure1.append(coord['Ycoordinate'][lure1_index])

    lure2_index = indeces[i] + lure2_distance[i]
    lure2_index = assign_index(lure2_index, max_i)
    lure2_indexes.append(lure2_index)
    xcoordinate_lure2.append(coord['Xcoordinate'][lure2_index])
    ycoordinate_lure2.append(coord['Ycoordinate'][lure2_index])

    foil_index = indeces[i] + foil_distance[i]
    foil_index = assign_index(foil_index, max_i)
    foil_indexes.append(foil_index)
    xcoordinate_foil.append(coord['Xcoordinate'][foil_index])
    ycoordinate_foil.append(coord['Ycoordinate'][foil_index])

coord['Xcoordinate_lure1'] = xcoordinate_lure1
coord['Ycoordinate_lure1'] = ycoordinate_lure1
coord['Xcoordinate_lure2'] = xcoordinate_lure1
coord['Ycoordinate_lure2'] = ycoordinate_lure1

coord['Xcoordinate_foil'] = xcoordinate_lure1
coord['Ycoordinate_foil'] = ycoordinate_lure1

coord['Lure1_Distance'] = lure1_distance
coord['Lure1_Index'] = lure1_indexes

coord['Lure2_Distance'] = lure2_distance
coord['Lure2_Index'] = lure2_indexes

coord['Foil_Distance'] = foil_distance
coord['Foil_Index'] = foil_indexes

coord.to_csv('coordinate_table.csv')
print(coord)
