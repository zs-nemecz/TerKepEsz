import pandas as pd
import matplotlib.pyplot as plt

fname = 'coordinate_table_discrete_1.csv'
stim_table = pd.read_csv(fname, sep=',', lineterminator='\n')
s = 90
plt.plot(stim_table['Xcoordinate'], stim_table['Ycoordinate'], alpha=0.5)
colors = ['r', 'g', 'k', 'gold', 'fuchsia', 'brown']
c=0

for i in [68, 102, 103]: # plot fist few locations
    c+=1
    plt.scatter(stim_table['Xcoordinate'][i], stim_table['Ycoordinate'][i], s=s, color=colors[c]) # original coordinates
    plt.scatter(stim_table['Xcoordinate_lure1'][i], stim_table['Ycoordinate_lure1'][i], marker = 'x', s=s, color=colors[c]) # lure 1 coordinates
    plt.scatter(stim_table['Xcoordinate_lure2'][i], stim_table['Ycoordinate_lure2'][i], marker = 'd', s=s, color=colors[c]) # lure 2 coordinates

    plt.plot([stim_table['Xcoordinate'][i], stim_table['Xcoordinate_lure1'][i], stim_table['Xcoordinate_lure2'][i]], [stim_table['Ycoordinate'][i], stim_table['Ycoordinate_lure1'][i], stim_table['Ycoordinate_lure2'][i]], linestyle='--')

# for i in range(len(stim_table)):
    plt.scatter(stim_table['Xcoordinate_foil'][i], stim_table['Ycoordinate_foil'][i], marker = '1', s=s, linewidth=3, color=colors[c]) # foil coordinates
plt.show()
