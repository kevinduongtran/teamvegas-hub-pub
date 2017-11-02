1. run sudo pip install -r requirements.txt
2. install MongoDB
    1. curl -o https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-3.0.13.tgz
    2. extract
    3. add export PATH=<mongodb-extracted-dir:$PATH to ~/.bashrc
    4. make folder /data/db
    5. sudo chmod g+w /data/db on that folder
3. run sudo python main.py to start server


API Endpoint IP
    192.168.1.15:81

Adding Task
    ENDPOINT/api/task
    Headers:
        Content-Type: application/json
        Authorization: 1234
    Body:
        {
            task:string,
            action:string
        }


Speak Task

    {
        "task":"speak",
        "action":"speak",
        "params": {
            "phrase":"This is a test of the emergancy alert system"
        },
        "address":"123 Fake St"
    }

Set Light Powerlevel Task

    {
        "task":"set_light_power",
        "action":"set_light_power",
        "params": {
            "device_ID":int,
            "power_level":int
        },
        "address":"123 Fake St"
    }




