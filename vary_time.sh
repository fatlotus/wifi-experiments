#!/bin/bash -ex
# 
# Experimental procedure:
# 
# - Execute `setup.sh` to initialize the random data used in the experiment.
# - Run the following command on the ASUS UX32VD test laptop with Ubuntu 13.10.
# 
#     ./vary_time.sh 2>&1 | tee vary_time.log
# 
#   This will collect data for 24 hours.
#

while [ true ]; do
   date
   
   ping -c 10 linux2.cs.uchicago.edu
   
   time scp randomblob linux2.cs.uchicago.edu:/tmp/largefile$USER
   time scp linux2.cs.uchicago.edu:/tmp/largefile$USER download

   time wget -O - http://www.cvg.ethz.ch/research/mountain-localization/mountain-localization.tgz > /dev/null
   time wget -O - https://dev.qu.tu-berlin.de/attachments/download/1287/SoundScapeRenderer-0.3.4-MacOSX-10.6-10.7-64bit.dmg > /dev/null
   sleep 30
done
