# digitalDelegation
Cisco Spark integration with SigFox button

## What is it?
* Bt.tn / Sigfox button as trigger
* Cisco Spark as Space for human and data
* => When the Button is pushed Cisco Spark space is created and people are added

## Based on
* [Flask](http://flask.pocoo.org/) (Python)
* [bt.tn](https://my.bt.tn) (can provide simulator or physical button)

## PreRequisites
Configuration is provided for Apache and WSGI server.
But you can also get only the python with another web server, container...
* Apache2
* MySQL
* python (2.7)
* * Flask
* * MySQLdb

## Install

### Clone localy
> git clone https://github.com/guillain/digitalDerogation.git
> cd digitalDerogation

### Configure and set apache configuration
* For unsecure http (80)

> cp conf/digitalDerogation_apache.conf.default conf/digitalDerogation_apache.conf
> vi conf/digitalDerogation_apache.conf 
> ln -s /var/www/digitalDerogation/conf/digitalDerogation_apache.conf /etc/apache2/conf-enabled/digitalDerogation_apache.conf

* For secure http (443)

> cp conf/digitalDerogation_apache-secure.conf.default conf/digitalDerogation_apache_secure.conf
> vi conf/digitalDerogation_apache-secure.conf 
> ln -s /var/www/digitalDerogation/conf/digitalDerogation_apache-secure.conf /etc/apache2/conf-enabled/digitalDerogation_apache-secure.conf

### Configure the database
> mysqladmin create digitalDerogation -utoto -p
> mysql digitalDerogation -utoto -p < conf/mysql.sql
> mysql digitalDerogation -utoto -p < conf/mysql_data.sql (add users can be useful...)

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
Remember to have or create an access toekn for Cisco Spark
* [Cisco Spark](http://developper.ciscospark.com) client ID and secret

> cp conf/settings.cfg.default conf/settings.cfg
> vi conf/settings.cfg

### Run the application
Two configuration availables

1/ For the dev, node is used

> vi run (adapt at least the path)
> ./run manual

2/ For the prod, apache + SGI are used (install also this dependency)
Pickup the CLI accoring to your apache script

> /etc/init.apache restart 
> service http restart
> ...

### Test
* Push your button!!!
* Check in your Cisco Spark ;)

### Troubleshooting
Start with the dev run mode and follow the traces in the screen.
This should be the good point to start... As for all troubleshooting... logs first ;)
If no specific issue appear you can follow the action plan hereafter.

Token access = TA

* No Spark space created: 
* * Are you sure about your Cisco Spark TA?
* * If you use this Cisco Spark TA with postman it works?


Have fun
