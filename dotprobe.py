# import modules
from psychopy import prefs
from psychopy import visual, event, core, gui
import time, numpy
from numpy import random
import os
import platform

# participant information gui
info = {"Participant number":0, "Full Name":"Name LastName", "Gender":["Male", "Female", "X"], "Age":0}  ##Heb Gender nog aangepast naar de 3 opties
infoDlg = gui.DlgFromDict(dictionary=info, title="Dot Probe Experiment")
if infoDlg.OK:  # this will be True (user hit OK) or False (cancelled)
    print(info)
else:
    print("User Cancelled")

# extract the name of the participant from the dialog box information
subject_name = info["Full Name"]
firstName = info["Full Name"].split()[0].capitalize() ## Ik heb het hier bij gezet, denk dat dat wat overzichtelijker is en heb ook gezord dat de eerste letter een hoofdletter is

#Experiment variables

nTrials = 25                                            # Total number of trials = gelijk aan aantal woordparen

#Fixation cross
fixationCross = visual.TextStim(win, text="+")
fixationTime = 0.25                                     # duration of fixation cross

#Dot stimulus
dotStim = visual.circle(win, radius=0.5, fillColor= "blue", lineColor = "blue")
dotPos = numpy.array([0.5, -0.5]) ##place dot on top or bottom (geen idee of dit klopt, kan je dat even nakijken aub?)

dotSides = numpy.array(["top", "bottom"]) # to add the presentation side to the trial matrix

#Word variables
wordPosition = numpy.array([0.5, -0.5])                 ##To place the word on top or bottom location (opnieuw geen idee of dit klopt)
stimTime = numpy.array([0.5, 0.6, 0.7, 0.8, 0.9])       # duration of stimulus presentation

#Neutral Words
NeutralWord = numpy.array(["Parked", "Dried", "Physics","Clarets","Wagons","Data","Detail","Hill","Remarks","Crew","Approximate","Racket","Pupils","Tent","Edited","Note","Check","Furniture","Campus","Pond","Saddle","Cars","League","Laws","Lists"])

#Emotional Words
EmotionalWord = numpy.array(["Suffer","Wound","Attacks","Panicky","Horror","Dead","Afraid","Evil","Disease","Bomb","Catastrophe","Lethal","Terror","Trap","Coffin","Fear","Enemy","Destroyed","Damage","Harm","Cancer","Shot","Danger","Pain","Dying"])

# Response keys
responseKeys=numpy.array(['j','f'])
# assign response keys to all trials according to the blocks
# blocks 1 and 2 have j as the response key, blocks 3 and 4 have f as the response key
respKey = numpy.repeat(numpy.repeat(responseKeys, nBlock/len(responseKeys)), nBlockTrials) ##dit heb ik gekopieerd, moet nog aangepast worden aan ons experiment, aangezien we geen blocks hebben weet ik niet hoe we dat kunnen doen

# initialize empty arrays for the response columns of the trial matrix
keypress=numpy.repeat("", nTrials)
rt=numpy.repeat(-99.9, nTrials)
accuracy=numpy.repeat(-99.9, nTrials)  ## heb de -1 veranderd naar -99.9 zodat het echt heel hard opvalt als het fout is gegaan

# initialize arrays for participant ID
subjID = numpy.repeat(info["Participant ID"],nTrials)  ## moet dit niet "Participant number" zijn?


## form the trial matrix (hier ben ik niet goed in dus kan je dit even nakijken of dit klopt aub?)

trials = numpy.column_stack([subjID, stimSide, dotSides, wordPosition, dotPos, dotSides, NeutralWord, EmotionalWord, respKey, keypress, rt, accuracy])

# initializing
win = visual.Window(color= "black", units="norm", size = fullscr)  #create window
my_clock = core.Clock() #create clock

#stop the experiment whenever you want with Q key
event.globalKeys.add(key='q', func=core.quit, name='shutdown') ## moest op de vorige test dus zet het er hier ook maar bij, zo kunnen we altijd uit het experiment gaan


#initializing message text

firstName = info["Full Name"].split()[0]
welcomeMsg = visual.TextStim(win, text = "Welcome " + firstName + "!\n\nPress the space bar to continue.")
instructionMsg = visual.TextStim(win, text = "Placeholder", height=.1)
goodbyeMsg = visual.TextStim(win, text = "Thanks for your participation " + firstName + "!\n\nPress the space bar to end the experiment.")
stimulus = visual.TextStim(win, text="X") #the word that will be presented


instructionMsg.text = ( "In this experiment you will see two words on the screen, one at the top and one at the bottom.\n" +
                        "Whenever you see a blue dot at the top, press the 'J' button on your keyboard.\n" +
                        "Whenever you see a blue dot at the bottom, press the 'F' button on your keyboard.\n" +
                        "Press the space bar to proceed to the first block.")

# Function: the welcome message
def Welcome():
    welcomeMsg.draw()
    win.flip()
    event.waitKeys(keyList = "space")

# Function: the instruction message
def Instructions():
    instructionMsg.draw()
    win.flip()
    event.waitKeys(keyList = "space")

##hieronder moet dan de trial loop komen, ik denk dat de meeste variabelen er al zijn die we moeten hebben. Ze moeten wel nog gerandomiseerd worden.




# Function: the goodbye message
def Goodbye():
    goodbyeMsg.draw() 
    win.flip()
    event.waitKeys(keyList = "space")



## Ik heb alles in definities gegooid zoals in hoofdstuk 6
# Display the welcome message
Welcome()
# Display the instructions
Instructions()
# Display the stimuli

# Display the goodbye message
Goodbye()


#print the resulting trial matrix
print(trials)
# end the experiment
win.close()
