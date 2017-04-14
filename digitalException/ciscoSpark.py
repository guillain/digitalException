# Target: app init 
# Version: 0.1
# Date: 2017/01/04
# Author: Guillain (guillain@gmail.com)
# Copyright 2017 GPL - Guillain

from flask import Flask, request, jsonify
from tools import exeReq, wEvent
from pyCiscoSpark import post_room, post_markdown, post_roommembership, post_webhook, get_message, del_room
import re, base64

# Conf and create app
app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('FLASK_SETTING')

# Spark room initialisation after button event
def sparkInit(roomname,roommsg):
    # Cisco Spark room creation
    try:
        room = post_room(app.config['SPARK_ACCESS_TOKEN'],roomname)
        wEvent('sparkInit',room['id'],"Room created",'1',room)
    except Exception as e:
        wEvent('sparkInit',roomname,"Issue during room creation",'0',e)
        return 'KO'

    # Cisco Spark room membership
    try:
        membership = post_roommembership(app.config['SPARK_ACCESS_TOKEN'],room['id'],app.config['APP_MAIL'],True)
        wEvent('sparkInit',room['id'],"Admin membership added",'1',membership)
    except Exception as e:
        wEvent('sparkInit',room['id'],"Issue during admin membership add",'0',e)
        return 'KO'
    try:
        membership = post_roommembership(app.config['SPARK_ACCESS_TOKEN'],room['id'],app.config['SPARK_ROOM_MAIL'],False)
        wEvent('sparkInit',room['id'],"Membership added",'1',membership)
    except Exception as e:
        wEvent('sparkInit',room['id'],"Issue during membership add",'0',e)
        return 'KO'

    # Cisco Spark room webhook on message
    try:
        webhook = post_webhook(app.config['SPARK_ACCESS_TOKEN'], roomname, app.config['SPARK_WEBHOOK']+'/message', 'messages', 'all', str('roomId='+room['id']))
        wEvent('sparkInit',room['id'],"Webhook added",'1',webhook)
    except Exception as e:
        status = 'KO'
        wEvent('sparkInit',room['id'],"Issue during webhook add",'0',e)

    # Cisco Spark room message post
    try:
        msg = post_markdown(app.config['SPARK_ACCESS_TOKEN'],room['id'],roommsg)
        wEvent('sparkInit',room['id'],"Message posted",'1',msg)
    except Exception as e:
        wEvent('sparkInit',room['id'],"Issue during post message",'0',e)
        return 'KO'

    return 'OK'

# Get Spark posted message, analysis it and if necessayr perform action
def sparkMsg(roomid,msgid):
    # Get message
    try:
        msg = get_message(app.config['SPARK_ACCESS_TOKEN'],msgid)
        msgtxt = msg.get('text').strip()
        wEvent('sparkMsg',roomid,msgtxt,'1',msg)
    except Exception as e:
        wEvent('sparkMsg',roomid,'Issue during get message data','0',e)
        return 'KO'

    
    # Search request
    if (re.search('^search',msgtxt)):
        return sparkSearch(roomid,msgtxt)

    # Close request
    if (re.search('^close$',msgtxt)):
        return sparkClose(roomid)

    # Escalation request
    if (re.search('^escalation$',msgtxt)) or (re.search('^escalade$',msgtxt)):
        return sparkEscalation(roomid)

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
        sql  = "SELECT id, msg FROM events "
        sql += "WHERE module = 'sparkMsg' AND msg LIKE '%" + msgtofind + "%' AND msg NOT LIKE 'search %'"
        msgs = exeReq(sql)
        wEvent('sparkSearch',roomid,msgtofind,'1',msgs)
    except Exception as e:
        wEvent('sparkSearch',roomid,msgtofind,'0',e)

    # Format and send the result
    for msg in msgs:
      roomlink = re.split('ciscospark://us/ROOM/', str(base64.b64decode(msg[0])))
      roomurl = 'https://web.ciscospark.com/#/rooms/' + str(roomlink[1])
      newmsg += '* [' + str(i) + '](' + roomurl + ') ' + msg[1] + '\n'
      i = i + 1
    try:
        room = post_markdown(app.config['SPARK_ACCESS_TOKEN'],roomid,newmsg)
        wEvent('sparkSearch',roomid,newmsg,'1', room)
    except Exception as e:
        wEvent('sparkSearch',roomid,"Issue during the post of the result message",'0',e)

    return 'OK'

# Cisco Spark room closure
def sparkClose(roomid):
    try:
        room = del_room(app.config['SPARK_ACCESS_TOKEN'],roomid)
        wEvent('sparkClose',roomid,"Room deleted",'1',room)
    except Exception as e:
        wEvent('sparkClose',roomid,"Issue during room delete",'0',e)
    return 'OK'

# Cisco Spark room escalation membership + message post
def sparkEscalation(roomid):
    try:
        membership = post_roommembership(app.config['SPARK_ACCESS_TOKEN'],roomid,app.config['SPARK_ROOM_MAIL_ESCALATION'],False)
        wEvent('sparkEscalation',roomid,"Escalation membership added",'1',membership)
    except Exception as e:
        wEvent('sparkEscalation',roomid,"Issue during escalation membership add",'0',e)

    try:
        msg = post_markdown(app.config['SPARK_ACCESS_TOKEN'],roomid,app.config['SPARK_MSG_ESCLATION'])
        wEvent('sparkEscalation',roomid,"Escalation message posted",'1',msg)
    except Exception as e:
        wEvent('sparkEscalation',roomid,"Issue during post escalation message",'0',e)
   
    return ''

