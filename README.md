# digitalException
Cisco Spark integration with SigFox button

## What is it?
* Bt.tn / Sigfox button as trigger
* Cisco Spark as Space for human and data
* Local DB for historical and data post processing treatment... analytics ready :)

When the Button is pushed Cisco Spark space is created and people are added.

If **escalation** word is enter an escalation process is launch and additionnal member is added.

## Based on
* [Flask](http://flask.pocoo.org/) (Python)
* [bt.tn](https://my.bt.tn) (can provide simulator or physical button)
* [Cisco Spark](https://web.ciscospark.com) (for free)

## Features
* Escalation: add new member when keyword 'escalation' or 'escalade' is enter
* Close: close spacer when keyword 'close' is enter
* Search: search in the room history the previous message and print the list with web url to click on and jump in the original space.
* Display: print welcome and tips messages (to configure in the [settings.py](settings.py) file)
* Tips: random tips for new message

## PreRequisites
Configuration is provided for Apache and WSGI server.
But you can also get only the python with another web server, container...
* Apache2: to provide HTTP server
* MySQL: to record locally event as connector availability...
* python (2.7): development language
* * Flask
* * MySQLdb

## Install

### Clone localy
```bash
git clone https://github.com/guillain/digitalException.git
cd digitalException
```

### Install the Python requirements
```bash
pip install -r requirements.txt
```

### Configure and set apache configuration
If you use one dedicated alias on your web server for this specific web app, follow the explanation below (virtual host creation with default config file).
Else put the WSGI content of the default file in your virtual host definiton

* For unsecure http (80)
```bash
cp conf/digitalException_apache.conf.default conf/digitalException_apache.conf
vi conf/digitalException_apache.conf 
ln -s /var/www/digitalException/conf/digitalException_apache.conf /etc/apache2/conf-enabled/digitalException_apache.conf
```

* For secure http (443)
```bash
cp conf/digitalException_apache-secure.conf.default conf/digitalException_apache_secure.conf
vi conf/digitalException_apache-secure.conf 
ln -s /var/www/digitalException/conf/digitalException_apache-secure.conf /etc/apache2/conf-enabled/digitalException_apache-secure.conf
```

### Configure the database
```bash
mysqladmin create digitalException -utoto -p
mysql digitalException -utoto -p < conf/mysql.sql
```

### Config your [bt.tn](https://my.bt.tn/home)
Configure your button (virtual or physical) with the following parameter:
* action: HTTP
* HTTP URL: your url
* HTTP Method: POST
* Arguments: application/json
```
{"ID":"<ID>","EID":"<EID>","DEVICEID":"<DEVICEID>","counter":"<COUNTER>","date":"<DATE>", "time": "<TIME>","name":"<NAME>","user":"<USER>","location":"<LOCATION>","emailaddress":"<EMAILADDRESS>"}
```

### Configure the Cisco Spark application
Remember to have or create an access token for Cisco Spark
* [Cisco Spark](http://developper.ciscospark.com) 
```bash
cp conf/settings.cfg.default conf/settings.cfg
vi conf/settings.cfg
```

### Run the application
Two configuration are availables

1/ For the dev, node is used
```bash
vi run (adapt at least the path)
./run manual
```
2/ For the prod, apache + SGI are used (install also this dependency)
Pickup the CLI accoring to your apache script
```bash
/etc/init.apache restart 
service http restart
...
```

### Test
* Push your button!!!
* Check in your Cisco Spark ;)
* Launch the escalation process by enter : escalation

### Troubleshooting
Start with the dev run mode and follow the traces in the screen.

This should be the good point to start... As for all troubleshooting... logs first ;)

If no specific issue appear you can follow the action plan hereafter.

Token access = TA
* No Spark space created: 
* * Are you sure about your Cisco Spark TA?
* * If you use this Cisco Spark TA with postman it works?

## Report bug
[issues](issues)


Have fun ;)
