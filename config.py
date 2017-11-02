from datetime import datetime

"""
	Configuration for house profile
"""
app = {
    'dev':True,
    'lutron':{
    		'ip':'192.168.1.254'
    },
    'cox': {
    	'partnerid':'PARTNER ID HERE',
    	'site':'SITE ID HERE'
    }
}
config = {
	'address': '123 Fake St',
	'name': 'Test House',
	'status': {
		'mode':'eco',
		'devices':[]
	},
	'ts_added': datetime.now(),
	'automation_todo':[],
	'automation_todo_failed':[],
	'automation_todo_completed':[]
}

db_config = {
	'db_name':'automation_database'
}

sched_config = {
	'day_length_s': 1
}
