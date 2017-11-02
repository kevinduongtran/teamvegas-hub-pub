'''
    Automation Hub Main
'''


from utils import *
import datetime
import modules.taskmanager.tsk_main as taskManager
import modules.database.db_main as dbManager
import modules.speak.s_watch as speakManager
import modules.api.api_main as apiManager
import modules.house.house_ctrl as houseController
import modules.hooks.cox.c_main as coxManager
# from house_profile import *


def main():

    '''
        Initially checks for a house profile in database
        and creates if not found.

        starts task manger in parallel

        Note: use clear_collection() to clear collection
    '''

    print "[Main] Starting Home Automation Service"
    print "[Main] Time: " + str(datetime.datetime.now())

    notify('[Main] Hub Started')

    houseController.check_house_profile()

    runInParallel(
        apiManager.start,
        speakManager.watch,
        taskManager.start,
        dbManager.db_manager_start,
        coxManager.watch
        )

if __name__ == '__main__':
    main()

    
