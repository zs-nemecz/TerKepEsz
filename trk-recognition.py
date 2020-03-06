# TODO:
# add third button check,
# improve log files

# Task Procedure
# 1. Welcome Screen
# 2. Left and Right Button Check
# 3. Screen Check
# 4. Instructions
# 5. Demo
# 6. Practice
# 7. Task
#    - loop through stimuli list
#    - with a break every 3 blocks
# 8. Thanks & good bye

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
import os
import sys
import pandas as pd

import trk_module as trk

from psychopy.hardware import keyboard

task = 'recognition'

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.2.4'
expName = 'TérKépÉsz'
expInfo = {'participant': '', 'demo': '1', 'practice': '1', 'trial': '0'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion
expInfo['Task'] = task

# check user settings
first_trial = int(expInfo['trial']) # which trial to start from
demo = int(expInfo['demo']) # should there be a stimuli demonstration?
practice = int(expInfo['practice']) # sould there be practice trials?

# save relevant data to csv file
filename = _thisDir + os.sep + u'data/%s_%s_%s_%s' % (expInfo['participant'],task, expName, expInfo['date'])
dataFile = open(filename+'.csv', 'w')  # a simple text file with 'comma-separated-values'

# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

# read files for stimuli psentation
stimuli_fname = os.path.join('data','stim_tables',expInfo['participant']+'_recognition_table.csv')
jitters = trk.read_jitters('jitters-Recognition.txt')
stim_table = pd.read_csv(stimuli_fname, sep=',', lineterminator='\n')
practice_table = pd.read_csv('recognition_practice_trials.csv', sep=',', lineterminator='\n')
demo_table = pd.read_csv('stimuli_demo.csv', sep=',', lineterminator='\n')

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

# Continue/Escape Flag (1/0) and Task Type
cont = 1

# Response buttons
resp_0 = 'f' # response 'old'
resp_1 = 'j' # response 'similar
resp_2 = 'k' # response 'new'
next = 'right'
back = 'left'
pause_button = 'p'
experimenter = 'space'

pause_duration = 2.0
welcome_duration = 2.0
goodbye_duration = 2.0
image_presentation_time = 4.0
pause = 1

# Welcome Image Components
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

# Instruction components
instr_text = visual.TextStim(win=win, name='instr_text',
    text='A következő feladatban ismét absztrakt képeket fog látni, és ezekről kell eldöntenie, látta-e őket az első, műalkotás válogató feladataban, és hogy ugyanott látta-e őket.\
    \n A feladatot két alfeladatra bontottuk. Az egyikben a képekről, a másikban a képek pozíciójáról kell döntenie.\
    \n\nA folytatáshoz nyomja le a jobb nyilat.',
    font='Arial',
    units='deg', pos=(0, 0), height=0.8, wrapWidth=40, ori=0,
    color='black', colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=0.0);

inst_task_text = 'A következő feladatban ismét absztrakt képeket fog látni, és ezekről kell eldöntenie, látta-e őket az első, műalkotás válogató feladataban, és hogy ugyanott látta-e őket.\
    \n A feladatot két alfeladatra bontottuk. Az egyikben a képekről, a másikban a képek pozíciójáról kell döntenie.\
    \n\nA folytatáshoz nyomja le a jobb nyilat.'

instr_image_text = 'A \'Kép\' nevű alfeladatban azt kell eldöntenie, látta-e már ezeket a képeket az első, műalkotás válogató feladataban.\
                    \nHárom csoportba oszthatóak a megjelenő képek:\
                    \n - Régi: Ezek a képek pontosan megegyeznek majd az első feladatban látott képek egyikével.\
                    \n - Hasonló: Ezek a képek nagyon hasonlítanak az első feladatban látott képek egyikéhez.\
                    \n - Új: Teljesen új képek, amelyek nem jelentek meg az első feladatban.\
                    \nAz Ön feladata, hogy eldöntse, melyik kép ugyanaz, mint az első feladatban, melyik hasonló, és melyik új. \nMinden képet nézzen meg figyelmesen, és minden képre adjon választ, akkor is, ha a döntés nehéz.\
                    \n\nA döntését így jelölje:\n\tRégi - F\t Hasonló - J\t Új - K\
                    \n\n A folytatáshoz nyomja le a jobb nyilat'


instr_location_text= 'A \'Hely\' nevű alfeladatban azt kell eldöntenie, a képek ugyanott jelennek-e meg, mint az első, műalkotás válogató feladataban.\
                    \nEbben az alfeladatban minden kép pontos mása annak, amit az első feladatban látott. A helyek azonban három csoportba oszthatóak:\
                    \n - Régi: Pontosan ugyanitt jelent meg ez a kép az első feladatban.\
                    \n - Hasonló: Egy hasonló helyen jelent meg ez a kép az első feladatban.\
                    \n - Új: Egy teljesen másik helyen jelent meg ez a kép az első feladatban.\
                    \nAz Ön feladata, hogy eldöntse, melyik kép jelent meg ugyanott, hasonló, és teljesen új helyen.\nMinden képet nézzen meg figyelmesen, és minden képre adjon választ, akkor is, ha a döntés nehéz.\
                    \n\nA döntését így jelölje:\n\tRégi - F\t Hasonló - J\t Új - K\
                    \n\nA folytatáshoz nyomja le a jobb nyilat.'

instr_demo_text= 'A következőkben bemutatjuk Önnek, milyenek a \'hasonló\'/\'új\' képek és helyek. \nA jobb nyillal tud továbblépni.'

instr_practice_text= 'Most a gyakorlás következik. Ha készen áll a gyakorlásra, nyomja le a jobb nyilat.\n\nHa újra megnézné a bemutatót, nyomjon le bármilyen más gombot.'

inst_texts = [inst_task_text, instr_image_text, instr_location_text, instr_demo_text]

# Practice Components
correct_answer = visual.TextStim(win=win, name='start_task_text',
    text='',
    font='Arial',
    units='deg',pos=(0, 1.5), height=0.9, wrapWidth=None, ori=0,
    color='black', colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=0.0);

answer_given = visual.TextStim(win=win, name='start_task_text',
    text='',
    font='Arial',
    units = 'deg', pos=(0, -1.5), height=0.9, wrapWidth=None, ori=0,
    color='black', colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=0.0);

# Demo compoenents
stim_type_text = visual.TextStim(win=win, name='start_task_text',
    text='',
    font='Arial',
    units = 'deg', pos=(-2, 0), height=0.9, wrapWidth=None, ori=0,
    color='black', colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=0.0);

trial_type_text = visual.TextStim(win=win, name='start_task_text',
    text='',
    font='Arial',
    units = 'deg', pos=(2, 0), height=0.9, wrapWidth=None, ori=0,
    color='black', colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=0.0);

demo_image = visual.ImageStim(
    win=win,
    name='main_image', units='pix',
    image=stim_table.at[0, 'ImagePresented'], mask=None,
    ori=0, pos=[0,0], size=300,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Trial Components
# Gallery Map
galley_map = visual.ImageStim(
    win=win,
    name='map_inside_fx', units='pix',
    image='Stimuli/GalleryPlanInside.jpg', mask=None,
    ori=0, pos=(0, -25), size=(1040, 1000),
    color=[1,1,1], colorSpace='rgb', opacity=0.7,
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
    image=stim_table.at[0, 'ImagePresented'], mask=None,
    ori=0, pos=[0,0], size=300,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Pause and Next Run Components
text_long_pause = visual.TextStim(win=win, name='text_pause',
    text='Szünet. A folytatáshoz nyomja le a jobb nyilat.',
    font='Arial',
    units='deg', pos=(0, 0), height=0.9, wrapWidth=None, ori=0,
    color='black', colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=-2.0);

text_practice = visual.TextStim(win=win, name='start_task_text',
    text='Figyeljen, kezdődik a gyakorlás...',
    font='Arial',
    pos=(0, 0), height=0.9, wrapWidth=None, ori=0,
    color='black', colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=0.0);

# Start taks Components
start_task_text = visual.TextStim(win=win, name='start_task_text',
    text='Ez volt a gyakorlás.\
    \n\nEmlékeztető: \nRégi - F\nHasonló - J\nÚj - K\
    \n\nHa készen áll a feladatra, nyomja le a jobb nyilat. Ha újra szeretne gyakorolni, nyomjon le bármilyen más gombot.',
    font='Arial',
    pos=(0, 0), height=0.9, wrapWidth=None, ori=0,
    color='black', colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=0.0);

# Trial Type Components
text_trial = visual.TextStim(win=win, name='text_trial_type',
    text='Kép',
    font='Arial',
    units='deg', pos=(0, 15), height=0.9, wrapWidth=None, ori=0,
    color='black', colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=-2.0);

text_trial_image = visual.TextStim(win=win, name='text_trial_type',
    text='Kép',
    font='Arial',
    units='deg', pos=(0, 0), height=0.9, wrapWidth=None, ori=0,
    color='black', colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=-2.0);

text_trial_location = visual.TextStim(win=win, name='text_trial_type',
    text='Hely',
    font='Arial',
    units='deg', pos=(0, 0), height=0.9, wrapWidth=None, ori=0,
    color='black', colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=-2.0);

text_inst_reminder= visual.TextStim(win=win, name='text_trial_type',
    text='Régi - F\t\t\t Hasonló - J\t\t\t Új - K',
    font='Arial',
    units='deg', pos=(0, -10), height=0.9, wrapWidth=30, ori=0,
    color='black', colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=-2.0);

# Goodbye Message Components
text_goodbye = visual.TextStim(win=win, name='text_pause',
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
for text in inst_texts:
    instr_text.setText(text)
    instructions = 1
    while instructions and cont:
        instr_text.draw()
        win.flip()
        allKeys=event.getKeys()
        if allKeys == ['escape']:
            cont = 0
        elif allKeys == [next]:
            instructions=0


# 5. Demo and practice
fixationTimer = core.CountdownTimer()
feedbackTimer = core.CountdownTimer()
imageTimer = core.CountdownTimer()
trialtypeTimer = core.CountdownTimer()
practiceTimer = core.CountdownTimer()
prev_type = 'LOC'
while demo and cont:
    trials = len(demo_table.index)
    for dm in range(trials):
        main_image.setPos((demo_table.at[dm, 'Xcoordinate'], demo_table.at[dm, 'Ycoordinate']))
        main_image.setImage(demo_table.at[dm, 'ImagePresented'])
        demo_image.setPos((demo_table.at[dm, 'Xcoordinate_demo'], demo_table.at[dm, 'Ycoordinate_demo']))
        demo_image.setImage(demo_table.at[dm, 'DemoImage'])

        if demo_table.at[dm, 'StimType'] == 'TARGET':
            stim_type_text.setText('Régi')
        elif demo_table.at[dm, 'StimType'] == 'LURE':
            stim_type_text.setText('Hasonló')
        elif demo_table.at[dm, 'StimType'] == 'FOIL':
            stim_type_text.setText('Új')
        else:
            stim_type_text.setText('StimType Unkown')

        if demo_table.at[dm, 'TrialType'] == 'OBJ':
            trial_type_text.setText('Képek')
        elif demo_table.at[dm, 'TrialType'] == 'LOC':
            trial_type_text.setText('Helyek')
        else:
            trial_type_text.setText('TrialType Unkown')

        show_demo_images = 1
        while cont and show_demo_images:
            if demo_table.at[dm, 'TrialType'] == 'LOC':
                galley_map.draw()
            stim_type_text.draw()
            trial_type_text.draw()
            main_image.draw()
            demo_image.draw()
            win.flip()
            core.wait(0.5)
            theseKeys = keyboard.Keyboard().getKeys()
            if theseKeys == ['escape']:
                cont = 0
            elif theseKeys == [next]:
                show_demo_images = 0
            elif theseKeys == [pause_button]:
                cont = insert_pause()

    if cont:
        instr_text.setText(instr_practice_text)
        instr_text.draw()
        win.flip()
        anyKey=event.waitKeys()
        if anyKey == ['escape']:
            cont = 0
        elif anyKey == [next]:
            demo = 0
        else:
            demo = 1

# Start practice
while practice and cont:
    trials = len(practice_table.index)
    practiceTimer.reset(2.0)
    while cont and practiceTimer.getTime() > 0:
        text_practice.draw()
        win.flip()
        thisKey = keyboard.Keyboard().getKeys()
        if thisKey == ['escape']:
            cont = 0
        elif thisKey == [pause_button]:
            cont = insert_pause()

    for pr in range(trials):
        # update component parameters for each repeat
        main_image.setPos(trk.set_position(practice_table,pr))
        main_image.setImage(trk.set_image(practice_table,pr, task))

        # Set correct answer for feedback
        if practice_table.at[pr, 'StimType'] == 'FOIL':
            correct_answer.setText('A helyes válasz: Új')
        elif practice_table.at[pr, 'StimType'] == 'LURE':
            correct_answer.setText('A helyes válasz: Hasonló')
        elif practice_table.at[pr, 'StimType'] == 'TARGET':
            correct_answer.setText('A helyes válasz: Régi')

        if prev_type != trk.get_trialtype(practice_table, pr):
            trialtypeTimer.reset(2.0)
            if trk.get_trialtype(practice_table, pr) == 'LOC':
                prev_type = 'LOC'
                # display location block info
                while cont and trialtypeTimer.getTime() > 0:
                    text_trial.setText('Hely')
                    text_trial_location.draw()
                    text_inst_reminder.draw()
                    win.flip()
                    thisKey = keyboard.Keyboard().getKeys()
                    if thisKey == ['escape']:
                        cont = 0
                    elif thisKey == [pause_button]:
                        cont = insert_pause()
            elif trk.get_trialtype(practice_table, pr) == 'OBJ':
                prev_type = 'OBJ'
                # display object block info
                while cont and trialtypeTimer.getTime() > 0:
                    text_trial.setText('Kép')
                    text_trial_image.draw()
                    text_inst_reminder.draw()
                    win.flip()
                    thisKey = keyboard.Keyboard().getKeys()
                    if thisKey == ['escape']:
                        cont = 0
                    elif thisKey == [pause_button]:
                        cont = insert_pause()

        fx = 1
        while cont and fx:
            fixationTimer.reset(practice_table.at[pr, 'Jitter'])
            while cont and fixationTimer.getTime() > 0:
                text_trial.draw()
                galley_map.draw()
                fixation_cross.draw()
                win.flip()
                theseKeys = keyboard.Keyboard().getKeys()
                if theseKeys == ['escape']:
                    cont = 0
                elif theseKeys == [pause_button]:
                    cont = insert_pause()
                    fx = 1
                else:
                    fx = 0

        imageTimer.reset(image_presentation_time)
        while cont and imageTimer.getTime() > 0:
            text_trial.draw()
            galley_map.draw()
            main_image.draw()
            win.flip()
            theseKeys = keyboard.Keyboard().getKeys()
            if theseKeys == ['escape']:
                cont = 0
            elif theseKeys == [resp_0]:
                answer_given.setText('Az Ön válasza: Régi')
            elif theseKeys == [resp_1]:
                answer_given.setText('Az Ön válasza: Hasonló')
            elif theseKeys == [resp_2]:
                answer_given.setText('Az Ön válasza: Új')
            elif theseKeys == [pause_button]:
                cont = insert_pause()

        # Give some feedback to the participant
        feedbackTimer.reset(2)
        while cont and feedbackTimer.getTime() > 0:
            correct_answer.draw()
            answer_given.draw()
            win.flip()
            thisKey=keyboard.Keyboard().getKeys()
            if thisKey == ['escape']:
                cont = 0
            elif thisKey == [pause_button]:
                cont = insert_pause()
        correct_answer.setText('')
        answer_given.setText('')
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

instr_text.setText('Régi - F\nHasonló - J\nÚj - K\n\nA kísérletvezető indítja a feladatot.')
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
    elif thisKey == [pause_button]:
        cont = insert_pause()


# 6. task
trials = np.arange(first_trial,len(stim_table.index),1, dtype =int)
#create vars for logging and log file header
t_index = 0
t_type = 'NaN'
s_type = 'NaN'
dataFile.write('TrialIndex,TrialType,StimType,FX/IMG,Response,RT,TimePassed\n')
# Timers and counters
expClock = core.Clock()  # to track the time since experiment started
block_nr = 0

# Reset timer and start experiment
rt_timer = core.Clock() # for reaction time
expClock.reset()
for tr in trials:
    # Check whether we are starting a new block
    if prev_type != trk.get_trialtype(stim_table, tr):
        block_nr += 1
        # check if it is time for a break before the new block
        if block_nr == 4 or tr == 7:
            pause = 1
            while pause and cont:
                text_long_pause.draw()
                win.flip()
                thisKey = keyboard.Keyboard().getKeys()
                if thisKey == ['escape']:
                    cont = 0
                elif thisKey == [next]:
                    pause = 0

        trialtypeTimer.reset(2.0)
        if trk.get_trialtype(stim_table, tr) == 'LOC':
            prev_type = 'LOC'
            # display location block info
            while cont and trialtypeTimer.getTime() > 0:
                text_trial.setText('Hely')
                text_trial_location.draw()
                text_inst_reminder.draw()
                win.flip()
                thisKey = keyboard.Keyboard().getKeys()
                if thisKey == ['escape']:
                    cont = 0
                elif thisKey == [pause_button]:
                    cont = insert_pause()
        elif trk.get_trialtype(stim_table, tr) == 'OBJ':
            prev_type = 'OBJ'
            # display object block info
            while cont and trialtypeTimer.getTime() > 0:
                text_trial.setText('Kép')
                text_trial_image.draw()
                text_inst_reminder.draw()
                win.flip()
                thisKey = keyboard.Keyboard().getKeys()
                if thisKey == ['escape']:
                    cont = 0
                elif thisKey == [pause_button]:
                    cont = insert_pause()

    # update component parameters for each repeat
    main_image.setPos(trk.set_position(stim_table,tr))
    main_image.setImage(trk.set_image(stim_table,tr, task))

    fx = 1
    while cont and fx:
        fixationTimer.reset(jitters[tr])
        while cont and fixationTimer.getTime() > 0:
            text_trial.draw()
            galley_map.draw()
            fixation_cross.draw()
            win.flip()
            theseKeys = keyboard.Keyboard().getKeys()
            if theseKeys == ['escape']:
                cont = 0
            elif len(theseKeys) != 0:
                dataFile.write('%i,%s,%s,%s,%s,%.6f,%.6f\n' %(t_index, t_type, s_type,'FX',theseKeys[0].name, rt_timer.getTime(), expClock.getTime())) #log events during fixation belonging to the previous trial (image not seen yet)
                if theseKeys == [pause_button]:
                    cont = insert_pause()
                    fx = 1
                else:
                    fx = 0
            else:
                fx = 0

    # update trial index, type and stimulus type for logging
    t_index = stim_table.at[tr, 'TrialIndex']
    t_type = stim_table.at[tr, 'TrialType']
    s_type = stim_table.at[tr, 'StimType']
    # text_trial.setText(s_type) # for testing testing the right input
    imageTimer.reset(image_presentation_time)
    rt_timer.reset()
    while cont and imageTimer.getTime() > 0:
        text_trial.draw()
        galley_map.draw()
        main_image.draw()
        win.flip()
        theseKeys = keyboard.Keyboard().getKeys()
        if theseKeys == ['escape']:
            cont = 0
        elif len(theseKeys) != 0:
            dataFile.write('%i,%s,%s,%s,%s,%.6f,%.6f\n' %(t_index, t_type, s_type,'IMG',theseKeys[0].name, rt_timer.getTime(), expClock.getTime()))
            if theseKeys == [pause_button]:
                cont = insert_pause()

    theseKeys = keyboard.Keyboard().getKeys()
    if 'escape' in theseKeys:
        cont = 0
    elif len(theseKeys) != 0:
        dataFile.write('%i,%s,%s,%s,%s,%.6f,%.6f\n' %(t_index, t_type, s_type,'-',theseKeys[0].name, rt_timer.getTime(), expClock.getTime()))
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
