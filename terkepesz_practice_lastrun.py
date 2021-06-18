#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.4),
    on June 17, 2021, at 14:33
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

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
expName = 'TRK-online'  # from the Builder filename that created this script
expInfo = {'ID': ''}
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
    originPath='D:\\Zsuzsa\\HCCCL\\experiment\\computer_based_tasks\\mTRK\\TerKepEsz\\terkepesz_practice_lastrun.py',
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

# Initialize components for Routine "general_instructions_1"
general_instructions_1Clock = core.Clock()
general_instructions_text = visual.TextStim(win=win, name='general_instructions_text',
    text='A vizsgálat kétféle feladattípusból áll.\n\nAz első feladattípus a Galériaberendezés. Ebben a feladatban képeket kell beválogatnia egy modern művészeti galériába. \n\nA második feladattípus a Képfelismerés. Ebben a feladatban azt kell eldöntenie, a bemutatott képeket látta-e a megelőző Galériaberendezés feladat során. \n\nA vizsgálatot 6 körre osztottuk, úgy, hogy egy Képfelismerés feladatot Önnek mindig a közvetlenül megelőző Galériaberendezés feladat alapján kell elvégeznie. \n\nEgy kör 8 percet vesz igénybe, a körök között rövid (maximum 2 perces) szünetet tud tartani. A harmadik kör után tarthat egy hosszabb (maximum 10 perces) szünetet. \n\n\n\n\n\n',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
general_instructions_key = keyboard.Keyboard()
general_instructions_continue = visual.TextStim(win=win, name='general_instructions_continue',
    text='A folytatáshoz nyomja le a jobb nyilat. ',
    font='Arial',
    pos=(0, -0.4), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "general_instructions_2"
general_instructions_2Clock = core.Clock()
general_instructions_text_2 = visual.TextStim(win=win, name='general_instructions_text_2',
    text="Mindkét feladatnak két típusa van: 'Kép' és 'Hely'.\n\nGalériaberendezés:\nHa az alfeladat neve 'Kép', akkor arról kell döntést hoznia, hogy a bemutatott kép ki legyen-e állítva a következő kiállításon.\nHa az alfeladat neve 'Hely', akkor azt kell eldöntenie, a bemutatt kép az aktuálisan jelzett helyen legyen-e kiállítva.",
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
general_instructions_key_2 = keyboard.Keyboard()
general_instructions_continue_2 = visual.TextStim(win=win, name='general_instructions_continue_2',
    text='A folytatáshoz nyomja le a jobb nyilat. ',
    font='Arial',
    pos=(0, -0.4), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "general_instructions_3"
general_instructions_3Clock = core.Clock()
general_instructions_text_3 = visual.TextStim(win=win, name='general_instructions_text_3',
    text="Képfelismerés:\nHa az alfeladat neve 'Kép', akkor arra kell választ adnia, a bemutatott kép pontosan megegyezik-e a Galériaberendezés feladatban látot képek egyikével. \nHa az alfeladat neve 'Hely', akkor a képek pozíciójáról kell döntenie: a képernyő ugyanezen pontján látta korábban a bemutatott képet?\n\nA vizsgálatot 6 körre osztottuk, úgy, hogy egy Képfelismerés blokkot Önnek mindig a közvetlenül megelőző Galériaberendezés blokk alapján kell elvégeznie. \nA sorrend lehet például:\n\n'Kép' Galériaberendezés -> 'Kép' Képfelismerés\n'Hely' Galériaberendezés -> 'Hely' Képfelismerés\n",
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
general_instructions_key_3 = keyboard.Keyboard()
general_instructions_continue_3 = visual.TextStim(win=win, name='general_instructions_continue_3',
    text='Most részletesebben bemutatjuk Önnek a Galériaberendezés feladatot. \nA folytatáshoz nyomja le a jobb nyilat. ',
    font='Arial',
    pos=(0, -0.4), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "encoding_title"
encoding_titleClock = core.Clock()
encoding_title_text = visual.TextStim(win=win, name='encoding_title_text',
    text='Galéria berendezés',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "enc_instructions_1"
enc_instructions_1Clock = core.Clock()
enc_instructions_1_text = visual.TextStim(win=win, name='enc_instructions_1_text',
    text='Ön ennek a modern képgalériának a kurátora. \n\nA legújabb kiállításra a vártnál több kép érkezett.\nKurátorként az Ön feladata lesz eldönteni, mely képeket válogatjuk be a kiállított darabok közé, és hogy a mások által beválogatott képek illeszkednek-e a galéria adott pontjára.\n\nAz Ön ideje nagyon drága a galériának, így a döntésre egy-egy képről csak 3 másodperce lesz.',
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
    text='A folytatáshoz nyomja le a jobb nyilat. ',
    font='Arial',
    pos=(0, -0.4), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "enc_instructions_2"
enc_instructions_2Clock = core.Clock()
enc_instructions_2_text = visual.TextStim(win=win, name='enc_instructions_2_text',
    text="Ez a kiállítóterem, nézze meg figyelmesen. \n\nA feladat során a képek a falra vetítve jelennek meg. A képek előtt egy keresztet fog látni, ami jelzi a képek pontos helyét.\n\nA 'Kép' nevű alfeladat alatt döntse el a képekről, hogy ki legyenek-e állítva a galériában. \n\nA beválogatott képek száma nincsen korlátozva. Minden egyes képről Ön dönt. \n\nHa több képet válogat be, mint amennyi a galériába fér, akkor a képeket az év során felváltva állítjuk ki.\n",
    font='Arial',
    pos=(-0.35, 0), height=0.03, wrapWidth=0.52, ori=0, 
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
    text='A folytatáshoz nyomja le a jobb nyilat. ',
    font='Arial',
    pos=(0,-0.4), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "enc_instructions_3"
enc_instructions_3Clock = core.Clock()
enc_instructions_2_text_2 = visual.TextStim(win=win, name='enc_instructions_2_text_2',
    text="A 'Hely' nevű alfeladat alatt azt döntse el, a bemutatott kép maradhat-e a galéria adott pontján.\nEzeket a képeket mindenképp kiállítjuk, itt csak a képek helyéről tud dönteni. \n\nMinden képet nézzen meg figyelmesen, és minden képre adjon választ. ",
    font='Arial',
    pos=(-0.35, 0), height=0.03, wrapWidth=0.52, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
enc_instructions_2_image_2 = visual.ImageStim(
    win=win,
    name='enc_instructions_2_image_2', units='norm', 
    image='stimuli/GalleryInterior.png', mask=None,
    ori=0, pos=(0.4427, 0), size=(0.7604, 0.8185),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
enc_instructions_2_key_2 = keyboard.Keyboard()
instructions_2_continue_2 = visual.TextStim(win=win, name='instructions_2_continue_2',
    text='A folytatáshoz nyomja le a jobb nyilat. ',
    font='Arial',
    pos=(0,-0.4), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "enc_instructions_4"
enc_instructions_4Clock = core.Clock()
enc_instructions_3_text = visual.TextStim(win=win, name='enc_instructions_3_text',
    text="A 'Kép' alfeladat alatt a 'J' billentyűvel jelölje azokat a képeket, amelyeket beválogat a kiállításra. \n\nAz 'F' billentyűvel jelölje a képeket, amelyeket nem válogat be a kiállításra.\n\n\nA 'Hely' nevű alfeladatban a 'J' billentyűvel jelölje azokat a képeket, amelyek maradhatnak a galéria adott pontján. \n\nAz 'F' billentyűvel jelölje a képeket, amelyek nem maradhatnak a galéria adott pontján.\n\nMost a Galériaberendezés gyakorlása következik. \n",
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
enc_instructions_3_key = keyboard.Keyboard()
enc_instructions_3_continue = visual.TextStim(win=win, name='enc_instructions_3_continue',
    text='Ha készen áll a gyakorlásra, nyomja le a jobb nyilat.',
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

# Initialize components for Routine "encoding_title"
encoding_titleClock = core.Clock()
encoding_title_text = visual.TextStim(win=win, name='encoding_title_text',
    text='Galéria berendezés',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "practice_block_start"
practice_block_startClock = core.Clock()
practice_end = 0
step = 1

start_practice_block = visual.TextStim(win=win, name='start_practice_block',
    text='',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "enc_fx_practice"
enc_fx_practiceClock = core.Clock()
w_size = win.size

x_size = w_size[0]
y_size = w_size[1]

scr_resolution = x_size/y_size
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
    units='norm', pos=(0, 0.87), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
enc_fx_instructions_text_practice = visual.TextStim(win=win, name='enc_fx_instructions_text_practice',
    text='[F - Nem marad]      [J - Marad]',
    font='Arial',
    units='norm', pos=(0, -0.833), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);

# Initialize components for Routine "enc_trial_practice"
enc_trial_practiceClock = core.Clock()
w_size = win.size

x_size = w_size[0]
y_size = w_size[1]

scr_resolution = x_size/y_size
enc_trial_interior_practice = visual.ImageStim(
    win=win,
    name='enc_trial_interior_practice', units='norm', 
    image='stimuli/GalleryInterior.png', mask=None,
    ori=0, pos=(0, -0), size=(2.0, 2.0),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
enc_trial_main_image_practice = visual.ImageStim(
    win=win,
    name='enc_trial_main_image_practice', units='norm', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
enc_trial_key_practice = keyboard.Keyboard()
enc_trial_text_block_practice = visual.TextStim(win=win, name='enc_trial_text_block_practice',
    text='',
    font='Arial',
    units='norm', pos=(0, 0.87), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
enc_trial_instructions_text_practice = visual.TextStim(win=win, name='enc_trial_instructions_text_practice',
    text='[F - Nem marad]      [J - Marad]',
    font='Arial',
    units='norm', pos=(0, -0.833), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);

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
    units='norm', pos=(0, 0.87), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "end_practice"
end_practiceClock = core.Clock()
end_practice_text = visual.TextStim(win=win, name='end_practice_text',
    text='Ez volt a gyakorlás.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=0.8, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
end_practice_key = keyboard.Keyboard()
end_practice_continue = visual.TextStim(win=win, name='end_practice_continue',
    text='A folytatáshoz nyomja le a jobb nyilat. ',
    font='Arial',
    pos=(0,-0.4), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
coming_up_next_text = visual.TextStim(win=win, name='coming_up_next_text',
    text='',
    font='Arial',
    pos=(0, -0.2), height=0.05, wrapWidth=None, ori=0, 
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
    depth=0.0);

# Initialize components for Routine "rec_instructions_1"
rec_instructions_1Clock = core.Clock()
rec_instructions_1_text = visual.TextStim(win=win, name='rec_instructions_1_text',
    text='A Képfelismerés feladatban ismét absztrakt képeket fog látni, és ezekről kell eldöntenie, látta-e őket a megelőző Galériaberendezés feladataban, és hogy ugyanott látta-e őket.\n\nA feladatot két alfeladatra bontottuk. Az egyikben a képekről, a másikban a képek pozíciójáról kell döntenie.',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
rec_instructions_1_key = keyboard.Keyboard()
rec_instructions_1_continue = visual.TextStim(win=win, name='rec_instructions_1_continue',
    text='A folytatáshoz nyomja le a jobb nyilat. ',
    font='Arial',
    pos=(0,-0.4), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "rec_instructions_2"
rec_instructions_2Clock = core.Clock()
rec_instructions2_text = visual.TextStim(win=win, name='rec_instructions2_text',
    text="A 'Kép' nevű alfeladatban azt kell eldöntenie, látta-e már ezeket a képeket a megelőző Galériaberendezés blokkban.\n\nKét csoportba oszthatóak a megjelenő képek:\n - Régi: Ezek a képek pontosan megegyeznek a 'Galériaberendezés' megelőző sorozatában látott képek egyikével.\n - Új: Képek, amelyek nem jelentek meg a 'Galériaberendezés' feladatban. Ezek a képek lehetnek hasonlóak a korábban látottakhoz.\n\nAz Ön feladata, hogy eldöntse, melyik kép ugyanaz, mint a 'Galéria berendezés' feladatban, és melyik új. \nA döntésre 4 másodperce lesz.\nMinden képet nézzen meg figyelmesen, és minden képre adjon választ, akkor is, ha a döntés nehéz.\n\nDöntését így jelölje:\nRégi - F\nÚj - J",
    font='Arial',
    pos=(0, 0), height=0.025, wrapWidth=1, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
rec_instructions_2_key = keyboard.Keyboard()
rec_instructions_2_continue = visual.TextStim(win=win, name='rec_instructions_2_continue',
    text='A folytatáshoz nyomja le a jobb nyilat. ',
    font='Arial',
    pos=(0,-0.4), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
rec_instruction_2_title = visual.TextStim(win=win, name='rec_instruction_2_title',
    text="'Kép' alfeladat",
    font='Arial',
    pos=(0, 0.4), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "rec_instructions_3"
rec_instructions_3Clock = core.Clock()
rec_instrauction_3_text = visual.TextStim(win=win, name='rec_instrauction_3_text',
    text="A 'Hely' nevű alfeladatban azt kell eldöntenie, a képek a képernyő ugyanazon pontján jelennek-e meg, mint a megelőző Galériaberendezés sorozatban.\nEbben az alfeladatban minden kép pontos mása annak, amit a Galériaberendezés alatt látott. \n\nA helyek azonban két csoportba oszthatóak:\n - Régi: Pontosan ugyanitt jelent meg ez a kép a Galériaberendezés feladatban.\n - Új: Egy másik helyen jelent meg ez a kép a Galériaberendezés feladatban. Ez a hely lehet közeli az eredeti helyhez.\n\nAz Ön feladata, hogy eldöntse, melyik kép jelent meg ugyanott, és melyik új helyen.\nA döntésre 4 másodperce lesz.\nMinden képet nézzen meg figyelmesen, és minden képre adjon választ, akkor is, ha a döntés nehéz.\n\nA döntését így jelölje:\nRégi - F\nÚj - J",
    font='Arial',
    pos=(0, 0), height=0.025, wrapWidth=1, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
rec_instructions_3_key = keyboard.Keyboard()
rec_instructions_3_continue = visual.TextStim(win=win, name='rec_instructions_3_continue',
    text='A folytatáshoz nyomja le a jobb nyilat. ',
    font='Arial',
    pos=(0,-0.4), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
rec_instruction_3_title = visual.TextStim(win=win, name='rec_instruction_3_title',
    text="'Hely' alfeladat",
    font='Arial',
    pos=(0, 0.4), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "rec_instructions_4"
rec_instructions_4Clock = core.Clock()
rec_instructions_4_text = visual.TextStim(win=win, name='rec_instructions_4_text',
    text="A következőkben pár példával mutatjuk be Önnek, milyen hasonlóak lehetnek az új képek és helyek.\n\nA bemutatóban elsőként egy, a Galériaberendezés gyakorlása során már látott képet/helyet mutatunk Önnek, 'Régi' felirattal. \nA régi képet/helyet mindig egy új kép/hely követi a bemutatóban, 'Új' felirattal.\n",
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
rec_instructions_4_key = keyboard.Keyboard()
rec_instructions_4_continue = visual.TextStim(win=win, name='rec_instructions_4_continue',
    text='A folytatáshoz nyomja le a jobb nyilat. ',
    font='Arial',
    pos=(0,-0.4), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "demo_start"
demo_startClock = core.Clock()
demo_start_text = visual.TextStim(win=win, name='demo_start_text',
    text='Kezdődik a bemutató...',
    font='Arial',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "demo"
demoClock = core.Clock()
demo_interior = visual.ImageStim(
    win=win,
    name='demo_interior', units='norm', 
    image='stimuli/GalleryInterior.png', mask=None,
    ori=0, pos=(0, -0), size=(2.0, 2.0),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
demo_main_image = visual.ImageStim(
    win=win,
    name='demo_main_image', units='norm', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
demo_image = visual.ImageStim(
    win=win,
    name='demo_image', units='norm', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
demo_text = visual.TextStim(win=win, name='demo_text',
    text='',
    font='Arial',
    pos=(-0.025, 0.45), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
demo_key = keyboard.Keyboard()
demo_continue = visual.TextStim(win=win, name='demo_continue',
    text='A folytatáshoz nyomja le a jobb nyilat. ',
    font='Arial',
    pos=(0,-0.4), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);

# Initialize components for Routine "demo_end"
demo_endClock = core.Clock()
demo_end_text = visual.TextStim(win=win, name='demo_end_text',
    text='Ez volt a bemutató. Most a Képfelismerés gyakorlása következik.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
demo_end_key = keyboard.Keyboard()
demo_end_continue = visual.TextStim(win=win, name='demo_end_continue',
    text='A folytatáshoz nyomja le a jobb nyilat. ',
    font='Arial',
    pos=(0,-0.4), height=0.03, wrapWidth=None, ori=0, 
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
practice_end = 0
step = 1

start_practice_block = visual.TextStim(win=win, name='start_practice_block',
    text='',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "rec_fx_practice"
rec_fx_practiceClock = core.Clock()
w_size = win.size

x_size = w_size[0]
y_size = w_size[1]

scr_resolution = x_size/y_size
rec_fx_interior_practice = visual.ImageStim(
    win=win,
    name='rec_fx_interior_practice', units='norm', 
    image='stimuli/GalleryInterior.png', mask=None,
    ori=0, pos=(0,0), size=(2.0, 2.0),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
rec_fx_cross_practice = visual.TextStim(win=win, name='rec_fx_cross_practice',
    text='+',
    font='Arial',
    units='norm', pos=[0,0], height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
rec_fx_key_practice = keyboard.Keyboard()
rec_fx_text_block_practice = visual.TextStim(win=win, name='rec_fx_text_block_practice',
    text='',
    font='Arial',
    units='norm', pos=(0, 0.87), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
rec_fx_instructions_text_practice = visual.TextStim(win=win, name='rec_fx_instructions_text_practice',
    text='[F - Régi]      [J - Új]',
    font='Arial',
    units='norm', pos=(0, -0.833), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);

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
    depth=0.0);
end_practice_key = keyboard.Keyboard()
end_practice_continue = visual.TextStim(win=win, name='end_practice_continue',
    text='A folytatáshoz nyomja le a jobb nyilat. ',
    font='Arial',
    pos=(0,-0.4), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
coming_up_next_text = visual.TextStim(win=win, name='coming_up_next_text',
    text='',
    font='Arial',
    pos=(0, -0.2), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

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
practice_end = 0
step = 1

start_practice_block = visual.TextStim(win=win, name='start_practice_block',
    text='',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "enc_fx_practice"
enc_fx_practiceClock = core.Clock()
w_size = win.size

x_size = w_size[0]
y_size = w_size[1]

scr_resolution = x_size/y_size
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
    units='norm', pos=(0, 0.87), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
enc_fx_instructions_text_practice = visual.TextStim(win=win, name='enc_fx_instructions_text_practice',
    text='[F - Nem marad]      [J - Marad]',
    font='Arial',
    units='norm', pos=(0, -0.833), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);

# Initialize components for Routine "enc_trial_practice"
enc_trial_practiceClock = core.Clock()
w_size = win.size

x_size = w_size[0]
y_size = w_size[1]

scr_resolution = x_size/y_size
enc_trial_interior_practice = visual.ImageStim(
    win=win,
    name='enc_trial_interior_practice', units='norm', 
    image='stimuli/GalleryInterior.png', mask=None,
    ori=0, pos=(0, -0), size=(2.0, 2.0),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
enc_trial_main_image_practice = visual.ImageStim(
    win=win,
    name='enc_trial_main_image_practice', units='norm', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
enc_trial_key_practice = keyboard.Keyboard()
enc_trial_text_block_practice = visual.TextStim(win=win, name='enc_trial_text_block_practice',
    text='',
    font='Arial',
    units='norm', pos=(0, 0.87), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
enc_trial_instructions_text_practice = visual.TextStim(win=win, name='enc_trial_instructions_text_practice',
    text='[F - Nem marad]      [J - Marad]',
    font='Arial',
    units='norm', pos=(0, -0.833), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);

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
    units='norm', pos=(0, 0.87), height=0.05, wrapWidth=None, ori=0, 
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
    depth=0.0);

# Initialize components for Routine "block_title"
block_titleClock = core.Clock()
block_title_text = visual.TextStim(win=win, name='block_title_text',
    text='',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "rec_fx_practice"
rec_fx_practiceClock = core.Clock()
w_size = win.size

x_size = w_size[0]
y_size = w_size[1]

scr_resolution = x_size/y_size
rec_fx_interior_practice = visual.ImageStim(
    win=win,
    name='rec_fx_interior_practice', units='norm', 
    image='stimuli/GalleryInterior.png', mask=None,
    ori=0, pos=(0,0), size=(2.0, 2.0),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
rec_fx_cross_practice = visual.TextStim(win=win, name='rec_fx_cross_practice',
    text='+',
    font='Arial',
    units='norm', pos=[0,0], height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
rec_fx_key_practice = keyboard.Keyboard()
rec_fx_text_block_practice = visual.TextStim(win=win, name='rec_fx_text_block_practice',
    text='',
    font='Arial',
    units='norm', pos=(0, 0.87), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
rec_fx_instructions_text_practice = visual.TextStim(win=win, name='rec_fx_instructions_text_practice',
    text='[F - Régi]      [J - Új]',
    font='Arial',
    units='norm', pos=(0, -0.833), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);

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
    depth=0.0);
end_practice_key = keyboard.Keyboard()
end_practice_continue = visual.TextStim(win=win, name='end_practice_continue',
    text='A folytatáshoz nyomja le a jobb nyilat. ',
    font='Arial',
    pos=(0,-0.4), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
coming_up_next_text = visual.TextStim(win=win, name='coming_up_next_text',
    text='',
    font='Arial',
    pos=(0, -0.2), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "general_instructions_1"-------
continueRoutine = True
routineTimer.add(300.000000)
# update component parameters for each repeat
general_instructions_key.keys = []
general_instructions_key.rt = []
_general_instructions_key_allKeys = []
# keep track of which components have finished
general_instructions_1Components = [general_instructions_text, general_instructions_key, general_instructions_continue]
for thisComponent in general_instructions_1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
general_instructions_1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "general_instructions_1"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = general_instructions_1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=general_instructions_1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
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
    
    # *general_instructions_key* updates
    waitOnFlip = False
    if general_instructions_key.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
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
        if tThisFlipGlobal > general_instructions_key.tStartRefresh + 290.0-frameTolerance:
            # keep track of stop time/frame for later
            general_instructions_key.tStop = t  # not accounting for scr refresh
            general_instructions_key.frameNStop = frameN  # exact frame index
            win.timeOnFlip(general_instructions_key, 'tStopRefresh')  # time at next scr refresh
            general_instructions_key.status = FINISHED
    if general_instructions_key.status == STARTED and not waitOnFlip:
        theseKeys = general_instructions_key.getKeys(keyList=['right'], waitRelease=False)
        _general_instructions_key_allKeys.extend(theseKeys)
        if len(_general_instructions_key_allKeys):
            general_instructions_key.keys = _general_instructions_key_allKeys[-1].name  # just the last key pressed
            general_instructions_key.rt = _general_instructions_key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *general_instructions_continue* updates
    if general_instructions_continue.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
        # keep track of start time/frame for later
        general_instructions_continue.frameNStart = frameN  # exact frame index
        general_instructions_continue.tStart = t  # local t and not account for scr refresh
        general_instructions_continue.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(general_instructions_continue, 'tStartRefresh')  # time at next scr refresh
        general_instructions_continue.setAutoDraw(True)
    if general_instructions_continue.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > general_instructions_continue.tStartRefresh + 290.0-frameTolerance:
            # keep track of stop time/frame for later
            general_instructions_continue.tStop = t  # not accounting for scr refresh
            general_instructions_continue.frameNStop = frameN  # exact frame index
            win.timeOnFlip(general_instructions_continue, 'tStopRefresh')  # time at next scr refresh
            general_instructions_continue.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in general_instructions_1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "general_instructions_1"-------
for thisComponent in general_instructions_1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('general_instructions_text.started', general_instructions_text.tStartRefresh)
thisExp.addData('general_instructions_text.stopped', general_instructions_text.tStopRefresh)
# check responses
if general_instructions_key.keys in ['', [], None]:  # No response was made
    general_instructions_key.keys = None
thisExp.addData('general_instructions_key.keys',general_instructions_key.keys)
if general_instructions_key.keys != None:  # we had a response
    thisExp.addData('general_instructions_key.rt', general_instructions_key.rt)
thisExp.addData('general_instructions_key.started', general_instructions_key.tStartRefresh)
thisExp.addData('general_instructions_key.stopped', general_instructions_key.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('general_instructions_continue.started', general_instructions_continue.tStartRefresh)
thisExp.addData('general_instructions_continue.stopped', general_instructions_continue.tStopRefresh)

# ------Prepare to start Routine "general_instructions_2"-------
continueRoutine = True
routineTimer.add(300.000000)
# update component parameters for each repeat
general_instructions_key_2.keys = []
general_instructions_key_2.rt = []
_general_instructions_key_2_allKeys = []
# keep track of which components have finished
general_instructions_2Components = [general_instructions_text_2, general_instructions_key_2, general_instructions_continue_2]
for thisComponent in general_instructions_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
general_instructions_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "general_instructions_2"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = general_instructions_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=general_instructions_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *general_instructions_text_2* updates
    if general_instructions_text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        general_instructions_text_2.frameNStart = frameN  # exact frame index
        general_instructions_text_2.tStart = t  # local t and not account for scr refresh
        general_instructions_text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(general_instructions_text_2, 'tStartRefresh')  # time at next scr refresh
        general_instructions_text_2.setAutoDraw(True)
    if general_instructions_text_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > general_instructions_text_2.tStartRefresh + 300.0-frameTolerance:
            # keep track of stop time/frame for later
            general_instructions_text_2.tStop = t  # not accounting for scr refresh
            general_instructions_text_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(general_instructions_text_2, 'tStopRefresh')  # time at next scr refresh
            general_instructions_text_2.setAutoDraw(False)
    
    # *general_instructions_key_2* updates
    waitOnFlip = False
    if general_instructions_key_2.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
        # keep track of start time/frame for later
        general_instructions_key_2.frameNStart = frameN  # exact frame index
        general_instructions_key_2.tStart = t  # local t and not account for scr refresh
        general_instructions_key_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(general_instructions_key_2, 'tStartRefresh')  # time at next scr refresh
        general_instructions_key_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(general_instructions_key_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(general_instructions_key_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if general_instructions_key_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > general_instructions_key_2.tStartRefresh + 290.0-frameTolerance:
            # keep track of stop time/frame for later
            general_instructions_key_2.tStop = t  # not accounting for scr refresh
            general_instructions_key_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(general_instructions_key_2, 'tStopRefresh')  # time at next scr refresh
            general_instructions_key_2.status = FINISHED
    if general_instructions_key_2.status == STARTED and not waitOnFlip:
        theseKeys = general_instructions_key_2.getKeys(keyList=['right'], waitRelease=False)
        _general_instructions_key_2_allKeys.extend(theseKeys)
        if len(_general_instructions_key_2_allKeys):
            general_instructions_key_2.keys = _general_instructions_key_2_allKeys[-1].name  # just the last key pressed
            general_instructions_key_2.rt = _general_instructions_key_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *general_instructions_continue_2* updates
    if general_instructions_continue_2.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
        # keep track of start time/frame for later
        general_instructions_continue_2.frameNStart = frameN  # exact frame index
        general_instructions_continue_2.tStart = t  # local t and not account for scr refresh
        general_instructions_continue_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(general_instructions_continue_2, 'tStartRefresh')  # time at next scr refresh
        general_instructions_continue_2.setAutoDraw(True)
    if general_instructions_continue_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > general_instructions_continue_2.tStartRefresh + 290.0-frameTolerance:
            # keep track of stop time/frame for later
            general_instructions_continue_2.tStop = t  # not accounting for scr refresh
            general_instructions_continue_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(general_instructions_continue_2, 'tStopRefresh')  # time at next scr refresh
            general_instructions_continue_2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in general_instructions_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "general_instructions_2"-------
for thisComponent in general_instructions_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('general_instructions_text_2.started', general_instructions_text_2.tStartRefresh)
thisExp.addData('general_instructions_text_2.stopped', general_instructions_text_2.tStopRefresh)
# check responses
if general_instructions_key_2.keys in ['', [], None]:  # No response was made
    general_instructions_key_2.keys = None
thisExp.addData('general_instructions_key_2.keys',general_instructions_key_2.keys)
if general_instructions_key_2.keys != None:  # we had a response
    thisExp.addData('general_instructions_key_2.rt', general_instructions_key_2.rt)
thisExp.addData('general_instructions_key_2.started', general_instructions_key_2.tStartRefresh)
thisExp.addData('general_instructions_key_2.stopped', general_instructions_key_2.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('general_instructions_continue_2.started', general_instructions_continue_2.tStartRefresh)
thisExp.addData('general_instructions_continue_2.stopped', general_instructions_continue_2.tStopRefresh)

# ------Prepare to start Routine "general_instructions_3"-------
continueRoutine = True
routineTimer.add(300.000000)
# update component parameters for each repeat
general_instructions_key_3.keys = []
general_instructions_key_3.rt = []
_general_instructions_key_3_allKeys = []
# keep track of which components have finished
general_instructions_3Components = [general_instructions_text_3, general_instructions_key_3, general_instructions_continue_3]
for thisComponent in general_instructions_3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
general_instructions_3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "general_instructions_3"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = general_instructions_3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=general_instructions_3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *general_instructions_text_3* updates
    if general_instructions_text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        general_instructions_text_3.frameNStart = frameN  # exact frame index
        general_instructions_text_3.tStart = t  # local t and not account for scr refresh
        general_instructions_text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(general_instructions_text_3, 'tStartRefresh')  # time at next scr refresh
        general_instructions_text_3.setAutoDraw(True)
    if general_instructions_text_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > general_instructions_text_3.tStartRefresh + 300.0-frameTolerance:
            # keep track of stop time/frame for later
            general_instructions_text_3.tStop = t  # not accounting for scr refresh
            general_instructions_text_3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(general_instructions_text_3, 'tStopRefresh')  # time at next scr refresh
            general_instructions_text_3.setAutoDraw(False)
    
    # *general_instructions_key_3* updates
    waitOnFlip = False
    if general_instructions_key_3.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
        # keep track of start time/frame for later
        general_instructions_key_3.frameNStart = frameN  # exact frame index
        general_instructions_key_3.tStart = t  # local t and not account for scr refresh
        general_instructions_key_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(general_instructions_key_3, 'tStartRefresh')  # time at next scr refresh
        general_instructions_key_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(general_instructions_key_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(general_instructions_key_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if general_instructions_key_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > general_instructions_key_3.tStartRefresh + 290.0-frameTolerance:
            # keep track of stop time/frame for later
            general_instructions_key_3.tStop = t  # not accounting for scr refresh
            general_instructions_key_3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(general_instructions_key_3, 'tStopRefresh')  # time at next scr refresh
            general_instructions_key_3.status = FINISHED
    if general_instructions_key_3.status == STARTED and not waitOnFlip:
        theseKeys = general_instructions_key_3.getKeys(keyList=['right'], waitRelease=False)
        _general_instructions_key_3_allKeys.extend(theseKeys)
        if len(_general_instructions_key_3_allKeys):
            general_instructions_key_3.keys = _general_instructions_key_3_allKeys[-1].name  # just the last key pressed
            general_instructions_key_3.rt = _general_instructions_key_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *general_instructions_continue_3* updates
    if general_instructions_continue_3.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
        # keep track of start time/frame for later
        general_instructions_continue_3.frameNStart = frameN  # exact frame index
        general_instructions_continue_3.tStart = t  # local t and not account for scr refresh
        general_instructions_continue_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(general_instructions_continue_3, 'tStartRefresh')  # time at next scr refresh
        general_instructions_continue_3.setAutoDraw(True)
    if general_instructions_continue_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > general_instructions_continue_3.tStartRefresh + 290.0-frameTolerance:
            # keep track of stop time/frame for later
            general_instructions_continue_3.tStop = t  # not accounting for scr refresh
            general_instructions_continue_3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(general_instructions_continue_3, 'tStopRefresh')  # time at next scr refresh
            general_instructions_continue_3.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in general_instructions_3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "general_instructions_3"-------
for thisComponent in general_instructions_3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('general_instructions_text_3.started', general_instructions_text_3.tStartRefresh)
thisExp.addData('general_instructions_text_3.stopped', general_instructions_text_3.tStopRefresh)
# check responses
if general_instructions_key_3.keys in ['', [], None]:  # No response was made
    general_instructions_key_3.keys = None
thisExp.addData('general_instructions_key_3.keys',general_instructions_key_3.keys)
if general_instructions_key_3.keys != None:  # we had a response
    thisExp.addData('general_instructions_key_3.rt', general_instructions_key_3.rt)
thisExp.addData('general_instructions_key_3.started', general_instructions_key_3.tStartRefresh)
thisExp.addData('general_instructions_key_3.stopped', general_instructions_key_3.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('general_instructions_continue_3.started', general_instructions_continue_3.tStartRefresh)
thisExp.addData('general_instructions_continue_3.stopped', general_instructions_continue_3.tStopRefresh)

# ------Prepare to start Routine "encoding_title"-------
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
encoding_titleComponents = [encoding_title_text]
for thisComponent in encoding_titleComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
encoding_titleClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "encoding_title"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = encoding_titleClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=encoding_titleClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *encoding_title_text* updates
    if encoding_title_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        encoding_title_text.frameNStart = frameN  # exact frame index
        encoding_title_text.tStart = t  # local t and not account for scr refresh
        encoding_title_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(encoding_title_text, 'tStartRefresh')  # time at next scr refresh
        encoding_title_text.setAutoDraw(True)
    if encoding_title_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > encoding_title_text.tStartRefresh + 2.0-frameTolerance:
            # keep track of stop time/frame for later
            encoding_title_text.tStop = t  # not accounting for scr refresh
            encoding_title_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(encoding_title_text, 'tStopRefresh')  # time at next scr refresh
            encoding_title_text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in encoding_titleComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "encoding_title"-------
for thisComponent in encoding_titleComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('encoding_title_text.started', encoding_title_text.tStartRefresh)
thisExp.addData('encoding_title_text.stopped', encoding_title_text.tStopRefresh)

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
        theseKeys = enc_instructions_1_key.getKeys(keyList=['right'], waitRelease=False)
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
        theseKeys = enc_instructions_2_key.getKeys(keyList=['right'], waitRelease=False)
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
enc_instructions_2_key_2.keys = []
enc_instructions_2_key_2.rt = []
_enc_instructions_2_key_2_allKeys = []
# keep track of which components have finished
enc_instructions_3Components = [enc_instructions_2_text_2, enc_instructions_2_image_2, enc_instructions_2_key_2, instructions_2_continue_2]
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
    
    # *enc_instructions_2_text_2* updates
    if enc_instructions_2_text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        enc_instructions_2_text_2.frameNStart = frameN  # exact frame index
        enc_instructions_2_text_2.tStart = t  # local t and not account for scr refresh
        enc_instructions_2_text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(enc_instructions_2_text_2, 'tStartRefresh')  # time at next scr refresh
        enc_instructions_2_text_2.setAutoDraw(True)
    if enc_instructions_2_text_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > enc_instructions_2_text_2.tStartRefresh + 300.0-frameTolerance:
            # keep track of stop time/frame for later
            enc_instructions_2_text_2.tStop = t  # not accounting for scr refresh
            enc_instructions_2_text_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(enc_instructions_2_text_2, 'tStopRefresh')  # time at next scr refresh
            enc_instructions_2_text_2.setAutoDraw(False)
    
    # *enc_instructions_2_image_2* updates
    if enc_instructions_2_image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        enc_instructions_2_image_2.frameNStart = frameN  # exact frame index
        enc_instructions_2_image_2.tStart = t  # local t and not account for scr refresh
        enc_instructions_2_image_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(enc_instructions_2_image_2, 'tStartRefresh')  # time at next scr refresh
        enc_instructions_2_image_2.setAutoDraw(True)
    if enc_instructions_2_image_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > enc_instructions_2_image_2.tStartRefresh + 300.0-frameTolerance:
            # keep track of stop time/frame for later
            enc_instructions_2_image_2.tStop = t  # not accounting for scr refresh
            enc_instructions_2_image_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(enc_instructions_2_image_2, 'tStopRefresh')  # time at next scr refresh
            enc_instructions_2_image_2.setAutoDraw(False)
    
    # *enc_instructions_2_key_2* updates
    waitOnFlip = False
    if enc_instructions_2_key_2.status == NOT_STARTED and tThisFlip >= 5.0-frameTolerance:
        # keep track of start time/frame for later
        enc_instructions_2_key_2.frameNStart = frameN  # exact frame index
        enc_instructions_2_key_2.tStart = t  # local t and not account for scr refresh
        enc_instructions_2_key_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(enc_instructions_2_key_2, 'tStartRefresh')  # time at next scr refresh
        enc_instructions_2_key_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(enc_instructions_2_key_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(enc_instructions_2_key_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if enc_instructions_2_key_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > enc_instructions_2_key_2.tStartRefresh + 295.0-frameTolerance:
            # keep track of stop time/frame for later
            enc_instructions_2_key_2.tStop = t  # not accounting for scr refresh
            enc_instructions_2_key_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(enc_instructions_2_key_2, 'tStopRefresh')  # time at next scr refresh
            enc_instructions_2_key_2.status = FINISHED
    if enc_instructions_2_key_2.status == STARTED and not waitOnFlip:
        theseKeys = enc_instructions_2_key_2.getKeys(keyList=['right'], waitRelease=False)
        _enc_instructions_2_key_2_allKeys.extend(theseKeys)
        if len(_enc_instructions_2_key_2_allKeys):
            enc_instructions_2_key_2.keys = _enc_instructions_2_key_2_allKeys[-1].name  # just the last key pressed
            enc_instructions_2_key_2.rt = _enc_instructions_2_key_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *instructions_2_continue_2* updates
    if instructions_2_continue_2.status == NOT_STARTED and tThisFlip >= 5.0-frameTolerance:
        # keep track of start time/frame for later
        instructions_2_continue_2.frameNStart = frameN  # exact frame index
        instructions_2_continue_2.tStart = t  # local t and not account for scr refresh
        instructions_2_continue_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions_2_continue_2, 'tStartRefresh')  # time at next scr refresh
        instructions_2_continue_2.setAutoDraw(True)
    if instructions_2_continue_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > instructions_2_continue_2.tStartRefresh + 295.0-frameTolerance:
            # keep track of stop time/frame for later
            instructions_2_continue_2.tStop = t  # not accounting for scr refresh
            instructions_2_continue_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(instructions_2_continue_2, 'tStopRefresh')  # time at next scr refresh
            instructions_2_continue_2.setAutoDraw(False)
    
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
thisExp.addData('enc_instructions_2_text_2.started', enc_instructions_2_text_2.tStartRefresh)
thisExp.addData('enc_instructions_2_text_2.stopped', enc_instructions_2_text_2.tStopRefresh)
thisExp.addData('enc_instructions_2_image_2.started', enc_instructions_2_image_2.tStartRefresh)
thisExp.addData('enc_instructions_2_image_2.stopped', enc_instructions_2_image_2.tStopRefresh)
# check responses
if enc_instructions_2_key_2.keys in ['', [], None]:  # No response was made
    enc_instructions_2_key_2.keys = None
thisExp.addData('enc_instructions_2_key_2.keys',enc_instructions_2_key_2.keys)
if enc_instructions_2_key_2.keys != None:  # we had a response
    thisExp.addData('enc_instructions_2_key_2.rt', enc_instructions_2_key_2.rt)
thisExp.addData('enc_instructions_2_key_2.started', enc_instructions_2_key_2.tStartRefresh)
thisExp.addData('enc_instructions_2_key_2.stopped', enc_instructions_2_key_2.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('instructions_2_continue_2.started', instructions_2_continue_2.tStartRefresh)
thisExp.addData('instructions_2_continue_2.stopped', instructions_2_continue_2.tStopRefresh)

# ------Prepare to start Routine "enc_instructions_4"-------
continueRoutine = True
routineTimer.add(300.000000)
# update component parameters for each repeat
enc_instructions_3_key.keys = []
enc_instructions_3_key.rt = []
_enc_instructions_3_key_allKeys = []
# keep track of which components have finished
enc_instructions_4Components = [enc_instructions_3_text, enc_instructions_3_key, enc_instructions_3_continue]
for thisComponent in enc_instructions_4Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
enc_instructions_4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "enc_instructions_4"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = enc_instructions_4Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=enc_instructions_4Clock)
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
        theseKeys = enc_instructions_3_key.getKeys(keyList=['right'], waitRelease=False)
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
    for thisComponent in enc_instructions_4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "enc_instructions_4"-------
for thisComponent in enc_instructions_4Components:
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
coming_up_text='Most a Képfelismerés feladat bemutatása következik.'

# ------Prepare to start Routine "start_practice"-------
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
practice_start = 0
practice_end = 0
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

# ------Prepare to start Routine "encoding_title"-------
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
encoding_titleComponents = [encoding_title_text]
for thisComponent in encoding_titleComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
encoding_titleClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "encoding_title"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = encoding_titleClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=encoding_titleClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *encoding_title_text* updates
    if encoding_title_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        encoding_title_text.frameNStart = frameN  # exact frame index
        encoding_title_text.tStart = t  # local t and not account for scr refresh
        encoding_title_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(encoding_title_text, 'tStartRefresh')  # time at next scr refresh
        encoding_title_text.setAutoDraw(True)
    if encoding_title_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > encoding_title_text.tStartRefresh + 2.0-frameTolerance:
            # keep track of stop time/frame for later
            encoding_title_text.tStop = t  # not accounting for scr refresh
            encoding_title_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(encoding_title_text, 'tStopRefresh')  # time at next scr refresh
            encoding_title_text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in encoding_titleComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "encoding_title"-------
for thisComponent in encoding_titleComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('encoding_title_text.started', encoding_title_text.tStartRefresh)
thisExp.addData('encoding_title_text.stopped', encoding_title_text.tStopRefresh)

# set up handler to look after randomisation of conditions etc
enc_practice_trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('stimuli_tables/encoding_practice_trials.csv', selection='1,4'),
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
    
    # ------Prepare to start Routine "practice_block_start"-------
    continueRoutine = True
    routineTimer.add(1.500000)
    # update component parameters for each repeat
    practice_start = practice_end
    practice_end = practice_start + 3
    practice_selection = np.arange(practice_start, practice_end, step)
    
    block_name = ''
    if TrialType=='OBJ':
        block_name='Kép'
    elif TrialType=='LOC':
        block_name='Hely'
    else:
        block_name='Block Unknown'
    
    
    start_practice_block.setText(block_name)
    # keep track of which components have finished
    practice_block_startComponents = [start_practice_block]
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
        
        # *start_practice_block* updates
        if start_practice_block.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            start_practice_block.frameNStart = frameN  # exact frame index
            start_practice_block.tStart = t  # local t and not account for scr refresh
            start_practice_block.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(start_practice_block, 'tStartRefresh')  # time at next scr refresh
            start_practice_block.setAutoDraw(True)
        if start_practice_block.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > start_practice_block.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                start_practice_block.tStop = t  # not accounting for scr refresh
                start_practice_block.frameNStop = frameN  # exact frame index
                win.timeOnFlip(start_practice_block, 'tStopRefresh')  # time at next scr refresh
                start_practice_block.setAutoDraw(False)
        
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
    enc_practice_trials.addData('start_practice_block.started', start_practice_block.tStartRefresh)
    enc_practice_trials.addData('start_practice_block.stopped', start_practice_block.tStopRefresh)
    
    # set up handler to look after randomisation of conditions etc
    enc_practice_block = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('stimuli_tables/encoding_practice_trials.csv', selection=practice_selection),
        seed=None, name='enc_practice_block')
    thisExp.addLoop(enc_practice_block)  # add the loop to the experiment
    thisEnc_practice_block = enc_practice_block.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisEnc_practice_block.rgb)
    if thisEnc_practice_block != None:
        for paramName in thisEnc_practice_block:
            exec('{} = thisEnc_practice_block[paramName]'.format(paramName))
    
    for thisEnc_practice_block in enc_practice_block:
        currentLoop = enc_practice_block
        # abbreviate parameter names if possible (e.g. rgb = thisEnc_practice_block.rgb)
        if thisEnc_practice_block != None:
            for paramName in thisEnc_practice_block:
                exec('{} = thisEnc_practice_block[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "enc_fx_practice"-------
        continueRoutine = True
        # update component parameters for each repeat
        w_size = win.size
        
        x_size = w_size[0]
        y_size = w_size[1]
        
        scr_resolution = x_size/y_size
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
                theseKeys = enc_fx_key_practice.getKeys(keyList=['f', 'j'], waitRelease=False)
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
        enc_practice_block.addData('enc_fx_interior_practice.started', enc_fx_interior_practice.tStartRefresh)
        enc_practice_block.addData('enc_fx_interior_practice.stopped', enc_fx_interior_practice.tStopRefresh)
        enc_practice_block.addData('enc_fx_cross_practice.started', enc_fx_cross_practice.tStartRefresh)
        enc_practice_block.addData('enc_fx_cross_practice.stopped', enc_fx_cross_practice.tStopRefresh)
        # check responses
        if enc_fx_key_practice.keys in ['', [], None]:  # No response was made
            enc_fx_key_practice.keys = None
        enc_practice_block.addData('enc_fx_key_practice.keys',enc_fx_key_practice.keys)
        if enc_fx_key_practice.keys != None:  # we had a response
            enc_practice_block.addData('enc_fx_key_practice.rt', enc_fx_key_practice.rt)
        enc_practice_block.addData('enc_fx_key_practice.started', enc_fx_key_practice.tStartRefresh)
        enc_practice_block.addData('enc_fx_key_practice.stopped', enc_fx_key_practice.tStopRefresh)
        enc_practice_block.addData('enc_fx_text_block_practice.started', enc_fx_text_block_practice.tStartRefresh)
        enc_practice_block.addData('enc_fx_text_block_practice.stopped', enc_fx_text_block_practice.tStopRefresh)
        enc_practice_block.addData('enc_fx_instructions_text_practice.started', enc_fx_instructions_text_practice.tStartRefresh)
        enc_practice_block.addData('enc_fx_instructions_text_practice.stopped', enc_fx_instructions_text_practice.tStopRefresh)
        # the Routine "enc_fx_practice" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "enc_trial_practice"-------
        continueRoutine = True
        routineTimer.add(3.000000)
        # update component parameters for each repeat
        w_size = win.size
        
        x_size = w_size[0]
        y_size = w_size[1]
        
        scr_resolution = x_size/y_size
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
                theseKeys = enc_trial_key_practice.getKeys(keyList=['f', 'j'], waitRelease=False)
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
        enc_practice_block.addData('enc_trial_interior_practice.started', enc_trial_interior_practice.tStartRefresh)
        enc_practice_block.addData('enc_trial_interior_practice.stopped', enc_trial_interior_practice.tStopRefresh)
        enc_practice_block.addData('enc_trial_main_image_practice.started', enc_trial_main_image_practice.tStartRefresh)
        enc_practice_block.addData('enc_trial_main_image_practice.stopped', enc_trial_main_image_practice.tStopRefresh)
        # check responses
        if enc_trial_key_practice.keys in ['', [], None]:  # No response was made
            enc_trial_key_practice.keys = None
        enc_practice_block.addData('enc_trial_key_practice.keys',enc_trial_key_practice.keys)
        if enc_trial_key_practice.keys != None:  # we had a response
            enc_practice_block.addData('enc_trial_key_practice.rt', enc_trial_key_practice.rt)
        enc_practice_block.addData('enc_trial_key_practice.started', enc_trial_key_practice.tStartRefresh)
        enc_practice_block.addData('enc_trial_key_practice.stopped', enc_trial_key_practice.tStopRefresh)
        enc_practice_block.addData('enc_trial_text_block_practice.started', enc_trial_text_block_practice.tStartRefresh)
        enc_practice_block.addData('enc_trial_text_block_practice.stopped', enc_trial_text_block_practice.tStopRefresh)
        enc_practice_block.addData('enc_trial_instructions_text_practice.started', enc_trial_instructions_text_practice.tStartRefresh)
        enc_practice_block.addData('enc_trial_instructions_text_practice.stopped', enc_trial_instructions_text_practice.tStopRefresh)
        
        # ------Prepare to start Routine "enc_practice_feedback"-------
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        response = enc_trial_key_practice.keys
        feedback_text = ''
        if response == 'f':
            feedback_text = 'Az Ön válasza:\nA kép nem marad.'
        elif response == 'j':
            feedback_text = 'Az Ön válasza:\nA kép marad.'
        else:
            feedback_text = 'Nem adott választ.'
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
        enc_practice_block.addData('enc_practice_feedback_interior.started', enc_practice_feedback_interior.tStartRefresh)
        enc_practice_block.addData('enc_practice_feedback_interior.stopped', enc_practice_feedback_interior.tStopRefresh)
        enc_practice_block.addData('enc_practice_feedback_image.started', enc_practice_feedback_image.tStartRefresh)
        enc_practice_block.addData('enc_practice_feedback_image.stopped', enc_practice_feedback_image.tStopRefresh)
        enc_practice_block.addData('enc_practice_feedback_text.started', enc_practice_feedback_text.tStartRefresh)
        enc_practice_block.addData('enc_practice_feedback_text.stopped', enc_practice_feedback_text.tStopRefresh)
        enc_practice_block.addData('enc_practice_feedback_block.started', enc_practice_feedback_block.tStartRefresh)
        enc_practice_block.addData('enc_practice_feedback_block.stopped', enc_practice_feedback_block.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1 repeats of 'enc_practice_block'
    
# completed 1 repeats of 'enc_practice_trials'


# ------Prepare to start Routine "end_practice"-------
continueRoutine = True
routineTimer.add(600.000000)
# update component parameters for each repeat
end_practice_key.keys = []
end_practice_key.rt = []
_end_practice_key_allKeys = []
block_counter = 0
coming_up_next_text.setText(coming_up_text)
# keep track of which components have finished
end_practiceComponents = [end_practice_text, end_practice_key, end_practice_continue, coming_up_next_text]
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
        theseKeys = end_practice_key.getKeys(keyList=['right', 'left'], waitRelease=False)
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
    
    # *coming_up_next_text* updates
    if coming_up_next_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        coming_up_next_text.frameNStart = frameN  # exact frame index
        coming_up_next_text.tStart = t  # local t and not account for scr refresh
        coming_up_next_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(coming_up_next_text, 'tStartRefresh')  # time at next scr refresh
        coming_up_next_text.setAutoDraw(True)
    if coming_up_next_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > coming_up_next_text.tStartRefresh + 600.0-frameTolerance:
            # keep track of stop time/frame for later
            coming_up_next_text.tStop = t  # not accounting for scr refresh
            coming_up_next_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(coming_up_next_text, 'tStopRefresh')  # time at next scr refresh
            coming_up_next_text.setAutoDraw(False)
    
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
thisExp.addData('coming_up_next_text.started', coming_up_next_text.tStartRefresh)
thisExp.addData('coming_up_next_text.stopped', coming_up_next_text.tStopRefresh)

# ------Prepare to start Routine "recognition_title"-------
continueRoutine = True
routineTimer.add(2.500000)
# update component parameters for each repeat
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
        if tThisFlipGlobal > start_recognition_text.tStartRefresh + 2.5-frameTolerance:
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

# ------Prepare to start Routine "rec_instructions_1"-------
continueRoutine = True
routineTimer.add(300.000000)
# update component parameters for each repeat
rec_instructions_1_key.keys = []
rec_instructions_1_key.rt = []
_rec_instructions_1_key_allKeys = []
# keep track of which components have finished
rec_instructions_1Components = [rec_instructions_1_text, rec_instructions_1_key, rec_instructions_1_continue]
for thisComponent in rec_instructions_1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
rec_instructions_1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "rec_instructions_1"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = rec_instructions_1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=rec_instructions_1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *rec_instructions_1_text* updates
    if rec_instructions_1_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        rec_instructions_1_text.frameNStart = frameN  # exact frame index
        rec_instructions_1_text.tStart = t  # local t and not account for scr refresh
        rec_instructions_1_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(rec_instructions_1_text, 'tStartRefresh')  # time at next scr refresh
        rec_instructions_1_text.setAutoDraw(True)
    if rec_instructions_1_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > rec_instructions_1_text.tStartRefresh + 300.0-frameTolerance:
            # keep track of stop time/frame for later
            rec_instructions_1_text.tStop = t  # not accounting for scr refresh
            rec_instructions_1_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(rec_instructions_1_text, 'tStopRefresh')  # time at next scr refresh
            rec_instructions_1_text.setAutoDraw(False)
    
    # *rec_instructions_1_key* updates
    waitOnFlip = False
    if rec_instructions_1_key.status == NOT_STARTED and tThisFlip >= 5.0-frameTolerance:
        # keep track of start time/frame for later
        rec_instructions_1_key.frameNStart = frameN  # exact frame index
        rec_instructions_1_key.tStart = t  # local t and not account for scr refresh
        rec_instructions_1_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(rec_instructions_1_key, 'tStartRefresh')  # time at next scr refresh
        rec_instructions_1_key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(rec_instructions_1_key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(rec_instructions_1_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if rec_instructions_1_key.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > rec_instructions_1_key.tStartRefresh + 295.0-frameTolerance:
            # keep track of stop time/frame for later
            rec_instructions_1_key.tStop = t  # not accounting for scr refresh
            rec_instructions_1_key.frameNStop = frameN  # exact frame index
            win.timeOnFlip(rec_instructions_1_key, 'tStopRefresh')  # time at next scr refresh
            rec_instructions_1_key.status = FINISHED
    if rec_instructions_1_key.status == STARTED and not waitOnFlip:
        theseKeys = rec_instructions_1_key.getKeys(keyList=['right'], waitRelease=False)
        _rec_instructions_1_key_allKeys.extend(theseKeys)
        if len(_rec_instructions_1_key_allKeys):
            rec_instructions_1_key.keys = _rec_instructions_1_key_allKeys[-1].name  # just the last key pressed
            rec_instructions_1_key.rt = _rec_instructions_1_key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *rec_instructions_1_continue* updates
    if rec_instructions_1_continue.status == NOT_STARTED and tThisFlip >= 5.0-frameTolerance:
        # keep track of start time/frame for later
        rec_instructions_1_continue.frameNStart = frameN  # exact frame index
        rec_instructions_1_continue.tStart = t  # local t and not account for scr refresh
        rec_instructions_1_continue.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(rec_instructions_1_continue, 'tStartRefresh')  # time at next scr refresh
        rec_instructions_1_continue.setAutoDraw(True)
    if rec_instructions_1_continue.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > rec_instructions_1_continue.tStartRefresh + 295.0-frameTolerance:
            # keep track of stop time/frame for later
            rec_instructions_1_continue.tStop = t  # not accounting for scr refresh
            rec_instructions_1_continue.frameNStop = frameN  # exact frame index
            win.timeOnFlip(rec_instructions_1_continue, 'tStopRefresh')  # time at next scr refresh
            rec_instructions_1_continue.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in rec_instructions_1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "rec_instructions_1"-------
for thisComponent in rec_instructions_1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('rec_instructions_1_text.started', rec_instructions_1_text.tStartRefresh)
thisExp.addData('rec_instructions_1_text.stopped', rec_instructions_1_text.tStopRefresh)
# check responses
if rec_instructions_1_key.keys in ['', [], None]:  # No response was made
    rec_instructions_1_key.keys = None
thisExp.addData('rec_instructions_1_key.keys',rec_instructions_1_key.keys)
if rec_instructions_1_key.keys != None:  # we had a response
    thisExp.addData('rec_instructions_1_key.rt', rec_instructions_1_key.rt)
thisExp.addData('rec_instructions_1_key.started', rec_instructions_1_key.tStartRefresh)
thisExp.addData('rec_instructions_1_key.stopped', rec_instructions_1_key.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('rec_instructions_1_continue.started', rec_instructions_1_continue.tStartRefresh)
thisExp.addData('rec_instructions_1_continue.stopped', rec_instructions_1_continue.tStopRefresh)

# ------Prepare to start Routine "rec_instructions_2"-------
continueRoutine = True
routineTimer.add(300.000000)
# update component parameters for each repeat
rec_instructions_2_key.keys = []
rec_instructions_2_key.rt = []
_rec_instructions_2_key_allKeys = []
# keep track of which components have finished
rec_instructions_2Components = [rec_instructions2_text, rec_instructions_2_key, rec_instructions_2_continue, rec_instruction_2_title]
for thisComponent in rec_instructions_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
rec_instructions_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "rec_instructions_2"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = rec_instructions_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=rec_instructions_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *rec_instructions2_text* updates
    if rec_instructions2_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        rec_instructions2_text.frameNStart = frameN  # exact frame index
        rec_instructions2_text.tStart = t  # local t and not account for scr refresh
        rec_instructions2_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(rec_instructions2_text, 'tStartRefresh')  # time at next scr refresh
        rec_instructions2_text.setAutoDraw(True)
    if rec_instructions2_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > rec_instructions2_text.tStartRefresh + 300.0-frameTolerance:
            # keep track of stop time/frame for later
            rec_instructions2_text.tStop = t  # not accounting for scr refresh
            rec_instructions2_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(rec_instructions2_text, 'tStopRefresh')  # time at next scr refresh
            rec_instructions2_text.setAutoDraw(False)
    
    # *rec_instructions_2_key* updates
    waitOnFlip = False
    if rec_instructions_2_key.status == NOT_STARTED and tThisFlip >= 5.0-frameTolerance:
        # keep track of start time/frame for later
        rec_instructions_2_key.frameNStart = frameN  # exact frame index
        rec_instructions_2_key.tStart = t  # local t and not account for scr refresh
        rec_instructions_2_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(rec_instructions_2_key, 'tStartRefresh')  # time at next scr refresh
        rec_instructions_2_key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(rec_instructions_2_key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(rec_instructions_2_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if rec_instructions_2_key.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > rec_instructions_2_key.tStartRefresh + 295.0-frameTolerance:
            # keep track of stop time/frame for later
            rec_instructions_2_key.tStop = t  # not accounting for scr refresh
            rec_instructions_2_key.frameNStop = frameN  # exact frame index
            win.timeOnFlip(rec_instructions_2_key, 'tStopRefresh')  # time at next scr refresh
            rec_instructions_2_key.status = FINISHED
    if rec_instructions_2_key.status == STARTED and not waitOnFlip:
        theseKeys = rec_instructions_2_key.getKeys(keyList=['right'], waitRelease=False)
        _rec_instructions_2_key_allKeys.extend(theseKeys)
        if len(_rec_instructions_2_key_allKeys):
            rec_instructions_2_key.keys = _rec_instructions_2_key_allKeys[-1].name  # just the last key pressed
            rec_instructions_2_key.rt = _rec_instructions_2_key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *rec_instructions_2_continue* updates
    if rec_instructions_2_continue.status == NOT_STARTED and tThisFlip >= 5.0-frameTolerance:
        # keep track of start time/frame for later
        rec_instructions_2_continue.frameNStart = frameN  # exact frame index
        rec_instructions_2_continue.tStart = t  # local t and not account for scr refresh
        rec_instructions_2_continue.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(rec_instructions_2_continue, 'tStartRefresh')  # time at next scr refresh
        rec_instructions_2_continue.setAutoDraw(True)
    if rec_instructions_2_continue.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > rec_instructions_2_continue.tStartRefresh + 295.0-frameTolerance:
            # keep track of stop time/frame for later
            rec_instructions_2_continue.tStop = t  # not accounting for scr refresh
            rec_instructions_2_continue.frameNStop = frameN  # exact frame index
            win.timeOnFlip(rec_instructions_2_continue, 'tStopRefresh')  # time at next scr refresh
            rec_instructions_2_continue.setAutoDraw(False)
    
    # *rec_instruction_2_title* updates
    if rec_instruction_2_title.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        rec_instruction_2_title.frameNStart = frameN  # exact frame index
        rec_instruction_2_title.tStart = t  # local t and not account for scr refresh
        rec_instruction_2_title.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(rec_instruction_2_title, 'tStartRefresh')  # time at next scr refresh
        rec_instruction_2_title.setAutoDraw(True)
    if rec_instruction_2_title.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > rec_instruction_2_title.tStartRefresh + 300.0-frameTolerance:
            # keep track of stop time/frame for later
            rec_instruction_2_title.tStop = t  # not accounting for scr refresh
            rec_instruction_2_title.frameNStop = frameN  # exact frame index
            win.timeOnFlip(rec_instruction_2_title, 'tStopRefresh')  # time at next scr refresh
            rec_instruction_2_title.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in rec_instructions_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "rec_instructions_2"-------
for thisComponent in rec_instructions_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('rec_instructions2_text.started', rec_instructions2_text.tStartRefresh)
thisExp.addData('rec_instructions2_text.stopped', rec_instructions2_text.tStopRefresh)
# check responses
if rec_instructions_2_key.keys in ['', [], None]:  # No response was made
    rec_instructions_2_key.keys = None
thisExp.addData('rec_instructions_2_key.keys',rec_instructions_2_key.keys)
if rec_instructions_2_key.keys != None:  # we had a response
    thisExp.addData('rec_instructions_2_key.rt', rec_instructions_2_key.rt)
thisExp.addData('rec_instructions_2_key.started', rec_instructions_2_key.tStartRefresh)
thisExp.addData('rec_instructions_2_key.stopped', rec_instructions_2_key.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('rec_instructions_2_continue.started', rec_instructions_2_continue.tStartRefresh)
thisExp.addData('rec_instructions_2_continue.stopped', rec_instructions_2_continue.tStopRefresh)
thisExp.addData('rec_instruction_2_title.started', rec_instruction_2_title.tStartRefresh)
thisExp.addData('rec_instruction_2_title.stopped', rec_instruction_2_title.tStopRefresh)

# ------Prepare to start Routine "rec_instructions_3"-------
continueRoutine = True
routineTimer.add(300.000000)
# update component parameters for each repeat
rec_instructions_3_key.keys = []
rec_instructions_3_key.rt = []
_rec_instructions_3_key_allKeys = []
# keep track of which components have finished
rec_instructions_3Components = [rec_instrauction_3_text, rec_instructions_3_key, rec_instructions_3_continue, rec_instruction_3_title]
for thisComponent in rec_instructions_3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
rec_instructions_3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "rec_instructions_3"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = rec_instructions_3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=rec_instructions_3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *rec_instrauction_3_text* updates
    if rec_instrauction_3_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        rec_instrauction_3_text.frameNStart = frameN  # exact frame index
        rec_instrauction_3_text.tStart = t  # local t and not account for scr refresh
        rec_instrauction_3_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(rec_instrauction_3_text, 'tStartRefresh')  # time at next scr refresh
        rec_instrauction_3_text.setAutoDraw(True)
    if rec_instrauction_3_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > rec_instrauction_3_text.tStartRefresh + 300.0-frameTolerance:
            # keep track of stop time/frame for later
            rec_instrauction_3_text.tStop = t  # not accounting for scr refresh
            rec_instrauction_3_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(rec_instrauction_3_text, 'tStopRefresh')  # time at next scr refresh
            rec_instrauction_3_text.setAutoDraw(False)
    
    # *rec_instructions_3_key* updates
    waitOnFlip = False
    if rec_instructions_3_key.status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
        # keep track of start time/frame for later
        rec_instructions_3_key.frameNStart = frameN  # exact frame index
        rec_instructions_3_key.tStart = t  # local t and not account for scr refresh
        rec_instructions_3_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(rec_instructions_3_key, 'tStartRefresh')  # time at next scr refresh
        rec_instructions_3_key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(rec_instructions_3_key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(rec_instructions_3_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if rec_instructions_3_key.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > rec_instructions_3_key.tStartRefresh + 295-frameTolerance:
            # keep track of stop time/frame for later
            rec_instructions_3_key.tStop = t  # not accounting for scr refresh
            rec_instructions_3_key.frameNStop = frameN  # exact frame index
            win.timeOnFlip(rec_instructions_3_key, 'tStopRefresh')  # time at next scr refresh
            rec_instructions_3_key.status = FINISHED
    if rec_instructions_3_key.status == STARTED and not waitOnFlip:
        theseKeys = rec_instructions_3_key.getKeys(keyList=['right'], waitRelease=False)
        _rec_instructions_3_key_allKeys.extend(theseKeys)
        if len(_rec_instructions_3_key_allKeys):
            rec_instructions_3_key.keys = _rec_instructions_3_key_allKeys[-1].name  # just the last key pressed
            rec_instructions_3_key.rt = _rec_instructions_3_key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *rec_instructions_3_continue* updates
    if rec_instructions_3_continue.status == NOT_STARTED and tThisFlip >= 5.0-frameTolerance:
        # keep track of start time/frame for later
        rec_instructions_3_continue.frameNStart = frameN  # exact frame index
        rec_instructions_3_continue.tStart = t  # local t and not account for scr refresh
        rec_instructions_3_continue.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(rec_instructions_3_continue, 'tStartRefresh')  # time at next scr refresh
        rec_instructions_3_continue.setAutoDraw(True)
    if rec_instructions_3_continue.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > rec_instructions_3_continue.tStartRefresh + 295.0-frameTolerance:
            # keep track of stop time/frame for later
            rec_instructions_3_continue.tStop = t  # not accounting for scr refresh
            rec_instructions_3_continue.frameNStop = frameN  # exact frame index
            win.timeOnFlip(rec_instructions_3_continue, 'tStopRefresh')  # time at next scr refresh
            rec_instructions_3_continue.setAutoDraw(False)
    
    # *rec_instruction_3_title* updates
    if rec_instruction_3_title.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        rec_instruction_3_title.frameNStart = frameN  # exact frame index
        rec_instruction_3_title.tStart = t  # local t and not account for scr refresh
        rec_instruction_3_title.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(rec_instruction_3_title, 'tStartRefresh')  # time at next scr refresh
        rec_instruction_3_title.setAutoDraw(True)
    if rec_instruction_3_title.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > rec_instruction_3_title.tStartRefresh + 300.0-frameTolerance:
            # keep track of stop time/frame for later
            rec_instruction_3_title.tStop = t  # not accounting for scr refresh
            rec_instruction_3_title.frameNStop = frameN  # exact frame index
            win.timeOnFlip(rec_instruction_3_title, 'tStopRefresh')  # time at next scr refresh
            rec_instruction_3_title.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in rec_instructions_3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "rec_instructions_3"-------
for thisComponent in rec_instructions_3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('rec_instrauction_3_text.started', rec_instrauction_3_text.tStartRefresh)
thisExp.addData('rec_instrauction_3_text.stopped', rec_instrauction_3_text.tStopRefresh)
# check responses
if rec_instructions_3_key.keys in ['', [], None]:  # No response was made
    rec_instructions_3_key.keys = None
thisExp.addData('rec_instructions_3_key.keys',rec_instructions_3_key.keys)
if rec_instructions_3_key.keys != None:  # we had a response
    thisExp.addData('rec_instructions_3_key.rt', rec_instructions_3_key.rt)
thisExp.addData('rec_instructions_3_key.started', rec_instructions_3_key.tStartRefresh)
thisExp.addData('rec_instructions_3_key.stopped', rec_instructions_3_key.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('rec_instructions_3_continue.started', rec_instructions_3_continue.tStartRefresh)
thisExp.addData('rec_instructions_3_continue.stopped', rec_instructions_3_continue.tStopRefresh)
thisExp.addData('rec_instruction_3_title.started', rec_instruction_3_title.tStartRefresh)
thisExp.addData('rec_instruction_3_title.stopped', rec_instruction_3_title.tStopRefresh)

# ------Prepare to start Routine "rec_instructions_4"-------
continueRoutine = True
routineTimer.add(300.000000)
# update component parameters for each repeat
rec_instructions_4_key.keys = []
rec_instructions_4_key.rt = []
_rec_instructions_4_key_allKeys = []
# keep track of which components have finished
rec_instructions_4Components = [rec_instructions_4_text, rec_instructions_4_key, rec_instructions_4_continue]
for thisComponent in rec_instructions_4Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
rec_instructions_4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "rec_instructions_4"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = rec_instructions_4Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=rec_instructions_4Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *rec_instructions_4_text* updates
    if rec_instructions_4_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        rec_instructions_4_text.frameNStart = frameN  # exact frame index
        rec_instructions_4_text.tStart = t  # local t and not account for scr refresh
        rec_instructions_4_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(rec_instructions_4_text, 'tStartRefresh')  # time at next scr refresh
        rec_instructions_4_text.setAutoDraw(True)
    if rec_instructions_4_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > rec_instructions_4_text.tStartRefresh + 300.0-frameTolerance:
            # keep track of stop time/frame for later
            rec_instructions_4_text.tStop = t  # not accounting for scr refresh
            rec_instructions_4_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(rec_instructions_4_text, 'tStopRefresh')  # time at next scr refresh
            rec_instructions_4_text.setAutoDraw(False)
    
    # *rec_instructions_4_key* updates
    waitOnFlip = False
    if rec_instructions_4_key.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
        # keep track of start time/frame for later
        rec_instructions_4_key.frameNStart = frameN  # exact frame index
        rec_instructions_4_key.tStart = t  # local t and not account for scr refresh
        rec_instructions_4_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(rec_instructions_4_key, 'tStartRefresh')  # time at next scr refresh
        rec_instructions_4_key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(rec_instructions_4_key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(rec_instructions_4_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if rec_instructions_4_key.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > rec_instructions_4_key.tStartRefresh + 299.0-frameTolerance:
            # keep track of stop time/frame for later
            rec_instructions_4_key.tStop = t  # not accounting for scr refresh
            rec_instructions_4_key.frameNStop = frameN  # exact frame index
            win.timeOnFlip(rec_instructions_4_key, 'tStopRefresh')  # time at next scr refresh
            rec_instructions_4_key.status = FINISHED
    if rec_instructions_4_key.status == STARTED and not waitOnFlip:
        theseKeys = rec_instructions_4_key.getKeys(keyList=['right'], waitRelease=False)
        _rec_instructions_4_key_allKeys.extend(theseKeys)
        if len(_rec_instructions_4_key_allKeys):
            rec_instructions_4_key.keys = _rec_instructions_4_key_allKeys[-1].name  # just the last key pressed
            rec_instructions_4_key.rt = _rec_instructions_4_key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *rec_instructions_4_continue* updates
    if rec_instructions_4_continue.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
        # keep track of start time/frame for later
        rec_instructions_4_continue.frameNStart = frameN  # exact frame index
        rec_instructions_4_continue.tStart = t  # local t and not account for scr refresh
        rec_instructions_4_continue.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(rec_instructions_4_continue, 'tStartRefresh')  # time at next scr refresh
        rec_instructions_4_continue.setAutoDraw(True)
    if rec_instructions_4_continue.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > rec_instructions_4_continue.tStartRefresh + 299.0-frameTolerance:
            # keep track of stop time/frame for later
            rec_instructions_4_continue.tStop = t  # not accounting for scr refresh
            rec_instructions_4_continue.frameNStop = frameN  # exact frame index
            win.timeOnFlip(rec_instructions_4_continue, 'tStopRefresh')  # time at next scr refresh
            rec_instructions_4_continue.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in rec_instructions_4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "rec_instructions_4"-------
for thisComponent in rec_instructions_4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('rec_instructions_4_text.started', rec_instructions_4_text.tStartRefresh)
thisExp.addData('rec_instructions_4_text.stopped', rec_instructions_4_text.tStopRefresh)
# check responses
if rec_instructions_4_key.keys in ['', [], None]:  # No response was made
    rec_instructions_4_key.keys = None
thisExp.addData('rec_instructions_4_key.keys',rec_instructions_4_key.keys)
if rec_instructions_4_key.keys != None:  # we had a response
    thisExp.addData('rec_instructions_4_key.rt', rec_instructions_4_key.rt)
thisExp.addData('rec_instructions_4_key.started', rec_instructions_4_key.tStartRefresh)
thisExp.addData('rec_instructions_4_key.stopped', rec_instructions_4_key.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('rec_instructions_4_continue.started', rec_instructions_4_continue.tStartRefresh)
thisExp.addData('rec_instructions_4_continue.stopped', rec_instructions_4_continue.tStopRefresh)

# ------Prepare to start Routine "demo_start"-------
continueRoutine = True
routineTimer.add(1.500000)
# update component parameters for each repeat
# keep track of which components have finished
demo_startComponents = [demo_start_text]
for thisComponent in demo_startComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
demo_startClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "demo_start"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = demo_startClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=demo_startClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *demo_start_text* updates
    if demo_start_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        demo_start_text.frameNStart = frameN  # exact frame index
        demo_start_text.tStart = t  # local t and not account for scr refresh
        demo_start_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(demo_start_text, 'tStartRefresh')  # time at next scr refresh
        demo_start_text.setAutoDraw(True)
    if demo_start_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > demo_start_text.tStartRefresh + 1.5-frameTolerance:
            # keep track of stop time/frame for later
            demo_start_text.tStop = t  # not accounting for scr refresh
            demo_start_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(demo_start_text, 'tStopRefresh')  # time at next scr refresh
            demo_start_text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in demo_startComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "demo_start"-------
for thisComponent in demo_startComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('demo_start_text.started', demo_start_text.tStartRefresh)
thisExp.addData('demo_start_text.stopped', demo_start_text.tStopRefresh)

# set up handler to look after randomisation of conditions etc
demo_trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('stimuli_tables/stimuli_demo.xlsx'),
    seed=None, name='demo_trials')
thisExp.addLoop(demo_trials)  # add the loop to the experiment
thisDemo_trial = demo_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisDemo_trial.rgb)
if thisDemo_trial != None:
    for paramName in thisDemo_trial:
        exec('{} = thisDemo_trial[paramName]'.format(paramName))

for thisDemo_trial in demo_trials:
    currentLoop = demo_trials
    # abbreviate parameter names if possible (e.g. rgb = thisDemo_trial.rgb)
    if thisDemo_trial != None:
        for paramName in thisDemo_trial:
            exec('{} = thisDemo_trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "demo"-------
    continueRoutine = True
    routineTimer.add(300.000000)
    # update component parameters for each repeat
    demo_main_image.setPos((CurrentX, CurrentY))
    demo_main_image.setSize((0.3125, 0.3125*scr_resolution))
    demo_main_image.setImage(CurrentImage)
    demo_image.setPos((DemoX, DemoY))
    demo_image.setSize((0.3125, 0.3125*scr_resolution))
    demo_image.setImage(DemoImage)
    demo_text.setText(DemoText)
    demo_key.keys = []
    demo_key.rt = []
    _demo_key_allKeys = []
    # keep track of which components have finished
    demoComponents = [demo_interior, demo_main_image, demo_image, demo_text, demo_key, demo_continue]
    for thisComponent in demoComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    demoClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "demo"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = demoClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=demoClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *demo_interior* updates
        if demo_interior.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            demo_interior.frameNStart = frameN  # exact frame index
            demo_interior.tStart = t  # local t and not account for scr refresh
            demo_interior.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(demo_interior, 'tStartRefresh')  # time at next scr refresh
            demo_interior.setAutoDraw(True)
        if demo_interior.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > demo_interior.tStartRefresh + 300.0-frameTolerance:
                # keep track of stop time/frame for later
                demo_interior.tStop = t  # not accounting for scr refresh
                demo_interior.frameNStop = frameN  # exact frame index
                win.timeOnFlip(demo_interior, 'tStopRefresh')  # time at next scr refresh
                demo_interior.setAutoDraw(False)
        
        # *demo_main_image* updates
        if demo_main_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            demo_main_image.frameNStart = frameN  # exact frame index
            demo_main_image.tStart = t  # local t and not account for scr refresh
            demo_main_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(demo_main_image, 'tStartRefresh')  # time at next scr refresh
            demo_main_image.setAutoDraw(True)
        if demo_main_image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > demo_main_image.tStartRefresh + 300.0-frameTolerance:
                # keep track of stop time/frame for later
                demo_main_image.tStop = t  # not accounting for scr refresh
                demo_main_image.frameNStop = frameN  # exact frame index
                win.timeOnFlip(demo_main_image, 'tStopRefresh')  # time at next scr refresh
                demo_main_image.setAutoDraw(False)
        
        # *demo_image* updates
        if demo_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            demo_image.frameNStart = frameN  # exact frame index
            demo_image.tStart = t  # local t and not account for scr refresh
            demo_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(demo_image, 'tStartRefresh')  # time at next scr refresh
            demo_image.setAutoDraw(True)
        if demo_image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > demo_image.tStartRefresh + 300.0-frameTolerance:
                # keep track of stop time/frame for later
                demo_image.tStop = t  # not accounting for scr refresh
                demo_image.frameNStop = frameN  # exact frame index
                win.timeOnFlip(demo_image, 'tStopRefresh')  # time at next scr refresh
                demo_image.setAutoDraw(False)
        
        # *demo_text* updates
        if demo_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            demo_text.frameNStart = frameN  # exact frame index
            demo_text.tStart = t  # local t and not account for scr refresh
            demo_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(demo_text, 'tStartRefresh')  # time at next scr refresh
            demo_text.setAutoDraw(True)
        if demo_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > demo_text.tStartRefresh + 300.0-frameTolerance:
                # keep track of stop time/frame for later
                demo_text.tStop = t  # not accounting for scr refresh
                demo_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(demo_text, 'tStopRefresh')  # time at next scr refresh
                demo_text.setAutoDraw(False)
        
        # *demo_key* updates
        waitOnFlip = False
        if demo_key.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            demo_key.frameNStart = frameN  # exact frame index
            demo_key.tStart = t  # local t and not account for scr refresh
            demo_key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(demo_key, 'tStartRefresh')  # time at next scr refresh
            demo_key.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(demo_key.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(demo_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if demo_key.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > demo_key.tStartRefresh + 298-frameTolerance:
                # keep track of stop time/frame for later
                demo_key.tStop = t  # not accounting for scr refresh
                demo_key.frameNStop = frameN  # exact frame index
                win.timeOnFlip(demo_key, 'tStopRefresh')  # time at next scr refresh
                demo_key.status = FINISHED
        if demo_key.status == STARTED and not waitOnFlip:
            theseKeys = demo_key.getKeys(keyList=['right'], waitRelease=False)
            _demo_key_allKeys.extend(theseKeys)
            if len(_demo_key_allKeys):
                demo_key.keys = _demo_key_allKeys[-1].name  # just the last key pressed
                demo_key.rt = _demo_key_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *demo_continue* updates
        if demo_continue.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            demo_continue.frameNStart = frameN  # exact frame index
            demo_continue.tStart = t  # local t and not account for scr refresh
            demo_continue.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(demo_continue, 'tStartRefresh')  # time at next scr refresh
            demo_continue.setAutoDraw(True)
        if demo_continue.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > demo_continue.tStartRefresh + 298.0-frameTolerance:
                # keep track of stop time/frame for later
                demo_continue.tStop = t  # not accounting for scr refresh
                demo_continue.frameNStop = frameN  # exact frame index
                win.timeOnFlip(demo_continue, 'tStopRefresh')  # time at next scr refresh
                demo_continue.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in demoComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "demo"-------
    for thisComponent in demoComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    demo_trials.addData('demo_interior.started', demo_interior.tStartRefresh)
    demo_trials.addData('demo_interior.stopped', demo_interior.tStopRefresh)
    demo_trials.addData('demo_main_image.started', demo_main_image.tStartRefresh)
    demo_trials.addData('demo_main_image.stopped', demo_main_image.tStopRefresh)
    demo_trials.addData('demo_image.started', demo_image.tStartRefresh)
    demo_trials.addData('demo_image.stopped', demo_image.tStopRefresh)
    demo_trials.addData('demo_text.started', demo_text.tStartRefresh)
    demo_trials.addData('demo_text.stopped', demo_text.tStopRefresh)
    # check responses
    if demo_key.keys in ['', [], None]:  # No response was made
        demo_key.keys = None
    demo_trials.addData('demo_key.keys',demo_key.keys)
    if demo_key.keys != None:  # we had a response
        demo_trials.addData('demo_key.rt', demo_key.rt)
    demo_trials.addData('demo_key.started', demo_key.tStartRefresh)
    demo_trials.addData('demo_key.stopped', demo_key.tStopRefresh)
    demo_trials.addData('demo_continue.started', demo_continue.tStartRefresh)
    demo_trials.addData('demo_continue.stopped', demo_continue.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'demo_trials'


# ------Prepare to start Routine "demo_end"-------
continueRoutine = True
routineTimer.add(300.000000)
# update component parameters for each repeat
demo_end_key.keys = []
demo_end_key.rt = []
_demo_end_key_allKeys = []
# keep track of which components have finished
demo_endComponents = [demo_end_text, demo_end_key, demo_end_continue]
for thisComponent in demo_endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
demo_endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "demo_end"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = demo_endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=demo_endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *demo_end_text* updates
    if demo_end_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        demo_end_text.frameNStart = frameN  # exact frame index
        demo_end_text.tStart = t  # local t and not account for scr refresh
        demo_end_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(demo_end_text, 'tStartRefresh')  # time at next scr refresh
        demo_end_text.setAutoDraw(True)
    if demo_end_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > demo_end_text.tStartRefresh + 300.0-frameTolerance:
            # keep track of stop time/frame for later
            demo_end_text.tStop = t  # not accounting for scr refresh
            demo_end_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(demo_end_text, 'tStopRefresh')  # time at next scr refresh
            demo_end_text.setAutoDraw(False)
    
    # *demo_end_key* updates
    waitOnFlip = False
    if demo_end_key.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
        # keep track of start time/frame for later
        demo_end_key.frameNStart = frameN  # exact frame index
        demo_end_key.tStart = t  # local t and not account for scr refresh
        demo_end_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(demo_end_key, 'tStartRefresh')  # time at next scr refresh
        demo_end_key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(demo_end_key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(demo_end_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if demo_end_key.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > demo_end_key.tStartRefresh + 299.0-frameTolerance:
            # keep track of stop time/frame for later
            demo_end_key.tStop = t  # not accounting for scr refresh
            demo_end_key.frameNStop = frameN  # exact frame index
            win.timeOnFlip(demo_end_key, 'tStopRefresh')  # time at next scr refresh
            demo_end_key.status = FINISHED
    if demo_end_key.status == STARTED and not waitOnFlip:
        theseKeys = demo_end_key.getKeys(keyList=['right'], waitRelease=False)
        _demo_end_key_allKeys.extend(theseKeys)
        if len(_demo_end_key_allKeys):
            demo_end_key.keys = _demo_end_key_allKeys[-1].name  # just the last key pressed
            demo_end_key.rt = _demo_end_key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *demo_end_continue* updates
    if demo_end_continue.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
        # keep track of start time/frame for later
        demo_end_continue.frameNStart = frameN  # exact frame index
        demo_end_continue.tStart = t  # local t and not account for scr refresh
        demo_end_continue.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(demo_end_continue, 'tStartRefresh')  # time at next scr refresh
        demo_end_continue.setAutoDraw(True)
    if demo_end_continue.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > demo_end_continue.tStartRefresh + 299.0-frameTolerance:
            # keep track of stop time/frame for later
            demo_end_continue.tStop = t  # not accounting for scr refresh
            demo_end_continue.frameNStop = frameN  # exact frame index
            win.timeOnFlip(demo_end_continue, 'tStopRefresh')  # time at next scr refresh
            demo_end_continue.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in demo_endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "demo_end"-------
for thisComponent in demo_endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('demo_end_text.started', demo_end_text.tStartRefresh)
thisExp.addData('demo_end_text.stopped', demo_end_text.tStopRefresh)
# check responses
if demo_end_key.keys in ['', [], None]:  # No response was made
    demo_end_key.keys = None
thisExp.addData('demo_end_key.keys',demo_end_key.keys)
if demo_end_key.keys != None:  # we had a response
    thisExp.addData('demo_end_key.rt', demo_end_key.rt)
thisExp.addData('demo_end_key.started', demo_end_key.tStartRefresh)
thisExp.addData('demo_end_key.stopped', demo_end_key.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('demo_end_continue.started', demo_end_continue.tStartRefresh)
thisExp.addData('demo_end_continue.stopped', demo_end_continue.tStopRefresh)
coming_up_text='Most a két feladattípus együttes gyakorlása következik.'

# ------Prepare to start Routine "start_practice"-------
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
practice_start = 0
practice_end = 0
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
rec_practice_blocks = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('stimuli_tables/recognition_practice_trials.csv', selection='1,4'),
    seed=None, name='rec_practice_blocks')
thisExp.addLoop(rec_practice_blocks)  # add the loop to the experiment
thisRec_practice_block = rec_practice_blocks.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisRec_practice_block.rgb)
if thisRec_practice_block != None:
    for paramName in thisRec_practice_block:
        exec('{} = thisRec_practice_block[paramName]'.format(paramName))

for thisRec_practice_block in rec_practice_blocks:
    currentLoop = rec_practice_blocks
    # abbreviate parameter names if possible (e.g. rgb = thisRec_practice_block.rgb)
    if thisRec_practice_block != None:
        for paramName in thisRec_practice_block:
            exec('{} = thisRec_practice_block[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "practice_block_start"-------
    continueRoutine = True
    routineTimer.add(1.500000)
    # update component parameters for each repeat
    practice_start = practice_end
    practice_end = practice_start + 3
    practice_selection = np.arange(practice_start, practice_end, step)
    
    block_name = ''
    if TrialType=='OBJ':
        block_name='Kép'
    elif TrialType=='LOC':
        block_name='Hely'
    else:
        block_name='Block Unknown'
    
    
    start_practice_block.setText(block_name)
    # keep track of which components have finished
    practice_block_startComponents = [start_practice_block]
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
        
        # *start_practice_block* updates
        if start_practice_block.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            start_practice_block.frameNStart = frameN  # exact frame index
            start_practice_block.tStart = t  # local t and not account for scr refresh
            start_practice_block.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(start_practice_block, 'tStartRefresh')  # time at next scr refresh
            start_practice_block.setAutoDraw(True)
        if start_practice_block.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > start_practice_block.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                start_practice_block.tStop = t  # not accounting for scr refresh
                start_practice_block.frameNStop = frameN  # exact frame index
                win.timeOnFlip(start_practice_block, 'tStopRefresh')  # time at next scr refresh
                start_practice_block.setAutoDraw(False)
        
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
    rec_practice_blocks.addData('start_practice_block.started', start_practice_block.tStartRefresh)
    rec_practice_blocks.addData('start_practice_block.stopped', start_practice_block.tStopRefresh)
    
    # set up handler to look after randomisation of conditions etc
    rec_practice_trials = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('stimuli_tables/recognition_practice_trials.csv', selection=practice_selection),
        seed=None, name='rec_practice_trials')
    thisExp.addLoop(rec_practice_trials)  # add the loop to the experiment
    thisRec_practice_trial = rec_practice_trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisRec_practice_trial.rgb)
    if thisRec_practice_trial != None:
        for paramName in thisRec_practice_trial:
            exec('{} = thisRec_practice_trial[paramName]'.format(paramName))
    
    for thisRec_practice_trial in rec_practice_trials:
        currentLoop = rec_practice_trials
        # abbreviate parameter names if possible (e.g. rgb = thisRec_practice_trial.rgb)
        if thisRec_practice_trial != None:
            for paramName in thisRec_practice_trial:
                exec('{} = thisRec_practice_trial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "rec_fx_practice"-------
        continueRoutine = True
        # update component parameters for each repeat
        w_size = win.size
        
        x_size = w_size[0]
        y_size = w_size[1]
        
        scr_resolution = x_size/y_size
        rec_fx_cross_practice.setPos((CurrentX, CurrentY))
        rec_fx_key_practice.keys = []
        rec_fx_key_practice.rt = []
        _rec_fx_key_practice_allKeys = []
        rec_fx_text_block_practice.setText(block_name
)
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
                theseKeys = rec_fx_key_practice.getKeys(keyList=['f', 'j'], waitRelease=False)
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
        rec_practice_trials.addData('rec_fx_interior_practice.started', rec_fx_interior_practice.tStartRefresh)
        rec_practice_trials.addData('rec_fx_interior_practice.stopped', rec_fx_interior_practice.tStopRefresh)
        rec_practice_trials.addData('rec_fx_cross_practice.started', rec_fx_cross_practice.tStartRefresh)
        rec_practice_trials.addData('rec_fx_cross_practice.stopped', rec_fx_cross_practice.tStopRefresh)
        # check responses
        if rec_fx_key_practice.keys in ['', [], None]:  # No response was made
            rec_fx_key_practice.keys = None
        rec_practice_trials.addData('rec_fx_key_practice.keys',rec_fx_key_practice.keys)
        if rec_fx_key_practice.keys != None:  # we had a response
            rec_practice_trials.addData('rec_fx_key_practice.rt', rec_fx_key_practice.rt)
        rec_practice_trials.addData('rec_fx_key_practice.started', rec_fx_key_practice.tStartRefresh)
        rec_practice_trials.addData('rec_fx_key_practice.stopped', rec_fx_key_practice.tStopRefresh)
        rec_practice_trials.addData('rec_fx_text_block_practice.started', rec_fx_text_block_practice.tStartRefresh)
        rec_practice_trials.addData('rec_fx_text_block_practice.stopped', rec_fx_text_block_practice.tStopRefresh)
        rec_practice_trials.addData('rec_fx_instructions_text_practice.started', rec_fx_instructions_text_practice.tStartRefresh)
        rec_practice_trials.addData('rec_fx_instructions_text_practice.stopped', rec_fx_instructions_text_practice.tStopRefresh)
        # the Routine "rec_fx_practice" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
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
        if rec_trial_key_practice_practice.keys == 'f':
            response = 'Az Ön válasza: Régi'
        
        elif rec_trial_key_practice.keys == 'j':
            response = 'Az Ön válasza: Új'
            
        feedback_text = correct_response +'\n'+ response
        
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
        rec_practice_trials.addData('rec_practice_feedback_text.started', rec_practice_feedback_text.tStartRefresh)
        rec_practice_trials.addData('rec_practice_feedback_text.stopped', rec_practice_feedback_text.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1 repeats of 'rec_practice_trials'
    
# completed 1 repeats of 'rec_practice_blocks'


# ------Prepare to start Routine "end_practice"-------
continueRoutine = True
routineTimer.add(600.000000)
# update component parameters for each repeat
end_practice_key.keys = []
end_practice_key.rt = []
_end_practice_key_allKeys = []
block_counter = 0
coming_up_next_text.setText(coming_up_text)
# keep track of which components have finished
end_practiceComponents = [end_practice_text, end_practice_key, end_practice_continue, coming_up_next_text]
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
        theseKeys = end_practice_key.getKeys(keyList=['right', 'left'], waitRelease=False)
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
    
    # *coming_up_next_text* updates
    if coming_up_next_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        coming_up_next_text.frameNStart = frameN  # exact frame index
        coming_up_next_text.tStart = t  # local t and not account for scr refresh
        coming_up_next_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(coming_up_next_text, 'tStartRefresh')  # time at next scr refresh
        coming_up_next_text.setAutoDraw(True)
    if coming_up_next_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > coming_up_next_text.tStartRefresh + 600.0-frameTolerance:
            # keep track of stop time/frame for later
            coming_up_next_text.tStop = t  # not accounting for scr refresh
            coming_up_next_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(coming_up_next_text, 'tStopRefresh')  # time at next scr refresh
            coming_up_next_text.setAutoDraw(False)
    
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
thisExp.addData('coming_up_next_text.started', coming_up_next_text.tStartRefresh)
thisExp.addData('coming_up_next_text.stopped', coming_up_next_text.tStopRefresh)

# ------Prepare to start Routine "start_practice"-------
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
practice_start = 0
practice_end = 0
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
full_practce = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('stimuli_tables/recognition_full_practice_trials.csv', selection='1, 4'),
    seed=None, name='full_practce')
thisExp.addLoop(full_practce)  # add the loop to the experiment
thisFull_practce = full_practce.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisFull_practce.rgb)
if thisFull_practce != None:
    for paramName in thisFull_practce:
        exec('{} = thisFull_practce[paramName]'.format(paramName))

for thisFull_practce in full_practce:
    currentLoop = full_practce
    # abbreviate parameter names if possible (e.g. rgb = thisFull_practce.rgb)
    if thisFull_practce != None:
        for paramName in thisFull_practce:
            exec('{} = thisFull_practce[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "practice_block_start"-------
    continueRoutine = True
    routineTimer.add(1.500000)
    # update component parameters for each repeat
    practice_start = practice_end
    practice_end = practice_start + 3
    practice_selection = np.arange(practice_start, practice_end, step)
    
    block_name = ''
    if TrialType=='OBJ':
        block_name='Kép'
    elif TrialType=='LOC':
        block_name='Hely'
    else:
        block_name='Block Unknown'
    
    
    start_practice_block.setText(block_name)
    # keep track of which components have finished
    practice_block_startComponents = [start_practice_block]
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
        
        # *start_practice_block* updates
        if start_practice_block.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            start_practice_block.frameNStart = frameN  # exact frame index
            start_practice_block.tStart = t  # local t and not account for scr refresh
            start_practice_block.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(start_practice_block, 'tStartRefresh')  # time at next scr refresh
            start_practice_block.setAutoDraw(True)
        if start_practice_block.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > start_practice_block.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                start_practice_block.tStop = t  # not accounting for scr refresh
                start_practice_block.frameNStop = frameN  # exact frame index
                win.timeOnFlip(start_practice_block, 'tStopRefresh')  # time at next scr refresh
                start_practice_block.setAutoDraw(False)
        
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
    full_practce.addData('start_practice_block.started', start_practice_block.tStartRefresh)
    full_practce.addData('start_practice_block.stopped', start_practice_block.tStopRefresh)
    
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
        w_size = win.size
        
        x_size = w_size[0]
        y_size = w_size[1]
        
        scr_resolution = x_size/y_size
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
                theseKeys = enc_fx_key_practice.getKeys(keyList=['f', 'j'], waitRelease=False)
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
        w_size = win.size
        
        x_size = w_size[0]
        y_size = w_size[1]
        
        scr_resolution = x_size/y_size
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
                theseKeys = enc_trial_key_practice.getKeys(keyList=['f', 'j'], waitRelease=False)
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
        if response == 'f':
            feedback_text = 'Az Ön válasza:\nA kép nem marad.'
        elif response == 'j':
            feedback_text = 'Az Ön válasza:\nA kép marad.'
        else:
            feedback_text = 'Nem adott választ.'
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
    routineTimer.add(2.500000)
    # update component parameters for each repeat
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
            if tThisFlipGlobal > start_recognition_text.tStartRefresh + 2.5-frameTolerance:
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
    full_practce.addData('start_recognition_text.started', start_recognition_text.tStartRefresh)
    full_practce.addData('start_recognition_text.stopped', start_recognition_text.tStopRefresh)
    
    # ------Prepare to start Routine "block_title"-------
    continueRoutine = True
    routineTimer.add(1.500000)
    # update component parameters for each repeat
    block_title_text.setText(block_name)
    # keep track of which components have finished
    block_titleComponents = [block_title_text]
    for thisComponent in block_titleComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    block_titleClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "block_title"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = block_titleClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=block_titleClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *block_title_text* updates
        if block_title_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            block_title_text.frameNStart = frameN  # exact frame index
            block_title_text.tStart = t  # local t and not account for scr refresh
            block_title_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(block_title_text, 'tStartRefresh')  # time at next scr refresh
            block_title_text.setAutoDraw(True)
        if block_title_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > block_title_text.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                block_title_text.tStop = t  # not accounting for scr refresh
                block_title_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(block_title_text, 'tStopRefresh')  # time at next scr refresh
                block_title_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in block_titleComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "block_title"-------
    for thisComponent in block_titleComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    full_practce.addData('block_title_text.started', block_title_text.tStartRefresh)
    full_practce.addData('block_title_text.stopped', block_title_text.tStopRefresh)
    coming_up_text='A feladat következik. A feladat során már nem kap visszajelzést.'
    
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
        w_size = win.size
        
        x_size = w_size[0]
        y_size = w_size[1]
        
        scr_resolution = x_size/y_size
        rec_fx_cross_practice.setPos((CurrentX, CurrentY))
        rec_fx_key_practice.keys = []
        rec_fx_key_practice.rt = []
        _rec_fx_key_practice_allKeys = []
        rec_fx_text_block_practice.setText(block_name
)
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
                theseKeys = rec_fx_key_practice.getKeys(keyList=['f', 'j'], waitRelease=False)
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
        if rec_trial_key_practice_practice.keys == 'f':
            response = 'Az Ön válasza: Régi'
        
        elif rec_trial_key_practice.keys == 'j':
            response = 'Az Ön válasza: Új'
            
        feedback_text = correct_response +'\n'+ response
        
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
        thisExp.nextEntry()
        
    # completed 1 repeats of 'rec_full_practice'
    
    thisExp.nextEntry()
    
# completed 1 repeats of 'full_practce'


# ------Prepare to start Routine "end_practice"-------
continueRoutine = True
routineTimer.add(600.000000)
# update component parameters for each repeat
end_practice_key.keys = []
end_practice_key.rt = []
_end_practice_key_allKeys = []
block_counter = 0
coming_up_next_text.setText(coming_up_text)
# keep track of which components have finished
end_practiceComponents = [end_practice_text, end_practice_key, end_practice_continue, coming_up_next_text]
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
        theseKeys = end_practice_key.getKeys(keyList=['right', 'left'], waitRelease=False)
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
    
    # *coming_up_next_text* updates
    if coming_up_next_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        coming_up_next_text.frameNStart = frameN  # exact frame index
        coming_up_next_text.tStart = t  # local t and not account for scr refresh
        coming_up_next_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(coming_up_next_text, 'tStartRefresh')  # time at next scr refresh
        coming_up_next_text.setAutoDraw(True)
    if coming_up_next_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > coming_up_next_text.tStartRefresh + 600.0-frameTolerance:
            # keep track of stop time/frame for later
            coming_up_next_text.tStop = t  # not accounting for scr refresh
            coming_up_next_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(coming_up_next_text, 'tStopRefresh')  # time at next scr refresh
            coming_up_next_text.setAutoDraw(False)
    
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
thisExp.addData('coming_up_next_text.started', coming_up_next_text.tStartRefresh)
thisExp.addData('coming_up_next_text.stopped', coming_up_next_text.tStopRefresh)

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
