'''
	These functions pertains to execution of tasks
	for the
'''

import modules.database.db_main as dbManager
from config import config
from datetime import datetime
from utils import *

def check_house_profile():
	'''
		Add house profile if missing
	'''

	data = dbManager.db_GetValue('house',{'address':config['address']})
	if data is None:
		res = dbManager.db_InsertOne('house',config)

def check_house(address):
	'''
		Check if house exist
	'''

	data = dbManager.db_GetValue('house',{'address':config['address']})
	if data is None:
		return False
	else:
		return True

def clear_collection():
	'''
		Clears all task from todo, failed, and completed
	'''

	print "Clearing All Tasks"
	dbManager.db_Clean('house')

def get_first_todo():
	'''
		Get first task todo from automation_todo 
	'''

	res = dbManager.db_GetValue('house',{'address':config['address']},{'automation_todo':{ '$slice' : 1 }})['automation_todo']
	if len(res) > 0:
		return res[0]
	else:
		return None

def add_todo(task,params={}):
	'''
		Add a todo to automation_todo
	'''

	todo = {
		'ts': datetime.now(),
		'task_id': task,
		'_id': dbManager.db_ID(),
        'params': params
	}
	res = dbManager.db_Update('house',{"address": config['address']},
			{ "$push": 
				{ 'automation_todo' : 
					todo
				}
			})
	return res

def move_to_completed(ID,source):
	'''
		Moves a task from source to completed by ID
	'''

	task = dbManager.db_GetValueNestedByID('house',ID, source)
	eprint('[Task Manager] Executed Task')
	pprint(task)
	eprint('\n')
	res = dbManager.db_Update('house',{"address": config['address']},
		{ "$push": 
			{ 'automation_todo_completed' : 
				task
			}
		})
	pull = dbManager.db_Update('house',{'address':config['address']},{'$pull' : {source : {"_id":dbManager.db_toID(ID)}}})


def move_to_failed(task,source):
	'''
		Moves a task from source to failed by ID
	'''

	task = dbManager.db_GetValueNestedByID('house',ID, source)
	res = dbManager.db_Update('house',{"address": config['address']},
		{ "$push": 
			{ 'automation_todo_failed' : 
				task
			}
		})
	pull = dbManager.db_Update('house',{'address':config['address']},{'$pull' : {source : {"_id":dbManager.db_toID(ID)}}})

