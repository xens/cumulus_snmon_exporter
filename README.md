## Intro

Tool to parse the output of smontctl (cumuluslinux hardware probing tool)
into Prometheus text-file format.

The following states are translated this way into integers:

* OK = 1
* ABSENT = -1
* BAD = 0


```console
  cumulus:~$ python smonctl_parser.py
  # HELP smon_fan (-1=ABSENT, 0=BAD, 1=OK)
  # TYPE smon_fan gauge
  smon_fan{name="fan1",description="Fan Tray 1"} 1
  smon_fan{name="fan2",description="Fan Tray 2"} 1
  smon_fan{name="fan3",description="Fan Tray 3"} 1
  smon_fan{name="fan4",description="Fan Tray 4"} 1
  smon_fan{name="fan5",description="Fan Tray 5"} 1
  smon_fan{name="fan6",description="Fan Tray 1"} 1
  smon_fan{name="fan7",description="Fan Tray 2"} 1
  smon_fan{name="fan8",description="Fan Tray 3"} 1
  smon_fan{name="fan9",description="Fan Tray 4"} 1
  smon_fan{name="fan10",description="Fan Tray 5"} 1
  smon_fan{name="psu1fan1",description="PSU1 Fan"} 1
  smon_fan{name="psu2fan1",description="PSU2 Fan"} 1

  # HELP smon_temp (-1=ABSENT, 0=BAD, 1=OK)
  # TYPE smon_temp gauge
  smon_temp{name="psu1temp1",description="PSU1 Inlet Temp Sensor"} 1
  smon_temp{name="psu1temp2",description="PSU1 Max Temp Sensor"} 1
  smon_temp{name="psu2temp1",description="PSU2 Inlet Temp Sensor"} 1
  smon_temp{name="psu2temp2",description="PSU2 Max Temp Sensor"} 1
  smon_temp{name="temp1",description="Rear Outlet Air sensor"} 1
  smon_temp{name="temp2",description="Front Outlet Air sensor"} 1
  smon_temp{name="temp3",description="Temp Sensor close to Networking ASIC"} 1
  smon_temp{name="temp4",description="Intel CPU die sensor"} 1
  smon_temp{name="temp5",description="Intel CPU die sensor"} 1
  smon_temp{name="temp6",description="Intel CPU die sensor"} 1
  smon_temp{name="temp7",description="Intel CPU die sensor"} 1

  # HELP smon_power (-1=ABSENT, 0=BAD, 1=OK)
  # TYPE smon_power gauge
  smon_power{name="psu1",description="PSU1"} 1
  smon_power{name="psu2",description="PSU2"} 1

```

## Usage

`$ smonctl_parser.py`
