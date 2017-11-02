import boto3
import sys
from contextlib import closing
from boto3 import Session
import time
import os
from utils import *

def main():
	eprint('[Speak] Started')


def get_audio_from_string(string):
	eprint('[Speak] Downloading sound for "' + string + '"')
	session = Session(region_name="us-west-2")
	polly = session.client("polly")
	response = polly.synthesize_speech(
	    Text= string,
	    OutputFormat="mp3",
	    VoiceId="Brian")

	with closing(response["AudioStream"]) as stream:
	    ts = time.time()
	    print ts
	    if not os.path.isdir('./modules/speak/output'):
	        os.mkdir('./modules/speak/output')
	    	
	    target = './modules/speak/output/voice-' + str(ts) + '.mp3.lock'

	    with open(target, 'w') as f:
	        f.write(stream.read())
	        f.close()
	        os.rename(target, target.replace(".lock",""))
	eprint('[Speak] Success!')

if __name__ == '__main__':
	main()
    
