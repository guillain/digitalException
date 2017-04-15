# Target: app init 
# Version: 0.1
# Date: 2017/01/04
# Author: Guillain (guillain@gmail.com)
# Copyright 2017 GPL - Guillain

from flask import Flask, request, jsonify
from tools import exeReq, wEvent
from pyCiscoSpark import post_room, post_markdown, post_roommembership, post_webhook, get_message, del_room
import re, base64, random

# Conf and create app
app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('FLASK_SETTING')

# Spark room initialisation after button event
def sparkInit(roomname):
    # Cisco Spark room creation
    try:
        room = post_room(app.config['SPARK_ACCESS_TOKEN'],roomname)
        wEvent('sparkInit',room['id'],"Room created",'app','1',room)
    except Exception as e:
        wEvent('sparkInit',roomname,"Issue during room creation",'app','0',e)
        return 'KO'

    # Cisco Spark room membership
    try:
        membership = post_roommembership(app.config['SPARK_ACCESS_TOKEN'],room['id'],app.config['APP_MAIL'],True)
        wEvent('sparkInit',room['id'],"Admin membership added",'app','1',membership)
    except Exception as e:
        wEvent('sparkInit',room['id'],"Issue during admin membership add",'app','0',e)
        return 'KO'
    try:
        membership = post_roommembership(app.config['SPARK_ACCESS_TOKEN'],room['id'],app.config['SPARK_ROOM_MAIL'],False)
        wEvent('sparkInit',room['id'],"Membership added",'app','1',membership)
    except Exception as e:
        wEvent('sparkInit',room['id'],"Issue during membership add",'app','0',e)
        return 'KO'

    # Cisco Spark room webhook on message
    try:
        webhook = post_webhook(app.config['SPARK_ACCESS_TOKEN'], roomname, app.config['SPARK_WEBHOOK']+'/message', 'messages', 'all', str('roomId='+room['id']))
        wEvent('sparkInit',room['id'],"Webhook added",'app','1',webhook)
    except Exception as e:
        status = 'KO'
        wEvent('sparkInit',room['id'],"Issue during webhook add",'app','0',e)

    return room['id']

# Post a message in the Spark space
def sparkPostMsg(roomid,msg):
    try:
        msg = post_markdown(app.config['SPARK_ACCESS_TOKEN'],roomid,msg)
        wEvent('sparkPostMsg',roomid,"Message posted",'app','1',msg)
    except Exception as e:
        wEvent('sparkPostMsg',roomid,"Issue during post message",'app','0',e)
        return 'KO'
    return 'OK'


# Get Spark posted message, analysis it and if necessayr perform action
def sparkMsg(roomid,msgid):
    # Get message
    try:
        msg = get_message(app.config['SPARK_ACCESS_TOKEN'],msgid)
        msgtxt = msg.get('text').strip()
    except Exception as e:
        wEvent('sparkMsg',roomid,'Issue during get message data','app','0',e)
        return 'KO'

    # Search request
    if (re.search('^search',msgtxt)):
        return sparkSearch(roomid,msgtxt)

    # Close request
    elif (re.search('^close$',msgtxt)):
        return sparkClose(roomid)

    # Escalation request
    elif (re.search('^escalation$',msgtxt)) or (re.search('^escalade$',msgtxt)):
        return sparkEscalation(roomid)

    # Tips message
    elif ( not re.search('Tips',msgtxt) ):
        return sparkPostMsg(roomid, '_Tips_ : ' + random.choice( app.config['SPARK_MSG_TIPS'] ))

    # Record the message
    else:
        wEvent('sparkMsg',roomid,msgtxt,msg.get('personEmail'),'1',msg)

    return 'OK'

# Cisco Spark search text in room
def sparkSearch(roomid,text):
    i = 0
    newmsg = app.config['SPARK_MSG_SEARCH'] + '\n'

    # Remove search word
    p = re.compile('^search ')
    msgtofind = p.sub('',text)

    # Search in the event table (history) the text msg
    try:
        msgs = exeReq("SELECT id, msg FROM events WHERE msg LIKE '%" + msgtofind + "%' AND owner != 'app'")
        wEvent('sparkSearch',roomid,msgtofind,'app','1',msgs)
    except Exception as e:
        wEvent('sparkSearch',roomid,msgtofind,'app','0',e)

    # Format and send the result
    for msg in msgs:
      roomlink = re.split('ciscospark://us/ROOM/', str(base64.b64decode(msg[0])))
      roomurl = 'https://web.ciscospark.com/#/rooms/' + str(roomlink[1])
      newmsg += '* [' + str(i) + '](' + roomurl + ') ' + msg[1] + '\n'
      i = i + 1
    try:
        room = post_markdown(app.config['SPARK_ACCESS_TOKEN'],roomid,newmsg)
        wEvent('sparkSearch',roomid,newmsg,'app','1',room)
    except Exception as e:
        wEvent('sparkSearch',roomid,"Issue during the post of the result message",'app','0',e)

    return 'OK'

# Cisco Spark room closure
def sparkClose(roomid):
    try:
        room = del_room(app.config['SPARK_ACCESS_TOKEN'],roomid)
        wEvent('sparkClose',roomid,"Room deleted",'app','1',room)
    except Exception as e:
        wEvent('sparkClose',roomid,"Issue during room delete",'app','0',e)
    return 'OK'

# Cisco Spark room escalation membership + message post
def sparkEscalation(roomid):
    try:
        membership = post_roommembership(app.config['SPARK_ACCESS_TOKEN'],roomid,app.config['SPARK_ROOM_MAIL_ESCALATION'],False)
        wEvent('sparkEscalation',roomid,"Escalation membership added",'app','1',membership)
    except Exception as e:
        wEvent('sparkEscalation',roomid,"Issue during escalation membership add",'app','0',e)

    try:
        msg = post_markdown(app.config['SPARK_ACCESS_TOKEN'],roomid,app.config['SPARK_MSG_ESCLATION'])
        wEvent('sparkEscalation',roomid,"Escalation message posted",'app','1',msg)
    except Exception as e:
        wEvent('sparkEscalation',roomid,"Issue during post escalation message",'app','0',e)
   
    return ''

