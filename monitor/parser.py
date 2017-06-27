#!/usr/bin/env python

import re

patterns={}
patterns['shares'] = 'Share\s+accepted\:\s+(\d+)\/(\d+)\s+\((\d+\.\d+\%)\)'

def ShareData(data):
	resultData = {}
	result = re.findall(patterns['shares'],data)
	if (result):
		resultData['success'] = int(result[0][0])
		resultData['all'] = int(result[0][1])
		resultData['percent'] = result[0][2]
		return resultData
	else:
		return None
