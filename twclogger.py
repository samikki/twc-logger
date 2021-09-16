# converts tesla wall charger json to tsv and outputs to a daily log file
import json
import fileinput
from datetime import date,datetime
import os.path
from collections import OrderedDict

def qs(string):
    return "\"" + str(string) + "\""

variables=OrderedDict([
    ('time', 'Time'),
    ('vehicle_connected', 'Vehicle connected'),
    ('session_s', 'Session length'),
    ('grid_v', 'Grid voltage'),
    ('grid_hz', 'Grid frequency'),
    ('vehicle_current_a', 'Vehicle current'),
    ('currentA_a', 'Phase A current'),
    ('currentB_a', 'Phase B current'),
    ('currentC_a', 'Phase C current'),
    ('pcba_temp_c', 'PCBA temp'),
    ('handle_temp_c', 'Handle temp'),
    ('mcu_temp_c', 'MCU temp'),
    ('session_energy_wh', 'Session energy')
    ])

separator = ","
filetype = "csv"

today = date.today()
filename = datetime.strftime(date.today(), '%Y-%m-%d') + "." + filetype 

if os.path.isfile(filename):
    out = open(filename, "a")
else:
    out = open(filename, "x")
    out.write(separator.join('"{0}"'.format(w) for w in variables.values()) + "\n")

for inline in fileinput.input():
    data = json.loads(inline)
    line=[]
    for variable in variables.keys():
        if variable in data:
            line.append(str(data[variable]))
        elif variable == "time":
            line.append(datetime.strftime(datetime.now(), '%d.%m.%Y %H:%M:%S'))
        else:
            line.append("-")
    out.write (separator.join(line) + "\n")

