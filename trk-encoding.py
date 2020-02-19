# TODO:
# complete cover-up story
# improve log files #

# Task Procedure
# 1. Welcome Screen
# 2. Left and Right Button Check
# 3. Screen Check
# 4. Instructions
# 5. Practice
# 6. Task
#    - loop through stimuli list
#    - with a break every 3 blocks
# 7. Thanks & good bye
from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

import pandas as pd
# import own module #
import trk_module as trk

task = 'encoding'
image_size = 300
cont = 1 # Flag for continuing the experiment, 0 will quit

# Set durations
welcome_duration = 2.0
pause_duration = 2.0
welcome_duration = 2.0
goodbye_duration = 2.0
image_presentation_time = 2.5
pause = 1

# Response buttons
resp_0 = 'f' # response 'not art'
resp_1 = 'j' # response 'art'
next = 'right'
back = 'left'
pause_button = 'p'
experimenter = 'e'

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.2.4'
expName = 'TerKepEsz'  # from the Builder filename that created this script
expInfo = {'participant': '', 'practice': '1', 'trial': '0'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion
expInfo['Task'] = task

# start from trial specified by the user
first_trial = int(expInfo['trial'])
# check whether practice is needed
practice = int(expInfo['practice'])

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s_%s' % (expInfo['participant'],task, expName, expInfo['date'])
dataFile = open(filename+'.csv', 'w')  # a simple text file with 'comma-separated-values'

# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

# Select images and create stimulus table for BOTH tasks
jitters = trk.read_jitters('jitters-Encoding.txt')
images, foils = trk.select_images(n_images_used = 121, n_all_images= 145)
fname = 'data/stim_tables/' + expInfo['participant'] + '_stim_table.csv'
# try to read the participant's stimuli table, in case they have one already
try:
    stim_table = pd.read_csv(fname, sep=',', lineterminator='\n')
except:
    stim_table = trk.create_stimtable(images, 'StimuliTable-Encoding-3run-40-315-24568.csv')
    recogniton_table = trk.create_recognition_table(stim_table, foils, fname = 'StimTable-Recognition.txt')
    recogniton_table.to_csv(os.path.join('data','stim_tables',expInfo['participant']+'_recognition_table.csv'))
    stim_table.to_csv(os.path.join('data','stim_tables', expInfo['participant']+'_stim_table.csv'))

practice_table = pd.read_csv('practice_trials.csv', sep=',', lineterminator='\n')

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0,
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[1.000,1.000,1.000], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    units='deg')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Welcome Components
welcomeClock = core.Clock()
welcome_msg = visual.TextStim(win=win, name='welcome_msg',
    text='TérKépÉsz',
    font='Arial',
    pos=(0, 12), height=1, wrapWidth=None, ori=0,
    color='black', colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=0.0);
