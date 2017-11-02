'''
    Helper functions for MongoDB client
'''
import sys
import subprocess
from pprint import pprint
from pymongo import MongoClient
from pymongo import errors
import json
from bson.objectid import ObjectId
import time

from utils import *
from config import *

_host = 'localhost'
_port = 27017


client = MongoClient(_host,_port,serverSelectionTimeoutMS=1, connect=False)
db = client[db_config['db_name']]

def db_ID():
    '''
        Generated a new BSON ID Object
    '''

    return ObjectId()

def db_toID(id):
    '''
        Convert to BSON ID Object
    '''
    return ObjectId(id)

def db_Clean(collection):
    '''
        Flushes data in collection
    '''

    if not db_isOnline:
        return False

    result = db[collection].delete_many({})

    return result

def db_GetValue(collection, *query):
    '''
        querys MongoDB find_one in collection,
        expects pymongo query
    '''

    if not db_isOnline:
        return False

    item = db[collection].find_one(*query)
    return item

def db_GetValueNestedByID(collection,ID,array):
    '''
        returns an object with an ID that 
        lives in an array nested in a document
    '''

    if not db_isOnline:
        return False

    res = db[collection].find_one({array+'._id':db_toID(ID)},{array+'.$.':1})[array][0]
    return res

def db_InsertOne(collection,obj):
    '''
        inserts a object as a document into a collection
    '''

    if not db_isOnline:
        return False

    response = db[collection].insert_one(obj)
    return response

def db_Update(collection,*arg):
    '''
        MongoDB update in a collection,
        expects pymongo arguments
    '''

    if not db_isOnline:
        return False

    response = db[collection].update(*arg)
    return response

def db_UpdateUpsert(collection,*arg):
    '''
        MongoDB update in a collection,
        expects pymongo arguments
    '''

    if not db_isOnline:
        return False

    response = db[collection].update(*arg,upsert=True)
    return response

def check():
    while True:
        time.sleep(3)
        if not db_isOnline():
            eprint('[DB Manager]')
        check

def db_isOnline():
    '''
        Check if DB is online
        will report to Slack if there are issues and retuen false
        else True
    '''
    try:
        client.server_info()
    except:
        return False
    else:
        return True

def db_manager_start():
    '''
        Intended to be initially called
    '''

    subprocess.call(["mongod"])
    
    print 'Starting MongoDB Manager'
    print '\tHost: ' + _host
    print '\tPort: ' + str(_port)
    print '\tOnline: ' + str(db_isOnline())

if __name__ == '__main__':
    db_manager_start()





