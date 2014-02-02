import sys
import csv

out = csv.writer(sys.stdout)


#loop variables initialized here
curLoc = None
#use last 10 pings, ignore dropped packets
pingTimes = []
dlTime = None
ulTime = None
ucSecureSignals = {}
eduroamSignals = {}

class DataRow:
  def __init__(self, loc, pings, ulTime, dlTime, ucSecSignals, eduSignals):
    self.loc = loc
    self.pings = pings
    self.ulTime = ulTime
    self.dlTime = dlTime
    self.ucSecSignals = ucSecSignals
    self.eduSignals = eduSignals

datarows = []
routers = set()

for line in sys.stdin:
  fields = line.strip().split()
  if 'echo' in line and fields[-1] != curLoc:
    if curLoc is not None:
      #New location! Let's store the last one's info
      dr = DataRow(curLoc, pingTimes, ulTime, dlTime, ucSecureSignals, eduroamSignals)
      datarows.append(dr)

    pingTimes = []
    curLoc = fields[-1]
    ulTime = dlTime = None
    ucSecureSignals = {}
    eduroamSignals = {}
  
  if 'bytes from' in line:
    pingTimes.append(fields[-2].split('=')[1])

  if 'real' in line and fields[0] == 'real':
    if ulTime is None:
      ulTime = fields[1]
    else:
      dlTime = fields[1]

  if len(fields) > 0 and fields[0] == 'uchicago-secure':
    ucSecureSignals[fields[1]] = fields[2]
    routers.add(fields[1])

  if len(fields) > 0 and fields[0] == 'eduroam':
    eduroamSignals[fields[1]] = fields[2]
    routers.add(fields[1])

titles = ["Location","Upload time","Download time"]
for i in range(10): titles += ["Ping #" + str(i)]
for router in routers:
  titles += ["Eduroam " + router, "UC-Secure " + router]

out.writerow(titles)

for dr in datarows:
  row = [dr.loc, dr.ulTime,dr.dlTime] + dr.pings
  for router in routers:
    edu = dr.eduSignals[router] if router in dr.eduSignals else ""
    uc = dr.ucSecSignals[router] if router in dr.ucSecSignals else ""
    row += [edu,uc]
  out.writerow(row)
















