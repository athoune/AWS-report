import csv
from datetime import datetime

class Report:
	def __init__(self, f):
		self.f = f
	def __iter__(self):
		r = csv.reader(open(self.f), delimiter=',')
		r.next()
		for line in r:
			print line
			yield {
				'service' : line[0],
				'action': line[1:3],
				'start' : datetime.strptime(line[3], '%m/%d/%y %H:%M:%S'),
				'end'   : datetime.strptime(line[4], '%m/%d/%y %H:%M:%S'),
				'value' : float(line[5])
				}
	def sum(self, action, metric):
		total = 0.0
		for line in self.__iter__():
			if line['action'] == [action, metric]:
				total += line['value']
		return total

r = Report('report.csv')
for line in r:
	print line
#print
#print 'requests', r.sum('SelectGet', 'Requests')
#print 'box usage', r.sum('SelectGet', 'BoxUsage')