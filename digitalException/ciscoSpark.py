# Target: app init 
# Version: 0.1
# Date: 2017/01/04
# Author: Guillain (guillain@gmail.com)
# Copyright 2017 GPL - Guillain

from flask import Flask, request, jsonify
from tools import exeReq, wEvent
from pyCiscoSpark import post_room, post_markdown, post_roommembership, post_webhook, get_message, del_room

# Conf and create app
app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('FLASK_SETTING')

def sparkInit(roomname,roommsg):
    # Cisco Spark room creation
    try:
        room = post_room(app.config['SPARK_ACCESS_TOKEN'],roomname)
        wEvent('sparkInit',room['id'],"Room created",room)
    except Exception as e:
        wEvent('sparkInit',roomname,"Issue during room creation",e)
        return 'KO'

    # Cisco Spark room membership
    try:
        membership = post_roommembership(app.config['SPARK_ACCESS_TOKEN'],room['id'],app.config['APP_MAIL'],True)
        wEvent('sparkInit',room['id'],"Admin membership added",membership)
    except Exception as e:
        wEvent('sparkInit',room['id'],"Issue during admin membership add",e)
        return 'KO'
    try:
        membership = post_roommembership(app.config['SPARK_ACCESS_TOKEN'],room['id'],app.config['SPARK_ROOM_MAIL'],False)
        wEvent('sparkInit',room['id'],"Membership added",membership)
    except Exception as e:
        wEvent('sparkInit',room['id'],"Issue during membership add",e)
        return 'KO'

    # Cisco Spark room webhook on message
    try:
        webhook = post_webhook(app.config['SPARK_ACCESS_TOKEN'], roomname, app.config['SPARK_WEBHOOK']+'/message', 'messages', 'all', str('roomId='+room['id']))
        wEvent('sparkInit',room['id'],"Webhook added",webhook)
    except Exception as e:
        status = 'KO'
        wEvent('sparkInit',room['id'],"Issue during webhook add",e)

    # Cisco Spark room message post
    try:
        msg = post_markdown(app.config['SPARK_ACCESS_TOKEN'],room['id'],roommsg)
        wEvent('sparkInit',room['id'],"Message posted",msg)
    except Exception as e:
        wEvent('sparkInit',room['id'],"Issue during post message",e)
        return 'KO'

    return 'OK'

def sparkMsg(roomid,msgid):
    # Get message
    try:
        msg = get_message(app.config['SPARK_ACCESS_TOKEN'],msgid)
        wEvent('sparkMsg',roomid,'Message s data get',msg)
    except Exception as e:
        wEvent('sparkMsg',roomid,'Issue during get message data',e)
        return 'KO'

    # Action according to the msg
    msgtxt = msg.get('text')
    msgmd = msg.get('markdown')

    # Escalation request
    if (msgtxt == 'escalation') or (msgmd == 'escalation'):
        return sparkEscalation(roomid)

    # Close request
    if (msgtxt == 'close') or (msgmd == 'close'):
        return sparkClose(roomid)

    return 'OK'

def sparkClose(roomid):
    # Cisco Spark room closure
    try:
        room = del_room(app.config['SPARK_ACCESS_TOKEN'],roomid)
        wEvent('sparkClose',roomid,"Room deleted",room)
    except Exception as e:
        wEvent('sparkClose',roomid,"Issue during room delete",e)
    return 'OK'

def sparkEscalation(roomid):
    # Cisco Spark room escalation membership
    try:
        membership = post_roommembership(app.config['SPARK_ACCESS_TOKEN'],roomid,app.config['SPARK_ROOM_MAIL_ESCALATION'],False)
        wEvent('sparkEscalation',roomid,"Escalation membership added",membership)
    except Exception as e:
        wEvent('sparkEscalation',roomid,"Issue during escalation membership add",e)

    # Cisco Spark room escalation message post
    try:
        msg = post_markdown(app.config['SPARK_ACCESS_TOKEN'],roomid,app.config['SPARK_MSG_ESCLATION'])
        wEvent('sparkEscalation',roomid,"Escalation message posted",msg)
    except Exception as e:
        wEvent('sparkEscalation',roomid,"Issue during post escalation message",e)
   
    return ''

