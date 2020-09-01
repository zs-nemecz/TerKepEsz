#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.1.3),
    on August 27, 2020, at 16:17
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
expName = 'TRK-online'  # from the Builder filename that created this script
expInfo = {'Azonosító kód*': '', 'A vizsgálat feltételeibe beleegyezem. (igen/nem)*': '', 'Az adatkezelési feltételeket elfogadom. (igen/nem)*': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s_%s' % (expInfo['Azonosító kód*'],'pilot', expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='D:\\Zsuzsa\\HCCCL\\experiment\\computer_based_tasks\\terkepesz\\terkepesz_lastrun.py',
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

# Initialize components for Routine "experiment_information"
experiment_informationClock = core.Clock()
experiment_information_text = visual.TextStim(win=win, name='experiment_information_text',
    text='Kérjük, figyelmesen olvassa végig az alábbi instrukciókat!\n\nA vizsgálathoz használjon asztali számítógépet vagy laptopot. A vizsgálat nem végezhető el mobil eszközön, például okostelefonon vagy táblagépen. A feladatok elvégzéséhez szüksége lesz működő billentyűzetre és stabil internet kapcsolatra. Az optimális eredmény elérése érdekében Google Chrome, Firefox vagy Safari böngésző használata javasolt. Kérjük, használja a teljes képernyő módot.\nA kísérlet teljes körű, zavartalan figyelmet igényel. A vizsgálat két feladatból áll, és elvégzése 50-60 percet vesz igénybe. Bizonyosodjon meg róla, hogy elég időt tud szánni a vizsgálatra. Ügyeljen arra, hogy telefont, vagy más eszközöket közben ne használjon, és kerülje a másokkal való interakciót.\n\nA vizsgálat két feladatból áll, melyek során absztrakt képeket kell kiválogatnia a megadott szempontok szerint. A feladatok alatt és a feladatok között is lesz lehetősége rövid pihenőt tartani. \n\n\n',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
experiment_information_key = keyboard.Keyboard()
experiment_information_continue = visual.TextStim(win=win, name='experiment_information_continue',
    text='A folytatáshoz nyomja le a jobb nyilat. ',
    font='Arial',
    pos=(0, -0.4), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
proceed = False
consent = expInfo['A vizsgálat feltételeibe beleegyezem. (igen/nem)*']
dataprotection = expInfo['Az adatkezelési feltételeket elfogadom. (igen/nem)*']
consent_ok = False
data_ok = False

if consent == 'igen' or consent == 'i' or consent == 'Igen' or consent == 'I':
    consent_ok = True

if dataprotection == 'igen' or dataprotection == 'i' or dataprotection == 'Igen' or dataprotection == 'I':
    data_ok = True

if consent_ok & data_ok:
    proceed = True

if not proceed:
    core.quit()

# Initialize components for Routine "data_protection"
data_protectionClock = core.Clock()

# Initialize components for Routine "consent"
consentClock = core.Clock()

# Initialize components for Routine "lab_introduction"
lab_introductionClock = core.Clock()
lab_thanks = visual.TextStim(win=win, name='lab_thanks',
    text='Köszönjük, hogy hozzájárul kutatócsoportunk munkájához azzal, hogy részt vesz vizsgálatunkban!\n\n',
    font='Arial',
    pos=(0, 0.2), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
lab_key = keyboard.Keyboard()
lab_introduction_continue = visual.TextStim(win=win, name='lab_introduction_continue',
    text='A folytatáshoz nyomja le a jobb nyilat. ',
    font='Arial',
    pos=(0, 0.4), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
lab_members = visual.ImageStim(
    win=win,
    name='lab_members', units='norm', 
    image='stimuli/lab_members.jpg', mask=None,
    ori=0, pos=(0, -0.3704), size=(0.9458, 1.0),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)

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
    text='A folytatáshoz nyomja le a jobb nyilat. ',
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
    text='A folytatáshoz nyomja le a jobb nyilat. ',
    font='Arial',
    pos=(0,-0.4), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "enc_instructions_3"
enc_instructions_3Clock = core.Clock()
enc_instructions_3_text = visual.TextStim(win=win, name='enc_instructions_3_text',
    text="Az első feladat nagyjából 25 percet vesz igénybe, közben két rövid szünettel. Ügyeljen, hogy ezek a szünetek ne legyenek 2 percnél hosszabbak. \n\nA 'J' billentyűvel jelölje azokat a képeket, amelyek maradhatnak a galériában, a bemutatott helyen.\n\nAz 'F' billentyűvel jelölje a képeket, amelyek nem maradnak kiállítva a bemutatott helyen. \n\nMost a gyakorló feladat következik. \n",
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
    text='A folytatáshoz nyomja le a jobb nyilat. ',
    font='Arial',
    pos=(0,-0.4), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

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

# Initialize components for Routine "inter_task_break"
inter_task_breakClock = core.Clock()
inter_task_break_continue = visual.TextStim(win=win, name='inter_task_break_continue',
    text='Ha úgy érzi készen áll, nyomja le a jobb nyilat.',
    font='Arial',
    pos=(0,-0.4), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
inter_task_break_text = visual.TextStim(win=win, name='inter_task_break_text',
    text='Mielőtt tovább lépne a következő feladathoz, tartson egy rövid szünetet, hogy felfrissüljön. Ha teheti, álljon fel a számítógéptől, pihentesse szemeit, igyon egy pohár vizet. Ügyeljen, hogy ez a szünet ne tartson 10 percnél tovább. ',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
inter_task_break_key = keyboard.Keyboard()

# Initialize components for Routine "start_recognition"
start_recognitionClock = core.Clock()
start_recognition_text = visual.TextStim(win=win, name='start_recognition_text',
    text='Második feladat\nKépfelismerés',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "rec_instructions_1"
rec_instructions_1Clock = core.Clock()
rec_instructions_1_text = visual.TextStim(win=win, name='rec_instructions_1_text',
    text="A következő feladatban ismét absztrakt képeket fog látni, és ezekről kell eldöntenie, látta-e őket az első, 'Galéria berendezés' feladataban, és hogy ugyanott látta-e őket.\n\nA feladatot két alfeladatra bontottuk. Az egyikben a képekről, a másikban a képek pozíciójáról kell döntenie.",
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
    text="A Kép nevű alfeladatban azt kell eldöntenie, látta-e már ezeket a képeket a 'Galéria berendezés' feladataban.\n\nKét csoportba oszthatóak a megjelenő képek:\n - Régi: Ezek a képek pontosan megegyeznek a 'Galéria berendezés' feladatban látott képek egyikével.\n - Új: Képek, amelyek nem jelentek meg a 'Galéria berendezés' feladatban. Ezek a képek lehetnek hasonlóak a korábban látottakhoz.\n\nAz Ön feladata, hogy eldöntse, melyik kép ugyanaz, mint a 'Galéria berendezés' feladatban, és melyik új. \nA döntésre 4 másodperce lesz.\nMinden képet nézzen meg figyelmesen, és minden képre adjon választ, akkor is, ha a döntés nehéz.\n\nDöntését így jelölje:\nRégi - F\nÚj - J",
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
    text="A Hely nevű alfeladatban azt kell eldöntenie, a képek a képernyő ugyanazon pontján jelennek-e meg, mint a 'Galéria berendezés' feladataban.\nEbben az alfeladatban minden kép pontos mása annak, amit az első feladatban látott. \n\nA helyek azonban két csoportba oszthatóak:\n - Régi: Pontosan ugyanitt jelent meg ez a kép a 'Galéria berendezés' feladatban.\n - Új: Egy másik helyen jelent meg ez a kép a 'Galéria berendezés' feladatban. Ez a hely lehet közeli az eredeti helyhez.\n\nAz Ön feladata, hogy eldöntse, melyik kép jelent meg ugyanott, és melyik új helyen.\nA döntésre 4 másodperce lesz.\nMinden képet nézzen meg figyelmesen, és minden képre adjon választ, akkor is, ha a döntés nehéz.\n\nA döntését így jelölje:\nRégi - F\nÚj - J",
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
    text="A következőkben pár példával mutatjuk be Önnek, milyen hasonlóak lehetnek az új képek és helyek.\n\nA bemutatóban elsőként egy, a 'Galéria berendezés' feladat során már látott képet/helyet mutatunk Önnek, 'Régi' felirattal. \nA régi képet/helyet mindig egy új kép/hely követi a bemutatóban, 'Új' felirattal.\n",
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

# Initialize components for Routine "start_practice"
start_practiceClock = core.Clock()
start_practice_text = visual.TextStim(win=win, name='start_practice_text',
    text='Kezdődik a gyakorlás...',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "start_rec_practice_block"
start_rec_practice_blockClock = core.Clock()
rec_practice_block = [0,1,2]
block_name = "Kép"
block_counter = 0
rec_practice_block_text = visual.TextStim(win=win, name='rec_practice_block_text',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "rec_fx"
rec_fxClock = core.Clock()
rec_fx_interior = visual.ImageStim(
    win=win,
    name='rec_fx_interior', units='norm', 
    image='stimuli/GalleryInterior.png', mask=None,
    ori=0, pos=(0,0), size=(2.0, 2.0),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
rec_fx_cross = visual.TextStim(win=win, name='rec_fx_cross',
    text='+',
    font='Arial',
    units='norm', pos=[0,0], height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
rec_fx_key = keyboard.Keyboard()
rec_fx_text_block = visual.TextStim(win=win, name='rec_fx_text_block',
    text='default text',
    font='Arial',
    units='norm', pos=(0, 0.87), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
rec_fx_instructions_text = visual.TextStim(win=win, name='rec_fx_instructions_text',
    text='[F - Régi]      [J - Új]',
    font='Arial',
    units='norm', pos=(0, -0.833), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "rec_trial"
rec_trialClock = core.Clock()
rec_trial_interior = visual.ImageStim(
    win=win,
    name='rec_trial_interior', units='norm', 
    image='stimuli/GalleryInterior.png', mask=None,
    ori=0, pos=(0, -0), size=(2.0, 2.0),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
rec_trial_main_image = visual.ImageStim(
    win=win,
    name='rec_trial_main_image', units='norm', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
rec_trial_key = keyboard.Keyboard()
rec_trial_text_block = visual.TextStim(win=win, name='rec_trial_text_block',
    text='default text',
    font='Arial',
    units='norm', pos=(0, 0.87), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
rec_trial_instructions_text = visual.TextStim(win=win, name='rec_trial_instructions_text',
    text='[F - Régi]      [J - Új]',
    font='Arial',
    units='norm', pos=(0, -0.833), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "rec_practice_feedback"
rec_practice_feedbackClock = core.Clock()
rec_practice_feedback_text = visual.TextStim(win=win, name='rec_practice_feedback_text',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

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
    text='A folytatáshoz nyomja le a jobb nyilat. ',
    font='Arial',
    pos=(0,-0.4), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "start_rec_run"
start_rec_runClock = core.Clock()
start_rec_run_text = visual.TextStim(win=win, name='start_rec_run_text',
    text='Kezdődik a feladat...',
    font='Arial',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "start_rec_block"
start_rec_blockClock = core.Clock()
start_rec_block_text = visual.TextStim(win=win, name='start_rec_block_text',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "rec_fx"
rec_fxClock = core.Clock()
rec_fx_interior = visual.ImageStim(
    win=win,
    name='rec_fx_interior', units='norm', 
    image='stimuli/GalleryInterior.png', mask=None,
    ori=0, pos=(0,0), size=(2.0, 2.0),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
rec_fx_cross = visual.TextStim(win=win, name='rec_fx_cross',
    text='+',
    font='Arial',
    units='norm', pos=[0,0], height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
rec_fx_key = keyboard.Keyboard()
rec_fx_text_block = visual.TextStim(win=win, name='rec_fx_text_block',
    text='default text',
    font='Arial',
    units='norm', pos=(0, 0.87), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
rec_fx_instructions_text = visual.TextStim(win=win, name='rec_fx_instructions_text',
    text='[F - Régi]      [J - Új]',
    font='Arial',
    units='norm', pos=(0, -0.833), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "rec_trial"
rec_trialClock = core.Clock()
rec_trial_interior = visual.ImageStim(
    win=win,
    name='rec_trial_interior', units='norm', 
    image='stimuli/GalleryInterior.png', mask=None,
    ori=0, pos=(0, -0), size=(2.0, 2.0),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
rec_trial_main_image = visual.ImageStim(
    win=win,
    name='rec_trial_main_image', units='norm', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
rec_trial_key = keyboard.Keyboard()
rec_trial_text_block = visual.TextStim(win=win, name='rec_trial_text_block',
    text='default text',
    font='Arial',
    units='norm', pos=(0, 0.87), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
rec_trial_instructions_text = visual.TextStim(win=win, name='rec_trial_instructions_text',
    text='[F - Régi]      [J - Új]',
    font='Arial',
    units='norm', pos=(0, -0.833), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "end_rec_run"
end_rec_runClock = core.Clock()
end_rec_run_text = visual.TextStim(win=win, name='end_rec_run_text',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
end_rec_run_key = keyboard.Keyboard()

# Initialize components for Routine "end_experiment"
end_experimentClock = core.Clock()
end_experiment_text = visual.TextStim(win=win, name='end_experiment_text',
    text='Köszönjük a részvételt!\n\nJegyezze fel az alábbi kódot, amellyel a részvételét igazolja:',
    font='Arial',
    pos=(0, 0.15), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
code = np.random.randint(100000, high=999999)
end_experiment_code = visual.TextStim(win=win, name='end_experiment_code',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
end_experiment_continue = visual.TextStim(win=win, name='end_experiment_continue',
    text='A jobb nyíl lenyomásával megjelenik a vizsgálat végét jelző üzenet. Ezt fogadja el az OK gombbal, majd átirányítjuk egy felületre, ahol a kód megadásával igazolni tudja a részvételét.\nProbléma esetén írjon nekünk a terkep@ttk.hu email címen. ',
    font='Arial',
    pos=(0, -0.4), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
end_experiment_key = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "experiment_information"-------
continueRoutine = True
routineTimer.add(300.000000)
# update component parameters for each repeat
experiment_information_key.keys = []
experiment_information_key.rt = []
_experiment_information_key_allKeys = []
# keep track of which components have finished
experiment_informationComponents = [experiment_information_text, experiment_information_key, experiment_information_continue]
for thisComponent in experiment_informationComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
experiment_informationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "experiment_information"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = experiment_informationClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=experiment_informationClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *experiment_information_text* updates
    if experiment_information_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        experiment_information_text.frameNStart = frameN  # exact frame index
        experiment_information_text.tStart = t  # local t and not account for scr refresh
        experiment_information_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(experiment_information_text, 'tStartRefresh')  # time at next scr refresh
        experiment_information_text.setAutoDraw(True)
    if experiment_information_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > experiment_information_text.tStartRefresh + 300.0-frameTolerance:
            # keep track of stop time/frame for later
            experiment_information_text.tStop = t  # not accounting for scr refresh
            experiment_information_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(experiment_information_text, 'tStopRefresh')  # time at next scr refresh
            experiment_information_text.setAutoDraw(False)
    
    # *experiment_information_key* updates
    waitOnFlip = False
    if experiment_information_key.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
        # keep track of start time/frame for later
        experiment_information_key.frameNStart = frameN  # exact frame index
        experiment_information_key.tStart = t  # local t and not account for scr refresh
        experiment_information_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(experiment_information_key, 'tStartRefresh')  # time at next scr refresh
        experiment_information_key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(experiment_information_key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(experiment_information_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if experiment_information_key.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > experiment_information_key.tStartRefresh + 290.0-frameTolerance:
            # keep track of stop time/frame for later
            experiment_information_key.tStop = t  # not accounting for scr refresh
            experiment_information_key.frameNStop = frameN  # exact frame index
            win.timeOnFlip(experiment_information_key, 'tStopRefresh')  # time at next scr refresh
            experiment_information_key.status = FINISHED
    if experiment_information_key.status == STARTED and not waitOnFlip:
        theseKeys = experiment_information_key.getKeys(keyList=['right'], waitRelease=False)
        _experiment_information_key_allKeys.extend(theseKeys)
        if len(_experiment_information_key_allKeys):
            experiment_information_key.keys = _experiment_information_key_allKeys[-1].name  # just the last key pressed
            experiment_information_key.rt = _experiment_information_key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *experiment_information_continue* updates
    if experiment_information_continue.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
        # keep track of start time/frame for later
        experiment_information_continue.frameNStart = frameN  # exact frame index
        experiment_information_continue.tStart = t  # local t and not account for scr refresh
        experiment_information_continue.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(experiment_information_continue, 'tStartRefresh')  # time at next scr refresh
        experiment_information_continue.setAutoDraw(True)
    if experiment_information_continue.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > experiment_information_continue.tStartRefresh + 290.0-frameTolerance:
            # keep track of stop time/frame for later
            experiment_information_continue.tStop = t  # not accounting for scr refresh
            experiment_information_continue.frameNStop = frameN  # exact frame index
            win.timeOnFlip(experiment_information_continue, 'tStopRefresh')  # time at next scr refresh
            experiment_information_continue.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in experiment_informationComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "experiment_information"-------
for thisComponent in experiment_informationComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('experiment_information_text.started', experiment_information_text.tStartRefresh)
thisExp.addData('experiment_information_text.stopped', experiment_information_text.tStopRefresh)
# check responses
if experiment_information_key.keys in ['', [], None]:  # No response was made
    experiment_information_key.keys = None
thisExp.addData('experiment_information_key.keys',experiment_information_key.keys)
if experiment_information_key.keys != None:  # we had a response
    thisExp.addData('experiment_information_key.rt', experiment_information_key.rt)
thisExp.addData('experiment_information_key.started', experiment_information_key.tStartRefresh)
thisExp.addData('experiment_information_key.stopped', experiment_information_key.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('experiment_information_continue.started', experiment_information_continue.tStartRefresh)
thisExp.addData('experiment_information_continue.stopped', experiment_information_continue.tStopRefresh)

# ------Prepare to start Routine "data_protection"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
data_protectionComponents = []
for thisComponent in data_protectionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
data_protectionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "data_protection"-------
while continueRoutine:
    # get current time
    t = data_protectionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=data_protectionClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in data_protectionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "data_protection"-------
for thisComponent in data_protectionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "data_protection" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "consent"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
consentComponents = []
for thisComponent in consentComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
consentClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "consent"-------
while continueRoutine:
    # get current time
    t = consentClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=consentClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in consentComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "consent"-------
for thisComponent in consentComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "consent" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "lab_introduction"-------
continueRoutine = True
routineTimer.add(120.000000)
# update component parameters for each repeat
lab_key.keys = []
lab_key.rt = []
_lab_key_allKeys = []
# keep track of which components have finished
lab_introductionComponents = [lab_thanks, lab_key, lab_introduction_continue, lab_members]
for thisComponent in lab_introductionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
lab_introductionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "lab_introduction"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = lab_introductionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=lab_introductionClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *lab_thanks* updates
    if lab_thanks.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        lab_thanks.frameNStart = frameN  # exact frame index
        lab_thanks.tStart = t  # local t and not account for scr refresh
        lab_thanks.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(lab_thanks, 'tStartRefresh')  # time at next scr refresh
        lab_thanks.setAutoDraw(True)
    if lab_thanks.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > lab_thanks.tStartRefresh + 120.0-frameTolerance:
            # keep track of stop time/frame for later
            lab_thanks.tStop = t  # not accounting for scr refresh
            lab_thanks.frameNStop = frameN  # exact frame index
            win.timeOnFlip(lab_thanks, 'tStopRefresh')  # time at next scr refresh
            lab_thanks.setAutoDraw(False)
    
    # *lab_key* updates
    waitOnFlip = False
    if lab_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        lab_key.frameNStart = frameN  # exact frame index
        lab_key.tStart = t  # local t and not account for scr refresh
        lab_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(lab_key, 'tStartRefresh')  # time at next scr refresh
        lab_key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(lab_key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(lab_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if lab_key.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > lab_key.tStartRefresh + 120-frameTolerance:
            # keep track of stop time/frame for later
            lab_key.tStop = t  # not accounting for scr refresh
            lab_key.frameNStop = frameN  # exact frame index
            win.timeOnFlip(lab_key, 'tStopRefresh')  # time at next scr refresh
            lab_key.status = FINISHED
    if lab_key.status == STARTED and not waitOnFlip:
        theseKeys = lab_key.getKeys(keyList=['right'], waitRelease=False)
        _lab_key_allKeys.extend(theseKeys)
        if len(_lab_key_allKeys):
            lab_key.keys = _lab_key_allKeys[-1].name  # just the last key pressed
            lab_key.rt = _lab_key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *lab_introduction_continue* updates
    if lab_introduction_continue.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
        # keep track of start time/frame for later
        lab_introduction_continue.frameNStart = frameN  # exact frame index
        lab_introduction_continue.tStart = t  # local t and not account for scr refresh
        lab_introduction_continue.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(lab_introduction_continue, 'tStartRefresh')  # time at next scr refresh
        lab_introduction_continue.setAutoDraw(True)
    if lab_introduction_continue.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > lab_introduction_continue.tStartRefresh + 119.0-frameTolerance:
            # keep track of stop time/frame for later
            lab_introduction_continue.tStop = t  # not accounting for scr refresh
            lab_introduction_continue.frameNStop = frameN  # exact frame index
            win.timeOnFlip(lab_introduction_continue, 'tStopRefresh')  # time at next scr refresh
            lab_introduction_continue.setAutoDraw(False)
    
    # *lab_members* updates
    if lab_members.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        lab_members.frameNStart = frameN  # exact frame index
        lab_members.tStart = t  # local t and not account for scr refresh
        lab_members.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(lab_members, 'tStartRefresh')  # time at next scr refresh
        lab_members.setAutoDraw(True)
    if lab_members.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > lab_members.tStartRefresh + 120.0-frameTolerance:
            # keep track of stop time/frame for later
            lab_members.tStop = t  # not accounting for scr refresh
            lab_members.frameNStop = frameN  # exact frame index
            win.timeOnFlip(lab_members, 'tStopRefresh')  # time at next scr refresh
            lab_members.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in lab_introductionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "lab_introduction"-------
for thisComponent in lab_introductionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('lab_thanks.started', lab_thanks.tStartRefresh)
thisExp.addData('lab_thanks.stopped', lab_thanks.tStopRefresh)
# check responses
if lab_key.keys in ['', [], None]:  # No response was made
    lab_key.keys = None
thisExp.addData('lab_key.keys',lab_key.keys)
if lab_key.keys != None:  # we had a response
    thisExp.addData('lab_key.rt', lab_key.rt)
thisExp.addData('lab_key.started', lab_key.tStartRefresh)
thisExp.addData('lab_key.stopped', lab_key.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('lab_introduction_continue.started', lab_introduction_continue.tStartRefresh)
thisExp.addData('lab_introduction_continue.stopped', lab_introduction_continue.tStopRefresh)
thisExp.addData('lab_members.started', lab_members.tStartRefresh)
thisExp.addData('lab_members.stopped', lab_members.tStopRefresh)

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
enc_practice_trials = data.TrialHandler(nReps=1, method='sequential', 
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
            theseKeys = enc_fx_key.getKeys(keyList=['f', 'j'], waitRelease=False)
            _enc_fx_key_allKeys.extend(theseKeys)
            if len(_enc_fx_key_allKeys):
                enc_fx_key.keys = _enc_fx_key_allKeys[-1].name  # just the last key pressed
                enc_fx_key.rt = _enc_fx_key_allKeys[-1].rt
        
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
    enc_practice_trials.addData('enc_fx_interior.started', enc_fx_interior.tStartRefresh)
    enc_practice_trials.addData('enc_fx_interior.stopped', enc_fx_interior.tStopRefresh)
    enc_practice_trials.addData('enc_fx_cross.started', enc_fx_cross.tStartRefresh)
    enc_practice_trials.addData('enc_fx_cross.stopped', enc_fx_cross.tStopRefresh)
    # check responses
    if enc_fx_key.keys in ['', [], None]:  # No response was made
        enc_fx_key.keys = None
    enc_practice_trials.addData('enc_fx_key.keys',enc_fx_key.keys)
    if enc_fx_key.keys != None:  # we had a response
        enc_practice_trials.addData('enc_fx_key.rt', enc_fx_key.rt)
    enc_practice_trials.addData('enc_fx_key.started', enc_fx_key.tStartRefresh)
    enc_practice_trials.addData('enc_fx_key.stopped', enc_fx_key.tStopRefresh)
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
            theseKeys = enc_trial_key.getKeys(keyList=['f', 'j'], waitRelease=False)
            _enc_trial_key_allKeys.extend(theseKeys)
            if len(_enc_trial_key_allKeys):
                enc_trial_key.keys = _enc_trial_key_allKeys[-1].name  # just the last key pressed
                enc_trial_key.rt = _enc_trial_key_allKeys[-1].rt
        
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
    enc_practice_trials.addData('enc_trial_interior.started', enc_trial_interior.tStartRefresh)
    enc_practice_trials.addData('enc_trial_interior.stopped', enc_trial_interior.tStopRefresh)
    enc_practice_trials.addData('enc_trial_main_image.started', enc_trial_main_image.tStartRefresh)
    enc_practice_trials.addData('enc_trial_main_image.stopped', enc_trial_main_image.tStopRefresh)
    # check responses
    if enc_trial_key.keys in ['', [], None]:  # No response was made
        enc_trial_key.keys = None
    enc_practice_trials.addData('enc_trial_key.keys',enc_trial_key.keys)
    if enc_trial_key.keys != None:  # we had a response
        enc_practice_trials.addData('enc_trial_key.rt', enc_trial_key.rt)
    enc_practice_trials.addData('enc_trial_key.started', enc_trial_key.tStartRefresh)
    enc_practice_trials.addData('enc_trial_key.stopped', enc_trial_key.tStopRefresh)
    
    # ------Prepare to start Routine "enc_practice_feedback"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    response = enc_trial_key.keys
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
    
# completed 1 repeats of 'enc_practice_trials'


# ------Prepare to start Routine "end_practice"-------
continueRoutine = True
routineTimer.add(300.000000)
# update component parameters for each repeat
end_practice_key.keys = []
end_practice_key.rt = []
_end_practice_key_allKeys = []
block_counter = 0
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
enc_runs = data.TrialHandler(nReps=3, method='sequential', 
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
    
    # ------Prepare to start Routine "start_enc_run"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    start = end
    end = start + 3
    selection = np.arange(start, end, step)
    
    run_counter = run_counter + 1
    end_run_text = 'Rövid szünet\nA feladat folytatáshoz nyomja le a jobb nyilat'
    
    if run_counter >= 3:
        end_run_text = 'Vége az első feladatnak. A folytatáshoz nyomja le a jobb nyilat'
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
            if tThisFlipGlobal > start_enc_run_text.tStartRefresh + 2.0-frameTolerance:
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
                theseKeys = enc_fx_key.getKeys(keyList=['f', 'j'], waitRelease=False)
                _enc_fx_key_allKeys.extend(theseKeys)
                if len(_enc_fx_key_allKeys):
                    enc_fx_key.keys = _enc_fx_key_allKeys[-1].name  # just the last key pressed
                    enc_fx_key.rt = _enc_fx_key_allKeys[-1].rt
            
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
                theseKeys = enc_trial_key.getKeys(keyList=['f', 'j'], waitRelease=False)
                _enc_trial_key_allKeys.extend(theseKeys)
                if len(_enc_trial_key_allKeys):
                    enc_trial_key.keys = _enc_trial_key_allKeys[-1].name  # just the last key pressed
                    enc_trial_key.rt = _enc_trial_key_allKeys[-1].rt
            
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
    routineTimer.add(1200.000000)
    # update component parameters for each repeat
    end_enc_run_text.setText(end_run_text)
    enc_run_end_key.keys = []
    enc_run_end_key.rt = []
    _enc_run_end_key_allKeys = []
    # keep track of which components have finished
    end_enc_runComponents = [end_enc_run_text, enc_run_end_key]
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
            if tThisFlipGlobal > end_enc_run_text.tStartRefresh + 1200-frameTolerance:
                # keep track of stop time/frame for later
                end_enc_run_text.tStop = t  # not accounting for scr refresh
                end_enc_run_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(end_enc_run_text, 'tStopRefresh')  # time at next scr refresh
                end_enc_run_text.setAutoDraw(False)
        
        # *enc_run_end_key* updates
        waitOnFlip = False
        if enc_run_end_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
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
            if tThisFlipGlobal > enc_run_end_key.tStartRefresh + 1200-frameTolerance:
                # keep track of stop time/frame for later
                enc_run_end_key.tStop = t  # not accounting for scr refresh
                enc_run_end_key.frameNStop = frameN  # exact frame index
                win.timeOnFlip(enc_run_end_key, 'tStopRefresh')  # time at next scr refresh
                enc_run_end_key.status = FINISHED
        if enc_run_end_key.status == STARTED and not waitOnFlip:
            theseKeys = enc_run_end_key.getKeys(keyList=['right'], waitRelease=False)
            _enc_run_end_key_allKeys.extend(theseKeys)
            if len(_enc_run_end_key_allKeys):
                enc_run_end_key.keys = _enc_run_end_key_allKeys[-1].name  # just the last key pressed
                enc_run_end_key.rt = _enc_run_end_key_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
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
# completed 3 repeats of 'enc_runs'


# ------Prepare to start Routine "inter_task_break"-------
continueRoutine = True
routineTimer.add(1200.000000)
# update component parameters for each repeat
inter_task_break_key.keys = []
inter_task_break_key.rt = []
_inter_task_break_key_allKeys = []
# keep track of which components have finished
inter_task_breakComponents = [inter_task_break_continue, inter_task_break_text, inter_task_break_key]
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
    
    # *inter_task_break_continue* updates
    if inter_task_break_continue.status == NOT_STARTED and tThisFlip >= 5.0-frameTolerance:
        # keep track of start time/frame for later
        inter_task_break_continue.frameNStart = frameN  # exact frame index
        inter_task_break_continue.tStart = t  # local t and not account for scr refresh
        inter_task_break_continue.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(inter_task_break_continue, 'tStartRefresh')  # time at next scr refresh
        inter_task_break_continue.setAutoDraw(True)
    if inter_task_break_continue.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > inter_task_break_continue.tStartRefresh + 1195.0-frameTolerance:
            # keep track of stop time/frame for later
            inter_task_break_continue.tStop = t  # not accounting for scr refresh
            inter_task_break_continue.frameNStop = frameN  # exact frame index
            win.timeOnFlip(inter_task_break_continue, 'tStopRefresh')  # time at next scr refresh
            inter_task_break_continue.setAutoDraw(False)
    
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
        if tThisFlipGlobal > inter_task_break_text.tStartRefresh + 1200.0-frameTolerance:
            # keep track of stop time/frame for later
            inter_task_break_text.tStop = t  # not accounting for scr refresh
            inter_task_break_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(inter_task_break_text, 'tStopRefresh')  # time at next scr refresh
            inter_task_break_text.setAutoDraw(False)
    
    # *inter_task_break_key* updates
    waitOnFlip = False
    if inter_task_break_key.status == NOT_STARTED and tThisFlip >= 5.0-frameTolerance:
        # keep track of start time/frame for later
        inter_task_break_key.frameNStart = frameN  # exact frame index
        inter_task_break_key.tStart = t  # local t and not account for scr refresh
        inter_task_break_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(inter_task_break_key, 'tStartRefresh')  # time at next scr refresh
        inter_task_break_key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(inter_task_break_key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(inter_task_break_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if inter_task_break_key.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > inter_task_break_key.tStartRefresh + 1195-frameTolerance:
            # keep track of stop time/frame for later
            inter_task_break_key.tStop = t  # not accounting for scr refresh
            inter_task_break_key.frameNStop = frameN  # exact frame index
            win.timeOnFlip(inter_task_break_key, 'tStopRefresh')  # time at next scr refresh
            inter_task_break_key.status = FINISHED
    if inter_task_break_key.status == STARTED and not waitOnFlip:
        theseKeys = inter_task_break_key.getKeys(keyList=['right'], waitRelease=False)
        _inter_task_break_key_allKeys.extend(theseKeys)
        if len(_inter_task_break_key_allKeys):
            inter_task_break_key.keys = _inter_task_break_key_allKeys[-1].name  # just the last key pressed
            inter_task_break_key.rt = _inter_task_break_key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
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
thisExp.addData('inter_task_break_continue.started', inter_task_break_continue.tStartRefresh)
thisExp.addData('inter_task_break_continue.stopped', inter_task_break_continue.tStopRefresh)
thisExp.addData('inter_task_break_text.started', inter_task_break_text.tStartRefresh)
thisExp.addData('inter_task_break_text.stopped', inter_task_break_text.tStopRefresh)
# check responses
if inter_task_break_key.keys in ['', [], None]:  # No response was made
    inter_task_break_key.keys = None
thisExp.addData('inter_task_break_key.keys',inter_task_break_key.keys)
if inter_task_break_key.keys != None:  # we had a response
    thisExp.addData('inter_task_break_key.rt', inter_task_break_key.rt)
thisExp.addData('inter_task_break_key.started', inter_task_break_key.tStartRefresh)
thisExp.addData('inter_task_break_key.stopped', inter_task_break_key.tStopRefresh)
thisExp.nextEntry()

# ------Prepare to start Routine "start_recognition"-------
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
start = 0
end = 0
step = 1
n_runs = 4
run_counter = 0
stimuli_table = 'stimuli_tables/recognition_trials_'+ trial_table + '.csv'
# keep track of which components have finished
start_recognitionComponents = [start_recognition_text]
for thisComponent in start_recognitionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
start_recognitionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "start_recognition"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = start_recognitionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=start_recognitionClock)
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
        if tThisFlipGlobal > start_recognition_text.tStartRefresh + 2.0-frameTolerance:
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
    for thisComponent in start_recognitionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "start_recognition"-------
for thisComponent in start_recognitionComponents:
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
rec_practice_blocks = data.TrialHandler(nReps=2, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
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
    
    # ------Prepare to start Routine "start_rec_practice_block"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    block_counter = block_counter + 1
    if block_counter >= 2:
        rec_practice_block = [3,4,5]
        block_name = "Hely"
    
    rec_practice_block_text.setText(block_name)
    # keep track of which components have finished
    start_rec_practice_blockComponents = [rec_practice_block_text]
    for thisComponent in start_rec_practice_blockComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    start_rec_practice_blockClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "start_rec_practice_block"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = start_rec_practice_blockClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=start_rec_practice_blockClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *rec_practice_block_text* updates
        if rec_practice_block_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rec_practice_block_text.frameNStart = frameN  # exact frame index
            rec_practice_block_text.tStart = t  # local t and not account for scr refresh
            rec_practice_block_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rec_practice_block_text, 'tStartRefresh')  # time at next scr refresh
            rec_practice_block_text.setAutoDraw(True)
        if rec_practice_block_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > rec_practice_block_text.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                rec_practice_block_text.tStop = t  # not accounting for scr refresh
                rec_practice_block_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(rec_practice_block_text, 'tStopRefresh')  # time at next scr refresh
                rec_practice_block_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in start_rec_practice_blockComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "start_rec_practice_block"-------
    for thisComponent in start_rec_practice_blockComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    rec_practice_blocks.addData('rec_practice_block_text.started', rec_practice_block_text.tStartRefresh)
    rec_practice_blocks.addData('rec_practice_block_text.stopped', rec_practice_block_text.tStopRefresh)
    
    # set up handler to look after randomisation of conditions etc
    rec_practice_trials = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('stimuli_tables/recognition_practice_trials.csv', selection=rec_practice_block),
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
        
        # ------Prepare to start Routine "rec_fx"-------
        continueRoutine = True
        # update component parameters for each repeat
        rec_fx_cross.setPos((CurrentX, CurrentY))
        rec_fx_key.keys = []
        rec_fx_key.rt = []
        _rec_fx_key_allKeys = []
        rec_fx_text_block.setText(block_name
)
        # keep track of which components have finished
        rec_fxComponents = [rec_fx_interior, rec_fx_cross, rec_fx_key, rec_fx_text_block, rec_fx_instructions_text]
        for thisComponent in rec_fxComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        rec_fxClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "rec_fx"-------
        while continueRoutine:
            # get current time
            t = rec_fxClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=rec_fxClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *rec_fx_interior* updates
            if rec_fx_interior.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rec_fx_interior.frameNStart = frameN  # exact frame index
                rec_fx_interior.tStart = t  # local t and not account for scr refresh
                rec_fx_interior.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rec_fx_interior, 'tStartRefresh')  # time at next scr refresh
                rec_fx_interior.setAutoDraw(True)
            if rec_fx_interior.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > rec_fx_interior.tStartRefresh + Jitter/1000-frameTolerance:
                    # keep track of stop time/frame for later
                    rec_fx_interior.tStop = t  # not accounting for scr refresh
                    rec_fx_interior.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(rec_fx_interior, 'tStopRefresh')  # time at next scr refresh
                    rec_fx_interior.setAutoDraw(False)
            
            # *rec_fx_cross* updates
            if rec_fx_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rec_fx_cross.frameNStart = frameN  # exact frame index
                rec_fx_cross.tStart = t  # local t and not account for scr refresh
                rec_fx_cross.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rec_fx_cross, 'tStartRefresh')  # time at next scr refresh
                rec_fx_cross.setAutoDraw(True)
            if rec_fx_cross.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > rec_fx_cross.tStartRefresh + Jitter/1000-frameTolerance:
                    # keep track of stop time/frame for later
                    rec_fx_cross.tStop = t  # not accounting for scr refresh
                    rec_fx_cross.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(rec_fx_cross, 'tStopRefresh')  # time at next scr refresh
                    rec_fx_cross.setAutoDraw(False)
            
            # *rec_fx_key* updates
            waitOnFlip = False
            if rec_fx_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rec_fx_key.frameNStart = frameN  # exact frame index
                rec_fx_key.tStart = t  # local t and not account for scr refresh
                rec_fx_key.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rec_fx_key, 'tStartRefresh')  # time at next scr refresh
                rec_fx_key.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(rec_fx_key.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(rec_fx_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if rec_fx_key.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > rec_fx_key.tStartRefresh + Jitter/1000-frameTolerance:
                    # keep track of stop time/frame for later
                    rec_fx_key.tStop = t  # not accounting for scr refresh
                    rec_fx_key.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(rec_fx_key, 'tStopRefresh')  # time at next scr refresh
                    rec_fx_key.status = FINISHED
            if rec_fx_key.status == STARTED and not waitOnFlip:
                theseKeys = rec_fx_key.getKeys(keyList=['f', 'j'], waitRelease=False)
                _rec_fx_key_allKeys.extend(theseKeys)
                if len(_rec_fx_key_allKeys):
                    rec_fx_key.keys = _rec_fx_key_allKeys[-1].name  # just the last key pressed
                    rec_fx_key.rt = _rec_fx_key_allKeys[-1].rt
            
            # *rec_fx_text_block* updates
            if rec_fx_text_block.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rec_fx_text_block.frameNStart = frameN  # exact frame index
                rec_fx_text_block.tStart = t  # local t and not account for scr refresh
                rec_fx_text_block.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rec_fx_text_block, 'tStartRefresh')  # time at next scr refresh
                rec_fx_text_block.setAutoDraw(True)
            if rec_fx_text_block.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > rec_fx_text_block.tStartRefresh + Jitter/1000-frameTolerance:
                    # keep track of stop time/frame for later
                    rec_fx_text_block.tStop = t  # not accounting for scr refresh
                    rec_fx_text_block.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(rec_fx_text_block, 'tStopRefresh')  # time at next scr refresh
                    rec_fx_text_block.setAutoDraw(False)
            
            # *rec_fx_instructions_text* updates
            if rec_fx_instructions_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rec_fx_instructions_text.frameNStart = frameN  # exact frame index
                rec_fx_instructions_text.tStart = t  # local t and not account for scr refresh
                rec_fx_instructions_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rec_fx_instructions_text, 'tStartRefresh')  # time at next scr refresh
                rec_fx_instructions_text.setAutoDraw(True)
            if rec_fx_instructions_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > rec_fx_instructions_text.tStartRefresh + Jitter/1000-frameTolerance:
                    # keep track of stop time/frame for later
                    rec_fx_instructions_text.tStop = t  # not accounting for scr refresh
                    rec_fx_instructions_text.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(rec_fx_instructions_text, 'tStopRefresh')  # time at next scr refresh
                    rec_fx_instructions_text.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in rec_fxComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "rec_fx"-------
        for thisComponent in rec_fxComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        rec_practice_trials.addData('rec_fx_interior.started', rec_fx_interior.tStartRefresh)
        rec_practice_trials.addData('rec_fx_interior.stopped', rec_fx_interior.tStopRefresh)
        rec_practice_trials.addData('rec_fx_cross.started', rec_fx_cross.tStartRefresh)
        rec_practice_trials.addData('rec_fx_cross.stopped', rec_fx_cross.tStopRefresh)
        # check responses
        if rec_fx_key.keys in ['', [], None]:  # No response was made
            rec_fx_key.keys = None
        rec_practice_trials.addData('rec_fx_key.keys',rec_fx_key.keys)
        if rec_fx_key.keys != None:  # we had a response
            rec_practice_trials.addData('rec_fx_key.rt', rec_fx_key.rt)
        rec_practice_trials.addData('rec_fx_key.started', rec_fx_key.tStartRefresh)
        rec_practice_trials.addData('rec_fx_key.stopped', rec_fx_key.tStopRefresh)
        rec_practice_trials.addData('rec_fx_text_block.started', rec_fx_text_block.tStartRefresh)
        rec_practice_trials.addData('rec_fx_text_block.stopped', rec_fx_text_block.tStopRefresh)
        rec_practice_trials.addData('rec_fx_instructions_text.started', rec_fx_instructions_text.tStartRefresh)
        rec_practice_trials.addData('rec_fx_instructions_text.stopped', rec_fx_instructions_text.tStopRefresh)
        # the Routine "rec_fx" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "rec_trial"-------
        continueRoutine = True
        routineTimer.add(4.000000)
        # update component parameters for each repeat
        rec_trial_main_image.setPos((CurrentX, CurrentY))
        rec_trial_main_image.setSize((0.3125, 0.3125*scr_resolution))
        rec_trial_main_image.setImage(CurrentImage)
        rec_trial_key.keys = []
        rec_trial_key.rt = []
        _rec_trial_key_allKeys = []
        rec_trial_text_block.setText(block_name)
        # keep track of which components have finished
        rec_trialComponents = [rec_trial_interior, rec_trial_main_image, rec_trial_key, rec_trial_text_block, rec_trial_instructions_text]
        for thisComponent in rec_trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        rec_trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "rec_trial"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = rec_trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=rec_trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *rec_trial_interior* updates
            if rec_trial_interior.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rec_trial_interior.frameNStart = frameN  # exact frame index
                rec_trial_interior.tStart = t  # local t and not account for scr refresh
                rec_trial_interior.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rec_trial_interior, 'tStartRefresh')  # time at next scr refresh
                rec_trial_interior.setAutoDraw(True)
            if rec_trial_interior.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > rec_trial_interior.tStartRefresh + 4.0-frameTolerance:
                    # keep track of stop time/frame for later
                    rec_trial_interior.tStop = t  # not accounting for scr refresh
                    rec_trial_interior.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(rec_trial_interior, 'tStopRefresh')  # time at next scr refresh
                    rec_trial_interior.setAutoDraw(False)
            
            # *rec_trial_main_image* updates
            if rec_trial_main_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rec_trial_main_image.frameNStart = frameN  # exact frame index
                rec_trial_main_image.tStart = t  # local t and not account for scr refresh
                rec_trial_main_image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rec_trial_main_image, 'tStartRefresh')  # time at next scr refresh
                rec_trial_main_image.setAutoDraw(True)
            if rec_trial_main_image.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > rec_trial_main_image.tStartRefresh + 4.0-frameTolerance:
                    # keep track of stop time/frame for later
                    rec_trial_main_image.tStop = t  # not accounting for scr refresh
                    rec_trial_main_image.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(rec_trial_main_image, 'tStopRefresh')  # time at next scr refresh
                    rec_trial_main_image.setAutoDraw(False)
            
            # *rec_trial_key* updates
            waitOnFlip = False
            if rec_trial_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rec_trial_key.frameNStart = frameN  # exact frame index
                rec_trial_key.tStart = t  # local t and not account for scr refresh
                rec_trial_key.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rec_trial_key, 'tStartRefresh')  # time at next scr refresh
                rec_trial_key.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(rec_trial_key.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(rec_trial_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if rec_trial_key.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > rec_trial_key.tStartRefresh + 4.0-frameTolerance:
                    # keep track of stop time/frame for later
                    rec_trial_key.tStop = t  # not accounting for scr refresh
                    rec_trial_key.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(rec_trial_key, 'tStopRefresh')  # time at next scr refresh
                    rec_trial_key.status = FINISHED
            if rec_trial_key.status == STARTED and not waitOnFlip:
                theseKeys = rec_trial_key.getKeys(keyList=['f', 'j'], waitRelease=False)
                _rec_trial_key_allKeys.extend(theseKeys)
                if len(_rec_trial_key_allKeys):
                    rec_trial_key.keys = _rec_trial_key_allKeys[-1].name  # just the last key pressed
                    rec_trial_key.rt = _rec_trial_key_allKeys[-1].rt
            
            # *rec_trial_text_block* updates
            if rec_trial_text_block.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rec_trial_text_block.frameNStart = frameN  # exact frame index
                rec_trial_text_block.tStart = t  # local t and not account for scr refresh
                rec_trial_text_block.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rec_trial_text_block, 'tStartRefresh')  # time at next scr refresh
                rec_trial_text_block.setAutoDraw(True)
            if rec_trial_text_block.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > rec_trial_text_block.tStartRefresh + 4.0-frameTolerance:
                    # keep track of stop time/frame for later
                    rec_trial_text_block.tStop = t  # not accounting for scr refresh
                    rec_trial_text_block.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(rec_trial_text_block, 'tStopRefresh')  # time at next scr refresh
                    rec_trial_text_block.setAutoDraw(False)
            
            # *rec_trial_instructions_text* updates
            if rec_trial_instructions_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rec_trial_instructions_text.frameNStart = frameN  # exact frame index
                rec_trial_instructions_text.tStart = t  # local t and not account for scr refresh
                rec_trial_instructions_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rec_trial_instructions_text, 'tStartRefresh')  # time at next scr refresh
                rec_trial_instructions_text.setAutoDraw(True)
            if rec_trial_instructions_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > rec_trial_instructions_text.tStartRefresh + 4.0-frameTolerance:
                    # keep track of stop time/frame for later
                    rec_trial_instructions_text.tStop = t  # not accounting for scr refresh
                    rec_trial_instructions_text.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(rec_trial_instructions_text, 'tStopRefresh')  # time at next scr refresh
                    rec_trial_instructions_text.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in rec_trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "rec_trial"-------
        for thisComponent in rec_trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        rec_practice_trials.addData('rec_trial_interior.started', rec_trial_interior.tStartRefresh)
        rec_practice_trials.addData('rec_trial_interior.stopped', rec_trial_interior.tStopRefresh)
        rec_practice_trials.addData('rec_trial_main_image.started', rec_trial_main_image.tStartRefresh)
        rec_practice_trials.addData('rec_trial_main_image.stopped', rec_trial_main_image.tStopRefresh)
        # check responses
        if rec_trial_key.keys in ['', [], None]:  # No response was made
            rec_trial_key.keys = None
        rec_practice_trials.addData('rec_trial_key.keys',rec_trial_key.keys)
        if rec_trial_key.keys != None:  # we had a response
            rec_practice_trials.addData('rec_trial_key.rt', rec_trial_key.rt)
        rec_practice_trials.addData('rec_trial_key.started', rec_trial_key.tStartRefresh)
        rec_practice_trials.addData('rec_trial_key.stopped', rec_trial_key.tStopRefresh)
        rec_practice_trials.addData('rec_trial_text_block.started', rec_trial_text_block.tStartRefresh)
        rec_practice_trials.addData('rec_trial_text_block.stopped', rec_trial_text_block.tStopRefresh)
        rec_practice_trials.addData('rec_trial_instructions_text.started', rec_trial_instructions_text.tStartRefresh)
        rec_practice_trials.addData('rec_trial_instructions_text.stopped', rec_trial_instructions_text.tStopRefresh)
        
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
        if rec_trial_key.keys == 'f':
            response = 'Az Ön válasza: Régi'
        
        elif rec_trial_key.keys == 'j':
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
    
# completed 2 repeats of 'rec_practice_blocks'


# ------Prepare to start Routine "end_practice"-------
continueRoutine = True
routineTimer.add(300.000000)
# update component parameters for each repeat
end_practice_key.keys = []
end_practice_key.rt = []
_end_practice_key_allKeys = []
block_counter = 0
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
rec_runs = data.TrialHandler(nReps=4, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='rec_runs')
thisExp.addLoop(rec_runs)  # add the loop to the experiment
thisRec_run = rec_runs.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisRec_run.rgb)
if thisRec_run != None:
    for paramName in thisRec_run:
        exec('{} = thisRec_run[paramName]'.format(paramName))

for thisRec_run in rec_runs:
    currentLoop = rec_runs
    # abbreviate parameter names if possible (e.g. rgb = thisRec_run.rgb)
    if thisRec_run != None:
        for paramName in thisRec_run:
            exec('{} = thisRec_run[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "start_rec_run"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    run_counter = run_counter + 1
    end_run_text = 'Szünet\nA feladat folytatáshoz nyomja le a jobb nyilat'
    
    if run_counter >= n_runs:
        end_run_text = 'Vége a második feladatnak. Felteszünk Önnek pár kérdést, majd megkapja a vizsgálat befejezését igazoló kódot.\nHaladjon tovább a jobb nyíllal.'
    # keep track of which components have finished
    start_rec_runComponents = [start_rec_run_text]
    for thisComponent in start_rec_runComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    start_rec_runClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "start_rec_run"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = start_rec_runClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=start_rec_runClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *start_rec_run_text* updates
        if start_rec_run_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            start_rec_run_text.frameNStart = frameN  # exact frame index
            start_rec_run_text.tStart = t  # local t and not account for scr refresh
            start_rec_run_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(start_rec_run_text, 'tStartRefresh')  # time at next scr refresh
            start_rec_run_text.setAutoDraw(True)
        if start_rec_run_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > start_rec_run_text.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                start_rec_run_text.tStop = t  # not accounting for scr refresh
                start_rec_run_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(start_rec_run_text, 'tStopRefresh')  # time at next scr refresh
                start_rec_run_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in start_rec_runComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "start_rec_run"-------
    for thisComponent in start_rec_runComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    rec_runs.addData('start_rec_run_text.started', start_rec_run_text.tStartRefresh)
    rec_runs.addData('start_rec_run_text.stopped', start_rec_run_text.tStopRefresh)
    
    # set up handler to look after randomisation of conditions etc
    rec_blocks = data.TrialHandler(nReps=2, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='rec_blocks')
    thisExp.addLoop(rec_blocks)  # add the loop to the experiment
    thisRec_block = rec_blocks.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisRec_block.rgb)
    if thisRec_block != None:
        for paramName in thisRec_block:
            exec('{} = thisRec_block[paramName]'.format(paramName))
    
    for thisRec_block in rec_blocks:
        currentLoop = rec_blocks
        # abbreviate parameter names if possible (e.g. rgb = thisRec_block.rgb)
        if thisRec_block != None:
            for paramName in thisRec_block:
                exec('{} = thisRec_block[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "start_rec_block"-------
        continueRoutine = True
        routineTimer.add(1.500000)
        # update component parameters for each repeat
        start = end
        end = start + 3
        selection = np.arange(start,end, step)
        if block_counter == 0:
            block_name = "Kép"
        else:
            if TrialType == "LOC":
                block_name = "Kép"
            else: 
                block_name = "Hely"
        block_counter = block_counter + 1
        start_rec_block_text.setText(block_name)
        # keep track of which components have finished
        start_rec_blockComponents = [start_rec_block_text]
        for thisComponent in start_rec_blockComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        start_rec_blockClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "start_rec_block"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = start_rec_blockClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=start_rec_blockClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *start_rec_block_text* updates
            if start_rec_block_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                start_rec_block_text.frameNStart = frameN  # exact frame index
                start_rec_block_text.tStart = t  # local t and not account for scr refresh
                start_rec_block_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(start_rec_block_text, 'tStartRefresh')  # time at next scr refresh
                start_rec_block_text.setAutoDraw(True)
            if start_rec_block_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > start_rec_block_text.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    start_rec_block_text.tStop = t  # not accounting for scr refresh
                    start_rec_block_text.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(start_rec_block_text, 'tStopRefresh')  # time at next scr refresh
                    start_rec_block_text.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in start_rec_blockComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "start_rec_block"-------
        for thisComponent in start_rec_blockComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        rec_blocks.addData('start_rec_block_text.started', start_rec_block_text.tStartRefresh)
        rec_blocks.addData('start_rec_block_text.stopped', start_rec_block_text.tStopRefresh)
        
        # set up handler to look after randomisation of conditions etc
        rec_trials = data.TrialHandler(nReps=1, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions(stimuli_table, selection=selection),
            seed=None, name='rec_trials')
        thisExp.addLoop(rec_trials)  # add the loop to the experiment
        thisRec_trial = rec_trials.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisRec_trial.rgb)
        if thisRec_trial != None:
            for paramName in thisRec_trial:
                exec('{} = thisRec_trial[paramName]'.format(paramName))
        
        for thisRec_trial in rec_trials:
            currentLoop = rec_trials
            # abbreviate parameter names if possible (e.g. rgb = thisRec_trial.rgb)
            if thisRec_trial != None:
                for paramName in thisRec_trial:
                    exec('{} = thisRec_trial[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "rec_fx"-------
            continueRoutine = True
            # update component parameters for each repeat
            rec_fx_cross.setPos((CurrentX, CurrentY))
            rec_fx_key.keys = []
            rec_fx_key.rt = []
            _rec_fx_key_allKeys = []
            rec_fx_text_block.setText(block_name
)
            # keep track of which components have finished
            rec_fxComponents = [rec_fx_interior, rec_fx_cross, rec_fx_key, rec_fx_text_block, rec_fx_instructions_text]
            for thisComponent in rec_fxComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            rec_fxClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "rec_fx"-------
            while continueRoutine:
                # get current time
                t = rec_fxClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=rec_fxClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *rec_fx_interior* updates
                if rec_fx_interior.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    rec_fx_interior.frameNStart = frameN  # exact frame index
                    rec_fx_interior.tStart = t  # local t and not account for scr refresh
                    rec_fx_interior.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(rec_fx_interior, 'tStartRefresh')  # time at next scr refresh
                    rec_fx_interior.setAutoDraw(True)
                if rec_fx_interior.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > rec_fx_interior.tStartRefresh + Jitter/1000-frameTolerance:
                        # keep track of stop time/frame for later
                        rec_fx_interior.tStop = t  # not accounting for scr refresh
                        rec_fx_interior.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(rec_fx_interior, 'tStopRefresh')  # time at next scr refresh
                        rec_fx_interior.setAutoDraw(False)
                
                # *rec_fx_cross* updates
                if rec_fx_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    rec_fx_cross.frameNStart = frameN  # exact frame index
                    rec_fx_cross.tStart = t  # local t and not account for scr refresh
                    rec_fx_cross.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(rec_fx_cross, 'tStartRefresh')  # time at next scr refresh
                    rec_fx_cross.setAutoDraw(True)
                if rec_fx_cross.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > rec_fx_cross.tStartRefresh + Jitter/1000-frameTolerance:
                        # keep track of stop time/frame for later
                        rec_fx_cross.tStop = t  # not accounting for scr refresh
                        rec_fx_cross.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(rec_fx_cross, 'tStopRefresh')  # time at next scr refresh
                        rec_fx_cross.setAutoDraw(False)
                
                # *rec_fx_key* updates
                waitOnFlip = False
                if rec_fx_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    rec_fx_key.frameNStart = frameN  # exact frame index
                    rec_fx_key.tStart = t  # local t and not account for scr refresh
                    rec_fx_key.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(rec_fx_key, 'tStartRefresh')  # time at next scr refresh
                    rec_fx_key.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(rec_fx_key.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(rec_fx_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if rec_fx_key.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > rec_fx_key.tStartRefresh + Jitter/1000-frameTolerance:
                        # keep track of stop time/frame for later
                        rec_fx_key.tStop = t  # not accounting for scr refresh
                        rec_fx_key.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(rec_fx_key, 'tStopRefresh')  # time at next scr refresh
                        rec_fx_key.status = FINISHED
                if rec_fx_key.status == STARTED and not waitOnFlip:
                    theseKeys = rec_fx_key.getKeys(keyList=['f', 'j'], waitRelease=False)
                    _rec_fx_key_allKeys.extend(theseKeys)
                    if len(_rec_fx_key_allKeys):
                        rec_fx_key.keys = _rec_fx_key_allKeys[-1].name  # just the last key pressed
                        rec_fx_key.rt = _rec_fx_key_allKeys[-1].rt
                
                # *rec_fx_text_block* updates
                if rec_fx_text_block.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    rec_fx_text_block.frameNStart = frameN  # exact frame index
                    rec_fx_text_block.tStart = t  # local t and not account for scr refresh
                    rec_fx_text_block.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(rec_fx_text_block, 'tStartRefresh')  # time at next scr refresh
                    rec_fx_text_block.setAutoDraw(True)
                if rec_fx_text_block.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > rec_fx_text_block.tStartRefresh + Jitter/1000-frameTolerance:
                        # keep track of stop time/frame for later
                        rec_fx_text_block.tStop = t  # not accounting for scr refresh
                        rec_fx_text_block.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(rec_fx_text_block, 'tStopRefresh')  # time at next scr refresh
                        rec_fx_text_block.setAutoDraw(False)
                
                # *rec_fx_instructions_text* updates
                if rec_fx_instructions_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    rec_fx_instructions_text.frameNStart = frameN  # exact frame index
                    rec_fx_instructions_text.tStart = t  # local t and not account for scr refresh
                    rec_fx_instructions_text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(rec_fx_instructions_text, 'tStartRefresh')  # time at next scr refresh
                    rec_fx_instructions_text.setAutoDraw(True)
                if rec_fx_instructions_text.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > rec_fx_instructions_text.tStartRefresh + Jitter/1000-frameTolerance:
                        # keep track of stop time/frame for later
                        rec_fx_instructions_text.tStop = t  # not accounting for scr refresh
                        rec_fx_instructions_text.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(rec_fx_instructions_text, 'tStopRefresh')  # time at next scr refresh
                        rec_fx_instructions_text.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in rec_fxComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "rec_fx"-------
            for thisComponent in rec_fxComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            rec_trials.addData('rec_fx_interior.started', rec_fx_interior.tStartRefresh)
            rec_trials.addData('rec_fx_interior.stopped', rec_fx_interior.tStopRefresh)
            rec_trials.addData('rec_fx_cross.started', rec_fx_cross.tStartRefresh)
            rec_trials.addData('rec_fx_cross.stopped', rec_fx_cross.tStopRefresh)
            # check responses
            if rec_fx_key.keys in ['', [], None]:  # No response was made
                rec_fx_key.keys = None
            rec_trials.addData('rec_fx_key.keys',rec_fx_key.keys)
            if rec_fx_key.keys != None:  # we had a response
                rec_trials.addData('rec_fx_key.rt', rec_fx_key.rt)
            rec_trials.addData('rec_fx_key.started', rec_fx_key.tStartRefresh)
            rec_trials.addData('rec_fx_key.stopped', rec_fx_key.tStopRefresh)
            rec_trials.addData('rec_fx_text_block.started', rec_fx_text_block.tStartRefresh)
            rec_trials.addData('rec_fx_text_block.stopped', rec_fx_text_block.tStopRefresh)
            rec_trials.addData('rec_fx_instructions_text.started', rec_fx_instructions_text.tStartRefresh)
            rec_trials.addData('rec_fx_instructions_text.stopped', rec_fx_instructions_text.tStopRefresh)
            # the Routine "rec_fx" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # ------Prepare to start Routine "rec_trial"-------
            continueRoutine = True
            routineTimer.add(4.000000)
            # update component parameters for each repeat
            rec_trial_main_image.setPos((CurrentX, CurrentY))
            rec_trial_main_image.setSize((0.3125, 0.3125*scr_resolution))
            rec_trial_main_image.setImage(CurrentImage)
            rec_trial_key.keys = []
            rec_trial_key.rt = []
            _rec_trial_key_allKeys = []
            rec_trial_text_block.setText(block_name)
            # keep track of which components have finished
            rec_trialComponents = [rec_trial_interior, rec_trial_main_image, rec_trial_key, rec_trial_text_block, rec_trial_instructions_text]
            for thisComponent in rec_trialComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            rec_trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "rec_trial"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = rec_trialClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=rec_trialClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *rec_trial_interior* updates
                if rec_trial_interior.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    rec_trial_interior.frameNStart = frameN  # exact frame index
                    rec_trial_interior.tStart = t  # local t and not account for scr refresh
                    rec_trial_interior.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(rec_trial_interior, 'tStartRefresh')  # time at next scr refresh
                    rec_trial_interior.setAutoDraw(True)
                if rec_trial_interior.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > rec_trial_interior.tStartRefresh + 4.0-frameTolerance:
                        # keep track of stop time/frame for later
                        rec_trial_interior.tStop = t  # not accounting for scr refresh
                        rec_trial_interior.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(rec_trial_interior, 'tStopRefresh')  # time at next scr refresh
                        rec_trial_interior.setAutoDraw(False)
                
                # *rec_trial_main_image* updates
                if rec_trial_main_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    rec_trial_main_image.frameNStart = frameN  # exact frame index
                    rec_trial_main_image.tStart = t  # local t and not account for scr refresh
                    rec_trial_main_image.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(rec_trial_main_image, 'tStartRefresh')  # time at next scr refresh
                    rec_trial_main_image.setAutoDraw(True)
                if rec_trial_main_image.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > rec_trial_main_image.tStartRefresh + 4.0-frameTolerance:
                        # keep track of stop time/frame for later
                        rec_trial_main_image.tStop = t  # not accounting for scr refresh
                        rec_trial_main_image.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(rec_trial_main_image, 'tStopRefresh')  # time at next scr refresh
                        rec_trial_main_image.setAutoDraw(False)
                
                # *rec_trial_key* updates
                waitOnFlip = False
                if rec_trial_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    rec_trial_key.frameNStart = frameN  # exact frame index
                    rec_trial_key.tStart = t  # local t and not account for scr refresh
                    rec_trial_key.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(rec_trial_key, 'tStartRefresh')  # time at next scr refresh
                    rec_trial_key.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(rec_trial_key.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(rec_trial_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if rec_trial_key.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > rec_trial_key.tStartRefresh + 4.0-frameTolerance:
                        # keep track of stop time/frame for later
                        rec_trial_key.tStop = t  # not accounting for scr refresh
                        rec_trial_key.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(rec_trial_key, 'tStopRefresh')  # time at next scr refresh
                        rec_trial_key.status = FINISHED
                if rec_trial_key.status == STARTED and not waitOnFlip:
                    theseKeys = rec_trial_key.getKeys(keyList=['f', 'j'], waitRelease=False)
                    _rec_trial_key_allKeys.extend(theseKeys)
                    if len(_rec_trial_key_allKeys):
                        rec_trial_key.keys = _rec_trial_key_allKeys[-1].name  # just the last key pressed
                        rec_trial_key.rt = _rec_trial_key_allKeys[-1].rt
                
                # *rec_trial_text_block* updates
                if rec_trial_text_block.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    rec_trial_text_block.frameNStart = frameN  # exact frame index
                    rec_trial_text_block.tStart = t  # local t and not account for scr refresh
                    rec_trial_text_block.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(rec_trial_text_block, 'tStartRefresh')  # time at next scr refresh
                    rec_trial_text_block.setAutoDraw(True)
                if rec_trial_text_block.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > rec_trial_text_block.tStartRefresh + 4.0-frameTolerance:
                        # keep track of stop time/frame for later
                        rec_trial_text_block.tStop = t  # not accounting for scr refresh
                        rec_trial_text_block.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(rec_trial_text_block, 'tStopRefresh')  # time at next scr refresh
                        rec_trial_text_block.setAutoDraw(False)
                
                # *rec_trial_instructions_text* updates
                if rec_trial_instructions_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    rec_trial_instructions_text.frameNStart = frameN  # exact frame index
                    rec_trial_instructions_text.tStart = t  # local t and not account for scr refresh
                    rec_trial_instructions_text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(rec_trial_instructions_text, 'tStartRefresh')  # time at next scr refresh
                    rec_trial_instructions_text.setAutoDraw(True)
                if rec_trial_instructions_text.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > rec_trial_instructions_text.tStartRefresh + 4.0-frameTolerance:
                        # keep track of stop time/frame for later
                        rec_trial_instructions_text.tStop = t  # not accounting for scr refresh
                        rec_trial_instructions_text.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(rec_trial_instructions_text, 'tStopRefresh')  # time at next scr refresh
                        rec_trial_instructions_text.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in rec_trialComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "rec_trial"-------
            for thisComponent in rec_trialComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            rec_trials.addData('rec_trial_interior.started', rec_trial_interior.tStartRefresh)
            rec_trials.addData('rec_trial_interior.stopped', rec_trial_interior.tStopRefresh)
            rec_trials.addData('rec_trial_main_image.started', rec_trial_main_image.tStartRefresh)
            rec_trials.addData('rec_trial_main_image.stopped', rec_trial_main_image.tStopRefresh)
            # check responses
            if rec_trial_key.keys in ['', [], None]:  # No response was made
                rec_trial_key.keys = None
            rec_trials.addData('rec_trial_key.keys',rec_trial_key.keys)
            if rec_trial_key.keys != None:  # we had a response
                rec_trials.addData('rec_trial_key.rt', rec_trial_key.rt)
            rec_trials.addData('rec_trial_key.started', rec_trial_key.tStartRefresh)
            rec_trials.addData('rec_trial_key.stopped', rec_trial_key.tStopRefresh)
            rec_trials.addData('rec_trial_text_block.started', rec_trial_text_block.tStartRefresh)
            rec_trials.addData('rec_trial_text_block.stopped', rec_trial_text_block.tStopRefresh)
            rec_trials.addData('rec_trial_instructions_text.started', rec_trial_instructions_text.tStartRefresh)
            rec_trials.addData('rec_trial_instructions_text.stopped', rec_trial_instructions_text.tStopRefresh)
            thisExp.nextEntry()
            
        # completed 1 repeats of 'rec_trials'
        
    # completed 2 repeats of 'rec_blocks'
    
    
    # ------Prepare to start Routine "end_rec_run"-------
    continueRoutine = True
    routineTimer.add(300.000000)
    # update component parameters for each repeat
    end_rec_run_text.setText(end_run_text)
    end_rec_run_key.keys = []
    end_rec_run_key.rt = []
    _end_rec_run_key_allKeys = []
    # keep track of which components have finished
    end_rec_runComponents = [end_rec_run_text, end_rec_run_key]
    for thisComponent in end_rec_runComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    end_rec_runClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "end_rec_run"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = end_rec_runClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=end_rec_runClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *end_rec_run_text* updates
        if end_rec_run_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            end_rec_run_text.frameNStart = frameN  # exact frame index
            end_rec_run_text.tStart = t  # local t and not account for scr refresh
            end_rec_run_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(end_rec_run_text, 'tStartRefresh')  # time at next scr refresh
            end_rec_run_text.setAutoDraw(True)
        if end_rec_run_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > end_rec_run_text.tStartRefresh + 300.0-frameTolerance:
                # keep track of stop time/frame for later
                end_rec_run_text.tStop = t  # not accounting for scr refresh
                end_rec_run_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(end_rec_run_text, 'tStopRefresh')  # time at next scr refresh
                end_rec_run_text.setAutoDraw(False)
        
        # *end_rec_run_key* updates
        waitOnFlip = False
        if end_rec_run_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            end_rec_run_key.frameNStart = frameN  # exact frame index
            end_rec_run_key.tStart = t  # local t and not account for scr refresh
            end_rec_run_key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(end_rec_run_key, 'tStartRefresh')  # time at next scr refresh
            end_rec_run_key.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(end_rec_run_key.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(end_rec_run_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if end_rec_run_key.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > end_rec_run_key.tStartRefresh + 300-frameTolerance:
                # keep track of stop time/frame for later
                end_rec_run_key.tStop = t  # not accounting for scr refresh
                end_rec_run_key.frameNStop = frameN  # exact frame index
                win.timeOnFlip(end_rec_run_key, 'tStopRefresh')  # time at next scr refresh
                end_rec_run_key.status = FINISHED
        if end_rec_run_key.status == STARTED and not waitOnFlip:
            theseKeys = end_rec_run_key.getKeys(keyList=['right'], waitRelease=False)
            _end_rec_run_key_allKeys.extend(theseKeys)
            if len(_end_rec_run_key_allKeys):
                end_rec_run_key.keys = _end_rec_run_key_allKeys[-1].name  # just the last key pressed
                end_rec_run_key.rt = _end_rec_run_key_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in end_rec_runComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "end_rec_run"-------
    for thisComponent in end_rec_runComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    rec_runs.addData('end_rec_run_text.started', end_rec_run_text.tStartRefresh)
    rec_runs.addData('end_rec_run_text.stopped', end_rec_run_text.tStopRefresh)
    # check responses
    if end_rec_run_key.keys in ['', [], None]:  # No response was made
        end_rec_run_key.keys = None
    rec_runs.addData('end_rec_run_key.keys',end_rec_run_key.keys)
    if end_rec_run_key.keys != None:  # we had a response
        rec_runs.addData('end_rec_run_key.rt', end_rec_run_key.rt)
    rec_runs.addData('end_rec_run_key.started', end_rec_run_key.tStartRefresh)
    rec_runs.addData('end_rec_run_key.stopped', end_rec_run_key.tStopRefresh)
# completed 4 repeats of 'rec_runs'


# ------Prepare to start Routine "end_experiment"-------
continueRoutine = True
routineTimer.add(300.000000)
# update component parameters for each repeat
end_experiment_code.setText(code)
end_experiment_key.keys = []
end_experiment_key.rt = []
_end_experiment_key_allKeys = []
# keep track of which components have finished
end_experimentComponents = [end_experiment_text, end_experiment_code, end_experiment_continue, end_experiment_key]
for thisComponent in end_experimentComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
end_experimentClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "end_experiment"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = end_experimentClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=end_experimentClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *end_experiment_text* updates
    if end_experiment_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_experiment_text.frameNStart = frameN  # exact frame index
        end_experiment_text.tStart = t  # local t and not account for scr refresh
        end_experiment_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_experiment_text, 'tStartRefresh')  # time at next scr refresh
        end_experiment_text.setAutoDraw(True)
    if end_experiment_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > end_experiment_text.tStartRefresh + 300.0-frameTolerance:
            # keep track of stop time/frame for later
            end_experiment_text.tStop = t  # not accounting for scr refresh
            end_experiment_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(end_experiment_text, 'tStopRefresh')  # time at next scr refresh
            end_experiment_text.setAutoDraw(False)
    
    # *end_experiment_code* updates
    if end_experiment_code.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_experiment_code.frameNStart = frameN  # exact frame index
        end_experiment_code.tStart = t  # local t and not account for scr refresh
        end_experiment_code.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_experiment_code, 'tStartRefresh')  # time at next scr refresh
        end_experiment_code.setAutoDraw(True)
    if end_experiment_code.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > end_experiment_code.tStartRefresh + 300.0-frameTolerance:
            # keep track of stop time/frame for later
            end_experiment_code.tStop = t  # not accounting for scr refresh
            end_experiment_code.frameNStop = frameN  # exact frame index
            win.timeOnFlip(end_experiment_code, 'tStopRefresh')  # time at next scr refresh
            end_experiment_code.setAutoDraw(False)
    
    # *end_experiment_continue* updates
    if end_experiment_continue.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
        # keep track of start time/frame for later
        end_experiment_continue.frameNStart = frameN  # exact frame index
        end_experiment_continue.tStart = t  # local t and not account for scr refresh
        end_experiment_continue.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_experiment_continue, 'tStartRefresh')  # time at next scr refresh
        end_experiment_continue.setAutoDraw(True)
    if end_experiment_continue.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > end_experiment_continue.tStartRefresh + 297.0-frameTolerance:
            # keep track of stop time/frame for later
            end_experiment_continue.tStop = t  # not accounting for scr refresh
            end_experiment_continue.frameNStop = frameN  # exact frame index
            win.timeOnFlip(end_experiment_continue, 'tStopRefresh')  # time at next scr refresh
            end_experiment_continue.setAutoDraw(False)
    
    # *end_experiment_key* updates
    waitOnFlip = False
    if end_experiment_key.status == NOT_STARTED and tThisFlip >= 4.0-frameTolerance:
        # keep track of start time/frame for later
        end_experiment_key.frameNStart = frameN  # exact frame index
        end_experiment_key.tStart = t  # local t and not account for scr refresh
        end_experiment_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_experiment_key, 'tStartRefresh')  # time at next scr refresh
        end_experiment_key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(end_experiment_key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(end_experiment_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if end_experiment_key.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > end_experiment_key.tStartRefresh + 294.0-frameTolerance:
            # keep track of stop time/frame for later
            end_experiment_key.tStop = t  # not accounting for scr refresh
            end_experiment_key.frameNStop = frameN  # exact frame index
            win.timeOnFlip(end_experiment_key, 'tStopRefresh')  # time at next scr refresh
            end_experiment_key.status = FINISHED
    if end_experiment_key.status == STARTED and not waitOnFlip:
        theseKeys = end_experiment_key.getKeys(keyList=['right'], waitRelease=False)
        _end_experiment_key_allKeys.extend(theseKeys)
        if len(_end_experiment_key_allKeys):
            end_experiment_key.keys = _end_experiment_key_allKeys[-1].name  # just the last key pressed
            end_experiment_key.rt = _end_experiment_key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in end_experimentComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end_experiment"-------
for thisComponent in end_experimentComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('end_experiment_text.started', end_experiment_text.tStartRefresh)
thisExp.addData('end_experiment_text.stopped', end_experiment_text.tStopRefresh)
thisExp.addData('end_experiment_code.started', end_experiment_code.tStartRefresh)
thisExp.addData('end_experiment_code.stopped', end_experiment_code.tStopRefresh)
thisExp.addData('end_experiment_continue.started', end_experiment_continue.tStartRefresh)
thisExp.addData('end_experiment_continue.stopped', end_experiment_continue.tStopRefresh)
# check responses
if end_experiment_key.keys in ['', [], None]:  # No response was made
    end_experiment_key.keys = None
thisExp.addData('end_experiment_key.keys',end_experiment_key.keys)
if end_experiment_key.keys != None:  # we had a response
    thisExp.addData('end_experiment_key.rt', end_experiment_key.rt)
thisExp.addData('end_experiment_key.started', end_experiment_key.tStartRefresh)
thisExp.addData('end_experiment_key.stopped', end_experiment_key.tStopRefresh)
thisExp.nextEntry()

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
