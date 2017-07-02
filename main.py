#!/usr/bin/env python
import sys
import time
import monitor
import subprocess
import time

from fcntl import fcntl, F_GETFL, F_SETFL
from os import O_NONBLOCK, read
import pexpect

mon = '/sys/class/thermal/thermal_zone0/temp' # For raspberry or similar
maxTemp = 60.0

lastTimeSuccess = 0

minerPID = 0
minerName = 'miner'
minerPath = '/your_path/'
minerArg = '/your_path_to_config/xmr.conf'

acceptedBlock = 0
rejectBlock = 0
allBlock = 0
shareMaxWaitTime = 5 # In minutes

minerProcess = pexpect.spawn(minerPath,[minerArg],timeout=1)

flags = fcntl(minerProcess.stdout, F_GETFL)
fcntl(minerProcess.stdout, F_SETFL, flags | O_NONBLOCK)

while 1:
	time.sleep(2)
	try:
		f = open(mon,'r')
                temp = float(f.read())
		nowTime = time.time()
		day,hour,minute,second = monitor.SecondToTime(int(nowTime-(lastTimeSuccess,nowTime)[(lastTimeSuccess==0)]))
		if (minute>shareMaxWaitTime):
			monitor.KillMinerByName(minerName)
                        minerProcess = pexpect.spawn(minerPath,[minerArg],timeout=1)
                        lastTimeSuccess = time.time()
                print(">>> CPU Temp:"+str(temp)+" Last accepted: "+str(minute)+" min "+str(second)+" s All: "+str(acceptedBlock)+"/"+str(allBlock))
		while not minerProcess.eof():
		    strLine = minerProcess.readline()
		    print(">>> " + strLine)
                    shareData = monitor.ShareData(strLine)
		    if (shareData):
			    lastTimeSuccess = time.time()
			    acceptedBlock = shareData['success']
			    allBlock = shareData['all']
	except:
		continue

