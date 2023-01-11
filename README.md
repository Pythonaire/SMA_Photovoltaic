# SMA-Photovoltaic  
push SMA-Inverter Values to the Homekit, readable by Eve App

Based on HAP-Python and SBFSpot.
Older style SMA inverters my have readable Bluetooth interfaces. See the github SFBSpot project <https://github.com/SBFspot/SBFspot>, how to connect to the inverter and how to store inverter values into a SQLite database.
Under "/usr/local/lib/python3.x/dist-packages/pyhap/resources/" you will find predefined Homekit services and characteristics for using in the HAP-Python module as preloaded_service.

## SBFSpot Installation

```#!bash
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install make g++ libmariadb-dev-compat libmariadb-dev
sudo apt-get install libboost-date-time-dev libboost-system-dev libboost-filesystem-dev
sudo apt-get install libboost-regex-dev libboost-all-dev
sudo apt-get sqlite3
sudo apt-get install libsqlite3-dev
sudo apt-get --no-install-recommends install bluetooth libbluetooth-dev libbluetooth3
cd /home/YOUR_DATABASE_PATH
mkdir smadata
mkdir SBFspot
sudo mkdir /var/log/sbfspot.3
sudo chown -R YOUR_USER:YOUR_USER /var/log/sbfspot.3
wget -c https://github.com/SBFspot/SBFspot/archive/V3.7.0.tar.gz
tar -xvf V3.7.0.tar.gz -C SBFspot --strip-components 1
cd ~/SBFspot/SBFspot
make sqlite
sudo make install_sqlite
cd /home/pi/smadata
sqlite3 SBFspot.db < /home/YOUR_USER/SBFspot/SBFspot/CreateSQLiteDB.sql
hcitool scan 
cd /usr/local/bin/sbfspot.3
sudo cp SBFspot.default.cfg SBFspot.cfg
```

Modify Minimum Config for your setup:

sudo nano SBFspot.cfg

BTAddress=XX:XX:XX:XX:XX:XX --> the Bluetooth Address of your Inverter
OutputPath=/home/YOUR_USER/smadata/%Y
OutputPathEvents=/home/YOUR_USER/smadata/%Y/Events
Timezone ...
Locale ....
SQL_Database=/home/YOUR_USER/smadata/SBFspot.db

if your want to have additional CSV-Files 
CSV_Export=1

Where are a lot of other configs. See <https://github.com/SBFspot/SBFspot>

Test the database connection:

```#!bash
/usr/local/bin/sbfspot.3/SBFspot -v -finq -nocsv
```

## Automation

```#!bash
cd /usr/local/bin/sbfspot.3
sudo nano daydata
```

insert:  
log=/var/log/sbfspot.3/MyPlant_$(date '+%Y%m%d').log  
/usr/local/bin/sbfspot.3/SBFspot -v -ad1 -am0 -ae0  -nocsv >>$log

```#!bash
sudo chmod +x daydata
sudo nano monthdata
```

insert:  
log=/var/log/sbfspot.3/MyPlant_$(date '+%Y%m').log  
/usr/local/bin/sbfspot.3/SBFspot -v -sp0 -ad0 -am1 -ae1 -finq  -nocsv >>$log

```#!bash
sudo chmod +x daydata
sudo chmod +x monthdata
crontab -e
```

insert:  
*/5 6-22 * * * /usr/local/bin/sbfspot.3/daydata  
55 05 * * * /usr/local/bin/sbfspot.3/monthdata

```#!bash
sudo systemctl enable cron
sudo systemctl daemon-reload
```

## PHPLiteAdmin

Your can use PHPLiteAdmin for additionally Web View by installing 

```#!bash
sudo apt-get install -y phpliteadmin
```

## HAP-Python plugin

Because of iOS App changes, just the definition of standard Outlet in conjunction with eve based characteritics "TotalConsumption" and "CurrentConsumption" work.
 
