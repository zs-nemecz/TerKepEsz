# This module contais functions necessary for creating unique stimuli tables for
# each participant based on the queasi-randomized structure laid out in the
# StimuliTable-Encoding and StimTable-Recognition
# Taken from the offline TerKepEsz experiment version.
# Modified for online use and 'hard-coded' trial order.

# Abbreviations:
# OLP - Object Lure Pair
# LLP - Location Lure Pair
# ERP - Exact Repeat Pair
# BL - Baseline (repeated more than once)

import pandas as pd
import numpy as np
import random as rd

def get_exp_parameters(encoding_table, recognition_table):
    '''Read dataframes and return the number of encoding images, BL trials, and foil images'''
    n_bl = encoding_table[encoding_table.StimType == 'BL'].shape[0]
    # define number of images based on the number of rows in the StimuliTable
    # and the count of BL trials
    n_encoding_images = ((len(encoding_table.index) - n_bl)/2) + 1 # add 1 for the baseline image
    n_encoding_images = int(n_encoding_images)

    # define number of all images as encoding images plus Object trial - foil images
    object = recognition_table.TrialType == 'OBJ'
    foil = recognition_table.StimType == 'FOIL'
    object_foil = object & foil
    n_foils = recognition_table[object_foil].shape[0]
    n_all_images = n_foils + n_encoding_images
    n_all_images = int(n_all_images)

    return n_encoding_images, n_all_images

def select_images(n_images_used, n_all_images):
    '''Randomize image type order and select encoding and foil images. Images
    are organized in a 3 by n_all_images shape array.
    First dimensions are variants a,b and c, in random order.'''
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
            file = 'stimuli/fractals/' + str(im) + v + '.jpg'
            image_files.append(file)
    image_files = np.reshape(image_files, (n_images_used, 3))

    for f in foils:
        vars = variants.copy()
        rd.shuffle(vars)
        for v in vars:
            file = 'stimuli/fractals/' + str(f) + v + '.jpg'
            foil_files.append(file)
    foil_files = np.reshape(foil_files, (n_all_images - n_images_used, 3))

    return image_files, foil_files

def set_encoding_image(stim_table, trial_index):
    '''Set currently presented image for each trial based on trial type and
    order of presentation.'''
    image = None
    if stim_table.at[trial_index, 'StimType'] == 'OLP' and stim_table.at[trial_index, 'Order'] == 2:
        image = stim_table.at[trial_index, 'TripletMemberB']
    else:
        image = stim_table.at[trial_index, 'TripletMemberA']
    return image

def set_encoding_position(stim_table, tr):
    '''Set X and Y coordinate of currently presented image for each trial based
    on trial type and order of presentation. Returns with tuple (CurrentX, CurrentY).'''
    position = (0,0)
    if stim_table.at[tr, 'StimType'] == 'LLP' and stim_table.at[tr, 'Order'] == 2: #in the recognition table, StimType is always FOIL, TARGET or LURE. in the encodint stim_table, StimType is LLP, ERP or LLP
        position = (stim_table.at[tr, 'Xcoordinate_lure1'], stim_table.at[tr, 'Ycoordinate_lure1'])
    else:
        position = (stim_table.at[tr, 'Xcoordinate'], stim_table.at[tr, 'Ycoordinate'])

    return position

def set_encoding_trials(encoding_table, images):
    '''Create table of trials based on the StimuliTable-Encoding where images are
     randomized but bound by trial type and presentation order between pairs.'''
    encoding_trials = encoding_table
    TripletMembers = ['TripletMemberA','TripletMemberB','TripletMemberC']
    # change None (float) to 'None' (string) for image name columns
    for TripletMember in TripletMembers:
        encoding_trials[TripletMember] = encoding_trials[TripletMember].astype(str)
    encoding_trials['CurrentImage'] = encoding_trials['CurrentImage'].astype(str)

    im_index = 1 #index used to loop through the images - starts at 1 because BL is always image 0
    for i, row in encoding_trials.iterrows():
        delay = i + encoding_trials.at[i, 'Delay'] + 1
        # select image for BL #
        if row['Order'] == 0:
            for TripletMember, j in zip(TripletMembers, [0,1,2]):
                encoding_trials.at[i, TripletMember] = images[0][j]
        #select image for non-BL trials, first and second presentation
        elif row['Order'] == 1:
            for TripletMember, j in zip(TripletMembers, [0,1,2]):
                encoding_trials.at[i, TripletMember] = images[im_index][j] # first presentation
                encoding_trials.at[delay, TripletMember] = images[im_index][j] # second presentation (based on 'Delay' value)
            # increase image index only once per image pair (when Order==1)
            im_index += 1
        encoding_trials.at[i, 'CurrentImage'] = set_encoding_image(encoding_trials, i)
        encoding_trials.at[i, 'CurrentX'], encoding_trials.at[i, 'CurrentY'] = set_encoding_position(encoding_trials, i)
    return encoding_trials

