# Target: app init 
# Version: 0.1
# Date: 2017/01/04
# Author: Guillain (guillain@gmail.com)
# Copyright 2017 GPL - Guillain

from flask import Flask, request, jsonify
from ciscoSpark import sparkInit, sparkMsg, sparkPostMsg

# Conf and create app
app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('FLASK_SETTING')

# Create Analytics connector if analytics feature is activated
if( app.config['ANALYTICS'] == 'True'):
  import logging, sys, logstash, datetime

  analytics = logging.getLogger('python-logstash-logger')
  analytics.setLevel(logging.INFO)
  analytics.addHandler(logstash.TCPLogstashHandler(app.config['ANALYTICS_HOST'], app.config['ANALYTICS_PORT'], version=app.config['ANALYTICS_VERSION']))

# HTTP Request -----------------------------------------------------------------------

# Web the button is triggered, that's the scenario/space initialization
@app.route('/bttn', methods=['POST'])
def bttn():
    # Get bt.tn data & set Cisco Spark room params
    bttn = request.get_json(silent=True)
    roomname = str(app.config['SPARK_ROOM_NAME'] + " " + bttn.get('name'))

    # Cisco Spark: room creation, add membership
    roomid = sparkInit(roomname) 

    # Initial Spark room message
    roommsg = "New " + roomname + " created \n"
    for k, v in bttn.items():
        roommsg += "* " + str(k) + " : " + str(v) + "\n"
    welcome = sparkPostMsg(roomid,roommsg)

    # Post remaning action
    remaining = sparkPostMsg(roomid,app.config['SPARK_MSG_REMAINING_A'])

    return ''

# When the space received a message
@app.route('/message', methods=['POST'])
def message():
    # Get Spark msg event (webhook)
    json = request.json
    data = json.get('data')

    # If Analytics feaure activated
    if( app.config['ANALYTICS'] == 'True'):
      print 'Analytics data push'
      extra = {
        'timestamp': str(datetime.datetime.utcnow()),
        'message': data.get('text'),
        'from': data.get('personEmail'),
        'spaceid': data.get('roomId'),
        'spacename': data.get('roomTitle'),
        'level': 'info',
        'type': 'bot'
      }
      #analytics.info(json, extra=extra)
      analytics.info(json, extra={'type': 'bot'})
      #data.get('text'), extra=extra)

    # Analyse the msg and perform action if necessary
    return sparkMsg(data.get('roomId'),data.get('id'))

# End of App --------------------------------------------------------------------------
if __name__ == '__main__':
    sess.init_app(app)

    app.debug = app.config['DEBUG']
    app.run()

