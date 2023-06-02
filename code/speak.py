# engine.runAndWait() blocks window.mainloop() and therefore must use subprocess
# otherwise the main program will close
import sys
import pyttsx3           # Text to Speech Component

# goodVoices = [7, 33, 0, 17, 26, 28]   # this line is goodVoices variable, add voices you want from selection here
# good voice numbers are the following: 7(daniel)*, 33(samantha)*, 0(Alex), 17(karen), 26(melina), 28(moira)

engine = pyttsx3.init()
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
engine.setProperty('voice', voices[int(sys.argv[2])].id)    # comment out this line and uncomment the line below + goodVoices variable to limit voice selection (make sure to do the same in speak.py)
#engine.setProperty('voice', voices[goodVoices[int(sys.argv[2])]].id)
engine.setProperty('rate', rate+int(sys.argv[3]))
if (int(sys.argv[4])):
    engine.say(str(sys.argv[1]))
else:
    engine.save_to_file(str(sys.argv[1]), str(sys.argv[5]))
engine.runAndWait()