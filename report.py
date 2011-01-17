import csv
import datetime

class Report:
	def __init__(self, f):
		self.reader = csv.reader(open(f), delimiter=',')
	def __iter__(self):
		for line in self.reader:
			yield {
				'service' : line[0],
				'action': line[1:2],
				'start' : line[3],
				'end'   : line[4],
				'value' : line[5]
				}

r = Report('report.csv')
for line in r:
	print line
