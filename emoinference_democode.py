#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.10),
    on March 26, 2021, at 19:08
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
psychopyVersion = '2020.2.10'
expName = 'blockedTrials'  # from the Builder filename that created this script
expInfo = {'session': '001', 'participant': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\ayesh\\Desktop\\Gradstuff\\contingentproject\\mem-gen_study\\memgen_images_blocks\\emoinference_democode.py',
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
    size=[1536, 864], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "init"
initClock = core.Clock()
import random
import numpy as np

# use psychopy's method to get a list of dictionaries
# {'colName', 'colValue'}

allfaceDictList = data.importConditions("all_faces_demo.csv")
allobjectDictList = data.importConditions("object_code.csv")
#for files
EfaceDictList = data.importConditions("emo_code.csv")
NfaceDictList = data.importConditions("neu_code.csv")
# convert to a simple list
allfaceList = [x['stimFile'] for x in allfaceDictList]
allobjectList = [x['Objects'] for x in allobjectDictList]

## divide objects in 2 lists for AB and BC study
shuffle (allfaceList)
shuffle(allobjectList)
objectAlist = allobjectList[:7]
objectClist = allobjectList[7:]

emofaceList = [x['emo_faces'] for x in EfaceDictList]
neufaceList = [x['neu_faces'] for x in NfaceDictList]

# Initialize components for Routine "start_inst"
start_instClock = core.Clock()
text_9 = visual.TextStim(win=win, name='text_9',
    text='This is just a demo. Please press spacebar to begin. Hopefully it works :)\n',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_6 = keyboard.Keyboard()

# Initialize components for Routine "AB1"
AB1Clock = core.Clock()
i = 0
study1pairs = []

face = visual.ImageStim(
    win=win,
    name='face', units='height', 
    image='sin', mask=None,
    ori=0, pos=(0.5, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
object = visual.ImageStim(
    win=win,
    name='object', 
    image='sin', mask=None,
    ori=0, pos=(-0.5, 0), size=(0.55, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
text_2 = visual.TextStim(win=win, name='text_2',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.5, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "AB1test"
AB1testClock = core.Clock()
msg = 'doh' #if this comes up we forgot to update the msg!
randord0 = list(range(6));
shuffle(randord0)
z = 0

cue = visual.ImageStim(
    win=win,
    name='cue', 
    image='sin', mask=None,
    ori=0, pos=(0, 0.45), size=(0.5, 0.85),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
polygon = visual.Rect(
    win=win, name='polygon',
    width=(0.55, 0.85)[0], height=(0.55, 0.85)[1],
    ori=0, pos=[0,0],
    lineWidth=3, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[0,0,0], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
correct_face = visual.ImageStim(
    win=win,
    name='correct_face', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.5, 0.8),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
foil1 = visual.ImageStim(
    win=win,
    name='foil1', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.5, 0.8),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
foil2 = visual.ImageStim(
    win=win,
    name='foil2', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.5, 0.8),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
key_resp = keyboard.Keyboard()

# Initialize components for Routine "break1"
break1Clock = core.Clock()
text_4 = visual.TextStim(win=win, name='text_4',
    text='End of AB1',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "AB2"
AB2Clock = core.Clock()
trialpair2 = []
study2pairs = []
#randord = list(range(0, 6))
randord1 = list(range(6));
shuffle(randord1)
ii = 0
    

face_2 = visual.ImageStim(
    win=win,
    name='face_2', units='height', 
    image='sin', mask=None,
    ori=0, pos=(0.5, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
object_2 = visual.ImageStim(
    win=win,
    name='object_2', 
    image='sin', mask=None,
    ori=0, pos=(-0.5, 0), size=(0.55, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
text = visual.TextStim(win=win, name='text',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.5, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "AB2test"
AB2testClock = core.Clock()
msg = 'doh' #if this comes up we forgot to update the msg!
randord2 = list(range(6));
shuffle(randord2)
zz = 0

key_resp_2 = keyboard.Keyboard()
cue_2 = visual.ImageStim(
    win=win,
    name='cue_2', 
    image='sin', mask=None,
    ori=0, pos=(0, 0.45), size=(0.5, 0.85),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
polygon_2 = visual.Rect(
    win=win, name='polygon_2',
    width=(0.55, 0.85)[0], height=(0.55, 0.85)[1],
    ori=0, pos=[0,0],
    lineWidth=3, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[0,0,0], fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
correct_face_2 = visual.ImageStim(
    win=win,
    name='correct_face_2', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.5, 0.8),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
foil1_2 = visual.ImageStim(
    win=win,
    name='foil1_2', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.5, 0.8),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
foil2_2 = visual.ImageStim(
    win=win,
    name='foil2_2', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.5, 0.8),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)

# Initialize components for Routine "break2"
break2Clock = core.Clock()
text_6 = visual.TextStim(win=win, name='text_6',
    text='End of AB2',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "AB3"
AB3Clock = core.Clock()
trialpair3 = []
study3pairs = []
#randord2 = list(range(0, 6))
randord3 = list(range(6));
shuffle(randord3)
iii = 0
face_3 = visual.ImageStim(
    win=win,
    name='face_3', units='height', 
    image='sin', mask=None,
    ori=0, pos=(0.5, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
object_3 = visual.ImageStim(
    win=win,
    name='object_3', 
    image='sin', mask=None,
    ori=0, pos=(-0.5, 0), size=(0.55, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
text_3 = visual.TextStim(win=win, name='text_3',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.5, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "AB3test"
AB3testClock = core.Clock()
msg = 'doh' #if this comes up we forgot to update the msg!
randord4 = list(range(6));
shuffle(randord4)
zzz = 0

key_resp_3 = keyboard.Keyboard()
cue_3 = visual.ImageStim(
    win=win,
    name='cue_3', 
    image='sin', mask=None,
    ori=0, pos=(0, 0.45), size=(0.5, 0.85),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
polygon_3 = visual.Rect(
    win=win, name='polygon_3',
    width=(0.55, 0.85)[0], height=(0.55, 0.85)[1],
    ori=0, pos=[0,0],
    lineWidth=3, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[0,0,0], fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
correct_face_3 = visual.ImageStim(
    win=win,
    name='correct_face_3', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.5, 0.8),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
foil1_3 = visual.ImageStim(
    win=win,
    name='foil1_3', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.5, 0.8),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
foil2_3 = visual.ImageStim(
    win=win,
    name='foil2_3', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.5, 0.8),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)

# Initialize components for Routine "break3"
break3Clock = core.Clock()
text_7 = visual.TextStim(win=win, name='text_7',
    text='End of AB3. Now you will see BC pairs!',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "BC"
BCClock = core.Clock()
trialpair4 = []
study4pairs = []
orig_object = []
#randord3 = list(range(0, 6))
randord5 = list(range(6));
shuffle(randord5)
g = 0
face_4 = visual.ImageStim(
    win=win,
    name='face_4', units='height', 
    image='sin', mask=None,
    ori=0, pos=(0.5, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
object_4 = visual.ImageStim(
    win=win,
    name='object_4', 
    image='sin', mask=None,
    ori=0, pos=(-0.5, 0), size=(0.55, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
text_5 = visual.TextStim(win=win, name='text_5',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.5, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "BCtest"
BCtestClock = core.Clock()
msg = 'doh' #if this comes up we forgot to update the msg!
randord6 = list(range(6));
shuffle(randord6)
bc_z = 0

key_resp_4 = keyboard.Keyboard()
cue_4 = visual.ImageStim(
    win=win,
    name='cue_4', 
    image='sin', mask=None,
    ori=0, pos=(0, 0.45), size=(0.5, 0.85),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
polygon_4 = visual.Rect(
    win=win, name='polygon_4',
    width=(0.55, 0.85)[0], height=(0.55, 0.85)[1],
    ori=0, pos=[0,0],
    lineWidth=3, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[0,0,0], fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
correct_face_4 = visual.ImageStim(
    win=win,
    name='correct_face_4', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.5, 0.8),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
foil1_4 = visual.ImageStim(
    win=win,
    name='foil1_4', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.5, 0.8),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
foil2_4 = visual.ImageStim(
    win=win,
    name='foil2_4', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.5, 0.8),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)

# Initialize components for Routine "BeginAC"
BeginACClock = core.Clock()
text_8 = visual.TextStim(win=win, name='text_8',
    text='Begin AC test!',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "AC_test"
AC_testClock = core.Clock()
randord7 = list(range(6));
shuffle(randord7)
ind_z = 0
fin_testpairs = []


cueC = visual.ImageStim(
    win=win,
    name='cueC', 
    image='sin', mask=None,
    ori=0, pos=(0, 0.45), size=(0.5, 0.85),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
cor_object = visual.ImageStim(
    win=win,
    name='cor_object', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.5, 0.8),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
foil1_image = visual.ImageStim(
    win=win,
    name='foil1_image', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.5, 0.8),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
foil2_image = visual.ImageStim(
    win=win,
    name='foil2_image', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.5, 0.8),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
key_resp_5 = keyboard.Keyboard()

# Initialize components for Routine "FinalAB_test"
FinalAB_testClock = core.Clock()
msg = 'doh' #if this comes up we forgot to update the msg!
randord8 = list(range(6));
shuffle(randord8)
end_z = 0

cue_5 = visual.ImageStim(
    win=win,
    name='cue_5', 
    image='sin', mask=None,
    ori=0, pos=(0, 0.45), size=(0.5, 0.85),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
polygon_5 = visual.Rect(
    win=win, name='polygon_5',
    width=(0.55, 0.85)[0], height=(0.55, 0.85)[1],
    ori=0, pos=[0,0],
    lineWidth=3, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[0,0,0], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
correct_face_5 = visual.ImageStim(
    win=win,
    name='correct_face_5', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.5, 0.8),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
foil1_5 = visual.ImageStim(
    win=win,
    name='foil1_5', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.5, 0.8),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
foil2_5 = visual.ImageStim(
    win=win,
    name='foil2_5', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.5, 0.8),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
key_resp_7 = keyboard.Keyboard()

# Initialize components for Routine "FinalBC_test"
FinalBC_testClock = core.Clock()
msg = 'doh' #if this comes up we forgot to update the msg!
randord9 = list(range(6));
shuffle(randord9)
end_y = 0

cue_6 = visual.ImageStim(
    win=win,
    name='cue_6', 
    image='sin', mask=None,
    ori=0, pos=(0, 0.45), size=(0.5, 0.85),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
polygon_6 = visual.Rect(
    win=win, name='polygon_6',
    width=(0.55, 0.85)[0], height=(0.55, 0.85)[1],
    ori=0, pos=[0,0],
    lineWidth=3, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[0,0,0], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
correct_face_6 = visual.ImageStim(
    win=win,
    name='correct_face_6', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.5, 0.8),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
foil1_6 = visual.ImageStim(
    win=win,
    name='foil1_6', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.5, 0.8),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
foil2_6 = visual.ImageStim(
    win=win,
    name='foil2_6', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.5, 0.8),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
key_resp_8 = keyboard.Keyboard()

# Initialize components for Routine "end"
endClock = core.Clock()
text_10 = visual.TextStim(win=win, name='text_10',
    text='It worked!',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "init"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
initComponents = []
for thisComponent in initComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
initClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "init"-------
while continueRoutine:
    # get current time
    t = initClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=initClock)
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
    for thisComponent in initComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "init"-------
for thisComponent in initComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('objectsA', objectAlist)
thisExp.addData('ObjectsC', objectClist)

print(objectAlist)
# the Routine "init" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "start_inst"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_6.keys = []
key_resp_6.rt = []
_key_resp_6_allKeys = []
# keep track of which components have finished
start_instComponents = [text_9, key_resp_6]
for thisComponent in start_instComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
start_instClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "start_inst"-------
while continueRoutine:
    # get current time
    t = start_instClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=start_instClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_9* updates
    if text_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_9.frameNStart = frameN  # exact frame index
        text_9.tStart = t  # local t and not account for scr refresh
        text_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_9, 'tStartRefresh')  # time at next scr refresh
        text_9.setAutoDraw(True)
    
    # *key_resp_6* updates
    waitOnFlip = False
    if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_6.frameNStart = frameN  # exact frame index
        key_resp_6.tStart = t  # local t and not account for scr refresh
        key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
        key_resp_6.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_6.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_6.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_6_allKeys.extend(theseKeys)
        if len(_key_resp_6_allKeys):
            key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
            key_resp_6.rt = _key_resp_6_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in start_instComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "start_inst"-------
for thisComponent in start_instComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_9.started', text_9.tStartRefresh)
thisExp.addData('text_9.stopped', text_9.tStopRefresh)
# check responses
if key_resp_6.keys in ['', [], None]:  # No response was made
    key_resp_6.keys = None
thisExp.addData('key_resp_6.keys',key_resp_6.keys)
if key_resp_6.keys != None:  # we had a response
    thisExp.addData('key_resp_6.rt', key_resp_6.rt)
thisExp.addData('key_resp_6.started', key_resp_6.tStartRefresh)
thisExp.addData('key_resp_6.stopped', key_resp_6.tStopRefresh)
thisExp.nextEntry()
# the Routine "start_inst" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
study1 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('all_df_demo.csv'),
    seed=None, name='study1')
thisExp.addLoop(study1)  # add the loop to the experiment
thisStudy1 = study1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisStudy1.rgb)
if thisStudy1 != None:
    for paramName in thisStudy1:
        exec('{} = thisStudy1[paramName]'.format(paramName))

for thisStudy1 in study1:
    currentLoop = study1
    # abbreviate parameter names if possible (e.g. rgb = thisStudy1.rgb)
    if thisStudy1 != None:
        for paramName in thisStudy1:
            exec('{} = thisStudy1[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "AB1"-------
    continueRoutine = True
    routineTimer.add(3.500000)
    # update component parameters for each repeat
    print(i)
    face_image = allfaceList[i]
    objectA_image = objectAlist[i]
    
    thisExp.addData('face_image', face_image)
    thisExp.addData('objectA_image', objectA_image)
    
    face.setImage(face_image)
    object.setImage(objectA_image)
    # keep track of which components have finished
    AB1Components = [face, object, text_2]
    for thisComponent in AB1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    AB1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "AB1"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = AB1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=AB1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *face* updates
        if face.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            face.frameNStart = frameN  # exact frame index
            face.tStart = t  # local t and not account for scr refresh
            face.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(face, 'tStartRefresh')  # time at next scr refresh
            face.setAutoDraw(True)
        if face.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > face.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                face.tStop = t  # not accounting for scr refresh
                face.frameNStop = frameN  # exact frame index
                win.timeOnFlip(face, 'tStopRefresh')  # time at next scr refresh
                face.setAutoDraw(False)
        
        # *object* updates
        if object.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            object.frameNStart = frameN  # exact frame index
            object.tStart = t  # local t and not account for scr refresh
            object.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(object, 'tStartRefresh')  # time at next scr refresh
            object.setAutoDraw(True)
        if object.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > object.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                object.tStop = t  # not accounting for scr refresh
                object.frameNStop = frameN  # exact frame index
                win.timeOnFlip(object, 'tStopRefresh')  # time at next scr refresh
                object.setAutoDraw(False)
        
        # *text_2* updates
        if text_2.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            text_2.frameNStart = frameN  # exact frame index
            text_2.tStart = t  # local t and not account for scr refresh
            text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
            text_2.setAutoDraw(True)
        if text_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_2.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                text_2.tStop = t  # not accounting for scr refresh
                text_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
                text_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in AB1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "AB1"-------
    for thisComponent in AB1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    print(i)
    thisExp.addData('face1', face_image[i])
    thisExp.addData('objectA', objectA_image[i])
    trialpair = [face_image, objectA_image]
    study1pairs.append(trialpair)
    i = i+1
    
    print(trialpair)
    print(study1pairs)
    study1.addData('face.started', face.tStartRefresh)
    study1.addData('face.stopped', face.tStopRefresh)
    study1.addData('object.started', object.tStartRefresh)
    study1.addData('object.stopped', object.tStopRefresh)
    study1.addData('text_2.started', text_2.tStartRefresh)
    study1.addData('text_2.stopped', text_2.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'study1'


# set up handler to look after randomisation of conditions etc
test1 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('all_df_test_emo.csv'),
    seed=None, name='test1')
thisExp.addLoop(test1)  # add the loop to the experiment
thisTest1 = test1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTest1.rgb)
if thisTest1 != None:
    for paramName in thisTest1:
        exec('{} = thisTest1[paramName]'.format(paramName))

for thisTest1 in test1:
    currentLoop = test1
    # abbreviate parameter names if possible (e.g. rgb = thisTest1.rgb)
    if thisTest1 != None:
        for paramName in thisTest1:
            exec('{} = thisTest1[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "AB1test"-------
    continueRoutine = True
    routineTimer.add(3.500000)
    # update component parameters for each repeat
    import random
    from numpy.random import random
    placement = random()
    
    test1_face_image = study1pairs[randord0[z]][0]
    test1_objectA_image = study1pairs[randord0[z]][-1]
    
    model = (test1_face_image[-12:-9])
    val = (test1_face_image[-8:-6])
    
    if val == 'NE':
        pickfrm = neufaceList
    if val == 'FE':
        pickfrm = emofaceList
    
    foils1 = []
    foils2 = []
    for stim in pickfrm:
        if stim != test1_face_image:
            foils1.append(stim)
    foil1_fc = foils1[z]
    
    for stim in pickfrm:
        if (stim != test1_face_image) and (stim != foil1_fc):
            foils2.append(stim)
    foil2_fc = foils2[z]
    thisExp.addData('test1_face_image', test1_face_image)
    thisExp.addData('test1_objectA_image', test1_objectA_image)
    thisExp.addData('test1_foil1_image', foil1_fc)
    thisExp.addData('test1_foil2_image', foil2_fc)
    
    if placement <= 0.33:
        targetPos=[-0.7, -0.5] #on the left
        foil1_pos=[0.0, -0.5] #in the middle
        foil2_pos=[0.7,-0.5] #on the right
        corrAns='1'
        feedback = targetPos
    if 0.33 < placement < 0.66:
        targetPos=[0.0, -0.5] #in the middle
        foil1_pos=[-0.7, -0.5] #on the left
        foil2_pos=[0.7, -0.5] #on the right
        corrAns= '2'
        feedback = targetPos
    if placement >= 0.66:
        targetPos=[0.7, -0.5] #on the right
        foil1_pos=[-0.7, -0.5] #on the left
        foil2_pos=[0.0, -0.5] #in the middle
        corrAns='3'
        feedback = targetPos
    
    #feedback = targetPos
    
    cue.setImage(test1_objectA_image)
    polygon.setPos(targetPos)
    correct_face.setPos(targetPos)
    correct_face.setImage(test1_face_image)
    foil1.setPos(foil1_pos)
    foil1.setImage(foil1_fc)
    foil2.setPos(foil2_pos)
    foil2.setImage(foil2_fc)
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    AB1testComponents = [cue, polygon, correct_face, foil1, foil2, key_resp]
    for thisComponent in AB1testComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    AB1testClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "AB1test"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = AB1testClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=AB1testClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *cue* updates
        if cue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cue.frameNStart = frameN  # exact frame index
            cue.tStart = t  # local t and not account for scr refresh
            cue.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cue, 'tStartRefresh')  # time at next scr refresh
            cue.setAutoDraw(True)
        if cue.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cue.tStartRefresh + 3.5-frameTolerance:
                # keep track of stop time/frame for later
                cue.tStop = t  # not accounting for scr refresh
                cue.frameNStop = frameN  # exact frame index
                win.timeOnFlip(cue, 'tStopRefresh')  # time at next scr refresh
                cue.setAutoDraw(False)
        
        # *polygon* updates
        if polygon.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            polygon.frameNStart = frameN  # exact frame index
            polygon.tStart = t  # local t and not account for scr refresh
            polygon.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
            polygon.setAutoDraw(True)
        if polygon.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                polygon.tStop = t  # not accounting for scr refresh
                polygon.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon, 'tStopRefresh')  # time at next scr refresh
                polygon.setAutoDraw(False)
        
        # *correct_face* updates
        if correct_face.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            correct_face.frameNStart = frameN  # exact frame index
            correct_face.tStart = t  # local t and not account for scr refresh
            correct_face.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(correct_face, 'tStartRefresh')  # time at next scr refresh
            correct_face.setAutoDraw(True)
        if correct_face.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > correct_face.tStartRefresh + 3.5-frameTolerance:
                # keep track of stop time/frame for later
                correct_face.tStop = t  # not accounting for scr refresh
                correct_face.frameNStop = frameN  # exact frame index
                win.timeOnFlip(correct_face, 'tStopRefresh')  # time at next scr refresh
                correct_face.setAutoDraw(False)
        
        # *foil1* updates
        if foil1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            foil1.frameNStart = frameN  # exact frame index
            foil1.tStart = t  # local t and not account for scr refresh
            foil1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(foil1, 'tStartRefresh')  # time at next scr refresh
            foil1.setAutoDraw(True)
        if foil1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > foil1.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                foil1.tStop = t  # not accounting for scr refresh
                foil1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(foil1, 'tStopRefresh')  # time at next scr refresh
                foil1.setAutoDraw(False)
        
        # *foil2* updates
        if foil2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            foil2.frameNStart = frameN  # exact frame index
            foil2.tStart = t  # local t and not account for scr refresh
            foil2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(foil2, 'tStartRefresh')  # time at next scr refresh
            foil2.setAutoDraw(True)
        if foil2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > foil2.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                foil2.tStop = t  # not accounting for scr refresh
                foil2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(foil2, 'tStopRefresh')  # time at next scr refresh
                foil2.setAutoDraw(False)
        
        # *key_resp* updates
        if key_resp.status == NOT_STARTED and t >= 0.75-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            key_resp.clock.reset()  # now t=0
            key_resp.clearEvents(eventType='keyboard')
        if key_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp.tStartRefresh + 2.25-frameTolerance:
                # keep track of stop time/frame for later
                key_resp.tStop = t  # not accounting for scr refresh
                key_resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp, 'tStopRefresh')  # time at next scr refresh
                key_resp.status = FINISHED
        if key_resp.status == STARTED:
            theseKeys = key_resp.getKeys(keyList=['1', '2', '3'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in AB1testComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "AB1test"-------
    for thisComponent in AB1testComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('test1_face', test1_face_image[z])
    thisExp.addData('test1_objectA', test1_objectA_image[z])
    thisExp.addData('test1_foil1', foil1_fc[z])
    thisExp.addData('test1_foil2', foil2_fc[z])
    
    z = z+1
    test1.addData('cue.started', cue.tStartRefresh)
    test1.addData('cue.stopped', cue.tStopRefresh)
    test1.addData('polygon.started', polygon.tStartRefresh)
    test1.addData('polygon.stopped', polygon.tStopRefresh)
    test1.addData('correct_face.started', correct_face.tStartRefresh)
    test1.addData('correct_face.stopped', correct_face.tStopRefresh)
    test1.addData('foil1.started', foil1.tStartRefresh)
    test1.addData('foil1.stopped', foil1.tStopRefresh)
    test1.addData('foil2.started', foil2.tStartRefresh)
    test1.addData('foil2.stopped', foil2.tStopRefresh)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    test1.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        test1.addData('key_resp.rt', key_resp.rt)
    test1.addData('key_resp.started', key_resp.tStart)
    test1.addData('key_resp.stopped', key_resp.tStop)
    thisExp.nextEntry()
    
# completed 1 repeats of 'test1'


# ------Prepare to start Routine "break1"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
break1Components = [text_4]
for thisComponent in break1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
break1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "break1"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = break1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=break1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_4* updates
    if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_4.frameNStart = frameN  # exact frame index
        text_4.tStart = t  # local t and not account for scr refresh
        text_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
        text_4.setAutoDraw(True)
    if text_4.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_4.tStartRefresh + 3.0-frameTolerance:
            # keep track of stop time/frame for later
            text_4.tStop = t  # not accounting for scr refresh
            text_4.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_4, 'tStopRefresh')  # time at next scr refresh
            text_4.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in break1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "break1"-------
for thisComponent in break1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_4.started', text_4.tStartRefresh)
thisExp.addData('text_4.stopped', text_4.tStopRefresh)

# set up handler to look after randomisation of conditions etc
study2 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('all_df_demo.csv'),
    seed=None, name='study2')
thisExp.addLoop(study2)  # add the loop to the experiment
thisStudy2 = study2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisStudy2.rgb)
if thisStudy2 != None:
    for paramName in thisStudy2:
        exec('{} = thisStudy2[paramName]'.format(paramName))

for thisStudy2 in study2:
    currentLoop = study2
    # abbreviate parameter names if possible (e.g. rgb = thisStudy2.rgb)
    if thisStudy2 != None:
        for paramName in thisStudy2:
            exec('{} = thisStudy2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "AB2"-------
    continueRoutine = True
    routineTimer.add(3.500000)
    # update component parameters for each repeat
    face_image2 = study1pairs[randord1[ii]][0]
    objectA_image2 = study1pairs[randord1[ii]][-1]
    
    thisExp.addData('face_image2', face_image2)
    thisExp.addData('objectA_image2', objectA_image2)
    
    
    face_2.setImage(face_image2)
    object_2.setImage(objectA_image2)
    # keep track of which components have finished
    AB2Components = [face_2, object_2, text]
    for thisComponent in AB2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    AB2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "AB2"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = AB2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=AB2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *face_2* updates
        if face_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            face_2.frameNStart = frameN  # exact frame index
            face_2.tStart = t  # local t and not account for scr refresh
            face_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(face_2, 'tStartRefresh')  # time at next scr refresh
            face_2.setAutoDraw(True)
        if face_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > face_2.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                face_2.tStop = t  # not accounting for scr refresh
                face_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(face_2, 'tStopRefresh')  # time at next scr refresh
                face_2.setAutoDraw(False)
        
        # *object_2* updates
        if object_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            object_2.frameNStart = frameN  # exact frame index
            object_2.tStart = t  # local t and not account for scr refresh
            object_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(object_2, 'tStartRefresh')  # time at next scr refresh
            object_2.setAutoDraw(True)
        if object_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > object_2.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                object_2.tStop = t  # not accounting for scr refresh
                object_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(object_2, 'tStopRefresh')  # time at next scr refresh
                object_2.setAutoDraw(False)
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
                text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in AB2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "AB2"-------
    for thisComponent in AB2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('face2', face_image2[ii])
    thisExp.addData('objectA2', objectA_image2[ii])
    trialpair2 = [face_image2, objectA_image2]
    study2pairs.append(trialpair2)
    ii = ii + 1
    study2.addData('face_2.started', face_2.tStartRefresh)
    study2.addData('face_2.stopped', face_2.tStopRefresh)
    study2.addData('object_2.started', object_2.tStartRefresh)
    study2.addData('object_2.stopped', object_2.tStopRefresh)
    study2.addData('text.started', text.tStartRefresh)
    study2.addData('text.stopped', text.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'study2'


# set up handler to look after randomisation of conditions etc
test2 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('all_df_test_emo.csv'),
    seed=None, name='test2')
thisExp.addLoop(test2)  # add the loop to the experiment
thisTest2 = test2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTest2.rgb)
if thisTest2 != None:
    for paramName in thisTest2:
        exec('{} = thisTest2[paramName]'.format(paramName))

for thisTest2 in test2:
    currentLoop = test2
    # abbreviate parameter names if possible (e.g. rgb = thisTest2.rgb)
    if thisTest2 != None:
        for paramName in thisTest2:
            exec('{} = thisTest2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "AB2test"-------
    continueRoutine = True
    routineTimer.add(3.500000)
    # update component parameters for each repeat
    #import random
    #from numpy.random import random
    placement = random()
    
    test2_face_image = study2pairs[randord2[zz]][0]
    test2_objectA_image = study2pairs[randord2[zz]][-1]
    
    model = (test2_face_image[-12:-9])
    val = (test2_face_image[-8:-6])
    
    if val == 'NE':
        pickfrm = neufaceList
    if val == 'FE':
        pickfrm = emofaceList
    
    foils1 = []
    foils2 = []
    for stim in pickfrm:
        if stim != test2_face_image:
            foils1.append(stim)
    foil1_fc = foils1[zz]
    
    for stim in pickfrm:
        if (stim != test2_face_image) and (stim != foil1_fc):
            foils2.append(stim)
    foil2_fc = foils2[zz]
    thisExp.addData('test2_face_image', test2_face_image)
    thisExp.addData('test2_objectA_image', test2_objectA_image)
    thisExp.addData('test2_foil1_image', foil1_fc)
    thisExp.addData('test2_foil2_image', foil2_fc)
    
    if placement <= 0.33:
        targetPos=[-0.7, -0.5] #on the left
        foil1_pos=[0.0, -0.5] #in the middle
        foil2_pos=[0.7,-0.5] #on the right
        corrAns='1'
        feedback = targetPos
    if 0.33 < placement < 0.66:
        targetPos=[0.0, -0.5] #in the middle
        foil1_pos=[-0.7, -0.5] #on the left
        foil2_pos=[0.7, -0.5] #on the right
        corrAns= '2'
        feedback = targetPos
    if placement >= 0.66:
        targetPos=[0.7, -0.5] #on the right
        foil1_pos=[-0.7, -0.5] #on the left
        foil2_pos=[0.0, -0.5] #in the middle
        corrAns='3'
        feedback = targetPos
    
    #feedback = targetPos
    
    key_resp_2.keys = []
    key_resp_2.rt = []
    _key_resp_2_allKeys = []
    cue_2.setImage(test2_objectA_image)
    polygon_2.setPos(targetPos)
    correct_face_2.setPos(targetPos)
    correct_face_2.setImage(test2_face_image)
    foil1_2.setPos(foil1_pos)
    foil1_2.setImage(foil1_fc)
    foil2_2.setPos(foil2_pos)
    foil2_2.setImage(foil2_fc)
    # keep track of which components have finished
    AB2testComponents = [key_resp_2, cue_2, polygon_2, correct_face_2, foil1_2, foil2_2]
    for thisComponent in AB2testComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    AB2testClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "AB2test"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = AB2testClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=AB2testClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_resp_2* updates
        waitOnFlip = False
        if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.75-frameTolerance:
            # keep track of start time/frame for later
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.tStart = t  # local t and not account for scr refresh
            key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_2.tStartRefresh + 2.25-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_2.tStop = t  # not accounting for scr refresh
                key_resp_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp_2, 'tStopRefresh')  # time at next scr refresh
                key_resp_2.status = FINISHED
        if key_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_2.getKeys(keyList=['1', '2', '3'], waitRelease=False)
            _key_resp_2_allKeys.extend(theseKeys)
            if len(_key_resp_2_allKeys):
                key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                key_resp_2.rt = _key_resp_2_allKeys[-1].rt
        
        # *cue_2* updates
        if cue_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cue_2.frameNStart = frameN  # exact frame index
            cue_2.tStart = t  # local t and not account for scr refresh
            cue_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cue_2, 'tStartRefresh')  # time at next scr refresh
            cue_2.setAutoDraw(True)
        if cue_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cue_2.tStartRefresh + 3.5-frameTolerance:
                # keep track of stop time/frame for later
                cue_2.tStop = t  # not accounting for scr refresh
                cue_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(cue_2, 'tStopRefresh')  # time at next scr refresh
                cue_2.setAutoDraw(False)
        
        # *polygon_2* updates
        if polygon_2.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_2.frameNStart = frameN  # exact frame index
            polygon_2.tStart = t  # local t and not account for scr refresh
            polygon_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_2, 'tStartRefresh')  # time at next scr refresh
            polygon_2.setAutoDraw(True)
        if polygon_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_2.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                polygon_2.tStop = t  # not accounting for scr refresh
                polygon_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon_2, 'tStopRefresh')  # time at next scr refresh
                polygon_2.setAutoDraw(False)
        
        # *correct_face_2* updates
        if correct_face_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            correct_face_2.frameNStart = frameN  # exact frame index
            correct_face_2.tStart = t  # local t and not account for scr refresh
            correct_face_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(correct_face_2, 'tStartRefresh')  # time at next scr refresh
            correct_face_2.setAutoDraw(True)
        if correct_face_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > correct_face_2.tStartRefresh + 3.5-frameTolerance:
                # keep track of stop time/frame for later
                correct_face_2.tStop = t  # not accounting for scr refresh
                correct_face_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(correct_face_2, 'tStopRefresh')  # time at next scr refresh
                correct_face_2.setAutoDraw(False)
        
        # *foil1_2* updates
        if foil1_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            foil1_2.frameNStart = frameN  # exact frame index
            foil1_2.tStart = t  # local t and not account for scr refresh
            foil1_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(foil1_2, 'tStartRefresh')  # time at next scr refresh
            foil1_2.setAutoDraw(True)
        if foil1_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > foil1_2.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                foil1_2.tStop = t  # not accounting for scr refresh
                foil1_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(foil1_2, 'tStopRefresh')  # time at next scr refresh
                foil1_2.setAutoDraw(False)
        
        # *foil2_2* updates
        if foil2_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            foil2_2.frameNStart = frameN  # exact frame index
            foil2_2.tStart = t  # local t and not account for scr refresh
            foil2_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(foil2_2, 'tStartRefresh')  # time at next scr refresh
            foil2_2.setAutoDraw(True)
        if foil2_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > foil2_2.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                foil2_2.tStop = t  # not accounting for scr refresh
                foil2_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(foil2_2, 'tStopRefresh')  # time at next scr refresh
                foil2_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in AB2testComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "AB2test"-------
    for thisComponent in AB2testComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('test2_face', test2_face_image[zz])
    thisExp.addData('test2_objectA', test2_objectA_image[zz])
    thisExp.addData('test2_foil1', foil1_fc[zz])
    thisExp.addData('test2_foil2', foil2_fc[zz])
    
    zz = zz + 1
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys = None
    test2.addData('key_resp_2.keys',key_resp_2.keys)
    if key_resp_2.keys != None:  # we had a response
        test2.addData('key_resp_2.rt', key_resp_2.rt)
    test2.addData('key_resp_2.started', key_resp_2.tStartRefresh)
    test2.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
    test2.addData('cue_2.started', cue_2.tStartRefresh)
    test2.addData('cue_2.stopped', cue_2.tStopRefresh)
    test2.addData('polygon_2.started', polygon_2.tStartRefresh)
    test2.addData('polygon_2.stopped', polygon_2.tStopRefresh)
    test2.addData('correct_face_2.started', correct_face_2.tStartRefresh)
    test2.addData('correct_face_2.stopped', correct_face_2.tStopRefresh)
    test2.addData('foil1_2.started', foil1_2.tStartRefresh)
    test2.addData('foil1_2.stopped', foil1_2.tStopRefresh)
    test2.addData('foil2_2.started', foil2_2.tStartRefresh)
    test2.addData('foil2_2.stopped', foil2_2.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'test2'


# ------Prepare to start Routine "break2"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
break2Components = [text_6]
for thisComponent in break2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
break2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "break2"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = break2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=break2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_6* updates
    if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_6.frameNStart = frameN  # exact frame index
        text_6.tStart = t  # local t and not account for scr refresh
        text_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
        text_6.setAutoDraw(True)
    if text_6.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_6.tStartRefresh + 3.0-frameTolerance:
            # keep track of stop time/frame for later
            text_6.tStop = t  # not accounting for scr refresh
            text_6.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_6, 'tStopRefresh')  # time at next scr refresh
            text_6.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in break2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "break2"-------
for thisComponent in break2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_6.started', text_6.tStartRefresh)
thisExp.addData('text_6.stopped', text_6.tStopRefresh)

# set up handler to look after randomisation of conditions etc
study3 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('all_df_demo.csv'),
    seed=None, name='study3')
thisExp.addLoop(study3)  # add the loop to the experiment
thisStudy3 = study3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisStudy3.rgb)
if thisStudy3 != None:
    for paramName in thisStudy3:
        exec('{} = thisStudy3[paramName]'.format(paramName))

for thisStudy3 in study3:
    currentLoop = study3
    # abbreviate parameter names if possible (e.g. rgb = thisStudy3.rgb)
    if thisStudy3 != None:
        for paramName in thisStudy3:
            exec('{} = thisStudy3[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "AB3"-------
    continueRoutine = True
    routineTimer.add(3.500000)
    # update component parameters for each repeat
    face_image3 = study1pairs[randord3[iii]][0]
    objectA_image3 = study1pairs[randord3[iii]][-1]
    
    thisExp.addData('face_image3', face_image3)
    thisExp.addData('objectA_image3', objectA_image3)
    face_3.setImage(face_image3)
    object_3.setImage(objectA_image3)
    # keep track of which components have finished
    AB3Components = [face_3, object_3, text_3]
    for thisComponent in AB3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    AB3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "AB3"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = AB3Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=AB3Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *face_3* updates
        if face_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            face_3.frameNStart = frameN  # exact frame index
            face_3.tStart = t  # local t and not account for scr refresh
            face_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(face_3, 'tStartRefresh')  # time at next scr refresh
            face_3.setAutoDraw(True)
        if face_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > face_3.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                face_3.tStop = t  # not accounting for scr refresh
                face_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(face_3, 'tStopRefresh')  # time at next scr refresh
                face_3.setAutoDraw(False)
        
        # *object_3* updates
        if object_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            object_3.frameNStart = frameN  # exact frame index
            object_3.tStart = t  # local t and not account for scr refresh
            object_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(object_3, 'tStartRefresh')  # time at next scr refresh
            object_3.setAutoDraw(True)
        if object_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > object_3.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                object_3.tStop = t  # not accounting for scr refresh
                object_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(object_3, 'tStopRefresh')  # time at next scr refresh
                object_3.setAutoDraw(False)
        
        # *text_3* updates
        if text_3.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            text_3.setAutoDraw(True)
        if text_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_3.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                text_3.tStop = t  # not accounting for scr refresh
                text_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_3, 'tStopRefresh')  # time at next scr refresh
                text_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in AB3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "AB3"-------
    for thisComponent in AB3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('face3', face_image3[iii])
    thisExp.addData('objectA3', objectA_image3[iii])
    trialpair3 = [face_image3, objectA_image3]
    study3pairs.append(trialpair3)
    iii = iii + 1
    study3.addData('face_3.started', face_3.tStartRefresh)
    study3.addData('face_3.stopped', face_3.tStopRefresh)
    study3.addData('object_3.started', object_3.tStartRefresh)
    study3.addData('object_3.stopped', object_3.tStopRefresh)
    study3.addData('text_3.started', text_3.tStartRefresh)
    study3.addData('text_3.stopped', text_3.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'study3'


# set up handler to look after randomisation of conditions etc
test3 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('all_df_test_emo.csv'),
    seed=None, name='test3')
thisExp.addLoop(test3)  # add the loop to the experiment
thisTest3 = test3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTest3.rgb)
if thisTest3 != None:
    for paramName in thisTest3:
        exec('{} = thisTest3[paramName]'.format(paramName))

for thisTest3 in test3:
    currentLoop = test3
    # abbreviate parameter names if possible (e.g. rgb = thisTest3.rgb)
    if thisTest3 != None:
        for paramName in thisTest3:
            exec('{} = thisTest3[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "AB3test"-------
    continueRoutine = True
    routineTimer.add(3.500000)
    # update component parameters for each repeat
    #import random
    #from numpy.random import random
    placement = random()
    
    test3_face_image = study3pairs[randord4[zzz]][0]
    test3_objectA_image = study3pairs[randord4[zzz]][-1]
    
    model = (test3_face_image[-12:-9])
    val = (test3_face_image[-8:-6])
    
    if val == 'NE':
        pickfrm = neufaceList
    if val == 'FE':
        pickfrm = emofaceList
    
    foils1 = []
    foils2 = []
    for stim in pickfrm:
        if stim != test3_face_image:
            foils1.append(stim)
    foil1_fc = foils1[zzz]
    
    for stim in pickfrm:
        if (stim != test3_face_image) and (stim != foil1_fc):
            foils2.append(stim)
    foil2_fc = foils2[zzz]
    thisExp.addData('test3_face_image', test3_face_image)
    thisExp.addData('test3_objectA_image', test3_objectA_image)
    thisExp.addData('test3_foil1_image', foil1_fc)
    thisExp.addData('test3_foil2_image', foil2_fc)
    
    if placement <= 0.33:
        targetPos=[-0.7, -0.5] #on the left
        foil1_pos=[0.0, -0.5] #in the middle
        foil2_pos=[0.7,-0.5] #on the right
        corrAns='1'
        feedback = targetPos
    if 0.33 < placement < 0.66:
        targetPos=[0.0, -0.5] #in the middle
        foil1_pos=[-0.7, -0.5] #on the left
        foil2_pos=[0.7, -0.5] #on the right
        corrAns= '2'
        feedback = targetPos
    if placement >= 0.66:
        targetPos=[0.7, -0.5] #on the right
        foil1_pos=[-0.7, -0.5] #on the left
        foil2_pos=[0.0, -0.5] #in the middle
        corrAns='3'
        feedback = targetPos
    
    #feedback = targetPos
    
    key_resp_3.keys = []
    key_resp_3.rt = []
    _key_resp_3_allKeys = []
    cue_3.setImage(test3_objectA_image)
    polygon_3.setPos(targetPos)
    correct_face_3.setPos(targetPos)
    correct_face_3.setImage(test3_face_image)
    foil1_3.setPos(foil1_pos)
    foil1_3.setImage(foil1_fc)
    foil2_3.setPos(foil2_pos)
    foil2_3.setImage(foil2_fc)
    # keep track of which components have finished
    AB3testComponents = [key_resp_3, cue_3, polygon_3, correct_face_3, foil1_3, foil2_3]
    for thisComponent in AB3testComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    AB3testClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "AB3test"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = AB3testClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=AB3testClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_resp_3* updates
        waitOnFlip = False
        if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.75-frameTolerance:
            # keep track of start time/frame for later
            key_resp_3.frameNStart = frameN  # exact frame index
            key_resp_3.tStart = t  # local t and not account for scr refresh
            key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
            key_resp_3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_3.tStartRefresh + 2.25-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_3.tStop = t  # not accounting for scr refresh
                key_resp_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp_3, 'tStopRefresh')  # time at next scr refresh
                key_resp_3.status = FINISHED
        if key_resp_3.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_3.getKeys(keyList=['1', '2', '3'], waitRelease=False)
            _key_resp_3_allKeys.extend(theseKeys)
            if len(_key_resp_3_allKeys):
                key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
                key_resp_3.rt = _key_resp_3_allKeys[-1].rt
        
        # *cue_3* updates
        if cue_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cue_3.frameNStart = frameN  # exact frame index
            cue_3.tStart = t  # local t and not account for scr refresh
            cue_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cue_3, 'tStartRefresh')  # time at next scr refresh
            cue_3.setAutoDraw(True)
        if cue_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cue_3.tStartRefresh + 3.5-frameTolerance:
                # keep track of stop time/frame for later
                cue_3.tStop = t  # not accounting for scr refresh
                cue_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(cue_3, 'tStopRefresh')  # time at next scr refresh
                cue_3.setAutoDraw(False)
        
        # *polygon_3* updates
        if polygon_3.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_3.frameNStart = frameN  # exact frame index
            polygon_3.tStart = t  # local t and not account for scr refresh
            polygon_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_3, 'tStartRefresh')  # time at next scr refresh
            polygon_3.setAutoDraw(True)
        if polygon_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_3.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                polygon_3.tStop = t  # not accounting for scr refresh
                polygon_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon_3, 'tStopRefresh')  # time at next scr refresh
                polygon_3.setAutoDraw(False)
        
        # *correct_face_3* updates
        if correct_face_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            correct_face_3.frameNStart = frameN  # exact frame index
            correct_face_3.tStart = t  # local t and not account for scr refresh
            correct_face_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(correct_face_3, 'tStartRefresh')  # time at next scr refresh
            correct_face_3.setAutoDraw(True)
        if correct_face_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > correct_face_3.tStartRefresh + 3.5-frameTolerance:
                # keep track of stop time/frame for later
                correct_face_3.tStop = t  # not accounting for scr refresh
                correct_face_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(correct_face_3, 'tStopRefresh')  # time at next scr refresh
                correct_face_3.setAutoDraw(False)
        
        # *foil1_3* updates
        if foil1_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            foil1_3.frameNStart = frameN  # exact frame index
            foil1_3.tStart = t  # local t and not account for scr refresh
            foil1_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(foil1_3, 'tStartRefresh')  # time at next scr refresh
            foil1_3.setAutoDraw(True)
        if foil1_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > foil1_3.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                foil1_3.tStop = t  # not accounting for scr refresh
                foil1_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(foil1_3, 'tStopRefresh')  # time at next scr refresh
                foil1_3.setAutoDraw(False)
        
        # *foil2_3* updates
        if foil2_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            foil2_3.frameNStart = frameN  # exact frame index
            foil2_3.tStart = t  # local t and not account for scr refresh
            foil2_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(foil2_3, 'tStartRefresh')  # time at next scr refresh
            foil2_3.setAutoDraw(True)
        if foil2_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > foil2_3.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                foil2_3.tStop = t  # not accounting for scr refresh
                foil2_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(foil2_3, 'tStopRefresh')  # time at next scr refresh
                foil2_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in AB3testComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "AB3test"-------
    for thisComponent in AB3testComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('test3_face', test3_face_image[zzz])
    thisExp.addData('test3_objectA', test3_objectA_image[zzz])
    thisExp.addData('test3_foil1', foil1_fc[zzz])
    thisExp.addData('test3_foil2', foil2_fc[zzz])
    
    zzz = zzz+1
    # check responses
    if key_resp_3.keys in ['', [], None]:  # No response was made
        key_resp_3.keys = None
    test3.addData('key_resp_3.keys',key_resp_3.keys)
    if key_resp_3.keys != None:  # we had a response
        test3.addData('key_resp_3.rt', key_resp_3.rt)
    test3.addData('key_resp_3.started', key_resp_3.tStartRefresh)
    test3.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
    test3.addData('cue_3.started', cue_3.tStartRefresh)
    test3.addData('cue_3.stopped', cue_3.tStopRefresh)
    test3.addData('polygon_3.started', polygon_3.tStartRefresh)
    test3.addData('polygon_3.stopped', polygon_3.tStopRefresh)
    test3.addData('correct_face_3.started', correct_face_3.tStartRefresh)
    test3.addData('correct_face_3.stopped', correct_face_3.tStopRefresh)
    test3.addData('foil1_3.started', foil1_3.tStartRefresh)
    test3.addData('foil1_3.stopped', foil1_3.tStopRefresh)
    test3.addData('foil2_3.started', foil2_3.tStartRefresh)
    test3.addData('foil2_3.stopped', foil2_3.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'test3'


# ------Prepare to start Routine "break3"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
break3Components = [text_7]
for thisComponent in break3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
break3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "break3"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = break3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=break3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_7* updates
    if text_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_7.frameNStart = frameN  # exact frame index
        text_7.tStart = t  # local t and not account for scr refresh
        text_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
        text_7.setAutoDraw(True)
    if text_7.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_7.tStartRefresh + 3.0-frameTolerance:
            # keep track of stop time/frame for later
            text_7.tStop = t  # not accounting for scr refresh
            text_7.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_7, 'tStopRefresh')  # time at next scr refresh
            text_7.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in break3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "break3"-------
for thisComponent in break3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_7.started', text_7.tStartRefresh)
thisExp.addData('text_7.stopped', text_7.tStopRefresh)

# set up handler to look after randomisation of conditions etc
BCstudy = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('all_df_demo.csv'),
    seed=None, name='BCstudy')
thisExp.addLoop(BCstudy)  # add the loop to the experiment
thisBCstudy = BCstudy.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBCstudy.rgb)
if thisBCstudy != None:
    for paramName in thisBCstudy:
        exec('{} = thisBCstudy[paramName]'.format(paramName))

for thisBCstudy in BCstudy:
    currentLoop = BCstudy
    # abbreviate parameter names if possible (e.g. rgb = thisBCstudy.rgb)
    if thisBCstudy != None:
        for paramName in thisBCstudy:
            exec('{} = thisBCstudy[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "BC"-------
    continueRoutine = True
    routineTimer.add(3.500000)
    # update component parameters for each repeat
    orig_objectA_image = study1pairs[randord5[g]][1]
    face_image4 = study1pairs[randord5[g]][0]
    objectC_image4 = objectClist[randord5[g]]
    
    thisExp.addData('face_image4', face_image4)
    thisExp.addData('objectC_image4', objectC_image4)
    thisExp.addData('orig_objectA_image', orig_objectA_image)
    face_4.setImage(face_image4)
    object_4.setImage(objectC_image4)
    # keep track of which components have finished
    BCComponents = [face_4, object_4, text_5]
    for thisComponent in BCComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    BCClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "BC"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = BCClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=BCClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *face_4* updates
        if face_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            face_4.frameNStart = frameN  # exact frame index
            face_4.tStart = t  # local t and not account for scr refresh
            face_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(face_4, 'tStartRefresh')  # time at next scr refresh
            face_4.setAutoDraw(True)
        if face_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > face_4.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                face_4.tStop = t  # not accounting for scr refresh
                face_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(face_4, 'tStopRefresh')  # time at next scr refresh
                face_4.setAutoDraw(False)
        
        # *object_4* updates
        if object_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            object_4.frameNStart = frameN  # exact frame index
            object_4.tStart = t  # local t and not account for scr refresh
            object_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(object_4, 'tStartRefresh')  # time at next scr refresh
            object_4.setAutoDraw(True)
        if object_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > object_4.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                object_4.tStop = t  # not accounting for scr refresh
                object_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(object_4, 'tStopRefresh')  # time at next scr refresh
                object_4.setAutoDraw(False)
        
        # *text_5* updates
        if text_5.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            text_5.frameNStart = frameN  # exact frame index
            text_5.tStart = t  # local t and not account for scr refresh
            text_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
            text_5.setAutoDraw(True)
        if text_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_5.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                text_5.tStop = t  # not accounting for scr refresh
                text_5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_5, 'tStopRefresh')  # time at next scr refresh
                text_5.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in BCComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "BC"-------
    for thisComponent in BCComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('face4', face_image4[g])
    thisExp.addData('objectC', objectC_image4[g])
    thisExp.addData('orig_objectA', orig_objectA_image[g])
    
    trialpair4 = [face_image4, objectC_image4]
    study4pairs.append(trialpair4)
    orig_object.append(orig_objectA_image)
    g = g + 1
    BCstudy.addData('face_4.started', face_4.tStartRefresh)
    BCstudy.addData('face_4.stopped', face_4.tStopRefresh)
    BCstudy.addData('object_4.started', object_4.tStartRefresh)
    BCstudy.addData('object_4.stopped', object_4.tStopRefresh)
    BCstudy.addData('text_5.started', text_5.tStartRefresh)
    BCstudy.addData('text_5.stopped', text_5.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'BCstudy'


# set up handler to look after randomisation of conditions etc
test4 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('all_df_demo.csv'),
    seed=None, name='test4')
thisExp.addLoop(test4)  # add the loop to the experiment
thisTest4 = test4.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTest4.rgb)
if thisTest4 != None:
    for paramName in thisTest4:
        exec('{} = thisTest4[paramName]'.format(paramName))

for thisTest4 in test4:
    currentLoop = test4
    # abbreviate parameter names if possible (e.g. rgb = thisTest4.rgb)
    if thisTest4 != None:
        for paramName in thisTest4:
            exec('{} = thisTest4[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "BCtest"-------
    continueRoutine = True
    routineTimer.add(3.500000)
    # update component parameters for each repeat
    #import random
    #from numpy.random import random
    placement = random()
    
    testBC_face_image = study4pairs[randord6[bc_z]][0]
    testBC_objectC_image = study4pairs[randord6[bc_z]][-1]
    
    model = (testBC_face_image[-12:-9])
    val = (testBC_face_image[-8:-6])
    
    if val == 'NE':
        pickfrm = neufaceList
    if val == 'FE':
        pickfrm = emofaceList
    
    foils1 = []
    foils2 = []
    for stim in pickfrm:
        if stim != testBC_face_image:
            foils1.append(stim)
    foil1_fc = foils1[bc_z]
    
    for stim in pickfrm:
        if (stim != testBC_face_image) and (stim != foil1_fc):
            foils2.append(stim)
    foil2_fc = foils2[bc_z]
    thisExp.addData('testBC_face_image', testBC_face_image)
    thisExp.addData('testBC_objectC_image', testBC_objectC_image)
    thisExp.addData('testBC_foil1_image', foil1_fc)
    thisExp.addData('testBC_foil2_image', foil2_fc)
    
    if placement <= 0.33:
        targetPos=[-0.7, -0.5] #on the left
        foil1_pos=[0.0, -0.5] #in the middle
        foil2_pos=[0.7,-0.5] #on the right
        corrAns='1'
        feedback = targetPos
    if 0.33 < placement < 0.66:
        targetPos=[0.0, -0.5] #in the middle
        foil1_pos=[-0.7, -0.5] #on the left
        foil2_pos=[0.7, -0.5] #on the right
        corrAns= '2'
        feedback = targetPos
    if placement >= 0.66:
        targetPos=[0.7, -0.5] #on the right
        foil1_pos=[-0.7, -0.5] #on the left
        foil2_pos=[0.0, -0.5] #in the middle
        corrAns='3'
        feedback = targetPos
    
    #feedback = targetPos
    
    key_resp_4.keys = []
    key_resp_4.rt = []
    _key_resp_4_allKeys = []
    cue_4.setImage(testBC_objectC_image)
    polygon_4.setPos(targetPos)
    correct_face_4.setPos(targetPos)
    correct_face_4.setImage(testBC_face_image)
    foil1_4.setPos(foil1_pos)
    foil1_4.setImage(foil1_fc)
    foil2_4.setPos(foil2_pos)
    foil2_4.setImage(foil2_fc)
    # keep track of which components have finished
    BCtestComponents = [key_resp_4, cue_4, polygon_4, correct_face_4, foil1_4, foil2_4]
    for thisComponent in BCtestComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    BCtestClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "BCtest"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = BCtestClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=BCtestClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_resp_4* updates
        waitOnFlip = False
        if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.75-frameTolerance:
            # keep track of start time/frame for later
            key_resp_4.frameNStart = frameN  # exact frame index
            key_resp_4.tStart = t  # local t and not account for scr refresh
            key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
            key_resp_4.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_4.tStartRefresh + 2.25-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_4.tStop = t  # not accounting for scr refresh
                key_resp_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp_4, 'tStopRefresh')  # time at next scr refresh
                key_resp_4.status = FINISHED
        if key_resp_4.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_4.getKeys(keyList=['1', '2', '3'], waitRelease=False)
            _key_resp_4_allKeys.extend(theseKeys)
            if len(_key_resp_4_allKeys):
                key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
                key_resp_4.rt = _key_resp_4_allKeys[-1].rt
        
        # *cue_4* updates
        if cue_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cue_4.frameNStart = frameN  # exact frame index
            cue_4.tStart = t  # local t and not account for scr refresh
            cue_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cue_4, 'tStartRefresh')  # time at next scr refresh
            cue_4.setAutoDraw(True)
        if cue_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cue_4.tStartRefresh + 3.5-frameTolerance:
                # keep track of stop time/frame for later
                cue_4.tStop = t  # not accounting for scr refresh
                cue_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(cue_4, 'tStopRefresh')  # time at next scr refresh
                cue_4.setAutoDraw(False)
        
        # *polygon_4* updates
        if polygon_4.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_4.frameNStart = frameN  # exact frame index
            polygon_4.tStart = t  # local t and not account for scr refresh
            polygon_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_4, 'tStartRefresh')  # time at next scr refresh
            polygon_4.setAutoDraw(True)
        if polygon_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_4.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                polygon_4.tStop = t  # not accounting for scr refresh
                polygon_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon_4, 'tStopRefresh')  # time at next scr refresh
                polygon_4.setAutoDraw(False)
        
        # *correct_face_4* updates
        if correct_face_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            correct_face_4.frameNStart = frameN  # exact frame index
            correct_face_4.tStart = t  # local t and not account for scr refresh
            correct_face_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(correct_face_4, 'tStartRefresh')  # time at next scr refresh
            correct_face_4.setAutoDraw(True)
        if correct_face_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > correct_face_4.tStartRefresh + 3.5-frameTolerance:
                # keep track of stop time/frame for later
                correct_face_4.tStop = t  # not accounting for scr refresh
                correct_face_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(correct_face_4, 'tStopRefresh')  # time at next scr refresh
                correct_face_4.setAutoDraw(False)
        
        # *foil1_4* updates
        if foil1_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            foil1_4.frameNStart = frameN  # exact frame index
            foil1_4.tStart = t  # local t and not account for scr refresh
            foil1_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(foil1_4, 'tStartRefresh')  # time at next scr refresh
            foil1_4.setAutoDraw(True)
        if foil1_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > foil1_4.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                foil1_4.tStop = t  # not accounting for scr refresh
                foil1_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(foil1_4, 'tStopRefresh')  # time at next scr refresh
                foil1_4.setAutoDraw(False)
        
        # *foil2_4* updates
        if foil2_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            foil2_4.frameNStart = frameN  # exact frame index
            foil2_4.tStart = t  # local t and not account for scr refresh
            foil2_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(foil2_4, 'tStartRefresh')  # time at next scr refresh
            foil2_4.setAutoDraw(True)
        if foil2_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > foil2_4.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                foil2_4.tStop = t  # not accounting for scr refresh
                foil2_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(foil2_4, 'tStopRefresh')  # time at next scr refresh
                foil2_4.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in BCtestComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "BCtest"-------
    for thisComponent in BCtestComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('testBC_face', testBC_face_image[bc_z])
    thisExp.addData('testBC_objectC', testBC_objectC_image[bc_z])
    thisExp.addData('testBC_foil1', foil1_fc[bc_z])
    thisExp.addData('testBC_foil2', foil2_fc[bc_z])
    
    bc_z = bc_z + 1
    # check responses
    if key_resp_4.keys in ['', [], None]:  # No response was made
        key_resp_4.keys = None
    test4.addData('key_resp_4.keys',key_resp_4.keys)
    if key_resp_4.keys != None:  # we had a response
        test4.addData('key_resp_4.rt', key_resp_4.rt)
    test4.addData('key_resp_4.started', key_resp_4.tStartRefresh)
    test4.addData('key_resp_4.stopped', key_resp_4.tStopRefresh)
    test4.addData('cue_4.started', cue_4.tStartRefresh)
    test4.addData('cue_4.stopped', cue_4.tStopRefresh)
    test4.addData('polygon_4.started', polygon_4.tStartRefresh)
    test4.addData('polygon_4.stopped', polygon_4.tStopRefresh)
    test4.addData('correct_face_4.started', correct_face_4.tStartRefresh)
    test4.addData('correct_face_4.stopped', correct_face_4.tStopRefresh)
    test4.addData('foil1_4.started', foil1_4.tStartRefresh)
    test4.addData('foil1_4.stopped', foil1_4.tStopRefresh)
    test4.addData('foil2_4.started', foil2_4.tStartRefresh)
    test4.addData('foil2_4.stopped', foil2_4.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'test4'


# ------Prepare to start Routine "BeginAC"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
BeginACComponents = [text_8]
for thisComponent in BeginACComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
BeginACClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "BeginAC"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = BeginACClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=BeginACClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_8* updates
    if text_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_8.frameNStart = frameN  # exact frame index
        text_8.tStart = t  # local t and not account for scr refresh
        text_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_8, 'tStartRefresh')  # time at next scr refresh
        text_8.setAutoDraw(True)
    if text_8.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_8.tStartRefresh + 3.0-frameTolerance:
            # keep track of stop time/frame for later
            text_8.tStop = t  # not accounting for scr refresh
            text_8.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_8, 'tStopRefresh')  # time at next scr refresh
            text_8.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in BeginACComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "BeginAC"-------
for thisComponent in BeginACComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_8.started', text_8.tStartRefresh)
thisExp.addData('text_8.stopped', text_8.tStopRefresh)

# set up handler to look after randomisation of conditions etc
fin_loop = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('all_df_demo.csv'),
    seed=None, name='fin_loop')
thisExp.addLoop(fin_loop)  # add the loop to the experiment
thisFin_loop = fin_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisFin_loop.rgb)
if thisFin_loop != None:
    for paramName in thisFin_loop:
        exec('{} = thisFin_loop[paramName]'.format(paramName))

for thisFin_loop in fin_loop:
    currentLoop = fin_loop
    # abbreviate parameter names if possible (e.g. rgb = thisFin_loop.rgb)
    if thisFin_loop != None:
        for paramName in thisFin_loop:
            exec('{} = thisFin_loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "AC_test"-------
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    testAC_objectA_image = orig_object[randord7[ind_z]]
    testAC_objectC_image = study4pairs[randord7[ind_z]][-1]
    
    foils1 = []
    foils2 = []
    for stim in objectClist:
        if (stim != testAC_objectA_image) and (stim != testAC_objectC_image):
            foils1.append(stim)
    foil1_obj = foils1[ind_z]
    
    for stim in objectClist:
        if (stim != testAC_objectA_image) and (stim != testAC_objectC_image) and (stim != foil1_obj):
            foils2.append(stim)
    foil2_obj = foils2[ind_z]
    thisExp.addData('testAC_objectA_image', testAC_objectA_image)
    thisExp.addData('testAC_objectC_image', testAC_objectC_image)
    thisExp.addData('testAC_foil1_image', foil1_obj)
    thisExp.addData('testAC_foil2_image', foil2_obj)
    
    if placement <= 0.33:
        targetPos=[-0.7, -0.5] #on the left
        foil1_pos=[0.0, -0.5] #in the middle
        foil2_pos=[0.7,-0.5] #on the right
        corrAns='1'
        feedback = targetPos
    if 0.33 < placement < 0.66:
        targetPos=[0.0, -0.5] #in the middle
        foil1_pos=[-0.7, -0.5] #on the left
        foil2_pos=[0.7, -0.5] #on the right
        corrAns= '2'
        feedback = targetPos
    if placement >= 0.66:
        targetPos=[0.7, -0.5] #on the right
        foil1_pos=[-0.7, -0.5] #on the left
        foil2_pos=[0.0, -0.5] #in the middle
        corrAns='3'
        feedback = targetPos
    cueC.setImage(testAC_objectC_image)
    cor_object.setPos(targetPos)
    cor_object.setImage(testAC_objectA_image)
    foil1_image.setPos(foil1_pos)
    foil1_image.setImage(foil1_obj)
    foil2_image.setPos(foil2_pos)
    foil2_image.setImage(foil2_obj)
    key_resp_5.keys = []
    key_resp_5.rt = []
    _key_resp_5_allKeys = []
    # keep track of which components have finished
    AC_testComponents = [cueC, cor_object, foil1_image, foil2_image, key_resp_5]
    for thisComponent in AC_testComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    AC_testClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "AC_test"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = AC_testClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=AC_testClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *cueC* updates
        if cueC.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cueC.frameNStart = frameN  # exact frame index
            cueC.tStart = t  # local t and not account for scr refresh
            cueC.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cueC, 'tStartRefresh')  # time at next scr refresh
            cueC.setAutoDraw(True)
        if cueC.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cueC.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                cueC.tStop = t  # not accounting for scr refresh
                cueC.frameNStop = frameN  # exact frame index
                win.timeOnFlip(cueC, 'tStopRefresh')  # time at next scr refresh
                cueC.setAutoDraw(False)
        
        # *cor_object* updates
        if cor_object.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cor_object.frameNStart = frameN  # exact frame index
            cor_object.tStart = t  # local t and not account for scr refresh
            cor_object.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cor_object, 'tStartRefresh')  # time at next scr refresh
            cor_object.setAutoDraw(True)
        if cor_object.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cor_object.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                cor_object.tStop = t  # not accounting for scr refresh
                cor_object.frameNStop = frameN  # exact frame index
                win.timeOnFlip(cor_object, 'tStopRefresh')  # time at next scr refresh
                cor_object.setAutoDraw(False)
        
        # *foil1_image* updates
        if foil1_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            foil1_image.frameNStart = frameN  # exact frame index
            foil1_image.tStart = t  # local t and not account for scr refresh
            foil1_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(foil1_image, 'tStartRefresh')  # time at next scr refresh
            foil1_image.setAutoDraw(True)
        if foil1_image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > foil1_image.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                foil1_image.tStop = t  # not accounting for scr refresh
                foil1_image.frameNStop = frameN  # exact frame index
                win.timeOnFlip(foil1_image, 'tStopRefresh')  # time at next scr refresh
                foil1_image.setAutoDraw(False)
        
        # *foil2_image* updates
        if foil2_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            foil2_image.frameNStart = frameN  # exact frame index
            foil2_image.tStart = t  # local t and not account for scr refresh
            foil2_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(foil2_image, 'tStartRefresh')  # time at next scr refresh
            foil2_image.setAutoDraw(True)
        if foil2_image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > foil2_image.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                foil2_image.tStop = t  # not accounting for scr refresh
                foil2_image.frameNStop = frameN  # exact frame index
                win.timeOnFlip(foil2_image, 'tStopRefresh')  # time at next scr refresh
                foil2_image.setAutoDraw(False)
        
        # *key_resp_5* updates
        if key_resp_5.status == NOT_STARTED and t >= 0.75-frameTolerance:
            # keep track of start time/frame for later
            key_resp_5.frameNStart = frameN  # exact frame index
            key_resp_5.tStart = t  # local t and not account for scr refresh
            key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
            key_resp_5.status = STARTED
            # keyboard checking is just starting
            key_resp_5.clock.reset()  # now t=0
            key_resp_5.clearEvents(eventType='keyboard')
        if key_resp_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_5.tStartRefresh + 2.25-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_5.tStop = t  # not accounting for scr refresh
                key_resp_5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp_5, 'tStopRefresh')  # time at next scr refresh
                key_resp_5.status = FINISHED
        if key_resp_5.status == STARTED:
            theseKeys = key_resp_5.getKeys(keyList=['1', '2', '3'], waitRelease=False)
            _key_resp_5_allKeys.extend(theseKeys)
            if len(_key_resp_5_allKeys):
                key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
                key_resp_5.rt = _key_resp_5_allKeys[-1].rt
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in AC_testComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "AC_test"-------
    for thisComponent in AC_testComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('testAC_objectA', testAC_objectA_image[ind_z])
    thisExp.addData('testAC_objectC', testAC_objectC_image[ind_z])
    thisExp.addData('testAC_foil1', foil1_obj[ind_z])
    thisExp.addData('testAC_foil2', foil2_obj[ind_z])
    
    ind_z = ind_z + 1
    fin_loop.addData('cueC.started', cueC.tStartRefresh)
    fin_loop.addData('cueC.stopped', cueC.tStopRefresh)
    fin_loop.addData('cor_object.started', cor_object.tStartRefresh)
    fin_loop.addData('cor_object.stopped', cor_object.tStopRefresh)
    fin_loop.addData('foil1_image.started', foil1_image.tStartRefresh)
    fin_loop.addData('foil1_image.stopped', foil1_image.tStopRefresh)
    fin_loop.addData('foil2_image.started', foil2_image.tStartRefresh)
    fin_loop.addData('foil2_image.stopped', foil2_image.tStopRefresh)
    # check responses
    if key_resp_5.keys in ['', [], None]:  # No response was made
        key_resp_5.keys = None
    fin_loop.addData('key_resp_5.keys',key_resp_5.keys)
    if key_resp_5.keys != None:  # we had a response
        fin_loop.addData('key_resp_5.rt', key_resp_5.rt)
    fin_loop.addData('key_resp_5.started', key_resp_5.tStart)
    fin_loop.addData('key_resp_5.stopped', key_resp_5.tStop)
    thisExp.nextEntry()
    
# completed 1 repeats of 'fin_loop'


# set up handler to look after randomisation of conditions etc
end_trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('all_df_demo.csv'),
    seed=None, name='end_trials')
thisExp.addLoop(end_trials)  # add the loop to the experiment
thisEnd_trial = end_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisEnd_trial.rgb)
if thisEnd_trial != None:
    for paramName in thisEnd_trial:
        exec('{} = thisEnd_trial[paramName]'.format(paramName))

for thisEnd_trial in end_trials:
    currentLoop = end_trials
    # abbreviate parameter names if possible (e.g. rgb = thisEnd_trial.rgb)
    if thisEnd_trial != None:
        for paramName in thisEnd_trial:
            exec('{} = thisEnd_trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "FinalAB_test"-------
    continueRoutine = True
    routineTimer.add(3.500000)
    # update component parameters for each repeat
    import random
    from numpy.random import random
    placement = random()
    
    endtest_face_image = study1pairs[randord8[end_z]][0]
    endtest_objectA_image = study1pairs[randord8[end_z]][-1]
    
    model = (endtest_face_image[-12:-9])
    val = (endtest_face_image[-8:-6])
    
    if val == 'NE':
        pickfrm = neufaceList
    if val == 'FE':
        pickfrm = emofaceList
    
    foils1 = []
    foils2 = []
    for stim in pickfrm:
        if stim != endtest_face_image:
            foils1.append(stim)
    foil1_fc = foils1[end_z]
    
    for stim in pickfrm:
        if (stim != endtest_face_image) and (stim != foil1_fc):
            foils2.append(stim)
    foil2_fc = foils2[end_z]
    thisExp.addData('endtest_face_image', endtest_face_image)
    thisExp.addData('endtest_objectA_image', endtest_objectA_image)
    thisExp.addData('endtest_foil1_image', foil1_fc)
    thisExp.addData('endtest_foil2_image', foil2_fc)
    
    if placement <= 0.33:
        targetPos=[-0.7, -0.5] #on the left
        foil1_pos=[0.0, -0.5] #in the middle
        foil2_pos=[0.7,-0.5] #on the right
        corrAns='1'
        feedback = targetPos
    if 0.33 < placement < 0.66:
        targetPos=[0.0, -0.5] #in the middle
        foil1_pos=[-0.7, -0.5] #on the left
        foil2_pos=[0.7, -0.5] #on the right
        corrAns= '2'
        feedback = targetPos
    if placement >= 0.66:
        targetPos=[0.7, -0.5] #on the right
        foil1_pos=[-0.7, -0.5] #on the left
        foil2_pos=[0.0, -0.5] #in the middle
        corrAns='3'
        feedback = targetPos
    
    #feedback = targetPos
    
    cue_5.setImage(endtest_objectA_image)
    polygon_5.setPos(targetPos)
    correct_face_5.setPos(targetPos)
    correct_face_5.setImage(endtest_face_image)
    foil1_5.setPos(foil1_pos)
    foil1_5.setImage(foil1_fc)
    foil2_5.setPos(foil2_pos)
    foil2_5.setImage(foil2_fc)
    key_resp_7.keys = []
    key_resp_7.rt = []
    _key_resp_7_allKeys = []
    # keep track of which components have finished
    FinalAB_testComponents = [cue_5, polygon_5, correct_face_5, foil1_5, foil2_5, key_resp_7]
    for thisComponent in FinalAB_testComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    FinalAB_testClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "FinalAB_test"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = FinalAB_testClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=FinalAB_testClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *cue_5* updates
        if cue_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cue_5.frameNStart = frameN  # exact frame index
            cue_5.tStart = t  # local t and not account for scr refresh
            cue_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cue_5, 'tStartRefresh')  # time at next scr refresh
            cue_5.setAutoDraw(True)
        if cue_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cue_5.tStartRefresh + 3.5-frameTolerance:
                # keep track of stop time/frame for later
                cue_5.tStop = t  # not accounting for scr refresh
                cue_5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(cue_5, 'tStopRefresh')  # time at next scr refresh
                cue_5.setAutoDraw(False)
        
        # *polygon_5* updates
        if polygon_5.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_5.frameNStart = frameN  # exact frame index
            polygon_5.tStart = t  # local t and not account for scr refresh
            polygon_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_5, 'tStartRefresh')  # time at next scr refresh
            polygon_5.setAutoDraw(True)
        if polygon_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_5.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                polygon_5.tStop = t  # not accounting for scr refresh
                polygon_5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon_5, 'tStopRefresh')  # time at next scr refresh
                polygon_5.setAutoDraw(False)
        
        # *correct_face_5* updates
        if correct_face_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            correct_face_5.frameNStart = frameN  # exact frame index
            correct_face_5.tStart = t  # local t and not account for scr refresh
            correct_face_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(correct_face_5, 'tStartRefresh')  # time at next scr refresh
            correct_face_5.setAutoDraw(True)
        if correct_face_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > correct_face_5.tStartRefresh + 3.5-frameTolerance:
                # keep track of stop time/frame for later
                correct_face_5.tStop = t  # not accounting for scr refresh
                correct_face_5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(correct_face_5, 'tStopRefresh')  # time at next scr refresh
                correct_face_5.setAutoDraw(False)
        
        # *foil1_5* updates
        if foil1_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            foil1_5.frameNStart = frameN  # exact frame index
            foil1_5.tStart = t  # local t and not account for scr refresh
            foil1_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(foil1_5, 'tStartRefresh')  # time at next scr refresh
            foil1_5.setAutoDraw(True)
        if foil1_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > foil1_5.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                foil1_5.tStop = t  # not accounting for scr refresh
                foil1_5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(foil1_5, 'tStopRefresh')  # time at next scr refresh
                foil1_5.setAutoDraw(False)
        
        # *foil2_5* updates
        if foil2_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            foil2_5.frameNStart = frameN  # exact frame index
            foil2_5.tStart = t  # local t and not account for scr refresh
            foil2_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(foil2_5, 'tStartRefresh')  # time at next scr refresh
            foil2_5.setAutoDraw(True)
        if foil2_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > foil2_5.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                foil2_5.tStop = t  # not accounting for scr refresh
                foil2_5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(foil2_5, 'tStopRefresh')  # time at next scr refresh
                foil2_5.setAutoDraw(False)
        
        # *key_resp_7* updates
        if key_resp_7.status == NOT_STARTED and t >= 0.75-frameTolerance:
            # keep track of start time/frame for later
            key_resp_7.frameNStart = frameN  # exact frame index
            key_resp_7.tStart = t  # local t and not account for scr refresh
            key_resp_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_7, 'tStartRefresh')  # time at next scr refresh
            key_resp_7.status = STARTED
            # keyboard checking is just starting
            key_resp_7.clock.reset()  # now t=0
            key_resp_7.clearEvents(eventType='keyboard')
        if key_resp_7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_7.tStartRefresh + 2.25-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_7.tStop = t  # not accounting for scr refresh
                key_resp_7.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp_7, 'tStopRefresh')  # time at next scr refresh
                key_resp_7.status = FINISHED
        if key_resp_7.status == STARTED:
            theseKeys = key_resp_7.getKeys(keyList=['1', '2', '3'], waitRelease=False)
            _key_resp_7_allKeys.extend(theseKeys)
            if len(_key_resp_7_allKeys):
                key_resp_7.keys = _key_resp_7_allKeys[-1].name  # just the last key pressed
                key_resp_7.rt = _key_resp_7_allKeys[-1].rt
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FinalAB_testComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "FinalAB_test"-------
    for thisComponent in FinalAB_testComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('endtest1_face', endtest_face_image[end_z])
    thisExp.addData('endtest1_objectA', endtest_objectA_image[end_z])
    thisExp.addData('endtest1_foil1', foil1_fc[end_z])
    thisExp.addData('endtest1_foil2', foil2_fc[end_z])
    
    end_z = end_z+1
    end_trials.addData('cue_5.started', cue_5.tStartRefresh)
    end_trials.addData('cue_5.stopped', cue_5.tStopRefresh)
    end_trials.addData('polygon_5.started', polygon_5.tStartRefresh)
    end_trials.addData('polygon_5.stopped', polygon_5.tStopRefresh)
    end_trials.addData('correct_face_5.started', correct_face_5.tStartRefresh)
    end_trials.addData('correct_face_5.stopped', correct_face_5.tStopRefresh)
    end_trials.addData('foil1_5.started', foil1_5.tStartRefresh)
    end_trials.addData('foil1_5.stopped', foil1_5.tStopRefresh)
    end_trials.addData('foil2_5.started', foil2_5.tStartRefresh)
    end_trials.addData('foil2_5.stopped', foil2_5.tStopRefresh)
    # check responses
    if key_resp_7.keys in ['', [], None]:  # No response was made
        key_resp_7.keys = None
    end_trials.addData('key_resp_7.keys',key_resp_7.keys)
    if key_resp_7.keys != None:  # we had a response
        end_trials.addData('key_resp_7.rt', key_resp_7.rt)
    end_trials.addData('key_resp_7.started', key_resp_7.tStart)
    end_trials.addData('key_resp_7.stopped', key_resp_7.tStop)
    
    # ------Prepare to start Routine "FinalBC_test"-------
    continueRoutine = True
    routineTimer.add(3.500000)
    # update component parameters for each repeat
    import random
    from numpy.random import random
    placement = random()
    
    endtest_face2_image = study4pairs[randord9[end_y]][0]
    endtest_objectC_image = study4pairs[randord9[end_y]][-1]
    
    model = (endtest_face2_image[-12:-9])
    val = (endtest_face2_image[-8:-6])
    
    if val == 'NE':
        pickfrm = neufaceList
    if val == 'FE':
        pickfrm = emofaceList
    
    foils1 = []
    foils2 = []
    for stim in pickfrm:
        if stim != endtest_face2_image:
            foils1.append(stim)
    foil1_fc = foils1[end_y]
    
    for stim in pickfrm:
        if (stim != endtest_face2_image) and (stim != foil1_fc):
            foils2.append(stim)
    foil2_fc = foils2[end_y]
    thisExp.addData('endtest_face2_image', endtest_face2_image)
    thisExp.addData('endtest_objectC_image', endtest_objectC_image)
    thisExp.addData('endtest_foil1_image', foil1_fc)
    thisExp.addData('endtest_foil2_image', foil2_fc)
    
    if placement <= 0.33:
        targetPos=[-0.7, -0.5] #on the left
        foil1_pos=[0.0, -0.5] #in the middle
        foil2_pos=[0.7,-0.5] #on the right
        corrAns='1'
        feedback = targetPos
    if 0.33 < placement < 0.66:
        targetPos=[0.0, -0.5] #in the middle
        foil1_pos=[-0.7, -0.5] #on the left
        foil2_pos=[0.7, -0.5] #on the right
        corrAns= '2'
        feedback = targetPos
    if placement >= 0.66:
        targetPos=[0.7, -0.5] #on the right
        foil1_pos=[-0.7, -0.5] #on the left
        foil2_pos=[0.0, -0.5] #in the middle
        corrAns='3'
        feedback = targetPos
    
    #feedback = targetPos
    
    cue_6.setImage(endtest_objectC_image)
    polygon_6.setPos(targetPos)
    correct_face_6.setPos(targetPos)
    correct_face_6.setImage(endtest_face2_image)
    foil1_6.setPos(foil1_pos)
    foil1_6.setImage(foil1_fc)
    foil2_6.setPos(foil2_pos)
    foil2_6.setImage(foil2_fc)
    key_resp_8.keys = []
    key_resp_8.rt = []
    _key_resp_8_allKeys = []
    # keep track of which components have finished
    FinalBC_testComponents = [cue_6, polygon_6, correct_face_6, foil1_6, foil2_6, key_resp_8]
    for thisComponent in FinalBC_testComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    FinalBC_testClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "FinalBC_test"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = FinalBC_testClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=FinalBC_testClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *cue_6* updates
        if cue_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cue_6.frameNStart = frameN  # exact frame index
            cue_6.tStart = t  # local t and not account for scr refresh
            cue_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cue_6, 'tStartRefresh')  # time at next scr refresh
            cue_6.setAutoDraw(True)
        if cue_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cue_6.tStartRefresh + 3.5-frameTolerance:
                # keep track of stop time/frame for later
                cue_6.tStop = t  # not accounting for scr refresh
                cue_6.frameNStop = frameN  # exact frame index
                win.timeOnFlip(cue_6, 'tStopRefresh')  # time at next scr refresh
                cue_6.setAutoDraw(False)
        
        # *polygon_6* updates
        if polygon_6.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_6.frameNStart = frameN  # exact frame index
            polygon_6.tStart = t  # local t and not account for scr refresh
            polygon_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_6, 'tStartRefresh')  # time at next scr refresh
            polygon_6.setAutoDraw(True)
        if polygon_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_6.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                polygon_6.tStop = t  # not accounting for scr refresh
                polygon_6.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon_6, 'tStopRefresh')  # time at next scr refresh
                polygon_6.setAutoDraw(False)
        
        # *correct_face_6* updates
        if correct_face_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            correct_face_6.frameNStart = frameN  # exact frame index
            correct_face_6.tStart = t  # local t and not account for scr refresh
            correct_face_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(correct_face_6, 'tStartRefresh')  # time at next scr refresh
            correct_face_6.setAutoDraw(True)
        if correct_face_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > correct_face_6.tStartRefresh + 3.5-frameTolerance:
                # keep track of stop time/frame for later
                correct_face_6.tStop = t  # not accounting for scr refresh
                correct_face_6.frameNStop = frameN  # exact frame index
                win.timeOnFlip(correct_face_6, 'tStopRefresh')  # time at next scr refresh
                correct_face_6.setAutoDraw(False)
        
        # *foil1_6* updates
        if foil1_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            foil1_6.frameNStart = frameN  # exact frame index
            foil1_6.tStart = t  # local t and not account for scr refresh
            foil1_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(foil1_6, 'tStartRefresh')  # time at next scr refresh
            foil1_6.setAutoDraw(True)
        if foil1_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > foil1_6.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                foil1_6.tStop = t  # not accounting for scr refresh
                foil1_6.frameNStop = frameN  # exact frame index
                win.timeOnFlip(foil1_6, 'tStopRefresh')  # time at next scr refresh
                foil1_6.setAutoDraw(False)
        
        # *foil2_6* updates
        if foil2_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            foil2_6.frameNStart = frameN  # exact frame index
            foil2_6.tStart = t  # local t and not account for scr refresh
            foil2_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(foil2_6, 'tStartRefresh')  # time at next scr refresh
            foil2_6.setAutoDraw(True)
        if foil2_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > foil2_6.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                foil2_6.tStop = t  # not accounting for scr refresh
                foil2_6.frameNStop = frameN  # exact frame index
                win.timeOnFlip(foil2_6, 'tStopRefresh')  # time at next scr refresh
                foil2_6.setAutoDraw(False)
        
        # *key_resp_8* updates
        if key_resp_8.status == NOT_STARTED and t >= 0.75-frameTolerance:
            # keep track of start time/frame for later
            key_resp_8.frameNStart = frameN  # exact frame index
            key_resp_8.tStart = t  # local t and not account for scr refresh
            key_resp_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_8, 'tStartRefresh')  # time at next scr refresh
            key_resp_8.status = STARTED
            # keyboard checking is just starting
            key_resp_8.clock.reset()  # now t=0
            key_resp_8.clearEvents(eventType='keyboard')
        if key_resp_8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_8.tStartRefresh + 2.25-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_8.tStop = t  # not accounting for scr refresh
                key_resp_8.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp_8, 'tStopRefresh')  # time at next scr refresh
                key_resp_8.status = FINISHED
        if key_resp_8.status == STARTED:
            theseKeys = key_resp_8.getKeys(keyList=['1', '2', '3'], waitRelease=False)
            _key_resp_8_allKeys.extend(theseKeys)
            if len(_key_resp_8_allKeys):
                key_resp_8.keys = _key_resp_8_allKeys[-1].name  # just the last key pressed
                key_resp_8.rt = _key_resp_8_allKeys[-1].rt
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FinalBC_testComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "FinalBC_test"-------
    for thisComponent in FinalBC_testComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('endtest2_face', endtest_face2_image[end_y])
    thisExp.addData('endtest2_objectA', endtest_objectC_image[end_y])
    thisExp.addData('endtest2_foil1', foil1_fc[end_y])
    thisExp.addData('endtest2_foil2', foil2_fc[end_y])
    
    end_y = end_y +1
    end_trials.addData('cue_6.started', cue_6.tStartRefresh)
    end_trials.addData('cue_6.stopped', cue_6.tStopRefresh)
    end_trials.addData('polygon_6.started', polygon_6.tStartRefresh)
    end_trials.addData('polygon_6.stopped', polygon_6.tStopRefresh)
    end_trials.addData('correct_face_6.started', correct_face_6.tStartRefresh)
    end_trials.addData('correct_face_6.stopped', correct_face_6.tStopRefresh)
    end_trials.addData('foil1_6.started', foil1_6.tStartRefresh)
    end_trials.addData('foil1_6.stopped', foil1_6.tStopRefresh)
    end_trials.addData('foil2_6.started', foil2_6.tStartRefresh)
    end_trials.addData('foil2_6.stopped', foil2_6.tStopRefresh)
    # check responses
    if key_resp_8.keys in ['', [], None]:  # No response was made
        key_resp_8.keys = None
    end_trials.addData('key_resp_8.keys',key_resp_8.keys)
    if key_resp_8.keys != None:  # we had a response
        end_trials.addData('key_resp_8.rt', key_resp_8.rt)
    end_trials.addData('key_resp_8.started', key_resp_8.tStart)
    end_trials.addData('key_resp_8.stopped', key_resp_8.tStop)
    thisExp.nextEntry()
    
# completed 1 repeats of 'end_trials'


# ------Prepare to start Routine "end"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
endComponents = [text_10]
for thisComponent in endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "end"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_10* updates
    if text_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_10.frameNStart = frameN  # exact frame index
        text_10.tStart = t  # local t and not account for scr refresh
        text_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_10, 'tStartRefresh')  # time at next scr refresh
        text_10.setAutoDraw(True)
    if text_10.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_10.tStartRefresh + 3.0-frameTolerance:
            # keep track of stop time/frame for later
            text_10.tStop = t  # not accounting for scr refresh
            text_10.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_10, 'tStopRefresh')  # time at next scr refresh
            text_10.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_10.started', text_10.tStartRefresh)
thisExp.addData('text_10.stopped', text_10.tStopRefresh)

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
