#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.4),
    on June 18, 2021, at 14:57
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

import psychopy
psychopy.useVersion('latest')


from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.1.4'
expName = 'TérKépÉsz'  # from the Builder filename that created this script
expInfo = {'ID': '', 'Session': 'OBJ/LOC'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s_%s' % (expInfo['ID'],'PRACTICE', expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='D:\\Zsuzsa\\HCCCL\\experiment\\computer_based_tasks\\mTRK\\TerKepEsz\\terkepesz_practice.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='NLL LCD', color=[0.114,0.310,0.380], colorSpace='rgb',
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

# Initialize components for Routine "experiment_setup"
experiment_setupClock = core.Clock()
w_size = win.size

x_size = w_size[0]
y_size = w_size[1]

scr_resolution = x_size/y_size
import os
os.system('color')
from termcolor import colored, cprint
import colorama
colorama.init()
win.mouseVisible = False
cprint('State: Experiment Setup', 'blue', 'on_white')
print('Mouse disabled on screen. Keep CMD window active!')
session = expInfo['Session']
if session == 'OBJ':
    task_name='Képszemle'
    block_name_selection=[0, 76]
    print('Session selected: OBJ')
elif session == 'LOC':
    task_name='Berendezés'
    block_name_selection=[152,228]
    print('Session selected: LOC')
else:
    block_name_selection=[0,76]
    print('Invalid Session! Will use OBJ.')
 
instruction_text = ''
if session == 'OBJ':
    instruction_text = "A Galériaberendezés alatt azt döntse el, beválogatja-e a képet a kiállításra.\
                        \n\n\t\tJobb Nyíl - Igen\n\t\tBal Nyíl - Nem\
                        \n-----------------------------------------------------------------------\
                        \nA Képfelismerés allatt azt döntse el, látta-e már pontosan ugyanezt a képet a Galériaberendezés alatt.\
                        \n\n\t\tJobb Nyíl - Új\
                        \n\t\tBal Nyíl - Régi"
elif session == 'LOC':
    instruction_text = "A Galériaberendezés alatt azt döntse el, maradhat-e a kép a bemutatott helyen.\
                        \n\n\t\tJobb Nyíl - Igen\n\t\tBal Nyíl - Nem\
                        \n-----------------------------------------------------------------------\
                        \nA Helyfelismerés allatt azt döntse el, pontosan ezen a helyen látta-e a képet.\
                        \n\n\t\tJobb Nyíl - Új\n\t\tBal Nyíl - Régi"
welcome_image = visual.ImageStim(
    win=win,
    name='welcome_image', units='pix', 
    image='stimuli/terkepesz.png', mask=None,
    ori=0, pos=(0, -100), size=(309,665),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
welcome_text = visual.TextStim(win=win, name='welcome_text',
    text='TérKépÉsz Feladatok',
    font='Arial',
    units='pix', pos=(0, 350), height=50, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);

# Initialize components for Routine "general_instructions"
general_instructionsClock = core.Clock()
general_instructions_key = keyboard.Keyboard()
general_instructions_4_continue = visual.TextStim(win=win, name='general_instructions_4_continue',
    text='A gyakorláshoz nyomja le a SPACE-t.',
    font='Arial',
    pos=(0,-0.4), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
general_instructions_text = visual.TextStim(win=win, name='general_instructions_text',
    text='',
    font='Arial',
    pos=(0, -0.01), height=0.03, wrapWidth=None, ori=0, 
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

# Initialize components for Routine "practice_block_start"
practice_block_startClock = core.Clock()
if session == 'OBJ':
    practice_start = 0
elif session == 'LOC':
    practice_start = 3
else:
    print('Invalid session! Will go with OBJ')
    practice_start = 0
step = 1

practice_block_text = visual.TextStim(win=win, name='practice_block_text',
    text='',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "enc_fx_practice"
enc_fx_practiceClock = core.Clock()
enc_fx_interior_practice = visual.ImageStim(
    win=win,
    name='enc_fx_interior_practice', units='norm', 
    image='stimuli/GalleryInterior.png', mask=None,
    ori=0, pos=(0, -0), size=(2.0, 2.0),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
enc_fx_cross_practice = visual.TextStim(win=win, name='enc_fx_cross_practice',
    text='+',
    font='Arial',
    units='norm', pos=[0,0], height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
enc_fx_key_practice = keyboard.Keyboard()
enc_fx_text_block_practice = visual.TextStim(win=win, name='enc_fx_text_block_practice',
    text='',
    font='Arial',
    units='norm', pos=(0, 0.87), height=0.06, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
enc_fx_instructions_text_practice = visual.TextStim(win=win, name='enc_fx_instructions_text_practice',
    text='[BAL Nyíl - Nem marad]      [JOBB Nyíl - Marad]',
    font='Arial',
    units='norm', pos=(0, -0.833), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);

# Initialize components for Routine "enc_trial_practice"
enc_trial_practiceClock = core.Clock()
enc_trial_interior_practice = visual.ImageStim(
    win=win,
    name='enc_trial_interior_practice', units='norm', 
    image='stimuli/GalleryInterior.png', mask=None,
    ori=0, pos=(0, -0), size=(2.0, 2.0),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
enc_trial_main_image_practice = visual.ImageStim(
    win=win,
    name='enc_trial_main_image_practice', units='norm', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
enc_trial_key_practice = keyboard.Keyboard()
enc_trial_text_block_practice = visual.TextStim(win=win, name='enc_trial_text_block_practice',
    text='',
    font='Arial',
    units='norm', pos=(0, 0.87), height=0.06, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
enc_trial_instructions_text_practice = visual.TextStim(win=win, name='enc_trial_instructions_text_practice',
    text='[BAL Nyíl - Nem marad]      [JOBB Nyíl - Marad]',
    font='Arial',
    units='norm', pos=(0, -0.833), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

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
    text='',
    font='Arial',
    units='norm', pos=[0,0], height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
enc_practice_feedback_block = visual.TextStim(win=win, name='enc_practice_feedback_block',
    text='',
    font='Arial',
    units='norm', pos=(0, 0.87), height=0.06, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "recognition_title"
recognition_titleClock = core.Clock()
start_recognition_text = visual.TextStim(win=win, name='start_recognition_text',
    text='Képfelismerés',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "rec_fx_practice"
rec_fx_practiceClock = core.Clock()
rec_fx_interior_practice = visual.ImageStim(
    win=win,
    name='rec_fx_interior_practice', units='norm', 
    image='stimuli/GalleryInterior.png', mask=None,
    ori=0, pos=(0,0), size=(2.0, 2.0),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
rec_fx_cross_practice = visual.TextStim(win=win, name='rec_fx_cross_practice',
    text='+',
    font='Arial',
    units='norm', pos=[0,0], height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
rec_fx_key_practice = keyboard.Keyboard()
rec_fx_text_block_practice = visual.TextStim(win=win, name='rec_fx_text_block_practice',
    text='',
    font='Arial',
    units='norm', pos=(0, 0.87), height=0.06, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
rec_fx_instructions_text_practice = visual.TextStim(win=win, name='rec_fx_instructions_text_practice',
    text='[BAL Nyíl - Régi]      [JOBB Nyíl - Új]',
    font='Arial',
    units='norm', pos=(0, -0.833), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "rec_trial_practice"
rec_trial_practiceClock = core.Clock()
rec_trial_interior_practice = visual.ImageStim(
    win=win,
    name='rec_trial_interior_practice', units='norm', 
    image='stimuli/GalleryInterior.png', mask=None,
    ori=0, pos=(0, -0), size=(2.0, 2.0),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
rec_trial_main_image_practice = visual.ImageStim(
    win=win,
    name='rec_trial_main_image_practice', units='norm', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
rec_trial_key_practice = keyboard.Keyboard()
rec_trial_text_block_practice = visual.TextStim(win=win, name='rec_trial_text_block_practice',
    text='',
    font='Arial',
    units='norm', pos=(0, 0.87), height=0.06, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
rec_trial_instructions_text_practice = visual.TextStim(win=win, name='rec_trial_instructions_text_practice',
    text='[BAL Nyíl - Régi]      [JOBB Nyíl - Új]',
    font='Arial',
    units='norm', pos=(0, -0.833), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "rec_practice_feedback"
rec_practice_feedbackClock = core.Clock()
rec_practice_feedback_text = visual.TextStim(win=win, name='rec_practice_feedback_text',
    text='',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "end_practice"
end_practiceClock = core.Clock()
end_practice_text = visual.TextStim(win=win, name='end_practice_text',
    text='Ez volt a gyakorlás.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=0.8, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
end_practice_key = keyboard.Keyboard()
end_practice_continue = visual.TextStim(win=win, name='end_practice_continue',
    text='A kilépéshez nyomja le a SPACE-t. ',
    font='Arial',
    pos=(0,-0.4), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "experiment_setup"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
logging.setDefaultClock(globalClock)
# keep track of which components have finished
experiment_setupComponents = [welcome_image, welcome_text]
for thisComponent in experiment_setupComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
experiment_setupClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "experiment_setup"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = experiment_setupClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=experiment_setupClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *welcome_image* updates
    if welcome_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcome_image.frameNStart = frameN  # exact frame index
        welcome_image.tStart = t  # local t and not account for scr refresh
        welcome_image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcome_image, 'tStartRefresh')  # time at next scr refresh
        welcome_image.setAutoDraw(True)
    if welcome_image.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > welcome_image.tStartRefresh + 3.0-frameTolerance:
            # keep track of stop time/frame for later
            welcome_image.tStop = t  # not accounting for scr refresh
            welcome_image.frameNStop = frameN  # exact frame index
            win.timeOnFlip(welcome_image, 'tStopRefresh')  # time at next scr refresh
            welcome_image.setAutoDraw(False)
    
    # *welcome_text* updates
    if welcome_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcome_text.frameNStart = frameN  # exact frame index
        welcome_text.tStart = t  # local t and not account for scr refresh
        welcome_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcome_text, 'tStartRefresh')  # time at next scr refresh
        welcome_text.setAutoDraw(True)
    if welcome_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > welcome_text.tStartRefresh + 3.0-frameTolerance:
            # keep track of stop time/frame for later
            welcome_text.tStop = t  # not accounting for scr refresh
            welcome_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(welcome_text, 'tStopRefresh')  # time at next scr refresh
            welcome_text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in experiment_setupComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "experiment_setup"-------
for thisComponent in experiment_setupComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('welcome_image.started', welcome_image.tStartRefresh)
thisExp.addData('welcome_image.stopped', welcome_image.tStopRefresh)
thisExp.addData('welcome_text.started', welcome_text.tStartRefresh)
thisExp.addData('welcome_text.stopped', welcome_text.tStopRefresh)

# ------Prepare to start Routine "general_instructions"-------
continueRoutine = True
routineTimer.add(300.000000)
# update component parameters for each repeat
general_instructions_key.keys = []
general_instructions_key.rt = []
_general_instructions_key_allKeys = []
general_instructions_text.setText(instruction_text)
cprint('On Screen: General instructions...', 'blue', 'on_white')
cprint('Waiting for participant\'s response (d)', 'yellow')
# keep track of which components have finished
general_instructionsComponents = [general_instructions_key, general_instructions_4_continue, general_instructions_text]
for thisComponent in general_instructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
general_instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "general_instructions"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = general_instructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=general_instructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *general_instructions_key* updates
    waitOnFlip = False
    if general_instructions_key.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
        # keep track of start time/frame for later
        general_instructions_key.frameNStart = frameN  # exact frame index
        general_instructions_key.tStart = t  # local t and not account for scr refresh
        general_instructions_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(general_instructions_key, 'tStartRefresh')  # time at next scr refresh
        general_instructions_key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(general_instructions_key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(general_instructions_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if general_instructions_key.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > general_instructions_key.tStartRefresh + 299.0-frameTolerance:
            # keep track of stop time/frame for later
            general_instructions_key.tStop = t  # not accounting for scr refresh
            general_instructions_key.frameNStop = frameN  # exact frame index
            win.timeOnFlip(general_instructions_key, 'tStopRefresh')  # time at next scr refresh
            general_instructions_key.status = FINISHED
    if general_instructions_key.status == STARTED and not waitOnFlip:
        theseKeys = general_instructions_key.getKeys(keyList=['d', 'space'], waitRelease=False)
        _general_instructions_key_allKeys.extend(theseKeys)
        if len(_general_instructions_key_allKeys):
            general_instructions_key.keys = _general_instructions_key_allKeys[-1].name  # just the last key pressed
            general_instructions_key.rt = _general_instructions_key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *general_instructions_4_continue* updates
    if general_instructions_4_continue.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
        # keep track of start time/frame for later
        general_instructions_4_continue.frameNStart = frameN  # exact frame index
        general_instructions_4_continue.tStart = t  # local t and not account for scr refresh
        general_instructions_4_continue.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(general_instructions_4_continue, 'tStartRefresh')  # time at next scr refresh
        general_instructions_4_continue.setAutoDraw(True)
    if general_instructions_4_continue.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > general_instructions_4_continue.tStartRefresh + 299.0-frameTolerance:
            # keep track of stop time/frame for later
            general_instructions_4_continue.tStop = t  # not accounting for scr refresh
            general_instructions_4_continue.frameNStop = frameN  # exact frame index
            win.timeOnFlip(general_instructions_4_continue, 'tStopRefresh')  # time at next scr refresh
            general_instructions_4_continue.setAutoDraw(False)
    
    # *general_instructions_text* updates
    if general_instructions_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        general_instructions_text.frameNStart = frameN  # exact frame index
        general_instructions_text.tStart = t  # local t and not account for scr refresh
        general_instructions_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(general_instructions_text, 'tStartRefresh')  # time at next scr refresh
        general_instructions_text.setAutoDraw(True)
    if general_instructions_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > general_instructions_text.tStartRefresh + 300.0-frameTolerance:
            # keep track of stop time/frame for later
            general_instructions_text.tStop = t  # not accounting for scr refresh
            general_instructions_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(general_instructions_text, 'tStopRefresh')  # time at next scr refresh
            general_instructions_text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in general_instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "general_instructions"-------
for thisComponent in general_instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if general_instructions_key.keys in ['', [], None]:  # No response was made
    general_instructions_key.keys = None
thisExp.addData('general_instructions_key.keys',general_instructions_key.keys)
if general_instructions_key.keys != None:  # we had a response
    thisExp.addData('general_instructions_key.rt', general_instructions_key.rt)
thisExp.addData('general_instructions_key.started', general_instructions_key.tStartRefresh)
thisExp.addData('general_instructions_key.stopped', general_instructions_key.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('general_instructions_4_continue.started', general_instructions_4_continue.tStartRefresh)
thisExp.addData('general_instructions_4_continue.stopped', general_instructions_4_continue.tStopRefresh)
thisExp.addData('general_instructions_text.started', general_instructions_text.tStartRefresh)
thisExp.addData('general_instructions_text.stopped', general_instructions_text.tStopRefresh)
cprint('key pressed: '+ general_instructions_key.keys, 'green')

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

# ------Prepare to start Routine "practice_block_start"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
practice_end = practice_start + 3
practice_selection = np.arange(practice_start, practice_end, step)
practice_block_text.setText(task_name)
# keep track of which components have finished
practice_block_startComponents = [practice_block_text]
for thisComponent in practice_block_startComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
practice_block_startClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "practice_block_start"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = practice_block_startClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=practice_block_startClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *practice_block_text* updates
    if practice_block_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        practice_block_text.frameNStart = frameN  # exact frame index
        practice_block_text.tStart = t  # local t and not account for scr refresh
        practice_block_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practice_block_text, 'tStartRefresh')  # time at next scr refresh
        practice_block_text.setAutoDraw(True)
    if practice_block_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > practice_block_text.tStartRefresh + 3.0-frameTolerance:
            # keep track of stop time/frame for later
            practice_block_text.tStop = t  # not accounting for scr refresh
            practice_block_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(practice_block_text, 'tStopRefresh')  # time at next scr refresh
            practice_block_text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in practice_block_startComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "practice_block_start"-------
for thisComponent in practice_block_startComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
print('Encoding practice loop starting with following parameters:')
thisExp.addData('practice_block_text.started', practice_block_text.tStartRefresh)
thisExp.addData('practice_block_text.stopped', practice_block_text.tStopRefresh)

# set up handler to look after randomisation of conditions etc
enc_full_practice = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('stimuli_tables/encoding_full_practice_trials.csv', selection=practice_selection),
    seed=None, name='enc_full_practice')
thisExp.addLoop(enc_full_practice)  # add the loop to the experiment
thisEnc_full_practice = enc_full_practice.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisEnc_full_practice.rgb)
if thisEnc_full_practice != None:
    for paramName in thisEnc_full_practice:
        exec('{} = thisEnc_full_practice[paramName]'.format(paramName))

for thisEnc_full_practice in enc_full_practice:
    currentLoop = enc_full_practice
    # abbreviate parameter names if possible (e.g. rgb = thisEnc_full_practice.rgb)
    if thisEnc_full_practice != None:
        for paramName in thisEnc_full_practice:
            exec('{} = thisEnc_full_practice[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "enc_fx_practice"-------
    continueRoutine = True
    # update component parameters for each repeat
    block_name = ''
    if TrialType=='OBJ':
        block_name='Képszemle'
    elif TrialType=='LOC':
        block_name='Berendezés'
    else:
        block_name='Block Unknown'
    enc_fx_cross_practice.setPos((CurrentX, CurrentY))
    enc_fx_key_practice.keys = []
    enc_fx_key_practice.rt = []
    _enc_fx_key_practice_allKeys = []
    enc_fx_text_block_practice.setText(block_name)
    # keep track of which components have finished
    enc_fx_practiceComponents = [enc_fx_interior_practice, enc_fx_cross_practice, enc_fx_key_practice, enc_fx_text_block_practice, enc_fx_instructions_text_practice]
    for thisComponent in enc_fx_practiceComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    enc_fx_practiceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "enc_fx_practice"-------
    while continueRoutine:
        # get current time
        t = enc_fx_practiceClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=enc_fx_practiceClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *enc_fx_interior_practice* updates
        if enc_fx_interior_practice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            enc_fx_interior_practice.frameNStart = frameN  # exact frame index
            enc_fx_interior_practice.tStart = t  # local t and not account for scr refresh
            enc_fx_interior_practice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(enc_fx_interior_practice, 'tStartRefresh')  # time at next scr refresh
            enc_fx_interior_practice.setAutoDraw(True)
        if enc_fx_interior_practice.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > enc_fx_interior_practice.tStartRefresh + Jitter/1000-frameTolerance:
                # keep track of stop time/frame for later
                enc_fx_interior_practice.tStop = t  # not accounting for scr refresh
                enc_fx_interior_practice.frameNStop = frameN  # exact frame index
                win.timeOnFlip(enc_fx_interior_practice, 'tStopRefresh')  # time at next scr refresh
                enc_fx_interior_practice.setAutoDraw(False)
        
        # *enc_fx_cross_practice* updates
        if enc_fx_cross_practice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            enc_fx_cross_practice.frameNStart = frameN  # exact frame index
            enc_fx_cross_practice.tStart = t  # local t and not account for scr refresh
            enc_fx_cross_practice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(enc_fx_cross_practice, 'tStartRefresh')  # time at next scr refresh
            enc_fx_cross_practice.setAutoDraw(True)
        if enc_fx_cross_practice.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > enc_fx_cross_practice.tStartRefresh + Jitter/1000-frameTolerance:
                # keep track of stop time/frame for later
                enc_fx_cross_practice.tStop = t  # not accounting for scr refresh
                enc_fx_cross_practice.frameNStop = frameN  # exact frame index
                win.timeOnFlip(enc_fx_cross_practice, 'tStopRefresh')  # time at next scr refresh
                enc_fx_cross_practice.setAutoDraw(False)
        
        # *enc_fx_key_practice* updates
        waitOnFlip = False
        if enc_fx_key_practice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            enc_fx_key_practice.frameNStart = frameN  # exact frame index
            enc_fx_key_practice.tStart = t  # local t and not account for scr refresh
            enc_fx_key_practice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(enc_fx_key_practice, 'tStartRefresh')  # time at next scr refresh
            enc_fx_key_practice.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(enc_fx_key_practice.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(enc_fx_key_practice.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if enc_fx_key_practice.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > enc_fx_key_practice.tStartRefresh + Jitter/1000-frameTolerance:
                # keep track of stop time/frame for later
                enc_fx_key_practice.tStop = t  # not accounting for scr refresh
                enc_fx_key_practice.frameNStop = frameN  # exact frame index
                win.timeOnFlip(enc_fx_key_practice, 'tStopRefresh')  # time at next scr refresh
                enc_fx_key_practice.status = FINISHED
        if enc_fx_key_practice.status == STARTED and not waitOnFlip:
            theseKeys = enc_fx_key_practice.getKeys(keyList=['b', 'c', 'right', 'left'], waitRelease=False)
            _enc_fx_key_practice_allKeys.extend(theseKeys)
            if len(_enc_fx_key_practice_allKeys):
                enc_fx_key_practice.keys = _enc_fx_key_practice_allKeys[-1].name  # just the last key pressed
                enc_fx_key_practice.rt = _enc_fx_key_practice_allKeys[-1].rt
        
        # *enc_fx_text_block_practice* updates
        if enc_fx_text_block_practice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            enc_fx_text_block_practice.frameNStart = frameN  # exact frame index
            enc_fx_text_block_practice.tStart = t  # local t and not account for scr refresh
            enc_fx_text_block_practice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(enc_fx_text_block_practice, 'tStartRefresh')  # time at next scr refresh
            enc_fx_text_block_practice.setAutoDraw(True)
        if enc_fx_text_block_practice.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > enc_fx_text_block_practice.tStartRefresh + Jitter/1000-frameTolerance:
                # keep track of stop time/frame for later
                enc_fx_text_block_practice.tStop = t  # not accounting for scr refresh
                enc_fx_text_block_practice.frameNStop = frameN  # exact frame index
                win.timeOnFlip(enc_fx_text_block_practice, 'tStopRefresh')  # time at next scr refresh
                enc_fx_text_block_practice.setAutoDraw(False)
        
        # *enc_fx_instructions_text_practice* updates
        if enc_fx_instructions_text_practice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            enc_fx_instructions_text_practice.frameNStart = frameN  # exact frame index
            enc_fx_instructions_text_practice.tStart = t  # local t and not account for scr refresh
            enc_fx_instructions_text_practice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(enc_fx_instructions_text_practice, 'tStartRefresh')  # time at next scr refresh
            enc_fx_instructions_text_practice.setAutoDraw(True)
        if enc_fx_instructions_text_practice.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > enc_fx_instructions_text_practice.tStartRefresh + Jitter/1000-frameTolerance:
                # keep track of stop time/frame for later
                enc_fx_instructions_text_practice.tStop = t  # not accounting for scr refresh
                enc_fx_instructions_text_practice.frameNStop = frameN  # exact frame index
                win.timeOnFlip(enc_fx_instructions_text_practice, 'tStopRefresh')  # time at next scr refresh
                enc_fx_instructions_text_practice.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in enc_fx_practiceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "enc_fx_practice"-------
    for thisComponent in enc_fx_practiceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    enc_full_practice.addData('enc_fx_interior_practice.started', enc_fx_interior_practice.tStartRefresh)
    enc_full_practice.addData('enc_fx_interior_practice.stopped', enc_fx_interior_practice.tStopRefresh)
    enc_full_practice.addData('enc_fx_cross_practice.started', enc_fx_cross_practice.tStartRefresh)
    enc_full_practice.addData('enc_fx_cross_practice.stopped', enc_fx_cross_practice.tStopRefresh)
    # check responses
    if enc_fx_key_practice.keys in ['', [], None]:  # No response was made
        enc_fx_key_practice.keys = None
    enc_full_practice.addData('enc_fx_key_practice.keys',enc_fx_key_practice.keys)
    if enc_fx_key_practice.keys != None:  # we had a response
        enc_full_practice.addData('enc_fx_key_practice.rt', enc_fx_key_practice.rt)
    enc_full_practice.addData('enc_fx_key_practice.started', enc_fx_key_practice.tStartRefresh)
    enc_full_practice.addData('enc_fx_key_practice.stopped', enc_fx_key_practice.tStopRefresh)
    enc_full_practice.addData('enc_fx_text_block_practice.started', enc_fx_text_block_practice.tStartRefresh)
    enc_full_practice.addData('enc_fx_text_block_practice.stopped', enc_fx_text_block_practice.tStopRefresh)
    enc_full_practice.addData('enc_fx_instructions_text_practice.started', enc_fx_instructions_text_practice.tStartRefresh)
    enc_full_practice.addData('enc_fx_instructions_text_practice.stopped', enc_fx_instructions_text_practice.tStopRefresh)
    # the Routine "enc_fx_practice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "enc_trial_practice"-------
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    enc_trial_main_image_practice.setPos((CurrentX, CurrentY))
    enc_trial_main_image_practice.setSize((0.3125, 0.3125*scr_resolution))
    enc_trial_main_image_practice.setImage(CurrentImage)
    enc_trial_key_practice.keys = []
    enc_trial_key_practice.rt = []
    _enc_trial_key_practice_allKeys = []
    enc_trial_text_block_practice.setText(block_name)
    # keep track of which components have finished
    enc_trial_practiceComponents = [enc_trial_interior_practice, enc_trial_main_image_practice, enc_trial_key_practice, enc_trial_text_block_practice, enc_trial_instructions_text_practice]
    for thisComponent in enc_trial_practiceComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    enc_trial_practiceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "enc_trial_practice"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = enc_trial_practiceClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=enc_trial_practiceClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *enc_trial_interior_practice* updates
        if enc_trial_interior_practice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            enc_trial_interior_practice.frameNStart = frameN  # exact frame index
            enc_trial_interior_practice.tStart = t  # local t and not account for scr refresh
            enc_trial_interior_practice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(enc_trial_interior_practice, 'tStartRefresh')  # time at next scr refresh
            enc_trial_interior_practice.setAutoDraw(True)
        if enc_trial_interior_practice.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > enc_trial_interior_practice.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                enc_trial_interior_practice.tStop = t  # not accounting for scr refresh
                enc_trial_interior_practice.frameNStop = frameN  # exact frame index
                win.timeOnFlip(enc_trial_interior_practice, 'tStopRefresh')  # time at next scr refresh
                enc_trial_interior_practice.setAutoDraw(False)
        
        # *enc_trial_main_image_practice* updates
        if enc_trial_main_image_practice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            enc_trial_main_image_practice.frameNStart = frameN  # exact frame index
            enc_trial_main_image_practice.tStart = t  # local t and not account for scr refresh
            enc_trial_main_image_practice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(enc_trial_main_image_practice, 'tStartRefresh')  # time at next scr refresh
            enc_trial_main_image_practice.setAutoDraw(True)
        if enc_trial_main_image_practice.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > enc_trial_main_image_practice.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                enc_trial_main_image_practice.tStop = t  # not accounting for scr refresh
                enc_trial_main_image_practice.frameNStop = frameN  # exact frame index
                win.timeOnFlip(enc_trial_main_image_practice, 'tStopRefresh')  # time at next scr refresh
                enc_trial_main_image_practice.setAutoDraw(False)
        
        # *enc_trial_key_practice* updates
        waitOnFlip = False
        if enc_trial_key_practice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            enc_trial_key_practice.frameNStart = frameN  # exact frame index
            enc_trial_key_practice.tStart = t  # local t and not account for scr refresh
            enc_trial_key_practice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(enc_trial_key_practice, 'tStartRefresh')  # time at next scr refresh
            enc_trial_key_practice.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(enc_trial_key_practice.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(enc_trial_key_practice.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if enc_trial_key_practice.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > enc_trial_key_practice.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                enc_trial_key_practice.tStop = t  # not accounting for scr refresh
                enc_trial_key_practice.frameNStop = frameN  # exact frame index
                win.timeOnFlip(enc_trial_key_practice, 'tStopRefresh')  # time at next scr refresh
                enc_trial_key_practice.status = FINISHED
        if enc_trial_key_practice.status == STARTED and not waitOnFlip:
            theseKeys = enc_trial_key_practice.getKeys(keyList=['b', 'c', 'right', 'left'], waitRelease=False)
            _enc_trial_key_practice_allKeys.extend(theseKeys)
            if len(_enc_trial_key_practice_allKeys):
                enc_trial_key_practice.keys = _enc_trial_key_practice_allKeys[-1].name  # just the last key pressed
                enc_trial_key_practice.rt = _enc_trial_key_practice_allKeys[-1].rt
        
        # *enc_trial_text_block_practice* updates
        if enc_trial_text_block_practice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            enc_trial_text_block_practice.frameNStart = frameN  # exact frame index
            enc_trial_text_block_practice.tStart = t  # local t and not account for scr refresh
            enc_trial_text_block_practice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(enc_trial_text_block_practice, 'tStartRefresh')  # time at next scr refresh
            enc_trial_text_block_practice.setAutoDraw(True)
        if enc_trial_text_block_practice.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > enc_trial_text_block_practice.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                enc_trial_text_block_practice.tStop = t  # not accounting for scr refresh
                enc_trial_text_block_practice.frameNStop = frameN  # exact frame index
                win.timeOnFlip(enc_trial_text_block_practice, 'tStopRefresh')  # time at next scr refresh
                enc_trial_text_block_practice.setAutoDraw(False)
        
        # *enc_trial_instructions_text_practice* updates
        if enc_trial_instructions_text_practice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            enc_trial_instructions_text_practice.frameNStart = frameN  # exact frame index
            enc_trial_instructions_text_practice.tStart = t  # local t and not account for scr refresh
            enc_trial_instructions_text_practice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(enc_trial_instructions_text_practice, 'tStartRefresh')  # time at next scr refresh
            enc_trial_instructions_text_practice.setAutoDraw(True)
        if enc_trial_instructions_text_practice.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > enc_trial_instructions_text_practice.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                enc_trial_instructions_text_practice.tStop = t  # not accounting for scr refresh
                enc_trial_instructions_text_practice.frameNStop = frameN  # exact frame index
                win.timeOnFlip(enc_trial_instructions_text_practice, 'tStopRefresh')  # time at next scr refresh
                enc_trial_instructions_text_practice.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in enc_trial_practiceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "enc_trial_practice"-------
    for thisComponent in enc_trial_practiceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    enc_full_practice.addData('enc_trial_interior_practice.started', enc_trial_interior_practice.tStartRefresh)
    enc_full_practice.addData('enc_trial_interior_practice.stopped', enc_trial_interior_practice.tStopRefresh)
    enc_full_practice.addData('enc_trial_main_image_practice.started', enc_trial_main_image_practice.tStartRefresh)
    enc_full_practice.addData('enc_trial_main_image_practice.stopped', enc_trial_main_image_practice.tStopRefresh)
    # check responses
    if enc_trial_key_practice.keys in ['', [], None]:  # No response was made
        enc_trial_key_practice.keys = None
    enc_full_practice.addData('enc_trial_key_practice.keys',enc_trial_key_practice.keys)
    if enc_trial_key_practice.keys != None:  # we had a response
        enc_full_practice.addData('enc_trial_key_practice.rt', enc_trial_key_practice.rt)
    enc_full_practice.addData('enc_trial_key_practice.started', enc_trial_key_practice.tStartRefresh)
    enc_full_practice.addData('enc_trial_key_practice.stopped', enc_trial_key_practice.tStopRefresh)
    enc_full_practice.addData('enc_trial_text_block_practice.started', enc_trial_text_block_practice.tStartRefresh)
    enc_full_practice.addData('enc_trial_text_block_practice.stopped', enc_trial_text_block_practice.tStopRefresh)
    enc_full_practice.addData('enc_trial_instructions_text_practice.started', enc_trial_instructions_text_practice.tStartRefresh)
    enc_full_practice.addData('enc_trial_instructions_text_practice.stopped', enc_trial_instructions_text_practice.tStopRefresh)
    
    # ------Prepare to start Routine "enc_practice_feedback"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    response = enc_trial_key_practice.keys
    feedback_text = ''
    if response == 'left':
        feedback_text = 'Az Ön válasza:\nA kép nem marad.'
    elif response == 'right':
        feedback_text = 'Az Ön válasza:\nA kép marad.'
    else:
        feedback_text = 'Nem adott választ.'
    print(feedback_text)
    enc_practice_feedback_image.setPos((CurrentX, CurrentY))
    enc_practice_feedback_image.setSize((0.3125, 0.3125*scr_resolution))
    enc_practice_feedback_image.setImage(CurrentImage)
    enc_practice_feedback_text.setPos((CurrentX, CurrentY - 0.4))
    enc_practice_feedback_text.setText(feedback_text)
    enc_practice_feedback_block.setText(block_name)
    # keep track of which components have finished
    enc_practice_feedbackComponents = [enc_practice_feedback_interior, enc_practice_feedback_image, enc_practice_feedback_text, enc_practice_feedback_block]
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
        
        # *enc_practice_feedback_block* updates
        if enc_practice_feedback_block.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            enc_practice_feedback_block.frameNStart = frameN  # exact frame index
            enc_practice_feedback_block.tStart = t  # local t and not account for scr refresh
            enc_practice_feedback_block.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(enc_practice_feedback_block, 'tStartRefresh')  # time at next scr refresh
            enc_practice_feedback_block.setAutoDraw(True)
        if enc_practice_feedback_block.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > enc_practice_feedback_block.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                enc_practice_feedback_block.tStop = t  # not accounting for scr refresh
                enc_practice_feedback_block.frameNStop = frameN  # exact frame index
                win.timeOnFlip(enc_practice_feedback_block, 'tStopRefresh')  # time at next scr refresh
                enc_practice_feedback_block.setAutoDraw(False)
        
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
    enc_full_practice.addData('enc_practice_feedback_interior.started', enc_practice_feedback_interior.tStartRefresh)
    enc_full_practice.addData('enc_practice_feedback_interior.stopped', enc_practice_feedback_interior.tStopRefresh)
    enc_full_practice.addData('enc_practice_feedback_image.started', enc_practice_feedback_image.tStartRefresh)
    enc_full_practice.addData('enc_practice_feedback_image.stopped', enc_practice_feedback_image.tStopRefresh)
    enc_full_practice.addData('enc_practice_feedback_text.started', enc_practice_feedback_text.tStartRefresh)
    enc_full_practice.addData('enc_practice_feedback_text.stopped', enc_practice_feedback_text.tStopRefresh)
    enc_full_practice.addData('enc_practice_feedback_block.started', enc_practice_feedback_block.tStartRefresh)
    enc_full_practice.addData('enc_practice_feedback_block.stopped', enc_practice_feedback_block.tStopRefresh)
# completed 1 repeats of 'enc_full_practice'


# ------Prepare to start Routine "recognition_title"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
block_name = ''
if TrialType=='OBJ':
    block_name='Képfelismerés'
elif TrialType=='LOC':
    block_name='Helyfelismerés'
else:
    block_name='Block Unknown'
# keep track of which components have finished
recognition_titleComponents = [start_recognition_text]
for thisComponent in recognition_titleComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
recognition_titleClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "recognition_title"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = recognition_titleClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=recognition_titleClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *start_recognition_text* updates
    if start_recognition_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        start_recognition_text.frameNStart = frameN  # exact frame index
        start_recognition_text.tStart = t  # local t and not account for scr refresh
        start_recognition_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(start_recognition_text, 'tStartRefresh')  # time at next scr refresh
        start_recognition_text.setAutoDraw(True)
    if start_recognition_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > start_recognition_text.tStartRefresh + 3.0-frameTolerance:
            # keep track of stop time/frame for later
            start_recognition_text.tStop = t  # not accounting for scr refresh
            start_recognition_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(start_recognition_text, 'tStopRefresh')  # time at next scr refresh
            start_recognition_text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in recognition_titleComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "recognition_title"-------
for thisComponent in recognition_titleComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('start_recognition_text.started', start_recognition_text.tStartRefresh)
thisExp.addData('start_recognition_text.stopped', start_recognition_text.tStopRefresh)
print('Recognition practice loop starting with following parameters:')

# set up handler to look after randomisation of conditions etc
rec_full_practice = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('stimuli_tables/recognition_full_practice_trials.csv', selection=practice_selection),
    seed=None, name='rec_full_practice')
thisExp.addLoop(rec_full_practice)  # add the loop to the experiment
thisRec_full_practice = rec_full_practice.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisRec_full_practice.rgb)
if thisRec_full_practice != None:
    for paramName in thisRec_full_practice:
        exec('{} = thisRec_full_practice[paramName]'.format(paramName))

for thisRec_full_practice in rec_full_practice:
    currentLoop = rec_full_practice
    # abbreviate parameter names if possible (e.g. rgb = thisRec_full_practice.rgb)
    if thisRec_full_practice != None:
        for paramName in thisRec_full_practice:
            exec('{} = thisRec_full_practice[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "rec_fx_practice"-------
    continueRoutine = True
    # update component parameters for each repeat
    rec_fx_cross_practice.setPos((CurrentX, CurrentY))
    rec_fx_key_practice.keys = []
    rec_fx_key_practice.rt = []
    _rec_fx_key_practice_allKeys = []
    rec_fx_text_block_practice.setText(block_name
)
    block_name = ''
    if TrialType=='OBJ':
        block_name='Képfelismerés'
    elif TrialType=='LOC':
        block_name='Helyfelismerés'
    else:
        block_name='Block Unknown'
    # keep track of which components have finished
    rec_fx_practiceComponents = [rec_fx_interior_practice, rec_fx_cross_practice, rec_fx_key_practice, rec_fx_text_block_practice, rec_fx_instructions_text_practice]
    for thisComponent in rec_fx_practiceComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    rec_fx_practiceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "rec_fx_practice"-------
    while continueRoutine:
        # get current time
        t = rec_fx_practiceClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=rec_fx_practiceClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *rec_fx_interior_practice* updates
        if rec_fx_interior_practice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rec_fx_interior_practice.frameNStart = frameN  # exact frame index
            rec_fx_interior_practice.tStart = t  # local t and not account for scr refresh
            rec_fx_interior_practice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rec_fx_interior_practice, 'tStartRefresh')  # time at next scr refresh
            rec_fx_interior_practice.setAutoDraw(True)
        if rec_fx_interior_practice.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > rec_fx_interior_practice.tStartRefresh + Jitter/1000-frameTolerance:
                # keep track of stop time/frame for later
                rec_fx_interior_practice.tStop = t  # not accounting for scr refresh
                rec_fx_interior_practice.frameNStop = frameN  # exact frame index
                win.timeOnFlip(rec_fx_interior_practice, 'tStopRefresh')  # time at next scr refresh
                rec_fx_interior_practice.setAutoDraw(False)
        
        # *rec_fx_cross_practice* updates
        if rec_fx_cross_practice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rec_fx_cross_practice.frameNStart = frameN  # exact frame index
            rec_fx_cross_practice.tStart = t  # local t and not account for scr refresh
            rec_fx_cross_practice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rec_fx_cross_practice, 'tStartRefresh')  # time at next scr refresh
            rec_fx_cross_practice.setAutoDraw(True)
        if rec_fx_cross_practice.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > rec_fx_cross_practice.tStartRefresh + Jitter/1000-frameTolerance:
                # keep track of stop time/frame for later
                rec_fx_cross_practice.tStop = t  # not accounting for scr refresh
                rec_fx_cross_practice.frameNStop = frameN  # exact frame index
                win.timeOnFlip(rec_fx_cross_practice, 'tStopRefresh')  # time at next scr refresh
                rec_fx_cross_practice.setAutoDraw(False)
        
        # *rec_fx_key_practice* updates
        waitOnFlip = False
        if rec_fx_key_practice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rec_fx_key_practice.frameNStart = frameN  # exact frame index
            rec_fx_key_practice.tStart = t  # local t and not account for scr refresh
            rec_fx_key_practice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rec_fx_key_practice, 'tStartRefresh')  # time at next scr refresh
            rec_fx_key_practice.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(rec_fx_key_practice.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(rec_fx_key_practice.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if rec_fx_key_practice.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > rec_fx_key_practice.tStartRefresh + Jitter/1000-frameTolerance:
                # keep track of stop time/frame for later
                rec_fx_key_practice.tStop = t  # not accounting for scr refresh
                rec_fx_key_practice.frameNStop = frameN  # exact frame index
                win.timeOnFlip(rec_fx_key_practice, 'tStopRefresh')  # time at next scr refresh
                rec_fx_key_practice.status = FINISHED
        if rec_fx_key_practice.status == STARTED and not waitOnFlip:
            theseKeys = rec_fx_key_practice.getKeys(keyList=['b', 'c', 'right', 'left'], waitRelease=False)
            _rec_fx_key_practice_allKeys.extend(theseKeys)
            if len(_rec_fx_key_practice_allKeys):
                rec_fx_key_practice.keys = _rec_fx_key_practice_allKeys[-1].name  # just the last key pressed
                rec_fx_key_practice.rt = _rec_fx_key_practice_allKeys[-1].rt
        
        # *rec_fx_text_block_practice* updates
        if rec_fx_text_block_practice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rec_fx_text_block_practice.frameNStart = frameN  # exact frame index
            rec_fx_text_block_practice.tStart = t  # local t and not account for scr refresh
            rec_fx_text_block_practice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rec_fx_text_block_practice, 'tStartRefresh')  # time at next scr refresh
            rec_fx_text_block_practice.setAutoDraw(True)
        if rec_fx_text_block_practice.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > rec_fx_text_block_practice.tStartRefresh + Jitter/1000-frameTolerance:
                # keep track of stop time/frame for later
                rec_fx_text_block_practice.tStop = t  # not accounting for scr refresh
                rec_fx_text_block_practice.frameNStop = frameN  # exact frame index
                win.timeOnFlip(rec_fx_text_block_practice, 'tStopRefresh')  # time at next scr refresh
                rec_fx_text_block_practice.setAutoDraw(False)
        
        # *rec_fx_instructions_text_practice* updates
        if rec_fx_instructions_text_practice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rec_fx_instructions_text_practice.frameNStart = frameN  # exact frame index
            rec_fx_instructions_text_practice.tStart = t  # local t and not account for scr refresh
            rec_fx_instructions_text_practice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rec_fx_instructions_text_practice, 'tStartRefresh')  # time at next scr refresh
            rec_fx_instructions_text_practice.setAutoDraw(True)
        if rec_fx_instructions_text_practice.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > rec_fx_instructions_text_practice.tStartRefresh + Jitter/1000-frameTolerance:
                # keep track of stop time/frame for later
                rec_fx_instructions_text_practice.tStop = t  # not accounting for scr refresh
                rec_fx_instructions_text_practice.frameNStop = frameN  # exact frame index
                win.timeOnFlip(rec_fx_instructions_text_practice, 'tStopRefresh')  # time at next scr refresh
                rec_fx_instructions_text_practice.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in rec_fx_practiceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "rec_fx_practice"-------
    for thisComponent in rec_fx_practiceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    rec_full_practice.addData('rec_fx_interior_practice.started', rec_fx_interior_practice.tStartRefresh)
    rec_full_practice.addData('rec_fx_interior_practice.stopped', rec_fx_interior_practice.tStopRefresh)
    rec_full_practice.addData('rec_fx_cross_practice.started', rec_fx_cross_practice.tStartRefresh)
    rec_full_practice.addData('rec_fx_cross_practice.stopped', rec_fx_cross_practice.tStopRefresh)
    # check responses
    if rec_fx_key_practice.keys in ['', [], None]:  # No response was made
        rec_fx_key_practice.keys = None
    rec_full_practice.addData('rec_fx_key_practice.keys',rec_fx_key_practice.keys)
    if rec_fx_key_practice.keys != None:  # we had a response
        rec_full_practice.addData('rec_fx_key_practice.rt', rec_fx_key_practice.rt)
    rec_full_practice.addData('rec_fx_key_practice.started', rec_fx_key_practice.tStartRefresh)
    rec_full_practice.addData('rec_fx_key_practice.stopped', rec_fx_key_practice.tStopRefresh)
    rec_full_practice.addData('rec_fx_text_block_practice.started', rec_fx_text_block_practice.tStartRefresh)
    rec_full_practice.addData('rec_fx_text_block_practice.stopped', rec_fx_text_block_practice.tStopRefresh)
    rec_full_practice.addData('rec_fx_instructions_text_practice.started', rec_fx_instructions_text_practice.tStartRefresh)
    rec_full_practice.addData('rec_fx_instructions_text_practice.stopped', rec_fx_instructions_text_practice.tStopRefresh)
    # the Routine "rec_fx_practice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "rec_trial_practice"-------
    continueRoutine = True
    routineTimer.add(4.000000)
    # update component parameters for each repeat
    rec_trial_main_image_practice.setPos((CurrentX, CurrentY))
    rec_trial_main_image_practice.setSize((0.3125, 0.3125*scr_resolution))
    rec_trial_main_image_practice.setImage(CurrentImage)
    rec_trial_key_practice.keys = []
    rec_trial_key_practice.rt = []
    _rec_trial_key_practice_allKeys = []
    rec_trial_text_block_practice.setText(block_name)
    # keep track of which components have finished
    rec_trial_practiceComponents = [rec_trial_interior_practice, rec_trial_main_image_practice, rec_trial_key_practice, rec_trial_text_block_practice, rec_trial_instructions_text_practice]
    for thisComponent in rec_trial_practiceComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    rec_trial_practiceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "rec_trial_practice"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = rec_trial_practiceClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=rec_trial_practiceClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *rec_trial_interior_practice* updates
        if rec_trial_interior_practice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rec_trial_interior_practice.frameNStart = frameN  # exact frame index
            rec_trial_interior_practice.tStart = t  # local t and not account for scr refresh
            rec_trial_interior_practice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rec_trial_interior_practice, 'tStartRefresh')  # time at next scr refresh
            rec_trial_interior_practice.setAutoDraw(True)
        if rec_trial_interior_practice.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > rec_trial_interior_practice.tStartRefresh + 4.0-frameTolerance:
                # keep track of stop time/frame for later
                rec_trial_interior_practice.tStop = t  # not accounting for scr refresh
                rec_trial_interior_practice.frameNStop = frameN  # exact frame index
                win.timeOnFlip(rec_trial_interior_practice, 'tStopRefresh')  # time at next scr refresh
                rec_trial_interior_practice.setAutoDraw(False)
        
        # *rec_trial_main_image_practice* updates
        if rec_trial_main_image_practice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rec_trial_main_image_practice.frameNStart = frameN  # exact frame index
            rec_trial_main_image_practice.tStart = t  # local t and not account for scr refresh
            rec_trial_main_image_practice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rec_trial_main_image_practice, 'tStartRefresh')  # time at next scr refresh
            rec_trial_main_image_practice.setAutoDraw(True)
        if rec_trial_main_image_practice.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > rec_trial_main_image_practice.tStartRefresh + 4.0-frameTolerance:
                # keep track of stop time/frame for later
                rec_trial_main_image_practice.tStop = t  # not accounting for scr refresh
                rec_trial_main_image_practice.frameNStop = frameN  # exact frame index
                win.timeOnFlip(rec_trial_main_image_practice, 'tStopRefresh')  # time at next scr refresh
                rec_trial_main_image_practice.setAutoDraw(False)
        
        # *rec_trial_key_practice* updates
        waitOnFlip = False
        if rec_trial_key_practice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rec_trial_key_practice.frameNStart = frameN  # exact frame index
            rec_trial_key_practice.tStart = t  # local t and not account for scr refresh
            rec_trial_key_practice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rec_trial_key_practice, 'tStartRefresh')  # time at next scr refresh
            rec_trial_key_practice.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(rec_trial_key_practice.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(rec_trial_key_practice.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if rec_trial_key_practice.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > rec_trial_key_practice.tStartRefresh + 4.0-frameTolerance:
                # keep track of stop time/frame for later
                rec_trial_key_practice.tStop = t  # not accounting for scr refresh
                rec_trial_key_practice.frameNStop = frameN  # exact frame index
                win.timeOnFlip(rec_trial_key_practice, 'tStopRefresh')  # time at next scr refresh
                rec_trial_key_practice.status = FINISHED
        if rec_trial_key_practice.status == STARTED and not waitOnFlip:
            theseKeys = rec_trial_key_practice.getKeys(keyList=['b', 'c', 'right', 'left'], waitRelease=False)
            _rec_trial_key_practice_allKeys.extend(theseKeys)
            if len(_rec_trial_key_practice_allKeys):
                rec_trial_key_practice.keys = _rec_trial_key_practice_allKeys[-1].name  # just the last key pressed
                rec_trial_key_practice.rt = _rec_trial_key_practice_allKeys[-1].rt
        
        # *rec_trial_text_block_practice* updates
        if rec_trial_text_block_practice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rec_trial_text_block_practice.frameNStart = frameN  # exact frame index
            rec_trial_text_block_practice.tStart = t  # local t and not account for scr refresh
            rec_trial_text_block_practice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rec_trial_text_block_practice, 'tStartRefresh')  # time at next scr refresh
            rec_trial_text_block_practice.setAutoDraw(True)
        if rec_trial_text_block_practice.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > rec_trial_text_block_practice.tStartRefresh + 4.0-frameTolerance:
                # keep track of stop time/frame for later
                rec_trial_text_block_practice.tStop = t  # not accounting for scr refresh
                rec_trial_text_block_practice.frameNStop = frameN  # exact frame index
                win.timeOnFlip(rec_trial_text_block_practice, 'tStopRefresh')  # time at next scr refresh
                rec_trial_text_block_practice.setAutoDraw(False)
        
        # *rec_trial_instructions_text_practice* updates
        if rec_trial_instructions_text_practice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rec_trial_instructions_text_practice.frameNStart = frameN  # exact frame index
            rec_trial_instructions_text_practice.tStart = t  # local t and not account for scr refresh
            rec_trial_instructions_text_practice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rec_trial_instructions_text_practice, 'tStartRefresh')  # time at next scr refresh
            rec_trial_instructions_text_practice.setAutoDraw(True)
        if rec_trial_instructions_text_practice.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > rec_trial_instructions_text_practice.tStartRefresh + 4.0-frameTolerance:
                # keep track of stop time/frame for later
                rec_trial_instructions_text_practice.tStop = t  # not accounting for scr refresh
                rec_trial_instructions_text_practice.frameNStop = frameN  # exact frame index
                win.timeOnFlip(rec_trial_instructions_text_practice, 'tStopRefresh')  # time at next scr refresh
                rec_trial_instructions_text_practice.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in rec_trial_practiceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "rec_trial_practice"-------
    for thisComponent in rec_trial_practiceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    rec_full_practice.addData('rec_trial_interior_practice.started', rec_trial_interior_practice.tStartRefresh)
    rec_full_practice.addData('rec_trial_interior_practice.stopped', rec_trial_interior_practice.tStopRefresh)
    rec_full_practice.addData('rec_trial_main_image_practice.started', rec_trial_main_image_practice.tStartRefresh)
    rec_full_practice.addData('rec_trial_main_image_practice.stopped', rec_trial_main_image_practice.tStopRefresh)
    # check responses
    if rec_trial_key_practice.keys in ['', [], None]:  # No response was made
        rec_trial_key_practice.keys = None
    rec_full_practice.addData('rec_trial_key_practice.keys',rec_trial_key_practice.keys)
    if rec_trial_key_practice.keys != None:  # we had a response
        rec_full_practice.addData('rec_trial_key_practice.rt', rec_trial_key_practice.rt)
    rec_full_practice.addData('rec_trial_key_practice.started', rec_trial_key_practice.tStartRefresh)
    rec_full_practice.addData('rec_trial_key_practice.stopped', rec_trial_key_practice.tStopRefresh)
    rec_full_practice.addData('rec_trial_text_block_practice.started', rec_trial_text_block_practice.tStartRefresh)
    rec_full_practice.addData('rec_trial_text_block_practice.stopped', rec_trial_text_block_practice.tStopRefresh)
    rec_full_practice.addData('rec_trial_instructions_text_practice.started', rec_trial_instructions_text_practice.tStartRefresh)
    rec_full_practice.addData('rec_trial_instructions_text_practice.stopped', rec_trial_instructions_text_practice.tStopRefresh)
    
    # ------Prepare to start Routine "rec_practice_feedback"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    correct_response = ''
    if StimType == 'FOIL':
        correct_response = 'A helyes válasz: Új'
    elif StimType == 'LURE':
        correct_response = 'A helyes válasz: Új'
    elif StimType == 'TARGET':
        correct_response = 'A helyes válasz: Régi'
    
    response = ''
    if rec_trial_key_practice.keys == 'left':
        response = 'Az Ön válasza: Régi'
    
    elif rec_trial_key_practice.keys == 'right':
        response = 'Az Ön válasza: Új'
        
    feedback_text = correct_response +'\n'+ response
    print(feedback_text)
    
    rec_practice_feedback_text.setText(feedback_text)
    # keep track of which components have finished
    rec_practice_feedbackComponents = [rec_practice_feedback_text]
    for thisComponent in rec_practice_feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    rec_practice_feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "rec_practice_feedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = rec_practice_feedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=rec_practice_feedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *rec_practice_feedback_text* updates
        if rec_practice_feedback_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rec_practice_feedback_text.frameNStart = frameN  # exact frame index
            rec_practice_feedback_text.tStart = t  # local t and not account for scr refresh
            rec_practice_feedback_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rec_practice_feedback_text, 'tStartRefresh')  # time at next scr refresh
            rec_practice_feedback_text.setAutoDraw(True)
        if rec_practice_feedback_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > rec_practice_feedback_text.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                rec_practice_feedback_text.tStop = t  # not accounting for scr refresh
                rec_practice_feedback_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(rec_practice_feedback_text, 'tStopRefresh')  # time at next scr refresh
                rec_practice_feedback_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in rec_practice_feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "rec_practice_feedback"-------
    for thisComponent in rec_practice_feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    rec_full_practice.addData('rec_practice_feedback_text.started', rec_practice_feedback_text.tStartRefresh)
    rec_full_practice.addData('rec_practice_feedback_text.stopped', rec_practice_feedback_text.tStopRefresh)
# completed 1 repeats of 'rec_full_practice'


# ------Prepare to start Routine "end_practice"-------
continueRoutine = True
routineTimer.add(600.000000)
# update component parameters for each repeat
cprint('On screen: End of practice.', 'blue', 'on_white')
cprint('Waiting for participant\'s response (d)', 'yellow')
block_counter = 0
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
        if tThisFlipGlobal > end_practice_text.tStartRefresh + 600.0-frameTolerance:
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
        if tThisFlipGlobal > end_practice_key.tStartRefresh + 599.0-frameTolerance:
            # keep track of stop time/frame for later
            end_practice_key.tStop = t  # not accounting for scr refresh
            end_practice_key.frameNStop = frameN  # exact frame index
            win.timeOnFlip(end_practice_key, 'tStopRefresh')  # time at next scr refresh
            end_practice_key.status = FINISHED
    if end_practice_key.status == STARTED and not waitOnFlip:
        theseKeys = end_practice_key.getKeys(keyList=['d', 'right', 'space'], waitRelease=False)
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
        if tThisFlipGlobal > end_practice_continue.tStartRefresh + 599.0-frameTolerance:
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
cprint('key pressed: '+ end_practice_key.keys, 'green')
print('Scanner Run loop starting with following parameters:')
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

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
