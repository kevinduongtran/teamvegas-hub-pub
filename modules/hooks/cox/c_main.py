import requests
import requests.exceptions
import os
from utils import *
from config import app
import json
import time
import datetime as dt
import modules.database.db_main as dbManager


def get_devices():
	url = 'https://portal.coxhomelife.com/rest/'+  app['cox']['partnerid'] + '/sites/' + app['cox']['site'] + '/network/devices'

	headers= {
		'x-format':'json',
		'X-AppKey':'defaultKey',
		'x-login':'unlv2',
		'x-password':'demounlv'
	}

	r = requests.get(url, headers=headers)
	res = toJSON(r.text)
	for device in res['device']:
		test = dbManager.db_GetValue('house',{'address':config['address'],'status.devices.$.device_id':device['id']})
		if test is None:
			dbManager.db_Update('house',{'address':config['address']},{
				'$addToSet':{
						"status.devices": {
						'device_id':device['id'],
						'model':device['model'],
						'mfg':device['manufacturer']
						}
					}
				})
		else:
			dbManager.db_Update('house',{'address':config['address'],'status.devices.$.device_id':device['id']},{
				"$set": { 
					"status.devices.$.model": device['model'],
					"status.devices.$.mfg": device['manufacturer']
					} 
				})

		print device['id']


def watch():
	while True:
		time.sleep(0.5)
		tick()

def tick():
	get_devices()

def main():
	CoxInstance = CoxHomelife()
	print(CoxInstance.get())











if __name__ == '__main__':
	main()