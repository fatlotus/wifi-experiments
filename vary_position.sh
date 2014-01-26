#!/bin/bash -ex
# 
# Experimental procedure:
# 
# - Execute `setup.sh` to initialize the random data used in the experiment.
# - Run the following command on the ASUS UX32VD test laptop with Ubuntu 13.10.
# 
#     ./vary_position.sh 2>&1 | tee vary_position.log
# 
# - At each point, type the name of the position and press enter.
# - This will generate the vary_position.log output file.
#

while read position; do
   echo $position
   
   date
   
   ping -c 10 linux1.cs.uchicago.edu
   
   time scp randomblob jarcher@linux1.cs.uchicago.edu:/tmp/largefile
   time scp jarcher@linux1.cs.uchicago.edu:/tmp/largefile download
   
   if [[ "x$(uname)" == "xDarwin" ]]; then
      /System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current\
/Resources/airport -s
   else
      iwlist wlan0 scan
   fi
done