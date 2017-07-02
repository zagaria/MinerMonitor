#!/usr/bin/env python
import subprocess
import psutil
import re

def GetMinerPID(minerName):
        minerPID = 0
        for proc in psutil.process_iter():
            try:
                pinfo = proc.as_dict(attrs=['pid', 'name'])
                if (pinfo['name']==minerName):
                        minerPID = pinfo['pid']
            except psutil.NoSuchProcess:
                pass

        return minerPID

def KillMinerByPID(pid):
	p = psutil.Process(pid)
	p.terminate()

def KillMinerByName(name):
        minerPID = GetMinerPID(name)
        KillMinerByPID(minerPID)