def fill_from_encoding(recognition_trials, i, encoding_trials, stimuli_index):
    '''Copy corrsponding values from the encoding trials to the recognition trials'''
    TripletMembers = ['TripletMemberA', 'TripletMemberB', 'TripletMemberC']
    Coordinates = ['Xcoordinate', 'Ycoordinate',\
                  'Xcoordinate_lure1', 'Ycoordinate_lure1',\
                  'Xcoordinate_lure2', 'Ycoordinate_lure2',\
                  'Xcoordinate_foil','Ycoordinate_foil']
    recognition_trials.loc[i, TripletMembers] = encoding_trials.loc[stimuli_index, TripletMembers]
    recognition_trials.loc[i, Coordinates] = encoding_trials.loc[stimuli_index, Coordinates]

    return recognition_trials

def set_recognition_row(recognition_trials, i, trial_type, recognition_type,\
                        stimuli_table, stimuli_index, foilx=None, foily=None):
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
        n_ofoils = int(len(recognition_trials)/6)
        if foilx == None:
            foilx = np.full(n_ofoils,0)
            print('Warning: Object Foils will be presented at center horizontally.')
        if foily == None:
            foily = np.full(n_ofoils,0)
            print('Warning: Object Foils will be presented at center vertically.')

        recognition_trials.at[i, 'CurrentImage'] = stimuli_table[stimuli_index][0]
        recognition_trials.at[i, 'CurrentX'] = foilx[stimuli_index]
        recognition_trials.at[i, 'CurrentY'] = foily[stimuli_index]
        recognition_trials.at[i, 'EncodingImage'] = 'nan'
        recognition_trials.at[i, 'EncodingXcoordinate'] = 0
        recognition_trials.at[i, 'EncodingYcoordinate'] = 0
        recognition_trials.at[i, 'EncodingTrialIndex'] = 0
    else:
        recognition_trials.at[i, 'CurrentImage'] = stimuli_table.at[stimuli_index, image]
        recognition_trials.at[i, 'CurrentX'] = stimuli_table.at[stimuli_index, coordX]
        recognition_trials.at[i, 'CurrentY'] = stimuli_table.at[stimuli_index, coordY]
        recognition_trials.at[i, 'EncodingImage'] = stimuli_table.at[stimuli_index, 'CurrentImage']
        recognition_trials.at[i, 'EncodingXcoordinate'] = stimuli_table.at[stimuli_index, 'CurrentX']
        recognition_trials.at[i, 'EncodingYcoordinate'] = stimuli_table.at[stimuli_index, 'CurrentY']
        recognition_trials.at[i, 'EncodingTrialIndex'] = stimuli_table.at[stimuli_index, 'TrialIndex']
        fill_from_encoding(recognition_trials, i, stimuli_table, stimuli_index)

    return recognition_trials

def set_recognition_trials(recognition_table, encoding_trials, foils):

    # for recognition trials, use 1st presentation of OLP, LLP and ERP stimuli from the encoding task
    # get OLP stimuli
    olp = encoding_trials.loc[(encoding_trials['StimType'] == 'OLP') & (encoding_trials['Order'] == 1)].reset_index(drop=True)
    olp.sample(frac=1).reset_index(drop=True)
    i_olp = 0 # index, for looping through OLPs
    # get LLP stimuli
    llp =encoding_trials.loc[(encoding_trials['StimType'] == 'LLP') & (encoding_trials['Order'] == 1)].reset_index(drop=True)
    llp.sample(frac=1).reset_index(drop=True)
    i_llp = 0 # index, for looping through LLPs
    #get ERP stimuli
    erp =encoding_trials.loc[(encoding_trials['StimType'] == 'ERP') & (encoding_trials['Order'] == 1)].reset_index(drop=True)
    erp.sample(frac=1).reset_index(drop=True)
    i_erp = 0 # index, for looping through ERPs

    # OLP foil coordinates - obtain from encoding trials and shuffle together
    foilx = encoding_trials['Xcoordinate_foil']
    foily = encoding_trials['Ycoordinate_foil']
    temp = list(zip(foilx, foily))
    rd.shuffle(temp)
    foilx, foily = zip(*temp)

    # set Image columns to string
    recognition_trials = recognition_table
    recognition_trials['CurrentImage'] = recognition_trials['CurrentImage'].astype(str) # change to string Nan
    recognition_trials['EncodingImage'] = recognition_trials['EncodingImage'].astype(str) # change to string Nan

    # loop through recog table and complete rows
    i_foil = 0 #index for looping through foil image names
    for i, row in recognition_trials.iterrows():
        if row['StimType'] == 'FOIL' and row['TrialType'] == 'OBJ':
                recognition_trials = set_recognition_row(recognition_trials, i, 'OBJ', 'FOIL', foils, i_foil, foilx, foily)
                i_foil += 1
        else:
            if row['EncodingStimType'] == 'OLP':
                recognition_trials = set_recognition_row(recognition_trials, i, row['TrialType'], row['StimType'], olp, i_olp)
                i_olp += 1
            elif row['EncodingStimType'] == 'LLP':
                recognition_trials = set_recognition_row(recognition_trials, i, row['TrialType'], row['StimType'], llp, i_llp)
                i_llp += 1
            elif row['EncodingStimType'] == 'ERP':
                recognition_trials = set_recognition_row(recognition_trials, i, row['TrialType'], row['StimType'], erp, i_erp)
                i_erp += 1

    return recognition_trials
