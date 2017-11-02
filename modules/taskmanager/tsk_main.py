'''
    Manages task listed in house DB
'''

import time

import modules.database.db_main as dbManager
import modules.house.house_ctrl as houseController

import modules.speak.s_main as Speech
import modules.hooks.lutron.l_main as Lutron


from utils import *

import requests
import ast
import json

def run_async(func):
    """
        run_async(func)
            function decorator, intended to make "func" run in a separate
            thread (asynchronously).
            Returns the created Thread object

            E.g.:
            @run_async
            def task1():
                do_something

            @run_async
            def task2():
                do_something_too

            t1 = task1()
            t2 = task2()
            ...
            t1.join()
            t2.join()
    """
    from threading import Thread
    from functools import wraps

    @wraps(func)
    def async_func(*args, **kwargs):
        func_hl = Thread(target=func, args=args, kwargs=kwargs)
        func_hl.start()
        return func_hl

    return async_func


def exec_task(task):
    '''
        "Executes task"
        Todo: make this async and do stuff
    '''

    if task['task_id'] == 'speak':
        if task['params']:
            data = ast.literal_eval(task['params'])
            j = json.dumps(data)
            j = json.loads(j)
            Speech.get_audio_from_string(j['phrase'])

    if task['task_id'] == 'set_light_power':
        if task['params']:
            data = ast.literal_eval(task['params'])
            j = json.dumps(data)
            j = json.loads(j)
            print j['power_level']
            device = Lutron.LutronDevice()
            device.set_power_level(j['device_ID'],j['power_level'])


    houseController.move_to_completed(task['_id'],'automation_todo')

def watch():
    '''
        Watch for tasks in automation_todo
    '''
    if dbManager.db_isOnline():
        task = houseController.get_first_todo()
        if task is not None: 
            exec_task(task)
    
            
    url = 'http://ec2-54-88-224-202.compute-1.amazonaws.com/api/task'
    headers = {
        'Content-Type':'application/json',
        'Authorization':'1234'
    }
    payload = { 
        "task":"",
        "action":"grab",
        "address":"123 Fake St"
    }
    '''
    r = requests.post(url, headers=headers,data=json.dumps(payload))
    print("tickloldsda--------")
    content = toJSON(r.text)
    if content:
        if content['status'] == 'success':
            if content['task']:
                add_todo(content['task']['task_id'])
    '''


def start():
    eprint('[Task Manager] Started')
    '''
        This should be called asyncronously 
        and will loop infinitly
    '''
    while True:
        # eprint('[Task Manager] Tick')
        time.sleep(0.5)
        watch()
