#!/usr/bin/env python
#
# This script is horrible code; I'll clean it up if you actually want to read
# it. The following is the command I used to generate the data files:
#
#  $ tr '+\n' '\n ' < data/NETWORK.log | python crunch_time_data.py >
#    processed/NETWORK.csv
#
# Do as I say, not as I do.

import re
from dateutil.parser import parse
import sys
import csv

date = None
pings = []
download_time = None
upload_time = None
german_time = None
swiss_time = None
out = csv.writer(sys.stdout)
rows = []


def write_out():
    global date, pings, download_time, upload_time
    
    if date is not None and upload_time is not None:
        rows.append([date, download_time, upload_time, german_time, swiss_time]
                     + pings)

for line in sys.stdin:
    if 'randomblob sthaler@linux' in line: #<- you will need to adjust this line
    
        match = re.search("real\t([0-9]+)m([0-9\.]+)", line)
        m, s = match.groups() if match else [0, -1]
        upload_time = float(m) * 60 + float(s)
        
    elif 'largefilesthaler download' in line:
        match = re.search("real\t([0-9]+)m([0-9\.]+)", line)
        m, s = match.groups() if match else [0, -1]
        download_time = float(m) * 60 + float(s)
    
    elif 'www.cvg.ethz.ch' in line:
        match = re.search("real\t([0-9]+)m([0-9\.]+)", line)
        m, s = match.groups() if match else [0, -1]
        swiss_time = float(m) * 60 + float(s)
    
    elif 'dev.qu.tu-berlin.de' in line:
        match = re.search("real\t([0-9]+)m([0-9\.]+)", line)
        m, s = match.groups() if match else [0, -1]
        german_time = float(m) * 60 + float(s)
    
    elif 'ping' in line:
        pings = [float(x) for x in re.findall('time=([0-9\.]+)', line)]
        while len(pings) < 10:
            pings.append(-1)
    
    elif 'date' in line:
        time = parse(line[6:]).time()
        date = time.hour * 3600 + time.minute * 60 + time.second
        write_out()
    

write_out()

rows.sort()

out.writerow(["time_of_day", "download_time_in_s", "upload_time_in_s",
              "download_time_from_germany_in_s",
              "download_time_from_switzerland_in_s" ] +
             ["ping{:}_in_ms".format(i) for i in xrange(10)])

for row in rows:
    out.writerow(row)