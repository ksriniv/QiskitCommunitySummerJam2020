# Usage python3 Application.py <NumberofStrokes> <Loop>
import pyglet
from Q4C import *
import os
import sys
from time import sleep
sys.path.append("./Sounds")

def main():
    NumberofStrokes = 8
    if (len(sys.argv) > 1):
       NumberofStrokes = int(sys.argv[1])
    
    if (NumberofStrokes > 32):
        print(" Number of Too Strokes too long, Defaulting to 32")
        NumberofStrokes = 32

    if (NumberofStrokes <= 0):
        print(" Number of Too Strokes too short, Defaulting to 8")
        NumberofStrokes = 8
    
    Loop = 1
    
    if (len(sys.argv) > 2):
        Loop = int(sys.argv[2])
    
    if Loop < 1:
        Loop = 1
    ReturnList = Q4C(NumberofStrokes)
    
    print (" " + str(ReturnList))
    
    for i in range (Loop):
        print ("Playing Repetition -> " + str (i+1) + " for " + str(len(ReturnList)) + " strokes") 
        for sound in range(len(ReturnList)) :
            if ReturnList[sound] == ',':
                soundLocation = "Sounds/" + "Kaarvai.wav"
            else:
                soundLocation = "Sounds/" + str(ReturnList[sound]) + ".wav"
            music = pyglet.media.load(soundLocation)
            music.play()
            sleep(0.3)
if __name__ == '__main__':
    main()
