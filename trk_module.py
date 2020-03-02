# TODO:
# add function descriptions
# imrove OLP foil location
# add comments

import pandas as pd
import numpy as np
import random as rd

def read_jitters(fname):
    jitters_file = open(fname, 'r')
    jitters = jitters_file.read().split('\n')
    jitters = [float(jitter)/1000 for jitter in jitters]
    jitters_file.close()
    return jitters

def select_images(n_images_used = 121, n_all_images= 180):
    images = [im for im in range(1,n_all_images+1)]
    rd.shuffle(images)
    foils = images[n_images_used:]
    images = images[0:n_images_used]
    variants = ['a','b','c']
    image_files = []
    foil_files = []
    for im in images:
        vars = variants.copy()
        rd.shuffle(vars)
        for v in vars:
            file = 'Stimuli/Fractals/' + str(im) + v + '.jpg'
            image_files.append(file)
    image_files = np.reshape(image_files, (n_images_used, 3))

    for f in foils:
        vars = variants.copy()
        rd.shuffle(vars)
        for v in vars:
            file = 'Stimuli/Fractals/' + str(f) + v + '.jpg'
            foil_files.append(file)
    foil_files = np.reshape(foil_files, (n_all_images - n_images_used, 3))

    return image_files, foil_files

def create_stimtable(images, fname):
    stim_table = pd.read_excel(fname)
    TripletMembers = ['TripletMemberA','TripletMemberB','TripletMemberC']
    for TripletMember in TripletMembers:
        stim_table[TripletMember] = stim_table[TripletMember].astype(str) #change None (float) to 'None' (string)

    im_index = 1 #index used to loop through the images - starts at 1 because BL is always image 0
    for i, row in stim_table.iterrows():
        delay = i + stim_table.at[i, 'Delay'] + 1
        # select image for BL #
        if row['Order'] == 0:
            for TripletMember, j in zip(TripletMembers, [0,1,2]):
                stim_table.at[i, TripletMember] = images[0][j]
        #select image for non-BL trials, first and second presentation
        elif row['Order'] == 1:
            for TripletMember, j in zip(TripletMembers, [0,1,2]):
                stim_table.at[i, TripletMember] = images[im_index][j] # first presentation
                stim_table.at[delay, TripletMember] = images[im_index][j] # second presentation (based on 'Delay' value)

            im_index += 1

    return stim_table

def set_image(stim_table, tr, task):
    image = 'Error - no image found'
    #for encoding
    if task == 'encoding':
        if stim_table.at[tr, 'StimType'] == 'OLP' and stim_table.at[tr, 'Order'] == 2:
            image = stim_table.at[tr, 'TripletMemberB']
        else:
            image = stim_table.at[tr, 'TripletMemberA']
    elif task == 'recognition' or task=='practice':
        image = stim_table.at[tr, 'ImagePresented']
    else:
        print('Task unknown. Choose encoding, recognition or practice')
    return image

def set_position(stim_table, tr):
    position = (0,0)
    if stim_table.at[tr, 'StimType'] == 'LLP' and stim_table.at[tr, 'Order'] == 2: #in the recognition table, StimType is always FOIL, TARGET or LURE. in the encodint stim_table, StimType is LLP, ERP or LLP 
        position = (stim_table.at[tr, 'Xcoordinate_lure1'], stim_table.at[tr, 'Ycoordinate_lure1'])
    else:
        position = (stim_table.at[tr, 'Xcoordinate'], stim_table.at[tr, 'Ycoordinate'])

    return position

