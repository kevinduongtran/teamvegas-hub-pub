import time
from utils import *
from os import walk
import os

isPlaying = False

def tick():

	files = []
	for (dirpath, dirnames, filenames) in walk("./modules/speak/output"):
	    for file in filenames:
	    	files.append("./modules/speak/output/" + file)
	    break

	for file in files:
		if '.lock' not in file:
			print('playing ' + file)
			os.system('mpg321 ' + file)

			os.remove(file)


def watch():
	while True:
		time.sleep(0.5)
		tick()
		


		