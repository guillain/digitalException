# Target: app init 
# Version: 0.1
# Date: 2017/01/04
# Author: Guillain (guillain@gmail.com)
# Copyright 2017 GPL - Guillain

from flask import Flask, request, jsonify
from ciscoSpark import sparkInit, sparkMsg

# Conf and create app
app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('FLASK_SETTING')

# HTTP Request -----------------------------------------------------------------------
@app.route('/bttn', methods=['POST'])
def bttn():
    # Get bt.tn data & set Cisco Spark room params
    bttn = request.get_json(silent=True)

    roomname = str(app.config['SPARK_ROOM_NAME'] + " " + bttn.get('name'))

    # Prepare Cisco Spark room message
    roommsg = "New " + roomname + " created \n"
    for k, v in bttn.items():
        roommsg += "* " + str(k) + " : " + str(v) + "\n"
    roommsg += '\n_Tips_: \n' + app.config['SPARK_MSG_TIPS'] + '\n'
    roommsg += '\n**Remaing task**: \n' + app.config['SPARK_MSG_ASK'] + '\n'

    # Cisco Spark: room creation, add membership, post message
    return sparkInit(roomname,roommsg) 

@app.route('/message', methods=['POST'])
def message():
    # Get Spark msg event (webhook)
    json = request.json
    data = json.get('data')

    # Analyse the msg and perform action if necessary
    return sparkMsg(data.get('roomId'),data.get('id'))

# End of App --------------------------------------------------------------------------
if __name__ == '__main__':
    sess.init_app(app)

    app.debug = app.config['DEBUG']
    app.run()