def set_recognition_row(recognition_table, i, trial_type, recognition_type, stimuli_table, stimuli_index, foilx = None, foily = None):
    if trial_type == 'LOC':
        image = 'TripletMemberA'
        if recognition_type == 'FOIL':
            coordX = 'Xcoordinate_foil'
            coordY = 'Ycoordinate_foil'
        elif recognition_type == 'LURE':
            coordX = 'Xcoordinate_lure2'
            coordY = 'Ycoordinate_lure2'
        elif recognition_type == 'TARGET':
            coordX = 'Xcoordinate'
            coordY = 'Ycoordinate'
    elif trial_type == 'OBJ':
        coordX = 'Xcoordinate'
        coordY = 'Ycoordinate'
        if recognition_type == 'LURE':
            image = 'TripletMemberC'
        elif recognition_type == 'TARGET':
            image = 'TripletMemberA'
    if trial_type == 'OBJ' and recognition_type == 'FOIL':
        if foilx == None:
            foilx = [-299.9187724,-299.2692151,-297.9715073,-299.9187724,-296.0284596,-293.4442802,-290.2245658,190.1492902,-286.3762897,-281.9077862,238.5362389,-161.9251974,-276.8287333,274.0636373,\
                    -293.4442802,-290.2245658,118.8239298,-271.150131,-264.8842779,-276.8287333,-258.0447444,-250.6463434,-242.7050983,-234.238208,-225.2640099,-195.4971686,-234.238208,-264.8842779,\
                    -215.8019401,-205.8724914,-250.6463434,-242.7050983,-195.4971686,-225.2640099,-184.6984426,-215.8019401,-173.4997009,-161.9251974,-205.8724914,-173.4997009,-150,-137.749936,-125.2015363,\
                    -184.6984426,-161.9251974,-125.2015363,-112.381978,-99.31902537,-86.04096981,220.5927024,-137.749936,-72.57656868,-58.95498286,-258.0447444,-45.20571367,-299.9187724,-72.57656868,-58.95498286,\
                    -31.35853898,-17.44344867,-3.49057974,-45.20571367,10.46984901,24.4076024,-45.20571367,-31.35853898,24.4076024,-234.238208,38.29249436,52.0944533,65.78358726,-281.9077862,79.33024861,92.70509831,\
                    -58.95498286,79.33024861,105.8791694,118.8239298,92.70509831,65.78358726,131.511344,105.8791694,143.913934,-31.35853898,156.0048384,167.757871,179.1475775,190.1492902,200.7391819,143.913934,-184.6984426,\
                    294.816194,210.8943172,156.0048384,220.5927024,229.8133329,190.1492902,200.7391819,-150,238.5362389,246.7425286,220.5927024,254.4144288,261.5353241,238.5362389,246.7425286,268.0897921,274.0636373,\
                    -3.49057974,254.4144288,279.4439217,284.2189928,288.3785088,268.0897921,291.9134612,294.816194,-31.35853898,288.3785088,297.0804206,279.4439217,298.7012372,291.9134612,299.6751334,297.0804206,294.816194,\
                    298.7012372,300,300,299.6751334,300,298.7012372,299.6751334,297.0804206,294.816194,300,291.9134612,288.3785088,284.2189928,-205.8724914,298.7012372,279.4439217,297.0804206,274.0636373,-264.8842779,\
                    291.9134612,268.0897921,261.5353241,274.0636373,254.4144288,-99.31902537,246.7425286,-297.9715073,238.5362389,246.7425286,-86.04096981,254.4144288,229.8133329,220.5927024,210.8943172,200.7391819,\
                    -296.0284596,210.8943172,190.1492902,229.8133329,179.1475775,167.757871,156.0048384,143.913934,200.7391819,-99.31902537,131.511344,-17.44344867,167.757871,118.8239298,105.8791694,-31.35853898,\
                    92.70509831,79.33024861,118.8239298,131.511344,65.78358726,92.70509831,52.0944533,105.8791694,38.29249436,24.4076024,79.33024861,38.29249436,10.46984901,65.78358726,-3.49057974,279.4439217,24.4076024,\
                    -3.49057974,-17.44344867,-31.35853898,-45.20571367,-58.95498286,-72.57656868,-86.04096981,-125.2015363,-45.20571367,-250.6463434,-17.44344867,-99.31902537,-72.57656868,-112.381978,-45.20571367,-125.2015363,\
                    -137.749936,-150,-112.381978,-161.9251974,279.4439217,-173.4997009,-125.2015363,254.4144288,-184.6984426,-195.4971686,-205.8724914,-184.6984426,-173.4997009,-215.8019401,-225.2640099,-205.8724914,\
                    -195.4971686,-234.238208,-242.7050983,-250.6463434,300,-225.2640099,-234.238208,-258.0447444,298.7012372,-264.8842779,300,-271.150131,-264.8842779,-276.8287333,-31.35853898,-281.9077862,-286.3762897,\
                    -290.2245658,-281.9077862,-299.9187724,-276.8287333,-293.4442802,-296.0284596,-297.9715073,-293.4442802,-299.2692151,-297.9715073,-299.9187724,118.8239298,-296.0284596,-299.9187724]
        if foily == None:
            foily = [-6.980686912,-20.92694212,-34.82787424,-6.980686912,-48.65337693,-62.37350725,-75.95855043,232.0414778,-89.37908431,-102.606043,181.9353256,252.5474816,-115.6107798,122.0209929,-62.37350725,-75.95855043,\
                    275.4648321,-128.3651295,-140.8414688,-115.6107798,-153.0127769,-164.8526934,-176.3355757,-187.4365544,-198.1315872,-227.554075,-187.4365544,-140.8414688,-208.3975111,-218.2120925,-164.8526934,-176.3355757,\
                    -227.554075,-198.1315872,-236.4032261,-208.3975111,-244.7403804,-252.5474816,-218.2120925,-244.7403804,-259.8076211,-266.5050752,-272.6253387,-236.4032261,-252.5474816,-272.6253387,-278.1551564,-283.0825519,\
                    -287.3968537,-203.3195997,-266.5050752,-291.0887179,-294.1501487,-153.0127769,-296.5745158,6.980686912,-291.0887179,-294.1501487,-298.3565686,-299.4924475,-299.9796924,-296.5745158,-299.8172481,-299.0054664,\
                    296.5745158,-298.3565686,-299.0054664,-187.4365544,-297.5461055,-295.4423259,-292.6986841,-102.606043,-289.321122,-285.3169549,-294.1501487,-289.321122,-280.6948548,-275.4648321,-285.3169549,-292.6986841,\
                    -269.6382139,-280.6948548,-263.2276194,-298.3565686,-256.2469325,-248.7112718,-240.6369578,-232.0414778,-222.9434476,-263.2276194,-236.4032261,55.52847691,-213.3625716,-256.2469325,-203.3195997,-192.8362829,\
                    -232.0414778,-222.9434476,259.8076211,-181.9353256,-170.6403369,-203.3195997,-158.9757793,-146.9669155,-181.9353256,-170.6403369,-134.6397541,-122.0209929,-299.9796924,-158.9757793,-109.1379615,-96.01856153,\
                    -82.69120675,-134.6397541,-69.18476122,-55.52847691,-298.3565686,-82.69120675,-41.75193029,-109.1379615,-27.88495828,-69.18476122,-13.95759366,-41.75193029,-55.52847691,-27.88495828,-7.35E-14,0,13.95759366,\
                    -7.35E-14,27.88495828,13.95759366,41.75193029,55.52847691,0,69.18476122,82.69120675,96.01856153,-218.2120925,27.88495828,109.1379615,41.75193029,122.0209929,-140.8414688,69.18476122,134.6397541,146.9669155,\
                    122.0209929,158.9757793,283.0825519,170.6403369,-34.82787424,181.9353256,170.6403369,-287.3968537,158.9757793,192.8362829,203.3195997,213.3625716,222.9434476,-48.65337693,213.3625716,232.0414778,192.8362829,\
                    240.6369578,248.7112718,256.2469325,263.2276194,222.9434476,-283.0825519,269.6382139,299.4924475,248.7112718,275.4648321,280.6948548,-298.3565686,285.3169549,289.321122,275.4648321,269.6382139,292.6986841,\
                    285.3169549,295.4423259,280.6948548,297.5461055,299.0054664,289.321122,297.5461055,299.8172481,292.6986841,299.9796924,109.1379615,299.0054664,299.9796924,299.4924475,298.3565686,296.5745158,294.1501487,\
                    291.0887179,287.3968537,-272.6253387,296.5745158,-164.8526934,299.4924475,283.0825519,291.0887179,278.1551564,-296.5745158,272.6253387,266.5050752,259.8076211,278.1551564,252.5474816,109.1379615,244.7403804,\
                    272.6253387,-158.9757793,236.4032261,227.554075,218.2120925,236.4032261,244.7403804,208.3975111,198.1315872,218.2120925,227.554075,187.4365544,176.3355757,164.8526934,-7.35E-14,198.1315872,187.4365544,153.0127769,\
                    -27.88495828,140.8414688,-7.35E-14,128.3651295,140.8414688,115.6107798,298.3565686,102.606043,89.37908431,75.95855043,102.606043,-6.980686912,115.6107798,62.37350725,48.65337693,34.82787424,62.37350725,20.92694212,\
                    34.82787424,6.980686912,-275.4648321,48.65337693,6.980686912]

        recognition_table.at[i, 'ImagePresented'] = stimuli_table[stimuli_index][0]
        recognition_table.at[i, 'Xcoordinate'] = foilx[stimuli_index]
        recognition_table.at[i, 'Ycoordinate'] = foily[stimuli_index]
        recognition_table.at[i, 'EncodingImage'] = 'nan'
        recognition_table.at[i, 'EncodingXcoordinate'] = 0
        recognition_table.at[i, 'EncodingYcoordinate'] = 0
        recognition_table.at[i, 'EncodingTrialIndex'] = 0
    else:
        recognition_table.at[i, 'ImagePresented'] = stimuli_table.at[stimuli_index, image]
        recognition_table.at[i, 'Xcoordinate'] = stimuli_table.at[stimuli_index, coordX]
        recognition_table.at[i, 'Ycoordinate'] = stimuli_table.at[stimuli_index, coordY]
        recognition_table.at[i, 'EncodingImage'] = stimuli_table.at[stimuli_index, 'TripletMemberA']
        recognition_table.at[i, 'EncodingXcoordinate'] = stimuli_table.at[stimuli_index, 'Xcoordinate']
        recognition_table.at[i, 'EncodingYcoordinate'] = stimuli_table.at[stimuli_index, 'Ycoordinate']
        recognition_table.at[i, 'EncodingTrialIndex'] = stimuli_table.at[stimuli_index, 'TrialIndex']

    return recognition_table

