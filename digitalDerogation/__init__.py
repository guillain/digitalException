# Target: app init 
# Version: 0.1
# Date: 2017/01/04
# Author: Guillain (guillain@gmail.com)
# Copyright 2017 GPL - Guillain

from flask import Flask, request, jsonify
from tools import exeReq, wEvent
from pyCiscoSpark import post_room, post_message, post_roommembership

# Conf and create app
app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('FLASK_SETTING')

# HTTP Request -----------------------------------------------------------------------
@app.route('/bttn', methods=['POST'])
def my_form():
    status = 'OK'

    # Get bt.tn data & set Cisco Spark room params
    bttn = request.get_json(silent=True)
    roomname = str(app.config['SPARK_ROOM_NAME'] + " " + bttn.get('name'))
    roommsg = "New " + roomname + " created \n"
    for k, v in bttn.items():
        roommsg += "* " + str(k) + " : " + str(v) + "\n"
    wEvent('bttn',roomname,"Button s data get",bttn)

    # Cisco Spark room creation
    try:
        room = post_room(app.config['SPARK_ACCESS_TOKEN'],roomname)
        wEvent('bttn',roomname,"Room created",room)
    except Exception as e:
        status = 'KO'
        wEvent('bttn',roomname,"Issue during room creation",e)

    # Cisco Spark room membership
    try:
        membership = post_roommembership(app.config['SPARK_ACCESS_TOKEN'],room['id'],app.config['SPARK_ROOM_MAIL'],False)
        wEvent('bttn',roomname,"Membership added",membership)
    except Exception as e:
        status = 'KO'
        wEvent('bttn',roomname,"Issue during membership add",e)

    # Cisco Spark room message post
    try:
        msg = post_message(app.config['SPARK_ACCESS_TOKEN'],room['id'],roommsg)
        wEvent('bttn',roomname,"Message posted",msg)
    except Exception as e:
        status = 'KO'
        wEvent('bttn',roomname,"Issue during post message",e)

    return status

# End of App --------------------------------------------------------------------------
if __name__ == '__main__':
    sess.init_app(app)

    app.debug = True
    app.run()

