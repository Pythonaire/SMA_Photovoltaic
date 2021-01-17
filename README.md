# HAP-Python-Photovoltaic
push SMA-Inverter Values to the Homekit, readable by Eve App

Based on HAP-Python and SBFSpot.
The older style SMA inverter has a readable Bluetooth interface. See the github SFBSpot project, how to connect to the inverter and how to store inverter values into a SQLite database.
Under "/usr/local/lib/python3.x/dist-packages/pyhap/resources/" aou will find predefined Homkit services and characteristics.
Create 3 Version 4 UUID's with "https://www.uuidgenerator.net" for one service and two characteristics.  
Extend services.json with:

"PhotoVoltaic": {<br>
    "OptionalCharacteristics": [
     "Name" 
    ],
   "RequiredCharacteristics": [
   "YieldDay",
   "YieldYear"
   ],
   "UUID": "your UUID"
 }
 and characteristics.json with:
 
 
 
 "YieldDay": {
      "Format": "float",
      "Permissions": [
         "pr",
         "ev"
      ],
      "UUID": "your UUID",
      "unit": "Wh",
          "maxValue": 100000,
          "minValue": 0,
          "minStep": 1
   },
   "YieldYear": {
      "Format": "float",
      "Permissions": [
         "pr",
         "ev"
      ],
      "UUID": "your UUID",
      "unit": "kWh",
      "maxValue": 100000000000,
      "minValue": 0,
      "minStep": 0.001
   }
 
 Follow the HAP-Python installation steps by using Photovoltaic.py.
 