logo = visual.ImageStim(
    win=win,
    name='logo', units='norm',
    image='Stimuli/terkepesz.png', mask=None,
    ori=0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Button check Components
button_check = visual.TextStim(win=win, name='lb_check',
    text='Válaszgomb teszt:\n\nNyomja le az \'F\' billentyűt!',
    font='Arial',
    pos=(-23, 0), height=0.9, wrapWidth=None, ori=0,
    color='black', colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=0.0);

# Screen Check Components
left_upper = visual.ImageStim(
    win=win,
    name='left_upper', units='norm',
    image='Stimuli/ScreenCorner1.png', mask=None,
    ori=0, pos=(-0.9, 0.7), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
left_lower = visual.ImageStim(
    win=win,
    name='left_lower', units='norm',
    image='Stimuli/ScreenCorner2.png', mask=None,
    ori=0, pos=(-0.9, -0.7), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
right_upper = visual.ImageStim(
    win=win,
    name='right_upper', units='norm',
    image='Stimuli/ScreenCorner3.png', mask=None,
    ori=0, pos=(0.9, 0.7), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
right_lower = visual.ImageStim(
    win=win,
    name='right_lower', units='norm',
    image='Stimuli/ScreenCorner4.png', mask=None,
    ori=0, pos=(0.9, -0.7), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
screen_check_text = visual.TextStim(win=win, name='text_2',
    text='Ha a képernyő mind a négy sarkát látja, nyomja le a jobb nyilat.',
    font='Arial',
    units='deg', pos=(0, 0), height=0.9, wrapWidth=30, ori=0,
    color='black', colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=-4.0);

# Story and Instructions Components
gallery_outside_image = visual.ImageStim(
    win=win,
    name='story1_image', units='norm',
    image='Stimuli/GalleryBuildingFromOutside.jpg', mask=None,
    ori=0, pos=(0, 0.9), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
gallery_outside_text = visual.TextStim(win=win, name='story1_text',
    text='Ön ennek a modern képgalériának a kurátora.\nA legújabb kiállításra a vártnál több kép érkezett.\
    \n\nKurátorként az Ön feladata lesz eldönteni, mely képeket válogatjuk be a kiállított darabok közé, és hogy a kép illeszkedik-e a galéria adott pontjára.\
    Az Ön ideje nagyon drága a galériának, így a döntésre egy-egy képről csak 2.5 másodperce lesz.\
    \n\nA folytatáshoz nyomja le a jobb nyilat.',
    font='Arial',
    units='deg', pos=(0, -5), height=0.9, wrapWidth=30, ori=0,
    color='black', colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=-1.0);

gallery_inside_image = visual.ImageStim(
    win=win,
    name='story2_image', units='pix',
    image='Stimuli/GalleryInfo.jpg', mask=None,
    ori=0, pos=(425, 0), size=(1000,750),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

gallery_inside_text = visual.TextStim(win=win, name='story2_text',
    text='Ez a galéria térképe felülről, nézze meg figyelmesen.\n\nA feladat során a képek a térképre vetítve jelennek meg,\nazon a helyen, ahol kiállításra kerülhetnek.\n\nDöntse el a képekről, hogy ki legyenek-e állítva a bemutatott helyen.\
    \n\nMinden képet nézzen meg figyelmesen, és minden képre adjon választ.\
    \n\nA folytatáshoz nyomja le a jobb nyilat.\n',
    font='Arial',
    units='deg', pos=(-14, 0), height=0.9, wrapWidth=24, ori=0,
    color='black', colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=-2.0);

instr_text = visual.TextStim(win=win, name='instr_text',
    text='A \'J\' billentyűvel jelölje azokat a képeket, amelyek maradhatnak a galériában, a bemutatott helyen.\n\nAz \'F\' billentyűvel jelölje a képeket, amelyek nem maradnak kiállítva a bemutatott helyen. \n\nHa készen áll a gyakorlásra, nyomja le a jobb nyilat.',
    font='Arial',
    units='deg', pos=(0, 0), height=0.9, wrapWidth=None, ori=0,
    color='black', colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=0.0);

participant_choice = visual.TextStim(win=win, name='instr_text',
    text='',
    font='Arial',
    units='deg', pos=(0, 0), height=0.9, wrapWidth=None, ori=0,
    color='black', colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=0.0);

# Start Task Components
start_task_text = visual.TextStim(win=win, name='start_task_text',
    text='Ez volt a gyakorlás.\
    \n\nHa kezdhetjük a feladatot, nyomja le a jobb nyilat.\n\n Ha újra szeretne gyakorolni, nyomjon le bármilyen más billentyűt',
    font='Arial',
    pos=(0, 0), height=0.9, wrapWidth=None, ori=0,
    color='black', colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=0.0);

# Trial Components
# Gallery Map
fixationClock = core.Clock()
galley_map = visual.ImageStim(
    win=win,
    name='map_inside_fx', units='pix',
    image='Stimuli/GalleryPlanInside.jpg', mask=None,
    ori=0, pos=(0, -25), size=(1040, 1000),
    color=[1,1,1], colorSpace='rgb', opacity=0.5,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
# Fixation Cross
fixation_cross = visual.ShapeStim(
    win=win, name='fixation_cross', vertices='cross',units='pix',
    size=(20, 20),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[-1.000,-1.000,-1.000], lineColorSpace='rgb',
    fillColor=[-1.000,-1.000,-1.000], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
key_resp_fx = keyboard.Keyboard()
# Main image
main_image = visual.ImageStim(
    win=win,
    name='main_image', units='pix',
    image=stim_table.at[0, 'TripletMemberA'], mask=None,
    ori=0, pos=[0,0], size=300,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Next-Run Components
text_long_pause = visual.TextStim(win=win, name='text_pause',
    text='Szünet. A folytatáshoz nyomja le a jobb nyilat.',
    font='Arial',
    units='deg', pos=(0, 0), height=0.9, wrapWidth=None, ori=0,
    color='black', colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=-2.0);

text_pause = visual.TextStim(win=win, name='text_pause',
    text='Szünet...',
    font='Arial',
    units='deg', pos=(0, 0), height=0.7, wrapWidth=None, ori=0,
    color='black', colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=-2.0);

# Goodbye Message Components
text_goodbye = visual.TextStim(win=win, name='text_goodbye',
    text='Vége a feladatnak. Köszönjük!',
    font='Arial',
    units='deg', pos=(0, 0), height=1.5, wrapWidth=20, ori=0,
    color='black', colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=-2.0);

def insert_pause(text = text_long_pause, response = next):
    '''Will pause the experiment until response button is pressed.'''
    keep_paused = 1
    cont = 1
    while keep_paused and cont:
        text.draw()
        win.flip()
        thisKey = keyboard.Keyboard().getKeys()
        if thisKey == ['escape']:
            cont = 0
        elif thisKey == [response]:
            keep_paused = 0
    return cont

# ##############################################################################################################
# Procedure
# ##############################################################################################################

#1. Welcome
welcomeClock = core.Clock()
while welcomeClock.getTime() < welcome_duration and cont: # Clock times are in seconds
    thisKey = keyboard.Keyboard().getKeys()
    if thisKey == ['escape']:
        cont = 0
    welcome_msg.draw()
    logo.draw()
    win.flip()

#2. Button ckecks
resp_0_ok = 0
while resp_0_ok == 0 and cont:
    button_check.draw()
    win.flip()
    allKeys=event.waitKeys()
    if allKeys == ['escape']:
        cont = 0
    if allKeys == [resp_0]:
        resp_0_ok = 1

button_check.text ='Válaszgomb teszt:\n\nNyomja le a \'J\' billentyűt!'
button_check.pos = (23, 0)

resp_1_ok = 0
while resp_1_ok == 0 and cont:
    button_check.draw()
    win.flip()
    allKeys=event.waitKeys()
    if allKeys == ['escape']:
        cont = 0
    if allKeys == [resp_1]:
        resp_1_ok = 1

#3. Screen Check
screen_check = 1
while screen_check and cont:
    left_upper.draw()
    left_lower.draw()
    right_upper.draw()
    right_lower.draw()
    screen_check_text.draw()
    win.flip()
    allKeys=event.waitKeys()
    if allKeys == ['escape']:
        cont = 0
    if allKeys == [next]:
        screen_check = 0

#4. Instructions
gallery_outside = 1
while gallery_outside and cont:
    gallery_outside_image.draw()
    gallery_outside_text.draw()
    win.flip()
    allKeys=event.getKeys()
    if allKeys == ['escape']:
        cont = 0
    elif allKeys == [next]:
        gallery_outside=0

gallery_inside = 1
while gallery_inside and cont:
    gallery_inside_image.draw()
    gallery_inside_text.draw()
    win.flip()
    allKeys=event.getKeys()
    if allKeys == ['escape']:
        cont = 0
    elif allKeys == [next]:
        gallery_inside=0

instructions = 1
while instructions and cont:
    instr_text.draw()
    win.flip()
    allKeys=event.getKeys()
    if allKeys == ['escape']:
        cont = 0
    elif allKeys == [next]:
        instructions=0

# 5. Practice
fixationTimer = core.CountdownTimer()
feedbackTimer = core.CountdownTimer()
imageTimer = core.CountdownTimer()
practiceTimer = core.CountdownTimer()
while practice and cont:
    instr_text.setText('Figyeljen, kezdődik a gyakorlás.')
    trials = len(practice_table.index)
    practiceTimer.reset(2.0)
    while cont and practiceTimer.getTime() > 0:
        instr_text.draw()
        win.flip()
        thisKey = keyboard.Keyboard().getKeys()
        if thisKey == ['escape']:
            cont = 0
        elif thisKey == [pause_button]:
            cont = insert_pause()
    for pr in range(trials):
        # update component parameters for each repeat
        main_image.setPos(trk.set_position(practice_table,pr))
        main_image.setImage(trk.set_image(practice_table,pr, 'practice'))

        fx = 1
        while cont and fx:
            fixationTimer.reset(practice_table.at[pr, 'Jitter'])
            while cont and fixationTimer.getTime() > 0:
                galley_map.draw()
                fixation_cross.draw()
                win.flip()
                theseKeys = keyboard.Keyboard().getKeys()
                if theseKeys == ['escape']:
                    cont = 0
                elif theseKeys == [pause_button]:
                    fx = 1
                    cont = insert_pause()
                else:
                    fx = 0

        imageTimer.reset(image_presentation_time)
        while cont and imageTimer.getTime() > 0:
            galley_map.draw()
            main_image.draw()
            win.flip()
            theseKeys = keyboard.Keyboard().getKeys()
            if theseKeys == ['escape']:
                cont = 0
            elif theseKeys == [resp_1]:
                participant_choice.setText('Az Ön döntése: A kép marad.')
            elif theseKeys == [resp_0]:
                participant_choice.setText('Az Ön döntése: A kép nem marad.')
            elif theseKeys == [pause_button]:
                cont = insert_pause()

        # Give some feedback to the participant if there was an answer
        if participant_choice.text != '':
            feedbackTimer.reset(2)
            while cont and feedbackTimer.getTime() > 0:
                galley_map.draw()
                main_image.draw()
                participant_choice.draw()
                win.flip()
                thisKey=event.getKeys()
                if thisKey == ['escape']:
                    cont = 0
                elif thisKey == [pause_button]:
                    cont = insert_pause()

            participant_choice.setText('')

        theseKeys = keyboard.Keyboard().getKeys()
        if 'escape' in theseKeys:
            cont = 0

    # ask user if they want to practice more
    if cont:
        start_task_text.draw()
        win.flip()
        allKeys=event.waitKeys()
        if allKeys == ['escape']:
            cont = 0
        elif allKeys == [next]:
            practice = 0
        else:
            practice = 1

instr_text.setText('A kísérletvezető indítja a feladatot.')
starting = 1
while cont and starting:
    instr_text.draw()
    win.flip()
    thisKey = keyboard.Keyboard().getKeys()
    if thisKey == ['escape']:
        cont = 0
    elif thisKey == [experimenter]:
        starting =0

start_task_text.setText('Figyeljen, kezdődik a feladat...')
# Start task
startTaskTimer = core.CountdownTimer(2.)
while cont and startTaskTimer.getTime() > 0:
    start_task_text.draw()
    win.flip()
    thisKey = keyboard.Keyboard().getKeys()
    if thisKey == ['escape']:
        cont = 0

# 6. Task
t_index = 0
s_order = -1
s_type = 'NaN'
s_image = 'NaN'
xcoordinate = 0
ycoordinate = 0
dataFile.write('TrialIndex,Order,StimType,FX/IMG,ImagePreseneted,Xcoordinate,Ycoordinate,Response,RT, TimePassed\n')
#trials = len(stim_table.index)
trials = np.arange(first_trial,len(stim_table.index),1, dtype =int)
rt_timer = core.Clock() # for reaction time
expClock = core.Clock()  # to track the time since experiment started
previous_run = 1
for tr in trials:
    if stim_table['ScannerRun'][tr] != previous_run:
        cont = insert_pause()
        previous_run = stim_table['ScannerRun'][tr]
    # update component parameters for each repeat
    main_image.setPos(trk.set_position(stim_table,tr))
    main_image.setImage(trk.set_image(stim_table,tr, task))

    fx = 1
    while cont and fx:
        fixationTimer.reset(jitters[tr])
        while cont and fixationTimer.getTime() > 0:
            galley_map.draw()
            fixation_cross.draw()
            win.flip()
            theseKeys = keyboard.Keyboard().getKeys()
            if theseKeys == ['escape']:
                cont = 0
            elif len(theseKeys) != 0:
                dataFile.write('%i,%i,%s,%s,%s,%.6f,%.6f,%s,%.6f,%.6f\n' %(t_index, s_order, s_type,'FX',s_image, xcoordinate, ycoordinate,theseKeys[0].name, rt_timer.getTime(), expClock.getTime())) #log events during fixation belonging to the previous trial (image not seen yet)
                if theseKeys == [pause_button]:
                    cont = insert_pause()
                    fx = 1
                else:
                    fx = 0
            else:
                fx = 0


    # update trial index, type and stimulus type for logging
    t_index = stim_table.at[tr, 'TrialIndex']
    s_order = stim_table.at[tr, 'Order']
    s_type = stim_table.at[tr, 'StimType']
    s_image = main_image.image
    xcoordinate=main_image.pos[0]
    ycoordinate=main_image.pos[1]

    rt_timer.reset()
    imageTimer.reset(image_presentation_time)
    while cont and imageTimer.getTime() > 0:
        galley_map.draw()
        # text_trial.draw() # for testing the right input
        main_image.draw()
        win.flip()
        theseKeys = keyboard.Keyboard().getKeys()
        if theseKeys == ['escape']:
            cont = 0
        elif len(theseKeys) != 0:
            dataFile.write('%i,%i,%s,%s,%s,%.6f,%.6f,%s,%.6f,%.6f\n' %(t_index, s_order, s_type,'IMG',s_image, xcoordinate, ycoordinate,theseKeys[0].name, rt_timer.getTime(), expClock.getTime()))
            if theseKeys == [pause_button]:
                cont = insert_pause()

    theseKeys = keyboard.Keyboard().getKeys()
    if 'escape' in theseKeys:
        cont = 0
    elif len(theseKeys) != 0:
        dataFile.write('%i,%i,%s,%s,%s,%.6f,%.6f,%s,%.6f,%.6f\n' %(t_index, s_order, s_type,'-',s_image, xcoordinate, ycoordinate,theseKeys[0].name,rt_timer.getTime(), expClock.getTime()))
        if theseKeys == [pause_button]:
            cont = insert_pause()

    if cont == 0:
        break

dataFile.close()
#7. Goodbye
logo.opacity = 0.8
logo.draw()
text_goodbye.draw()
win.flip()
event.waitKeys()
core.quit()
