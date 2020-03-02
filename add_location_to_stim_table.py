import pandas as pd
import numpy as np
import random
fname ='StimuliTable-Encoding-3run-40-520-12345.csv'
stim_table = pd.read_csv(fname, sep=',', lineterminator='\n')
coord = pd.read_csv('coordinate_table_discrete_1.csv')
i = 0
for row in range(len(stim_table)):
    if stim_table['Order'][row] == 1:
        delay = stim_table['Delay'][row] + 1
        stim_table['Xcoordinate'][row] = coord['Xcoordinate'][i]
        stim_table['Ycoordinate'][row] = coord['Ycoordinate'][i]
        stim_table['Xcoordinate'][row + delay] = coord['Xcoordinate'][i]
        stim_table['Ycoordinate'][row+delay] = coord['Ycoordinate'][i]

        stim_table['Xcoordinate_lure1'][row] = coord['Xcoordinate_lure1'][i]
        stim_table['Ycoordinate_lure1'][row] = coord['Ycoordinate_lure1'][i]
        stim_table['Xcoordinate_lure1'][row+delay] = coord['Xcoordinate_lure1'][i]
        stim_table['Ycoordinate_lure1'][row+delay] = coord['Ycoordinate_lure1'][i]


        stim_table['Xcoordinate_lure2'][row] = coord['Xcoordinate_lure2'][i]
        stim_table['Ycoordinate_lure2'][row] = coord['Ycoordinate_lure2'][i]
        stim_table['Xcoordinate_lure2'][row+delay] = coord['Xcoordinate_lure2'][i]
        stim_table['Ycoordinate_lure2'][row+delay] = coord['Ycoordinate_lure2'][i]


        stim_table['Xcoordinate_foil'][row] = coord['Xcoordinate_foil'][i]
        stim_table['Ycoordinate_foil'][row] = coord['Ycoordinate_foil'][i]
        stim_table['Xcoordinate_foil'][row+delay] = coord['Xcoordinate_foil'][i]
        stim_table['Ycoordinate_foil'][row+delay] = coord['Ycoordinate_foil'][i]

        i +=1

stim_table.to_csv('StimuliTable-Encoding-3run-40-520-12345_new_coord.csv')