def create_recognition_table(encoding_table, foils, fname = 'StimTable-Recognition.txt'):
    # get OLP stimuli
    olp = encoding_table.loc[(encoding_table['StimType'] == 'OLP') & (encoding_table['Order'] == 1)].reset_index(drop=True)
    olp.sample(frac=1).reset_index(drop=True)
    i_olp = 0
    # get LLP stimuli
    llp =encoding_table.loc[(encoding_table['StimType'] == 'LLP') & (encoding_table['Order'] == 1)].reset_index(drop=True)
    llp.sample(frac=1).reset_index(drop=True)
    i_llp = 0
    #get ERP stimuli
    erp =encoding_table.loc[(encoding_table['StimType'] == 'ERP') & (encoding_table['Order'] == 1)].reset_index(drop=True)
    erp.sample(frac=1).reset_index(drop=True)
    i_erp = 0
    #get OLP foil locations
    #loop through recog table and add lines
    recognition_table = pd.read_csv(fname, sep='\t', lineterminator='\n')
    recognition_table['ImagePresented'] = recognition_table['ImagePresented'].astype(str) # change to string Nan
    recognition_table['EncodingImage'] = recognition_table['EncodingImage'].astype(str) # change to string Nan
    i_foil = 0 #index for looping through foils
    for i, row in recognition_table.iterrows():
        if row['StimType'] == 'FOIL' and row['TrialType'] == 'OBJ':
                recognition_table = set_recognition_row(recognition_table, i, 'OBJ', 'FOIL', foils, i_foil)
                i_foil += 1
        else:
            if row['EncodingStimType'] == 'OLP':
                recognition_table = set_recognition_row(recognition_table, i, row['TrialType'], row['StimType'], olp, i_olp)
                i_olp += 1
            elif row['EncodingStimType'] == 'LLP':
                recognition_table = set_recognition_row(recognition_table, i, row['TrialType'], row['StimType'], llp, i_llp)
                i_llp += 1
            elif row['EncodingStimType'] == 'ERP':
                recognition_table = set_recognition_row(recognition_table, i, row['TrialType'], row['StimType'], erp, i_erp)
                i_erp += 1

    return recognition_table

def get_trialtype(stim_table, tr):
     return stim_table.at[tr, 'TrialType']
