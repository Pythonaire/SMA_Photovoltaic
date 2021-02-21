# HAP-Python-Photovoltaic
push SMA-Inverter Values to the Homekit, readable by Eve App

Based on HAP-Python and SBFSpot.
Older style SMA inverters my have readable Bluetooth interfaces. See the github SFBSpot project <https://github.com/SBFspot/SBFspot>, how to connect to the inverter and how to store inverter values into a SQLite database.
Under "/usr/local/lib/python3.x/dist-packages/pyhap/resources/" you will find predefined Homekit services and characteristics for using in the HAP-Python module as preloaded_service.

## Installation

Create 3 Version 4 UUID's with "https://www.uuidgenerator.net" for one service and two characteristics. 

Extend services.json with:

```#!/usr/bin/env python3

"PhotoVoltaic": {
"OptionalCharacteristics":
["Name"],
"RequiredCharacteristics": [
"YieldDay",
"YieldYear"
],
"UUID": "your UUID"
 }
 and characteristics.json with:
 <br>
> "YieldDay": {
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
```
 
 Follow the HAP-Python installation steps by using Photovoltaic class.
 

