from flask import Flask, request
from flask_restful import Resource, Api, reqparse
import os
from utils import *


import modules.house.house_ctrl as houseController


app = Flask(__name__)
api = Api(app)



def token(token_str):
    if token_str == '1234':
        return str(token_str)
    else:
        raise ValueError(token_str + ' is not a valid token')

task_parser = reqparse.RequestParser()
task_parser.add_argument('task', location='json', required=True)
task_parser.add_argument('params', location='json')
task_parser.add_argument('Authorization', type=token, location='headers', required=True)


class TaskAPI(Resource):
    def get(self):
        return {'hello': 'world'}
    def post(self):
        args = task_parser.parse_args()
        houseController.add_todo(args['task'],args['params'])
        return {
            'status':'success',
            'task':args['task'],
            'params':args['params']
        }

api.add_resource(TaskAPI, '/api/task')

def start():
    eprint('[API Endpoint] Started')
    os.system("kill -9 $(lsof -t -i:81)")
    app.run(host='0.0.0.0', port=81)
