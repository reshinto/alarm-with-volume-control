from schalarm import *

def combi_sch(combi):
	"""
	Initialize alarm time.
	Set the basic settings to allow combinations of user input for alarm schedule.
	"""
	al_hr = input(" Please set the alarm hour (xx) time: ")
	al_min = input(" Please set the alarm minute (xx) time: ")
	al_time = al_hr + ":" + al_min
	# Looking for ways to simplify and make the following code more efficient
	a = schedule.every().monday.at(al_time).do(job)
	b = schedule.every().tuesday.at(al_time).do(job)
	c = schedule.every().wednesday.at(al_time).do(job)
	d = schedule.every().thursday.at(al_time).do(job)
	e = schedule.every().friday.at(al_time).do(job)
	f = schedule.every().saturday.at(al_time).do(job)
	g = schedule.every().sunday.at(al_time).do(job)
	run_schedule(combinations(combi, 7))

def main():
	"""
	The heart of the program, and displays alarm menu.
	Links settings to alarm schedules.
	"""
	combi = input("""\
 Choose a combination of the following:
 Weekdays   : abcde
 Weekends   : fg 
 Mondays    : a
 Tuesdays   : b		
 Wednesdays : c
 Thursdays  : d
 Fridays    : e
 Saturdays  : f
 Sundays    : g
 > """)
	# Needs work! prevent user from selecting invalid values
	if combi != "h":
		combi_sch(combi)
	else:
		print("Wrong")
		main()

# time_input() function is activated first to input required settings
if __name__=="__main__":
	time_input()
	main()
