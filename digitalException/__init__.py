# Target: app init 
# Version: 0.1
# Date: 2017/01/04
# Author: Guillain (guillain@gmail.com)
# Copyright 2017 GPL - Guillain

from flask import Flask, request, jsonify, render_template
from ciscoSpark import sparkInit, sparkMsg, sparkPostMsg, sparkWebhook

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

# Initiate global room monitoring
webhook = sparkWebhook('all')

# HTTP Request -----------------------------------------------------------------------
@app.route('/', methods=['GET'])
def root():
    print "hello, request is coming!"
    return render_template('index.html')

# Web the button is triggered, that's the scenario/space initialization
@app.route('/bttn', methods=['POST'])
def bttn():
    # Get bt.tn data & set Cisco Spark room params
    bttn = request.get_json(silent=True)
    try:
        button_name = bttn.get('name')
    except Exception as e:
        button_name = ''
    roomname = str(app.config['SPARK_ROOM_NAME'] + " " + button_name)

    # Cisco Spark: room creation, add membership
    roomid = sparkInit(roomname) 

    # Send initial Spark room message
    roommsg = "New " + roomname + " created \n"
    if button_name != '':
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
      analytics.info(json, extra={'type': 'bot'})

    # Analyse the msg and perform action if necessary
    return sparkMsg(data.get('roomId'), data.get('id'))

# End of App --------------------------------------------------------------------------
if __name__ == '__main__':
    sess.init_app(app)

    app.debug = app.config['DEBUG']
    app.run()

