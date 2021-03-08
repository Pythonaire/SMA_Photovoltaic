#!/usr/bin/env python3
from pyhap.accessory import Accessory
from pyhap.const import CATEGORY_SENSOR
import sqlite3 as sql
import logging

logging.basicConfig(level=logging.INFO, format="[%(module)s] %(message)s")

class PhotoVoltaic(Accessory):
    category = CATEGORY_SENSOR
    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs)
        self.displayName = args[1] # args[1] contained the device/class Name given
        self.dbFile = '/home/xxxx/smadata/SBFspot.db'
        self.thisDay = "SELECT max(round(TotalYield, 1)) - min(round(TotalYield,1)) AS power FROM DayData WHERE date(TimeStamp, 'unixepoch') = CURRENT_DATE"
        self.thisYear = "SELECT max(round(TotalYield, 1)) - min(round(TotalYield,1)) AS power FROM DayData WHERE datetime(TimeStamp, 'unixepoch') > date('now','start of year')"
        self.set_info_service(firmware_revision='0.0.1', manufacturer=None, model='MacServer SMAInverter', serial_number="MSSMA01")
        self.PhotoVoltaic = self.add_preload_service('PhotoVoltaic', chars = ['Name','YieldDay','YieldYear']) 
        self.YieldDay = self.PhotoVoltaic.configure_char('YieldDay', value = self.select_power(self.thisDay))
        self.YieldYear = self.PhotoVoltaic.configure_char('YieldYear', value = self.select_power(self.thisYear)/1000)
        

    def create_connection(self, dbFile):
        conn = None
        try:
            conn = sql.connect(dbFile)
        except Exception as e:
            logging.info('** Could not open {0} , err: {1}'.format(dbFile, e))
        return conn

    def select_power(self, command):
        conn = self.create_connection(self.dbFile)
        cur = conn.cursor()
        cur.execute(command)
        value = cur.fetchall() # return tuple
        logging.info('*** select value from {0} '.format(self.dbFile))
        cur.close()
        return value[0][0]

    @Accessory.run_at_interval(300) # SBFFspot update the values each 5 minutes
    def run(self):
        self.DayHarvest.set_value(self.select_power(self.thisDay))
        self.YearHarvest.set_value(self.select_power(self.thisYear)/1000)

    def stop(self):
        logging.info('Stopping accessory.')