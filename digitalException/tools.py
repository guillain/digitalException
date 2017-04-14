# Target: tools for the app (connection, exeReq wEvent)
# Version: 0.1
# Date: 2017/01/18
# Author: Guillain (guillain@gmail.com)

from flask import Flask
import MySQLdb

app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('FLASK_SETTING')

# FUNCTIONs ---------------------------
# Log function for event, log, ...
def wEvent(module, id, msg, dmp):
    print str("module:"+module+", id:"+id+", msg:"+msg)

    if app.debug == True:
        print str(">>> DEBUG:"+str(dmp))

    return exeReq("INSERT INTO events (module, id, msg) VALUES ('"+module+"', '"+id+"', '"+msg+"');")

def connection():
    conn = MySQLdb.connect(
        host = app.config['MYSQL_HOST'],
        user = app.config['MYSQL_USER'],
        passwd = app.config['MYSQL_PASSWORD'],
        db = app.config['MYSQL_DB']
    )
    c = conn.cursor()
    return c, conn


def exeReq(req):
    error = None

    try:
        c, conn = connection()
    except Exception as e:
        print 'DB connection issue'
        return e

    try:
        c.execute(req)
        conn.commit()
    except Exception as e:
        print 'DB req execution issue'
        return e

    try:
        d = c.fetchall()
        c.close()
        return d
    except Exception as e:
        print 'DB fetch data issue'
        return e

