#!/usr/bin/env python3

import time
import pathlib
import os
import subprocess
import glob


# takes screenshot with flameshot
# resizes screenshot, puts it on clipboard
# dedicated directory needed

# save screenshot with Ctrl+S

def launchFlameshot():
    flameshot = "flameshot gui -p " + myDir
    subprocess.Popen(flameshot, shell=True)
    while isDirEmpty(myDir):
        time.sleep(0.1)


def isDirEmpty(path):
    return len(os.listdir(path)) == 0


def resize():
    global files
    files = os.listdir(myDir)

    # alternative, simpler resizing:
    # resizeCommand = "mogrify -resize 70% " + myDir + files[0]

    # picture gets downsized, the -density and -quality settings cause the 140%
    resizeCommand = "convert " + myDir + files[0] + " -density 100 -quality 100 -resize 120% " + myDir + files[0]
    subprocess.call(resizeCommand, shell=True)


def saveToClip():
    saveToClipCommand = "xclip -selection clipboard -t image/png -i " + myDir + files[0]
    subprocess.call(saveToClipCommand, shell=True)


def removePNG():
    globInput = home + '/Pictures/clipboard/*.png'
    filesToDelete = glob.glob(globInput)
    if len(os.listdir(myDir)) > 0:
        for f in filesToDelete:
            try:
                os.remove(f)
            except OSError as e:
                print("Error: %s : %s" % (f, e.strerror))


home = str(pathlib.Path.home())
myDir = home + "/Pictures/clipboard/"
files = []
removePNG()
launchFlameshot()
resize()
saveToClip()
removePNG()

