'''
    Utilitys Library
'''

import slackweb
import sys
import os
import urllib2
from config import *
from datetime import datetime
from multiprocessing import Process
import json
from bson import json_util, ObjectId
import time


def eprint(string):
    if app['dev']:
        print string


def pprint(obj):
    '''
        print out pretty jsons
    '''

    print json.dumps(json.loads(json_util.dumps(obj)), sort_keys=True,
                        indent=4, separators=(',', ': '))


def toJSON(obj):
    return json.loads(obj)

proc = []
def runInParallel(*fns):
    '''
        Runs a list of functions in parallel
    '''

    for fn in fns:
        p = Process(target=fn)
        p.start()
        proc.append(p)
    for p in proc:
        p.join()




def notify(msg):
    '''
        A notification type message for slack
    '''

    finalMsg =  str("------------ NOTIFY ------------\n" +
        "Time: " + str(datetime.now().strftime("%A, %Y-%m-%d %H:%M:%S")) + "\n" +
        "Message: " + str(msg) + "\n")
    try:
        msg_slack(finalMsg)
    except urllib2.URLError as err:
        print(err)
        pass


def reportError(errorInfo,msg='none'):
    '''
        An error type message for slack
    '''
    
    exc_type, exc_obj, exc_tb = errorInfo
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]

    finalMsg =  str("------------ ERROR ------------\n" +
                "Time: " + str(datetime.now().strftime("%A, %Y-%m-%d %H:%M:%S")) + "\n" +
                "Error from file: " + str(fname) + "\n" +
                "Line: " + str(exc_tb.tb_lineno) + "\n" +
                "Exception Type: " + str(exc_type) + "\n" +
                "Message: " + str(msg) + "\n")

    print finalMsg
    try:
        msg_slack(finalMsg)
    except urllib2.URLError as err:
        pass

def msg_slack(msg):
    slack.notify(text=str(msg), channel="#automation-alerts", username="Auto-Bot")


slack = slackweb.Slack(url="SLACK URL API HERE")


def json_load_byteified(file_handle):
    return _byteify(
        json.load(file_handle, object_hook=_byteify),
        ignore_dicts=True
    )

def json_loads_byteified(json_text):
    return _byteify(
        json.loads(json_text, object_hook=_byteify),
        ignore_dicts=True
    )

def _byteify(data, ignore_dicts = False):
    # if this is a unicode string, return its string representation
    if isinstance(data, unicode):
        return data.encode('utf-8')
    # if this is a list of values, return list of byteified values
    if isinstance(data, list):
        return [ _byteify(item, ignore_dicts=True) for item in data ]
    # if this is a dictionary, return dictionary of byteified keys and values
    # but only if we haven't already byteified it
    if isinstance(data, dict) and not ignore_dicts:
        return {
            _byteify(key, ignore_dicts=True): _byteify(value, ignore_dicts=True)
            for key, value in data.iteritems()
        }
    # if it's anything else, return it in its original form
    return data

def byteify(input):
    if isinstance(input, dict):
        return {byteify(key): byteify(value)
                for key, value in input.iteritems()}
    elif isinstance(input, list):
        return [byteify(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input