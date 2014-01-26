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

for i in (1..1440); do
   date
   
   ping -c 10 linux1.cs.uchicago.edu
   
   time scp randomblob jarcher@linux1.cs.uchicago.edu:/tmp/largefile
   time scp jarcher@linux1.cs.uchicago.edu:/tmp/largefile download
   
   sleep 60
done