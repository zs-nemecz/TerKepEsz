#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.1.3),
    on August 31, 2020, at 11:48
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

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



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.1.3'
expName = 'TerKepEsz-Encoding_MR'  # from the Builder filename that created this script
expInfo = {'ID': '', 'practice': '1'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s_%s' % (expInfo['ID'],'pilot', expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='D:\\Zsuzsa\\HCCCL\\experiment\\computer_based_tasks\\terkepesz\\terkepesz-encoding_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='AOC', color=[0.804,0.804,0.961], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "start_encoding"
start_encodingClock = core.Clock()
start_encoding_text = visual.TextStim(win=win, name='start_encoding_text',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
tables = [0,1,2]
shuffle(tables)
trial_table = tables.pop()
print('selected file {}'.format(trial_table))
trial_table = str(trial_table)
stimuli_table = 'stimuli_tables/encoding_trials_'+ trial_table + '.csv'


# Initialize components for Routine "enc_instructions_1"
enc_instructions_1Clock = core.Clock()
enc_instructions_1_text = visual.TextStim(win=win, name='enc_instructions_1_text',
    text='Ön ennek a modern képgalériának a kurátora. \n\nA legújabb kiállításra a vártnál több kép érkezett.\nKurátorként az Ön feladata lesz eldönteni, mely képeket válogatjuk be a kiállított darabok közé, és hogy a kép illeszkedik-e a galéria adott pontjára.\n\nAz Ön ideje nagyon drága a galériának, így a döntésre egy-egy képről csak 3 másodperce lesz.',
    font='Arial',
    pos=(-0.3, 0), height=0.03, wrapWidth=0.65, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
enc_instructions_1_image = visual.ImageStim(
    win=win,
    name='enc_instructions_1_image', units='norm', 
    image='stimuli/GalleryBuildingFromOutside.jpg', mask=None,
    ori=0, pos=(0.4688, 0.0), size=(0.625, 0.8333),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
enc_instructions_1_key = keyboard.Keyboard()
instructions_1_continue = visual.TextStim(win=win, name='instructions_1_continue',
    text='A folytatáshoz nyomja meg a gombot a jobb hüvelykujjával. ',
    font='Arial',
    pos=(0, -0.4), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "enc_instructions_2"
enc_instructions_2Clock = core.Clock()
enc_instructions_2_text = visual.TextStim(win=win, name='enc_instructions_2_text',
    text='Ez a kiállítóterem, nézze meg figyelmesen. \n\nA feladat során a képek a falra vetítve jelennek meg, azon a helyen, ahol kiállításra kerülhetnek. A képek előtt egy keresztet fog látni, ami jelzi a képek pontos helyét.\n\nDöntse el a képekről, hogy ki legyenek-e állítva a bemutatott helyen. A beválogatott képek száma nincsen korlátozva. Minden egyes képről Ön dönt. Ha több képet válogat be, mint amennyi a galériában elfér, akkor a képeket az év során felváltva állítjuk ki.\n\nMinden képet nézzen meg figyelmesen, és minden képre adjon választ. ',
    font='Arial',
    pos=(-0.35, 0), height=0.03, wrapWidth=0.5, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
enc_instructions_2_image = visual.ImageStim(
    win=win,
    name='enc_instructions_2_image', units='norm', 
    image='stimuli/GalleryInterior.png', mask=None,
    ori=0, pos=(0.4427, 0), size=(0.7604, 0.8185),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
enc_instructions_2_key = keyboard.Keyboard()
instructions_2_continue = visual.TextStim(win=win, name='instructions_2_continue',
    text='A folytatáshoz nyomja le a gombot a jobb hüvelyujjával. ',
    font='Arial',
    pos=(0,-0.4), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "enc_instructions_3"
enc_instructions_3Clock = core.Clock()
enc_instructions_3_text = visual.TextStim(win=win, name='enc_instructions_3_text',
    text='Az első feladat nagyjából 25 percet vesz igénybe, közben két rövid szünettel. Ügyeljen, hogy ezek a szünetek ne legyenek 2 percnél hosszabbak. \n\nA jobb mutatóujjával jelölje azokat a képeket, amelyek maradhatnak a galériában, a bemutatott helyen.\n\nA bal mutatóujjával jelölje a képeket, amelyek nem maradnak kiállítva a bemutatott helyen. \n\nMost a gyakorló feladat következik. \n',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
enc_instructions_3_key = keyboard.Keyboard()
enc_instructions_3_continue = visual.TextStim(win=win, name='enc_instructions_3_continue',
    text='Ha készen áll a gyakorlásra, nyomja meg a gombot a jobb hüvelykujjával.',
    font='Arial',
    pos=(0, -0.4), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "start_practice"
start_practiceClock = core.Clock()
start_practice_text = visual.TextStim(win=win, name='start_practice_text',
    text='Kezdődik a gyakorlás...',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
practice = int(expInfo['practice'])

# Initialize components for Routine "enc_practice_fx"
enc_practice_fxClock = core.Clock()
enc_practice_fx_interior = visual.ImageStim(
    win=win,
    name='enc_practice_fx_interior', units='norm', 
    image='stimuli/GalleryInterior.png', mask=None,
    ori=0, pos=(0, -0), size=(2.0, 2.0),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
enc_practice_fx_cross = visual.TextStim(win=win, name='enc_practice_fx_cross',
    text='+',
    font='Arial',
    units='norm', pos=[0,0], height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
enc_practice_fx_key = keyboard.Keyboard()

# Initialize components for Routine "enc_practice_trial"
enc_practice_trialClock = core.Clock()
w_size = win.size

x_size = w_size[0]
y_size = w_size[1]

scr_resolution = x_size/y_size
enc_practice_trial_interior = visual.ImageStim(
    win=win,
    name='enc_practice_trial_interior', units='norm', 
    image='stimuli/GalleryInterior.png', mask=None,
    ori=0, pos=(0, -0), size=(2.0, 2.0),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
enc_practice_trial_main_image = visual.ImageStim(
    win=win,
    name='enc_practice_trial_main_image', units='norm', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
enc_practice_trial_key = keyboard.Keyboard()

# Initialize components for Routine "enc_practice_feedback"
enc_practice_feedbackClock = core.Clock()
enc_practice_feedback_interior = visual.ImageStim(
    win=win,
    name='enc_practice_feedback_interior', units='norm', 
    image='stimuli/GalleryInterior.png', mask=None,
    ori=0, pos=(0, -0), size=(2.0, 2.0),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
enc_practice_feedback_image = visual.ImageStim(
    win=win,
    name='enc_practice_feedback_image', units='norm', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
enc_practice_feedback_text = visual.TextStim(win=win, name='enc_practice_feedback_text',
    text='default text',
    font='Arial',
    units='norm', pos=[0,0], height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "end_practice"
end_practiceClock = core.Clock()
end_practice_text = visual.TextStim(win=win, name='end_practice_text',
    text='Ez volt a gyakorlás. A feladat következik. \nA feladat során már nem kap visszajelzést a döntéséről. ',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=0.8, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
end_practice_key = keyboard.Keyboard()
end_practice_continue = visual.TextStim(win=win, name='end_practice_continue',
    text='A folytatáshoz nyomja meg a gombot a jobb hüvelykujjával. ',
    font='Arial',
    pos=(0,-0.4), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "start_MR"
start_MRClock = core.Clock()
start_MR_text = visual.TextStim(win=win, name='start_MR_text',
    text='A vizsgálatvezető indítja a szkennert...',
    font='Arial',
    units='norm', pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
start_MR_trigger = keyboard.Keyboard()
trigger_key = 's'

def get_current_trigger_time():
    trigger = globalClock.getTime() - trigger_time
    thisExp.addData('triggers', trigger)
    thisExp.nextEntry()
    return trigger
    

# Initialize components for Routine "start_enc_run"
start_enc_runClock = core.Clock()
start_enc_run_text = visual.TextStim(win=win, name='start_enc_run_text',
    text='Kezdődik a feladat...',
    font='Arial',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "enc_fx"
enc_fxClock = core.Clock()
enc_fx_interior = visual.ImageStim(
    win=win,
    name='enc_fx_interior', units='norm', 
    image='stimuli/GalleryInterior.png', mask=None,
    ori=0, pos=(0, -0), size=(2.0, 2.0),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
enc_fx_cross = visual.TextStim(win=win, name='enc_fx_cross',
    text='+',
    font='Arial',
    units='norm', pos=[0,0], height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
enc_fx_key = keyboard.Keyboard()

# Initialize components for Routine "enc_trial"
enc_trialClock = core.Clock()
w_size = win.size

x_size = w_size[0]
y_size = w_size[1]

scr_resolution = x_size/y_size
enc_trial_interior = visual.ImageStim(
    win=win,
    name='enc_trial_interior', units='norm', 
    image='stimuli/GalleryInterior.png', mask=None,
    ori=0, pos=(0, -0), size=(2.0, 2.0),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
enc_trial_main_image = visual.ImageStim(
    win=win,
    name='enc_trial_main_image', units='norm', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
enc_trial_key = keyboard.Keyboard()

# Initialize components for Routine "end_enc_run"
end_enc_runClock = core.Clock()
end_enc_run_text = visual.TextStim(win=win, name='end_enc_run_text',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
enc_run_end_key = keyboard.Keyboard()
enc_run_end_continue = visual.TextStim(win=win, name='enc_run_end_continue',
    text='A folytatáshoz nyomja meg a gombot a jobb hüvelykujjával. ',
    font='Arial',
    pos=(0,-0.4), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "inter_task_break"
inter_task_breakClock = core.Clock()
inter_task_break_text = visual.TextStim(win=win, name='inter_task_break_text',
    text='Most kivesszük Önt a szkennerből.',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "start_encoding"-------
continueRoutine = True
routineTimer.add(1.500000)
# update component parameters for each repeat
start_encoding_text.setText('Első feladat\nGaléria berendezés')
start = 0
end = 0
step = 1
n_runs = 3
run_counter = 0
# keep track of which components have finished
start_encodingComponents = [start_encoding_text]
for thisComponent in start_encodingComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
start_encodingClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "start_encoding"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = start_encodingClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=start_encodingClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *start_encoding_text* updates
    if start_encoding_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        start_encoding_text.frameNStart = frameN  # exact frame index
        start_encoding_text.tStart = t  # local t and not account for scr refresh
        start_encoding_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(start_encoding_text, 'tStartRefresh')  # time at next scr refresh
        start_encoding_text.setAutoDraw(True)
    if start_encoding_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > start_encoding_text.tStartRefresh + 1.5-frameTolerance:
            # keep track of stop time/frame for later
            start_encoding_text.tStop = t  # not accounting for scr refresh
            start_encoding_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(start_encoding_text, 'tStopRefresh')  # time at next scr refresh
            start_encoding_text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in start_encodingComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "start_encoding"-------
for thisComponent in start_encodingComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('start_encoding_text.started', start_encoding_text.tStartRefresh)
thisExp.addData('start_encoding_text.stopped', start_encoding_text.tStopRefresh)

# ------Prepare to start Routine "enc_instructions_1"-------
continueRoutine = True
routineTimer.add(300.000000)
# update component parameters for each repeat
enc_instructions_1_key.keys = []
enc_instructions_1_key.rt = []
_enc_instructions_1_key_allKeys = []
# keep track of which components have finished
enc_instructions_1Components = [enc_instructions_1_text, enc_instructions_1_image, enc_instructions_1_key, instructions_1_continue]
for thisComponent in enc_instructions_1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
enc_instructions_1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "enc_instructions_1"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = enc_instructions_1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=enc_instructions_1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *enc_instructions_1_text* updates
    if enc_instructions_1_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        enc_instructions_1_text.frameNStart = frameN  # exact frame index
        enc_instructions_1_text.tStart = t  # local t and not account for scr refresh
        enc_instructions_1_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(enc_instructions_1_text, 'tStartRefresh')  # time at next scr refresh
        enc_instructions_1_text.setAutoDraw(True)
    if enc_instructions_1_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > enc_instructions_1_text.tStartRefresh + 300.0-frameTolerance:
            # keep track of stop time/frame for later
            enc_instructions_1_text.tStop = t  # not accounting for scr refresh
            enc_instructions_1_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(enc_instructions_1_text, 'tStopRefresh')  # time at next scr refresh
            enc_instructions_1_text.setAutoDraw(False)
    
    # *enc_instructions_1_image* updates
    if enc_instructions_1_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        enc_instructions_1_image.frameNStart = frameN  # exact frame index
        enc_instructions_1_image.tStart = t  # local t and not account for scr refresh
        enc_instructions_1_image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(enc_instructions_1_image, 'tStartRefresh')  # time at next scr refresh
        enc_instructions_1_image.setAutoDraw(True)
    if enc_instructions_1_image.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > enc_instructions_1_image.tStartRefresh + 300.0-frameTolerance:
            # keep track of stop time/frame for later
            enc_instructions_1_image.tStop = t  # not accounting for scr refresh
            enc_instructions_1_image.frameNStop = frameN  # exact frame index
            win.timeOnFlip(enc_instructions_1_image, 'tStopRefresh')  # time at next scr refresh
            enc_instructions_1_image.setAutoDraw(False)
    
    # *enc_instructions_1_key* updates
    waitOnFlip = False
    if enc_instructions_1_key.status == NOT_STARTED and tThisFlip >= 5.0-frameTolerance:
        # keep track of start time/frame for later
        enc_instructions_1_key.frameNStart = frameN  # exact frame index
        enc_instructions_1_key.tStart = t  # local t and not account for scr refresh
        enc_instructions_1_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(enc_instructions_1_key, 'tStartRefresh')  # time at next scr refresh
        enc_instructions_1_key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(enc_instructions_1_key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(enc_instructions_1_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if enc_instructions_1_key.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > enc_instructions_1_key.tStartRefresh + 295.0-frameTolerance:
            # keep track of stop time/frame for later
            enc_instructions_1_key.tStop = t  # not accounting for scr refresh
            enc_instructions_1_key.frameNStop = frameN  # exact frame index
            win.timeOnFlip(enc_instructions_1_key, 'tStopRefresh')  # time at next scr refresh
            enc_instructions_1_key.status = FINISHED
    if enc_instructions_1_key.status == STARTED and not waitOnFlip:
        theseKeys = enc_instructions_1_key.getKeys(keyList=['d'], waitRelease=False)
        _enc_instructions_1_key_allKeys.extend(theseKeys)
        if len(_enc_instructions_1_key_allKeys):
            enc_instructions_1_key.keys = _enc_instructions_1_key_allKeys[-1].name  # just the last key pressed
            enc_instructions_1_key.rt = _enc_instructions_1_key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *instructions_1_continue* updates
    if instructions_1_continue.status == NOT_STARTED and tThisFlip >= 5.0-frameTolerance:
        # keep track of start time/frame for later
        instructions_1_continue.frameNStart = frameN  # exact frame index
        instructions_1_continue.tStart = t  # local t and not account for scr refresh
        instructions_1_continue.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions_1_continue, 'tStartRefresh')  # time at next scr refresh
        instructions_1_continue.setAutoDraw(True)
    if instructions_1_continue.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > instructions_1_continue.tStartRefresh + 295.0-frameTolerance:
            # keep track of stop time/frame for later
            instructions_1_continue.tStop = t  # not accounting for scr refresh
            instructions_1_continue.frameNStop = frameN  # exact frame index
            win.timeOnFlip(instructions_1_continue, 'tStopRefresh')  # time at next scr refresh
            instructions_1_continue.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in enc_instructions_1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "enc_instructions_1"-------
for thisComponent in enc_instructions_1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('enc_instructions_1_text.started', enc_instructions_1_text.tStartRefresh)
thisExp.addData('enc_instructions_1_text.stopped', enc_instructions_1_text.tStopRefresh)
thisExp.addData('enc_instructions_1_image.started', enc_instructions_1_image.tStartRefresh)
thisExp.addData('enc_instructions_1_image.stopped', enc_instructions_1_image.tStopRefresh)
# check responses
if enc_instructions_1_key.keys in ['', [], None]:  # No response was made
    enc_instructions_1_key.keys = None
thisExp.addData('enc_instructions_1_key.keys',enc_instructions_1_key.keys)
if enc_instructions_1_key.keys != None:  # we had a response
    thisExp.addData('enc_instructions_1_key.rt', enc_instructions_1_key.rt)
thisExp.addData('enc_instructions_1_key.started', enc_instructions_1_key.tStartRefresh)
thisExp.addData('enc_instructions_1_key.stopped', enc_instructions_1_key.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('instructions_1_continue.started', instructions_1_continue.tStartRefresh)
thisExp.addData('instructions_1_continue.stopped', instructions_1_continue.tStopRefresh)

# ------Prepare to start Routine "enc_instructions_2"-------
continueRoutine = True
routineTimer.add(300.000000)
# update component parameters for each repeat
enc_instructions_2_key.keys = []
enc_instructions_2_key.rt = []
_enc_instructions_2_key_allKeys = []
# keep track of which components have finished
enc_instructions_2Components = [enc_instructions_2_text, enc_instructions_2_image, enc_instructions_2_key, instructions_2_continue]
for thisComponent in enc_instructions_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
enc_instructions_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "enc_instructions_2"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = enc_instructions_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=enc_instructions_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *enc_instructions_2_text* updates
    if enc_instructions_2_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        enc_instructions_2_text.frameNStart = frameN  # exact frame index
        enc_instructions_2_text.tStart = t  # local t and not account for scr refresh
        enc_instructions_2_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(enc_instructions_2_text, 'tStartRefresh')  # time at next scr refresh
        enc_instructions_2_text.setAutoDraw(True)
    if enc_instructions_2_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > enc_instructions_2_text.tStartRefresh + 300.0-frameTolerance:
            # keep track of stop time/frame for later
            enc_instructions_2_text.tStop = t  # not accounting for scr refresh
            enc_instructions_2_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(enc_instructions_2_text, 'tStopRefresh')  # time at next scr refresh
            enc_instructions_2_text.setAutoDraw(False)
    
    # *enc_instructions_2_image* updates
    if enc_instructions_2_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        enc_instructions_2_image.frameNStart = frameN  # exact frame index
        enc_instructions_2_image.tStart = t  # local t and not account for scr refresh
        enc_instructions_2_image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(enc_instructions_2_image, 'tStartRefresh')  # time at next scr refresh
        enc_instructions_2_image.setAutoDraw(True)
    if enc_instructions_2_image.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > enc_instructions_2_image.tStartRefresh + 300.0-frameTolerance:
            # keep track of stop time/frame for later
            enc_instructions_2_image.tStop = t  # not accounting for scr refresh
            enc_instructions_2_image.frameNStop = frameN  # exact frame index
            win.timeOnFlip(enc_instructions_2_image, 'tStopRefresh')  # time at next scr refresh
            enc_instructions_2_image.setAutoDraw(False)
    
    # *enc_instructions_2_key* updates
    waitOnFlip = False
    if enc_instructions_2_key.status == NOT_STARTED and tThisFlip >= 5.0-frameTolerance:
        # keep track of start time/frame for later
        enc_instructions_2_key.frameNStart = frameN  # exact frame index
        enc_instructions_2_key.tStart = t  # local t and not account for scr refresh
        enc_instructions_2_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(enc_instructions_2_key, 'tStartRefresh')  # time at next scr refresh
        enc_instructions_2_key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(enc_instructions_2_key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(enc_instructions_2_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if enc_instructions_2_key.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > enc_instructions_2_key.tStartRefresh + 295.0-frameTolerance:
            # keep track of stop time/frame for later
            enc_instructions_2_key.tStop = t  # not accounting for scr refresh
            enc_instructions_2_key.frameNStop = frameN  # exact frame index
            win.timeOnFlip(enc_instructions_2_key, 'tStopRefresh')  # time at next scr refresh
            enc_instructions_2_key.status = FINISHED
    if enc_instructions_2_key.status == STARTED and not waitOnFlip:
        theseKeys = enc_instructions_2_key.getKeys(keyList=['d'], waitRelease=False)
        _enc_instructions_2_key_allKeys.extend(theseKeys)
        if len(_enc_instructions_2_key_allKeys):
            enc_instructions_2_key.keys = _enc_instructions_2_key_allKeys[-1].name  # just the last key pressed
            enc_instructions_2_key.rt = _enc_instructions_2_key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *instructions_2_continue* updates
    if instructions_2_continue.status == NOT_STARTED and tThisFlip >= 5.0-frameTolerance:
        # keep track of start time/frame for later
        instructions_2_continue.frameNStart = frameN  # exact frame index
        instructions_2_continue.tStart = t  # local t and not account for scr refresh
        instructions_2_continue.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions_2_continue, 'tStartRefresh')  # time at next scr refresh
        instructions_2_continue.setAutoDraw(True)
    if instructions_2_continue.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > instructions_2_continue.tStartRefresh + 295.0-frameTolerance:
            # keep track of stop time/frame for later
            instructions_2_continue.tStop = t  # not accounting for scr refresh
            instructions_2_continue.frameNStop = frameN  # exact frame index
            win.timeOnFlip(instructions_2_continue, 'tStopRefresh')  # time at next scr refresh
            instructions_2_continue.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in enc_instructions_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "enc_instructions_2"-------
for thisComponent in enc_instructions_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('enc_instructions_2_text.started', enc_instructions_2_text.tStartRefresh)
thisExp.addData('enc_instructions_2_text.stopped', enc_instructions_2_text.tStopRefresh)
thisExp.addData('enc_instructions_2_image.started', enc_instructions_2_image.tStartRefresh)
thisExp.addData('enc_instructions_2_image.stopped', enc_instructions_2_image.tStopRefresh)
# check responses
if enc_instructions_2_key.keys in ['', [], None]:  # No response was made
    enc_instructions_2_key.keys = None
thisExp.addData('enc_instructions_2_key.keys',enc_instructions_2_key.keys)
if enc_instructions_2_key.keys != None:  # we had a response
    thisExp.addData('enc_instructions_2_key.rt', enc_instructions_2_key.rt)
thisExp.addData('enc_instructions_2_key.started', enc_instructions_2_key.tStartRefresh)
thisExp.addData('enc_instructions_2_key.stopped', enc_instructions_2_key.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('instructions_2_continue.started', instructions_2_continue.tStartRefresh)
thisExp.addData('instructions_2_continue.stopped', instructions_2_continue.tStopRefresh)

# ------Prepare to start Routine "enc_instructions_3"-------
continueRoutine = True
routineTimer.add(300.000000)
# update component parameters for each repeat
enc_instructions_3_key.keys = []
enc_instructions_3_key.rt = []
_enc_instructions_3_key_allKeys = []
# keep track of which components have finished
enc_instructions_3Components = [enc_instructions_3_text, enc_instructions_3_key, enc_instructions_3_continue]
for thisComponent in enc_instructions_3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
enc_instructions_3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "enc_instructions_3"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = enc_instructions_3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=enc_instructions_3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *enc_instructions_3_text* updates
    if enc_instructions_3_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        enc_instructions_3_text.frameNStart = frameN  # exact frame index
        enc_instructions_3_text.tStart = t  # local t and not account for scr refresh
        enc_instructions_3_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(enc_instructions_3_text, 'tStartRefresh')  # time at next scr refresh
        enc_instructions_3_text.setAutoDraw(True)
    if enc_instructions_3_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > enc_instructions_3_text.tStartRefresh + 300-frameTolerance:
            # keep track of stop time/frame for later
            enc_instructions_3_text.tStop = t  # not accounting for scr refresh
            enc_instructions_3_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(enc_instructions_3_text, 'tStopRefresh')  # time at next scr refresh
            enc_instructions_3_text.setAutoDraw(False)
    
    # *enc_instructions_3_key* updates
    waitOnFlip = False
    if enc_instructions_3_key.status == NOT_STARTED and tThisFlip >= 5.0-frameTolerance:
        # keep track of start time/frame for later
        enc_instructions_3_key.frameNStart = frameN  # exact frame index
        enc_instructions_3_key.tStart = t  # local t and not account for scr refresh
        enc_instructions_3_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(enc_instructions_3_key, 'tStartRefresh')  # time at next scr refresh
        enc_instructions_3_key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(enc_instructions_3_key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(enc_instructions_3_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if enc_instructions_3_key.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > enc_instructions_3_key.tStartRefresh + 295-frameTolerance:
            # keep track of stop time/frame for later
            enc_instructions_3_key.tStop = t  # not accounting for scr refresh
            enc_instructions_3_key.frameNStop = frameN  # exact frame index
            win.timeOnFlip(enc_instructions_3_key, 'tStopRefresh')  # time at next scr refresh
            enc_instructions_3_key.status = FINISHED
    if enc_instructions_3_key.status == STARTED and not waitOnFlip:
        theseKeys = enc_instructions_3_key.getKeys(keyList=['d'], waitRelease=False)
        _enc_instructions_3_key_allKeys.extend(theseKeys)
        if len(_enc_instructions_3_key_allKeys):
            enc_instructions_3_key.keys = _enc_instructions_3_key_allKeys[-1].name  # just the last key pressed
            enc_instructions_3_key.rt = _enc_instructions_3_key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *enc_instructions_3_continue* updates
    if enc_instructions_3_continue.status == NOT_STARTED and tThisFlip >= 5.0-frameTolerance:
        # keep track of start time/frame for later
        enc_instructions_3_continue.frameNStart = frameN  # exact frame index
        enc_instructions_3_continue.tStart = t  # local t and not account for scr refresh
        enc_instructions_3_continue.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(enc_instructions_3_continue, 'tStartRefresh')  # time at next scr refresh
        enc_instructions_3_continue.setAutoDraw(True)
    if enc_instructions_3_continue.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > enc_instructions_3_continue.tStartRefresh + 295.0-frameTolerance:
            # keep track of stop time/frame for later
            enc_instructions_3_continue.tStop = t  # not accounting for scr refresh
            enc_instructions_3_continue.frameNStop = frameN  # exact frame index
            win.timeOnFlip(enc_instructions_3_continue, 'tStopRefresh')  # time at next scr refresh
            enc_instructions_3_continue.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in enc_instructions_3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "enc_instructions_3"-------
for thisComponent in enc_instructions_3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('enc_instructions_3_text.started', enc_instructions_3_text.tStartRefresh)
thisExp.addData('enc_instructions_3_text.stopped', enc_instructions_3_text.tStopRefresh)
# check responses
if enc_instructions_3_key.keys in ['', [], None]:  # No response was made
    enc_instructions_3_key.keys = None
thisExp.addData('enc_instructions_3_key.keys',enc_instructions_3_key.keys)
if enc_instructions_3_key.keys != None:  # we had a response
    thisExp.addData('enc_instructions_3_key.rt', enc_instructions_3_key.rt)
thisExp.addData('enc_instructions_3_key.started', enc_instructions_3_key.tStartRefresh)
thisExp.addData('enc_instructions_3_key.stopped', enc_instructions_3_key.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('enc_instructions_3_continue.started', enc_instructions_3_continue.tStartRefresh)
thisExp.addData('enc_instructions_3_continue.stopped', enc_instructions_3_continue.tStopRefresh)

# ------Prepare to start Routine "start_practice"-------
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
start_practiceComponents = [start_practice_text]
for thisComponent in start_practiceComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
start_practiceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "start_practice"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = start_practiceClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=start_practiceClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *start_practice_text* updates
    if start_practice_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        start_practice_text.frameNStart = frameN  # exact frame index
        start_practice_text.tStart = t  # local t and not account for scr refresh
        start_practice_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(start_practice_text, 'tStartRefresh')  # time at next scr refresh
        start_practice_text.setAutoDraw(True)
    if start_practice_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > start_practice_text.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            start_practice_text.tStop = t  # not accounting for scr refresh
            start_practice_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(start_practice_text, 'tStopRefresh')  # time at next scr refresh
            start_practice_text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in start_practiceComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "start_practice"-------
for thisComponent in start_practiceComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('start_practice_text.started', start_practice_text.tStartRefresh)
thisExp.addData('start_practice_text.stopped', start_practice_text.tStopRefresh)

# set up handler to look after randomisation of conditions etc
enc_practice_trials = data.TrialHandler(nReps=practice, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('stimuli_tables/encoding_practice_trials.csv'),
    seed=None, name='enc_practice_trials')
thisExp.addLoop(enc_practice_trials)  # add the loop to the experiment
thisEnc_practice_trial = enc_practice_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisEnc_practice_trial.rgb)
if thisEnc_practice_trial != None:
    for paramName in thisEnc_practice_trial:
        exec('{} = thisEnc_practice_trial[paramName]'.format(paramName))

for thisEnc_practice_trial in enc_practice_trials:
    currentLoop = enc_practice_trials
    # abbreviate parameter names if possible (e.g. rgb = thisEnc_practice_trial.rgb)
    if thisEnc_practice_trial != None:
        for paramName in thisEnc_practice_trial:
            exec('{} = thisEnc_practice_trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "enc_practice_fx"-------
    continueRoutine = True
    # update component parameters for each repeat
    enc_practice_fx_cross.setPos((CurrentX, CurrentY))
    enc_practice_fx_key.keys = []
    enc_practice_fx_key.rt = []
    _enc_practice_fx_key_allKeys = []
    # keep track of which components have finished
    enc_practice_fxComponents = [enc_practice_fx_interior, enc_practice_fx_cross, enc_practice_fx_key]
    for thisComponent in enc_practice_fxComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    enc_practice_fxClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "enc_practice_fx"-------
    while continueRoutine:
        # get current time
        t = enc_practice_fxClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=enc_practice_fxClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *enc_practice_fx_interior* updates
        if enc_practice_fx_interior.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            enc_practice_fx_interior.frameNStart = frameN  # exact frame index
            enc_practice_fx_interior.tStart = t  # local t and not account for scr refresh
            enc_practice_fx_interior.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(enc_practice_fx_interior, 'tStartRefresh')  # time at next scr refresh
            enc_practice_fx_interior.setAutoDraw(True)
        if enc_practice_fx_interior.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > enc_practice_fx_interior.tStartRefresh + Jitter/1000-frameTolerance:
                # keep track of stop time/frame for later
                enc_practice_fx_interior.tStop = t  # not accounting for scr refresh
                enc_practice_fx_interior.frameNStop = frameN  # exact frame index
                win.timeOnFlip(enc_practice_fx_interior, 'tStopRefresh')  # time at next scr refresh
                enc_practice_fx_interior.setAutoDraw(False)
        
        # *enc_practice_fx_cross* updates
        if enc_practice_fx_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            enc_practice_fx_cross.frameNStart = frameN  # exact frame index
            enc_practice_fx_cross.tStart = t  # local t and not account for scr refresh
            enc_practice_fx_cross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(enc_practice_fx_cross, 'tStartRefresh')  # time at next scr refresh
            enc_practice_fx_cross.setAutoDraw(True)
        if enc_practice_fx_cross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > enc_practice_fx_cross.tStartRefresh + Jitter/1000-frameTolerance:
                # keep track of stop time/frame for later
                enc_practice_fx_cross.tStop = t  # not accounting for scr refresh
                enc_practice_fx_cross.frameNStop = frameN  # exact frame index
                win.timeOnFlip(enc_practice_fx_cross, 'tStopRefresh')  # time at next scr refresh
                enc_practice_fx_cross.setAutoDraw(False)
        
        # *enc_practice_fx_key* updates
        waitOnFlip = False
        if enc_practice_fx_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            enc_practice_fx_key.frameNStart = frameN  # exact frame index
            enc_practice_fx_key.tStart = t  # local t and not account for scr refresh
            enc_practice_fx_key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(enc_practice_fx_key, 'tStartRefresh')  # time at next scr refresh
            enc_practice_fx_key.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(enc_practice_fx_key.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(enc_practice_fx_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if enc_practice_fx_key.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > enc_practice_fx_key.tStartRefresh + Jitter/1000-frameTolerance:
                # keep track of stop time/frame for later
                enc_practice_fx_key.tStop = t  # not accounting for scr refresh
                enc_practice_fx_key.frameNStop = frameN  # exact frame index
                win.timeOnFlip(enc_practice_fx_key, 'tStopRefresh')  # time at next scr refresh
                enc_practice_fx_key.status = FINISHED
        if enc_practice_fx_key.status == STARTED and not waitOnFlip:
            theseKeys = enc_practice_fx_key.getKeys(keyList=['b', 'c'], waitRelease=False)
            _enc_practice_fx_key_allKeys.extend(theseKeys)
            if len(_enc_practice_fx_key_allKeys):
                enc_practice_fx_key.keys = _enc_practice_fx_key_allKeys[-1].name  # just the last key pressed
                enc_practice_fx_key.rt = _enc_practice_fx_key_allKeys[-1].rt
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in enc_practice_fxComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "enc_practice_fx"-------
    for thisComponent in enc_practice_fxComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    enc_practice_trials.addData('enc_practice_fx_interior.started', enc_practice_fx_interior.tStartRefresh)
    enc_practice_trials.addData('enc_practice_fx_interior.stopped', enc_practice_fx_interior.tStopRefresh)
    enc_practice_trials.addData('enc_practice_fx_cross.started', enc_practice_fx_cross.tStartRefresh)
    enc_practice_trials.addData('enc_practice_fx_cross.stopped', enc_practice_fx_cross.tStopRefresh)
    # check responses
    if enc_practice_fx_key.keys in ['', [], None]:  # No response was made
        enc_practice_fx_key.keys = None
    enc_practice_trials.addData('enc_practice_fx_key.keys',enc_practice_fx_key.keys)
    if enc_practice_fx_key.keys != None:  # we had a response
        enc_practice_trials.addData('enc_practice_fx_key.rt', enc_practice_fx_key.rt)
    enc_practice_trials.addData('enc_practice_fx_key.started', enc_practice_fx_key.tStartRefresh)
    enc_practice_trials.addData('enc_practice_fx_key.stopped', enc_practice_fx_key.tStopRefresh)
    # the Routine "enc_practice_fx" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "enc_practice_trial"-------
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    w_size = win.size
    
    x_size = w_size[0]
    y_size = w_size[1]
    
    scr_resolution = x_size/y_size
    enc_practice_trial_main_image.setPos((CurrentX, CurrentY))
    enc_practice_trial_main_image.setSize((0.3125, 0.3125*scr_resolution))
    enc_practice_trial_main_image.setImage(CurrentImage)
    enc_practice_trial_key.keys = []
    enc_practice_trial_key.rt = []
    _enc_practice_trial_key_allKeys = []
    # keep track of which components have finished
    enc_practice_trialComponents = [enc_practice_trial_interior, enc_practice_trial_main_image, enc_practice_trial_key]
    for thisComponent in enc_practice_trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    enc_practice_trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "enc_practice_trial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = enc_practice_trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=enc_practice_trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *enc_practice_trial_interior* updates
        if enc_practice_trial_interior.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            enc_practice_trial_interior.frameNStart = frameN  # exact frame index
            enc_practice_trial_interior.tStart = t  # local t and not account for scr refresh
            enc_practice_trial_interior.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(enc_practice_trial_interior, 'tStartRefresh')  # time at next scr refresh
            enc_practice_trial_interior.setAutoDraw(True)
        if enc_practice_trial_interior.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > enc_practice_trial_interior.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                enc_practice_trial_interior.tStop = t  # not accounting for scr refresh
                enc_practice_trial_interior.frameNStop = frameN  # exact frame index
                win.timeOnFlip(enc_practice_trial_interior, 'tStopRefresh')  # time at next scr refresh
                enc_practice_trial_interior.setAutoDraw(False)
        
        # *enc_practice_trial_main_image* updates
        if enc_practice_trial_main_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            enc_practice_trial_main_image.frameNStart = frameN  # exact frame index
            enc_practice_trial_main_image.tStart = t  # local t and not account for scr refresh
            enc_practice_trial_main_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(enc_practice_trial_main_image, 'tStartRefresh')  # time at next scr refresh
            enc_practice_trial_main_image.setAutoDraw(True)
        if enc_practice_trial_main_image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > enc_practice_trial_main_image.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                enc_practice_trial_main_image.tStop = t  # not accounting for scr refresh
                enc_practice_trial_main_image.frameNStop = frameN  # exact frame index
                win.timeOnFlip(enc_practice_trial_main_image, 'tStopRefresh')  # time at next scr refresh
                enc_practice_trial_main_image.setAutoDraw(False)
        
        # *enc_practice_trial_key* updates
        waitOnFlip = False
        if enc_practice_trial_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            enc_practice_trial_key.frameNStart = frameN  # exact frame index
            enc_practice_trial_key.tStart = t  # local t and not account for scr refresh
            enc_practice_trial_key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(enc_practice_trial_key, 'tStartRefresh')  # time at next scr refresh
            enc_practice_trial_key.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(enc_practice_trial_key.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(enc_practice_trial_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if enc_practice_trial_key.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > enc_practice_trial_key.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                enc_practice_trial_key.tStop = t  # not accounting for scr refresh
                enc_practice_trial_key.frameNStop = frameN  # exact frame index
                win.timeOnFlip(enc_practice_trial_key, 'tStopRefresh')  # time at next scr refresh
                enc_practice_trial_key.status = FINISHED
        if enc_practice_trial_key.status == STARTED and not waitOnFlip:
            theseKeys = enc_practice_trial_key.getKeys(keyList=['b', 'c'], waitRelease=False)
            _enc_practice_trial_key_allKeys.extend(theseKeys)
            if len(_enc_practice_trial_key_allKeys):
                enc_practice_trial_key.keys = _enc_practice_trial_key_allKeys[-1].name  # just the last key pressed
                enc_practice_trial_key.rt = _enc_practice_trial_key_allKeys[-1].rt
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in enc_practice_trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "enc_practice_trial"-------
    for thisComponent in enc_practice_trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    enc_practice_trials.addData('enc_practice_trial_interior.started', enc_practice_trial_interior.tStartRefresh)
    enc_practice_trials.addData('enc_practice_trial_interior.stopped', enc_practice_trial_interior.tStopRefresh)
    enc_practice_trials.addData('enc_practice_trial_main_image.started', enc_practice_trial_main_image.tStartRefresh)
    enc_practice_trials.addData('enc_practice_trial_main_image.stopped', enc_practice_trial_main_image.tStopRefresh)
    # check responses
    if enc_practice_trial_key.keys in ['', [], None]:  # No response was made
        enc_practice_trial_key.keys = None
    enc_practice_trials.addData('enc_practice_trial_key.keys',enc_practice_trial_key.keys)
    if enc_practice_trial_key.keys != None:  # we had a response
        enc_practice_trials.addData('enc_practice_trial_key.rt', enc_practice_trial_key.rt)
    enc_practice_trials.addData('enc_practice_trial_key.started', enc_practice_trial_key.tStartRefresh)
    enc_practice_trials.addData('enc_practice_trial_key.stopped', enc_practice_trial_key.tStopRefresh)
    
    # ------Prepare to start Routine "enc_practice_feedback"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    response = enc_practice_trial_key.keys
    feedback_text = ''
    if response == 'b':
        feedback_text = 'Az Ön válasza:\nA kép nem marad.'
    elif response == 'c':
        feedback_text = 'Az Ön válasza:\nA kép marad.'
    else:
        feedback_text = 'Nem adott választ.'
    enc_practice_feedback_image.setPos((CurrentX, CurrentY))
    enc_practice_feedback_image.setSize((0.3125, 0.3125*scr_resolution))
    enc_practice_feedback_image.setImage(CurrentImage)
    enc_practice_feedback_text.setPos((CurrentX, CurrentY - 0.4))
    enc_practice_feedback_text.setText(feedback_text)
    # keep track of which components have finished
    enc_practice_feedbackComponents = [enc_practice_feedback_interior, enc_practice_feedback_image, enc_practice_feedback_text]
    for thisComponent in enc_practice_feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    enc_practice_feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "enc_practice_feedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = enc_practice_feedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=enc_practice_feedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *enc_practice_feedback_interior* updates
        if enc_practice_feedback_interior.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            enc_practice_feedback_interior.frameNStart = frameN  # exact frame index
            enc_practice_feedback_interior.tStart = t  # local t and not account for scr refresh
            enc_practice_feedback_interior.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(enc_practice_feedback_interior, 'tStartRefresh')  # time at next scr refresh
            enc_practice_feedback_interior.setAutoDraw(True)
        if enc_practice_feedback_interior.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > enc_practice_feedback_interior.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                enc_practice_feedback_interior.tStop = t  # not accounting for scr refresh
                enc_practice_feedback_interior.frameNStop = frameN  # exact frame index
                win.timeOnFlip(enc_practice_feedback_interior, 'tStopRefresh')  # time at next scr refresh
                enc_practice_feedback_interior.setAutoDraw(False)
        
        # *enc_practice_feedback_image* updates
        if enc_practice_feedback_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            enc_practice_feedback_image.frameNStart = frameN  # exact frame index
            enc_practice_feedback_image.tStart = t  # local t and not account for scr refresh
            enc_practice_feedback_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(enc_practice_feedback_image, 'tStartRefresh')  # time at next scr refresh
            enc_practice_feedback_image.setAutoDraw(True)
        if enc_practice_feedback_image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > enc_practice_feedback_image.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                enc_practice_feedback_image.tStop = t  # not accounting for scr refresh
                enc_practice_feedback_image.frameNStop = frameN  # exact frame index
                win.timeOnFlip(enc_practice_feedback_image, 'tStopRefresh')  # time at next scr refresh
                enc_practice_feedback_image.setAutoDraw(False)
        
        # *enc_practice_feedback_text* updates
        if enc_practice_feedback_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            enc_practice_feedback_text.frameNStart = frameN  # exact frame index
            enc_practice_feedback_text.tStart = t  # local t and not account for scr refresh
            enc_practice_feedback_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(enc_practice_feedback_text, 'tStartRefresh')  # time at next scr refresh
            enc_practice_feedback_text.setAutoDraw(True)
        if enc_practice_feedback_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > enc_practice_feedback_text.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                enc_practice_feedback_text.tStop = t  # not accounting for scr refresh
                enc_practice_feedback_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(enc_practice_feedback_text, 'tStopRefresh')  # time at next scr refresh
                enc_practice_feedback_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in enc_practice_feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "enc_practice_feedback"-------
    for thisComponent in enc_practice_feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    enc_practice_trials.addData('enc_practice_feedback_interior.started', enc_practice_feedback_interior.tStartRefresh)
    enc_practice_trials.addData('enc_practice_feedback_interior.stopped', enc_practice_feedback_interior.tStopRefresh)
    enc_practice_trials.addData('enc_practice_feedback_image.started', enc_practice_feedback_image.tStartRefresh)
    enc_practice_trials.addData('enc_practice_feedback_image.stopped', enc_practice_feedback_image.tStopRefresh)
    enc_practice_trials.addData('enc_practice_feedback_text.started', enc_practice_feedback_text.tStartRefresh)
    enc_practice_trials.addData('enc_practice_feedback_text.stopped', enc_practice_feedback_text.tStopRefresh)
    thisExp.nextEntry()
    
# completed practice repeats of 'enc_practice_trials'


# ------Prepare to start Routine "end_practice"-------
continueRoutine = True
routineTimer.add(300.000000)
# update component parameters for each repeat
end_practice_key.keys = []
end_practice_key.rt = []
_end_practice_key_allKeys = []
# keep track of which components have finished
end_practiceComponents = [end_practice_text, end_practice_key, end_practice_continue]
for thisComponent in end_practiceComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
end_practiceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "end_practice"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = end_practiceClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=end_practiceClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *end_practice_text* updates
    if end_practice_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_practice_text.frameNStart = frameN  # exact frame index
        end_practice_text.tStart = t  # local t and not account for scr refresh
        end_practice_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_practice_text, 'tStartRefresh')  # time at next scr refresh
        end_practice_text.setAutoDraw(True)
    if end_practice_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > end_practice_text.tStartRefresh + 300.0-frameTolerance:
            # keep track of stop time/frame for later
            end_practice_text.tStop = t  # not accounting for scr refresh
            end_practice_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(end_practice_text, 'tStopRefresh')  # time at next scr refresh
            end_practice_text.setAutoDraw(False)
    
    # *end_practice_key* updates
    waitOnFlip = False
    if end_practice_key.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
        # keep track of start time/frame for later
        end_practice_key.frameNStart = frameN  # exact frame index
        end_practice_key.tStart = t  # local t and not account for scr refresh
        end_practice_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_practice_key, 'tStartRefresh')  # time at next scr refresh
        end_practice_key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(end_practice_key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(end_practice_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if end_practice_key.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > end_practice_key.tStartRefresh + 299.0-frameTolerance:
            # keep track of stop time/frame for later
            end_practice_key.tStop = t  # not accounting for scr refresh
            end_practice_key.frameNStop = frameN  # exact frame index
            win.timeOnFlip(end_practice_key, 'tStopRefresh')  # time at next scr refresh
            end_practice_key.status = FINISHED
    if end_practice_key.status == STARTED and not waitOnFlip:
        theseKeys = end_practice_key.getKeys(keyList=['d'], waitRelease=False)
        _end_practice_key_allKeys.extend(theseKeys)
        if len(_end_practice_key_allKeys):
            end_practice_key.keys = _end_practice_key_allKeys[-1].name  # just the last key pressed
            end_practice_key.rt = _end_practice_key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *end_practice_continue* updates
    if end_practice_continue.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
        # keep track of start time/frame for later
        end_practice_continue.frameNStart = frameN  # exact frame index
        end_practice_continue.tStart = t  # local t and not account for scr refresh
        end_practice_continue.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_practice_continue, 'tStartRefresh')  # time at next scr refresh
        end_practice_continue.setAutoDraw(True)
    if end_practice_continue.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > end_practice_continue.tStartRefresh + 299.0-frameTolerance:
            # keep track of stop time/frame for later
            end_practice_continue.tStop = t  # not accounting for scr refresh
            end_practice_continue.frameNStop = frameN  # exact frame index
            win.timeOnFlip(end_practice_continue, 'tStopRefresh')  # time at next scr refresh
            end_practice_continue.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in end_practiceComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end_practice"-------
for thisComponent in end_practiceComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('end_practice_text.started', end_practice_text.tStartRefresh)
thisExp.addData('end_practice_text.stopped', end_practice_text.tStopRefresh)
# check responses
if end_practice_key.keys in ['', [], None]:  # No response was made
    end_practice_key.keys = None
thisExp.addData('end_practice_key.keys',end_practice_key.keys)
if end_practice_key.keys != None:  # we had a response
    thisExp.addData('end_practice_key.rt', end_practice_key.rt)
thisExp.addData('end_practice_key.started', end_practice_key.tStartRefresh)
thisExp.addData('end_practice_key.stopped', end_practice_key.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('end_practice_continue.started', end_practice_continue.tStartRefresh)
thisExp.addData('end_practice_continue.stopped', end_practice_continue.tStopRefresh)

# set up handler to look after randomisation of conditions etc
enc_runs = data.TrialHandler(nReps=2, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='enc_runs')
thisExp.addLoop(enc_runs)  # add the loop to the experiment
thisEnc_run = enc_runs.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisEnc_run.rgb)
if thisEnc_run != None:
    for paramName in thisEnc_run:
        exec('{} = thisEnc_run[paramName]'.format(paramName))

for thisEnc_run in enc_runs:
    currentLoop = enc_runs
    # abbreviate parameter names if possible (e.g. rgb = thisEnc_run.rgb)
    if thisEnc_run != None:
        for paramName in thisEnc_run:
            exec('{} = thisEnc_run[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "start_MR"-------
    continueRoutine = True
    # update component parameters for each repeat
    start_MR_trigger.keys = []
    start_MR_trigger.rt = []
    _start_MR_trigger_allKeys = []
    # keep track of which components have finished
    start_MRComponents = [start_MR_text, start_MR_trigger]
    for thisComponent in start_MRComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    start_MRClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "start_MR"-------
    while continueRoutine:
        # get current time
        t = start_MRClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=start_MRClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *start_MR_text* updates
        if start_MR_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            start_MR_text.frameNStart = frameN  # exact frame index
            start_MR_text.tStart = t  # local t and not account for scr refresh
            start_MR_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(start_MR_text, 'tStartRefresh')  # time at next scr refresh
            start_MR_text.setAutoDraw(True)
        
        # *start_MR_trigger* updates
        waitOnFlip = False
        if start_MR_trigger.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            start_MR_trigger.frameNStart = frameN  # exact frame index
            start_MR_trigger.tStart = t  # local t and not account for scr refresh
            start_MR_trigger.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(start_MR_trigger, 'tStartRefresh')  # time at next scr refresh
            start_MR_trigger.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(start_MR_trigger.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(start_MR_trigger.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if start_MR_trigger.status == STARTED and not waitOnFlip:
            theseKeys = start_MR_trigger.getKeys(keyList=['s'], waitRelease=False)
            _start_MR_trigger_allKeys.extend(theseKeys)
            if len(_start_MR_trigger_allKeys):
                start_MR_trigger.keys = [key.name for key in _start_MR_trigger_allKeys]  # storing all keys
                start_MR_trigger.rt = [key.rt for key in _start_MR_trigger_allKeys]
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in start_MRComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "start_MR"-------
    for thisComponent in start_MRComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    enc_runs.addData('start_MR_text.started', start_MR_text.tStartRefresh)
    enc_runs.addData('start_MR_text.stopped', start_MR_text.tStopRefresh)
    # check responses
    if start_MR_trigger.keys in ['', [], None]:  # No response was made
        start_MR_trigger.keys = None
    enc_runs.addData('start_MR_trigger.keys',start_MR_trigger.keys)
    if start_MR_trigger.keys != None:  # we had a response
        enc_runs.addData('start_MR_trigger.rt', start_MR_trigger.rt)
    enc_runs.addData('start_MR_trigger.started', start_MR_trigger.tStartRefresh)
    enc_runs.addData('start_MR_trigger.stopped', start_MR_trigger.tStopRefresh)
    trigger_time = globalClock.getTime()
    event.globalKeys.add(key=trigger_key, func=get_current_trigger_time)
    thisExp.addData('trigger_time', trigger_time)
    
    # the Routine "start_MR" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "start_enc_run"-------
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    start = end
    end = start + 3
    selection = np.arange(start, end, step)
    
    run_counter = run_counter + 1
    end_run_text = 'Rövid szünet.'
    
    if run_counter >= 2:
        end_run_text = 'Vége az első feladatnak.'
    # keep track of which components have finished
    start_enc_runComponents = [start_enc_run_text]
    for thisComponent in start_enc_runComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    start_enc_runClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "start_enc_run"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = start_enc_runClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=start_enc_runClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *start_enc_run_text* updates
        if start_enc_run_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            start_enc_run_text.frameNStart = frameN  # exact frame index
            start_enc_run_text.tStart = t  # local t and not account for scr refresh
            start_enc_run_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(start_enc_run_text, 'tStartRefresh')  # time at next scr refresh
            start_enc_run_text.setAutoDraw(True)
        if start_enc_run_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > start_enc_run_text.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                start_enc_run_text.tStop = t  # not accounting for scr refresh
                start_enc_run_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(start_enc_run_text, 'tStopRefresh')  # time at next scr refresh
                start_enc_run_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in start_enc_runComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "start_enc_run"-------
    for thisComponent in start_enc_runComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    enc_runs.addData('start_enc_run_text.started', start_enc_run_text.tStartRefresh)
    enc_runs.addData('start_enc_run_text.stopped', start_enc_run_text.tStopRefresh)
    
    # set up handler to look after randomisation of conditions etc
    enc_trials = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(stimuli_table, selection=selection),
        seed=None, name='enc_trials')
    thisExp.addLoop(enc_trials)  # add the loop to the experiment
    thisEnc_trial = enc_trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisEnc_trial.rgb)
    if thisEnc_trial != None:
        for paramName in thisEnc_trial:
            exec('{} = thisEnc_trial[paramName]'.format(paramName))
    
    for thisEnc_trial in enc_trials:
        currentLoop = enc_trials
        # abbreviate parameter names if possible (e.g. rgb = thisEnc_trial.rgb)
        if thisEnc_trial != None:
            for paramName in thisEnc_trial:
                exec('{} = thisEnc_trial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "enc_fx"-------
        continueRoutine = True
        # update component parameters for each repeat
        enc_fx_cross.setPos((CurrentX, CurrentY))
        enc_fx_key.keys = []
        enc_fx_key.rt = []
        _enc_fx_key_allKeys = []
        # keep track of which components have finished
        enc_fxComponents = [enc_fx_interior, enc_fx_cross, enc_fx_key]
        for thisComponent in enc_fxComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        enc_fxClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "enc_fx"-------
        while continueRoutine:
            # get current time
            t = enc_fxClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=enc_fxClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *enc_fx_interior* updates
            if enc_fx_interior.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                enc_fx_interior.frameNStart = frameN  # exact frame index
                enc_fx_interior.tStart = t  # local t and not account for scr refresh
                enc_fx_interior.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(enc_fx_interior, 'tStartRefresh')  # time at next scr refresh
                enc_fx_interior.setAutoDraw(True)
            if enc_fx_interior.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > enc_fx_interior.tStartRefresh + Jitter/1000-frameTolerance:
                    # keep track of stop time/frame for later
                    enc_fx_interior.tStop = t  # not accounting for scr refresh
                    enc_fx_interior.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(enc_fx_interior, 'tStopRefresh')  # time at next scr refresh
                    enc_fx_interior.setAutoDraw(False)
            
            # *enc_fx_cross* updates
            if enc_fx_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                enc_fx_cross.frameNStart = frameN  # exact frame index
                enc_fx_cross.tStart = t  # local t and not account for scr refresh
                enc_fx_cross.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(enc_fx_cross, 'tStartRefresh')  # time at next scr refresh
                enc_fx_cross.setAutoDraw(True)
            if enc_fx_cross.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > enc_fx_cross.tStartRefresh + Jitter/1000-frameTolerance:
                    # keep track of stop time/frame for later
                    enc_fx_cross.tStop = t  # not accounting for scr refresh
                    enc_fx_cross.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(enc_fx_cross, 'tStopRefresh')  # time at next scr refresh
                    enc_fx_cross.setAutoDraw(False)
            
            # *enc_fx_key* updates
            waitOnFlip = False
            if enc_fx_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                enc_fx_key.frameNStart = frameN  # exact frame index
                enc_fx_key.tStart = t  # local t and not account for scr refresh
                enc_fx_key.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(enc_fx_key, 'tStartRefresh')  # time at next scr refresh
                enc_fx_key.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(enc_fx_key.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(enc_fx_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if enc_fx_key.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > enc_fx_key.tStartRefresh + Jitter/1000-frameTolerance:
                    # keep track of stop time/frame for later
                    enc_fx_key.tStop = t  # not accounting for scr refresh
                    enc_fx_key.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(enc_fx_key, 'tStopRefresh')  # time at next scr refresh
                    enc_fx_key.status = FINISHED
            if enc_fx_key.status == STARTED and not waitOnFlip:
                theseKeys = enc_fx_key.getKeys(keyList=['b', 'c'], waitRelease=False)
                _enc_fx_key_allKeys.extend(theseKeys)
                if len(_enc_fx_key_allKeys):
                    enc_fx_key.keys = _enc_fx_key_allKeys[-1].name  # just the last key pressed
                    enc_fx_key.rt = _enc_fx_key_allKeys[-1].rt
            if enc_trials.thisN == 0 and frameN == 0: # start of the loop
                loop_start_time = globalClock.getTime() - trigger_time
                thisExp.addData('loop_start_time', loop_start_time)
            elif frameN == 1: # the zeroth frame has just been drawn
                fx_start_time = globalClock.getTime() - trigger_time
                # store the data:
                thisExp.addData('fx_start_time', fx_start_time)
            
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in enc_fxComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "enc_fx"-------
        for thisComponent in enc_fxComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        enc_trials.addData('enc_fx_interior.started', enc_fx_interior.tStartRefresh)
        enc_trials.addData('enc_fx_interior.stopped', enc_fx_interior.tStopRefresh)
        enc_trials.addData('enc_fx_cross.started', enc_fx_cross.tStartRefresh)
        enc_trials.addData('enc_fx_cross.stopped', enc_fx_cross.tStopRefresh)
        # check responses
        if enc_fx_key.keys in ['', [], None]:  # No response was made
            enc_fx_key.keys = None
        enc_trials.addData('enc_fx_key.keys',enc_fx_key.keys)
        if enc_fx_key.keys != None:  # we had a response
            enc_trials.addData('enc_fx_key.rt', enc_fx_key.rt)
        enc_trials.addData('enc_fx_key.started', enc_fx_key.tStartRefresh)
        enc_trials.addData('enc_fx_key.stopped', enc_fx_key.tStopRefresh)
        # the Routine "enc_fx" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "enc_trial"-------
        continueRoutine = True
        routineTimer.add(3.000000)
        # update component parameters for each repeat
        w_size = win.size
        
        x_size = w_size[0]
        y_size = w_size[1]
        
        scr_resolution = x_size/y_size
        enc_trial_main_image.setPos((CurrentX, CurrentY))
        enc_trial_main_image.setSize((0.3125, 0.3125*scr_resolution))
        enc_trial_main_image.setImage(CurrentImage)
        enc_trial_key.keys = []
        enc_trial_key.rt = []
        _enc_trial_key_allKeys = []
        # keep track of which components have finished
        enc_trialComponents = [enc_trial_interior, enc_trial_main_image, enc_trial_key]
        for thisComponent in enc_trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        enc_trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "enc_trial"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = enc_trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=enc_trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *enc_trial_interior* updates
            if enc_trial_interior.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                enc_trial_interior.frameNStart = frameN  # exact frame index
                enc_trial_interior.tStart = t  # local t and not account for scr refresh
                enc_trial_interior.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(enc_trial_interior, 'tStartRefresh')  # time at next scr refresh
                enc_trial_interior.setAutoDraw(True)
            if enc_trial_interior.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > enc_trial_interior.tStartRefresh + 3.0-frameTolerance:
                    # keep track of stop time/frame for later
                    enc_trial_interior.tStop = t  # not accounting for scr refresh
                    enc_trial_interior.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(enc_trial_interior, 'tStopRefresh')  # time at next scr refresh
                    enc_trial_interior.setAutoDraw(False)
            
            # *enc_trial_main_image* updates
            if enc_trial_main_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                enc_trial_main_image.frameNStart = frameN  # exact frame index
                enc_trial_main_image.tStart = t  # local t and not account for scr refresh
                enc_trial_main_image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(enc_trial_main_image, 'tStartRefresh')  # time at next scr refresh
                enc_trial_main_image.setAutoDraw(True)
            if enc_trial_main_image.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > enc_trial_main_image.tStartRefresh + 3.0-frameTolerance:
                    # keep track of stop time/frame for later
                    enc_trial_main_image.tStop = t  # not accounting for scr refresh
                    enc_trial_main_image.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(enc_trial_main_image, 'tStopRefresh')  # time at next scr refresh
                    enc_trial_main_image.setAutoDraw(False)
            
            # *enc_trial_key* updates
            waitOnFlip = False
            if enc_trial_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                enc_trial_key.frameNStart = frameN  # exact frame index
                enc_trial_key.tStart = t  # local t and not account for scr refresh
                enc_trial_key.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(enc_trial_key, 'tStartRefresh')  # time at next scr refresh
                enc_trial_key.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(enc_trial_key.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(enc_trial_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if enc_trial_key.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > enc_trial_key.tStartRefresh + 3.0-frameTolerance:
                    # keep track of stop time/frame for later
                    enc_trial_key.tStop = t  # not accounting for scr refresh
                    enc_trial_key.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(enc_trial_key, 'tStopRefresh')  # time at next scr refresh
                    enc_trial_key.status = FINISHED
            if enc_trial_key.status == STARTED and not waitOnFlip:
                theseKeys = enc_trial_key.getKeys(keyList=['b', 'c'], waitRelease=False)
                _enc_trial_key_allKeys.extend(theseKeys)
                if len(_enc_trial_key_allKeys):
                    enc_trial_key.keys = _enc_trial_key_allKeys[-1].name  # just the last key pressed
                    enc_trial_key.rt = _enc_trial_key_allKeys[-1].rt
            if frameN == 0: # start of the trial
                trial_start_time = globalClock.getTime() - trigger_time
                thisExp.addData('trial_start_time', trial_start_time)
            elif frameN == 1: # the zeroth frame has just been drawn
                stimulus_start_time = globalClock.getTime() - trigger_time
                # store the data:
                thisExp.addData('stimulus_start_time', stimulus_start_time)
            
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in enc_trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "enc_trial"-------
        for thisComponent in enc_trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        enc_trials.addData('enc_trial_interior.started', enc_trial_interior.tStartRefresh)
        enc_trials.addData('enc_trial_interior.stopped', enc_trial_interior.tStopRefresh)
        enc_trials.addData('enc_trial_main_image.started', enc_trial_main_image.tStartRefresh)
        enc_trials.addData('enc_trial_main_image.stopped', enc_trial_main_image.tStopRefresh)
        # check responses
        if enc_trial_key.keys in ['', [], None]:  # No response was made
            enc_trial_key.keys = None
        enc_trials.addData('enc_trial_key.keys',enc_trial_key.keys)
        if enc_trial_key.keys != None:  # we had a response
            enc_trials.addData('enc_trial_key.rt', enc_trial_key.rt)
        enc_trials.addData('enc_trial_key.started', enc_trial_key.tStartRefresh)
        enc_trials.addData('enc_trial_key.stopped', enc_trial_key.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1 repeats of 'enc_trials'
    
    
    # ------Prepare to start Routine "end_enc_run"-------
    continueRoutine = True
    routineTimer.add(180.000000)
    # update component parameters for each repeat
    end_enc_run_text.setText(end_run_text)
    enc_run_end_key.keys = []
    enc_run_end_key.rt = []
    _enc_run_end_key_allKeys = []
    # keep track of which components have finished
    end_enc_runComponents = [end_enc_run_text, enc_run_end_key, enc_run_end_continue]
    for thisComponent in end_enc_runComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    end_enc_runClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "end_enc_run"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = end_enc_runClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=end_enc_runClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *end_enc_run_text* updates
        if end_enc_run_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            end_enc_run_text.frameNStart = frameN  # exact frame index
            end_enc_run_text.tStart = t  # local t and not account for scr refresh
            end_enc_run_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(end_enc_run_text, 'tStartRefresh')  # time at next scr refresh
            end_enc_run_text.setAutoDraw(True)
        if end_enc_run_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > end_enc_run_text.tStartRefresh + 180-frameTolerance:
                # keep track of stop time/frame for later
                end_enc_run_text.tStop = t  # not accounting for scr refresh
                end_enc_run_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(end_enc_run_text, 'tStopRefresh')  # time at next scr refresh
                end_enc_run_text.setAutoDraw(False)
        
        # *enc_run_end_key* updates
        waitOnFlip = False
        if enc_run_end_key.status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
            # keep track of start time/frame for later
            enc_run_end_key.frameNStart = frameN  # exact frame index
            enc_run_end_key.tStart = t  # local t and not account for scr refresh
            enc_run_end_key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(enc_run_end_key, 'tStartRefresh')  # time at next scr refresh
            enc_run_end_key.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(enc_run_end_key.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(enc_run_end_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if enc_run_end_key.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > enc_run_end_key.tStartRefresh + 175-frameTolerance:
                # keep track of stop time/frame for later
                enc_run_end_key.tStop = t  # not accounting for scr refresh
                enc_run_end_key.frameNStop = frameN  # exact frame index
                win.timeOnFlip(enc_run_end_key, 'tStopRefresh')  # time at next scr refresh
                enc_run_end_key.status = FINISHED
        if enc_run_end_key.status == STARTED and not waitOnFlip:
            theseKeys = enc_run_end_key.getKeys(keyList=['d'], waitRelease=False)
            _enc_run_end_key_allKeys.extend(theseKeys)
            if len(_enc_run_end_key_allKeys):
                enc_run_end_key.keys = _enc_run_end_key_allKeys[-1].name  # just the last key pressed
                enc_run_end_key.rt = _enc_run_end_key_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *enc_run_end_continue* updates
        if enc_run_end_continue.status == NOT_STARTED and tThisFlip >= 5.0-frameTolerance:
            # keep track of start time/frame for later
            enc_run_end_continue.frameNStart = frameN  # exact frame index
            enc_run_end_continue.tStart = t  # local t and not account for scr refresh
            enc_run_end_continue.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(enc_run_end_continue, 'tStartRefresh')  # time at next scr refresh
            enc_run_end_continue.setAutoDraw(True)
        if enc_run_end_continue.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > enc_run_end_continue.tStartRefresh + 175-frameTolerance:
                # keep track of stop time/frame for later
                enc_run_end_continue.tStop = t  # not accounting for scr refresh
                enc_run_end_continue.frameNStop = frameN  # exact frame index
                win.timeOnFlip(enc_run_end_continue, 'tStopRefresh')  # time at next scr refresh
                enc_run_end_continue.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in end_enc_runComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "end_enc_run"-------
    for thisComponent in end_enc_runComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    enc_runs.addData('end_enc_run_text.started', end_enc_run_text.tStartRefresh)
    enc_runs.addData('end_enc_run_text.stopped', end_enc_run_text.tStopRefresh)
    # check responses
    if enc_run_end_key.keys in ['', [], None]:  # No response was made
        enc_run_end_key.keys = None
    enc_runs.addData('enc_run_end_key.keys',enc_run_end_key.keys)
    if enc_run_end_key.keys != None:  # we had a response
        enc_runs.addData('enc_run_end_key.rt', enc_run_end_key.rt)
    enc_runs.addData('enc_run_end_key.started', enc_run_end_key.tStartRefresh)
    enc_runs.addData('enc_run_end_key.stopped', enc_run_end_key.tStopRefresh)
    enc_runs.addData('enc_run_end_continue.started', enc_run_end_continue.tStartRefresh)
    enc_runs.addData('enc_run_end_continue.stopped', enc_run_end_continue.tStopRefresh)
# completed 2 repeats of 'enc_runs'


# ------Prepare to start Routine "inter_task_break"-------
continueRoutine = True
routineTimer.add(120.000000)
# update component parameters for each repeat
# keep track of which components have finished
inter_task_breakComponents = [inter_task_break_text]
for thisComponent in inter_task_breakComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
inter_task_breakClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "inter_task_break"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = inter_task_breakClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=inter_task_breakClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *inter_task_break_text* updates
    if inter_task_break_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        inter_task_break_text.frameNStart = frameN  # exact frame index
        inter_task_break_text.tStart = t  # local t and not account for scr refresh
        inter_task_break_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(inter_task_break_text, 'tStartRefresh')  # time at next scr refresh
        inter_task_break_text.setAutoDraw(True)
    if inter_task_break_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > inter_task_break_text.tStartRefresh + 120.0-frameTolerance:
            # keep track of stop time/frame for later
            inter_task_break_text.tStop = t  # not accounting for scr refresh
            inter_task_break_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(inter_task_break_text, 'tStopRefresh')  # time at next scr refresh
            inter_task_break_text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in inter_task_breakComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "inter_task_break"-------
for thisComponent in inter_task_breakComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('inter_task_break_text.started', inter_task_break_text.tStartRefresh)
thisExp.addData('inter_task_break_text.stopped', inter_task_break_text.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
