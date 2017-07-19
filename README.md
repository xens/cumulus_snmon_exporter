#### Intro

Parses the output of smontctl into Prometheus test-file format

```console
  cumulus:~$ python smon_exporter.py
  # HELP smon_fan1 Fan Tray 1
  # TYPE smon_fan1 gauge
  smon_fan1 1
  # HELP smon_fan2 Fan Tray 2
  # TYPE smon_fan2 gauge
  smon_fan2 1
  # HELP smon_fan3 Fan Tray 3
  # TYPE smon_fan3 gauge
  smon_fan3 1
  # HELP smon_fan4 Fan Tray 4
  # TYPE smon_fan4 gauge
  smon_fan4 1
  # HELP smon_fan5 Fan Tray 5
  # TYPE smon_fan5 gauge
  smon_fan5 1
  # HELP smon_fan6 Fan Tray 1
  # TYPE smon_fan6 gauge
  smon_fan6 1
  # HELP smon_fan7 Fan Tray 2
  # TYPE smon_fan7 gauge
  smon_fan7 1
  # HELP smon_fan8 Fan Tray 3
  # TYPE smon_fan8 gauge
  smon_fan8 1
  # HELP smon_fan9 Fan Tray 4
  # TYPE smon_fan9 gauge
  smon_fan9 1
  # HELP smon_fan10 Fan Tray 5
  # TYPE smon_fan10 gauge
  smon_fan10 1
  # HELP smon_psu1 PSU1
  # TYPE smon_psu1 gauge
  smon_psu1 1
  # HELP smon_psu2 PSU2
  # TYPE smon_psu2 gauge
  smon_psu2 1
  # HELP smon_psu1fan1 PSU1 Fan
  # TYPE smon_psu1fan1 gauge
  smon_psu1fan1 1
  # HELP smon_psu1temp1 PSU1 Inlet Temp Sensor
  # TYPE smon_psu1temp1 gauge
  smon_psu1temp1 1
  # HELP smon_psu1temp2 PSU1 Max Temp Sensor
  # TYPE smon_psu1temp2 gauge
  smon_psu1temp2 1
  # HELP smon_psu2fan1 PSU2 Fan
  # TYPE smon_psu2fan1 gauge
  smon_psu2fan1 1
  # HELP smon_psu2temp1 PSU2 Inlet Temp Sensor
  # TYPE smon_psu2temp1 gauge
  smon_psu2temp1 1
  # HELP smon_psu2temp2 PSU2 Max Temp Sensor
  # TYPE smon_psu2temp2 gauge
  smon_psu2temp2 1
  # HELP smon_temp1 Rear Outlet Air sensor
  # TYPE smon_temp1 gauge
  smon_temp1 1
  # HELP smon_temp2 Front Outlet Air sensor
  # TYPE smon_temp2 gauge
  smon_temp2 1
  # HELP smon_temp3 Temp Sensor close to Networking ASIC
  # TYPE smon_temp3 gauge
  smon_temp3 1
  # HELP smon_temp4 Intel CPU die sensor
  # TYPE smon_temp4 gauge
  smon_temp4 1
  # HELP smon_temp5 Intel CPU die sensor
  # TYPE smon_temp5 gauge
  smon_temp5 1
  # HELP smon_temp6 Intel CPU die sensor
  # TYPE smon_temp6 gauge
  smon_temp6 1
  # HELP smon_temp7 Intel CPU die sensor
  # TYPE smon_temp7 gauge
  smon_temp7 1
```

#### Usage

`$ smonctl_parser.py`
