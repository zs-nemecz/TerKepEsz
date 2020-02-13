import pandas as pd
import matplotlib.pyplot as plt

fname = 'StimuliTable-Encoding-3run-40-520-2468.csv'
stim_table = pd.read_csv(fname, sep='\t', lineterminator='\n')
s = 90
plt.plot(stim_table['Xcoordinate'], stim_table['Ycoordinate'], alpha=0.5)
colors = ['r', 'g', 'k', 'gold', 'fuchsia', 'brown']
for i in range(len(colors)): # plot fist few locations
    plt.scatter(stim_table['Xcoordinate'][i], stim_table['Ycoordinate'][i], s=s, color = colors[i]) # original coordinates
    plt.scatter(stim_table['Xcoordinate_lure1'][i], stim_table['Ycoordinate_lure1'][i], marker = 'x', s=s, color = colors[i]) # lure 1 coordinates
    plt.scatter(stim_table['Xcoordinate_lure2'][i], stim_table['Ycoordinate_lure2'][i], marker = 'd', s=s, color = colors[i]) # lure 2 coordinates
    plt.scatter(stim_table['Xcoordinate_foil'][i], stim_table['Ycoordinate_foil'][i], marker = '1', s=s, color = colors[i], linewidth=3) # foil coordinates
    plt.plot([stim_table['Xcoordinate'][i], stim_table['Xcoordinate_lure1'][i], stim_table['Xcoordinate_lure2'][i]], [stim_table['Ycoordinate'][i], stim_table['Ycoordinate_lure1'][i], stim_table['Ycoordinate_lure2'][i]], linestyle='--', color = colors[i])

plt.show()
