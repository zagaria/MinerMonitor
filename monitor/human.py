def SecondToTime(seconds):
	minute, second = divmod(seconds,60)
	hour, minute = divmod(minute, 60)
	day, hour = divmod(hour,24)
	return day,hour,minute,second
