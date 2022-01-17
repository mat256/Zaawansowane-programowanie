
from detection import detection
from os import listdir

ph = listdir("./photos")
for a in ph:
    detection("./photos/" + a)
