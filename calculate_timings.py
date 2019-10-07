'''
Readings: starts, finish
Participants
chip-number relation

Flux Diagram.

Step1:
	Read csv file with all readings
Step2:
	Save on arrays, start times and finish times
Step3:
	Calculate gun time: finish minus gunshot and save it
Step4:
	Calculate chip time: finish minus start time and save it
Step5:
	Locate chip code with his participant data and store it
Step6:
	Locate results with the relation of code and number stored it
Step7:
	Publish all relations on diferent file

Entities:
	- Event
	- Participant
	- Chip code
	- Number
	- Readings
'''

import csv

start_times = {}
finish_times = {}

def getStartTime(chip):
	severalTimes = []

def readStarts():
	try:
		with open('starts.csv','rt') as csvfile:
			st = csv.reader(csvfile)
			# readings = dict((readings[0],readings[1]) for row in data)
			start_times = dict((r[0],r[1]) for r in st)
			return start_times
	except IOError as e:
		raise e + "Archivo de salidas no encontrado"
    
def readFinish():
	try:
		with open('finish.csv','rt') as csvfile:
			fn = csv.DictReader(csvfile)
			# readings = dict((readings[0],readings[1]) for row in data)
			return fn
	except IOError as e:
		raise e + "Archivo de llegadas no encontrado"

def showStarts():
	start_times = readStarts()
	for row in start_times:
		print(row[0], row[1])

def showFinish():
	finish_times = readFinish()
	for row in finish_times:
		print(row['chip'], row['time'])

showStarts()
'''
if __name__ == "__main__":
	showStarts()
	print "x"*10
	showFinish()
'''