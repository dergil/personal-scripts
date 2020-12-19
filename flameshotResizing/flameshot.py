#!/usr/bin/env python3

import time
import pathlib
from os import walk
import os
import subprocess
import glob


def launchFlameshot():
    flameshot = "flameshot gui -p " + myDir
    # https://stackoverflow.com/questions/21936597/blocking-and-non-blocking-subprocess-calls
    process = subprocess.Popen(flameshot, shell=True)
    time.sleep(3)
    process.terminate()
    process.wait()


def resize():
    # compiling list of files in dir
    global files
    for (dirpath, dirnames, filenames) in walk(myDir):
        files.extend(filenames)
        break

    # alternative, simpler resizing:
    # resizeCommand = "mogrify -resize 70% " + mypath + files[0]

    # picture gets downsized, the -density and -quality settings cause the 140%
    resizeCommand = "convert " + myDir + files[0] + " -density 100 -quality 100 -resize 140% " + myDir + files[0]
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
launchFlameshot()
resize()
saveToClip()
removePNG()

