import csv
import datetime

class Report:
	def __init__(self, f):
		self.f = f
	def __iter__(self):
		for line in csv.reader(open(self.f), delimiter=','):
			yield {
				'service' : line[0],
				'action': line[1:3],
				'start' : line[3],
				'end'   : line[4],
				'value' : line[5]
				}
	def sum(self, action, metric):
		total = 0.0
		for line in self.__iter__():
			if line['action'] == [action, metric]:
				total += float(line['value'])
		return total

r = Report('report.csv')
#for line in r:
#	print line
print
print 'requests', r.sum('SelectGet', 'Requests')
print 'box usage', r.sum('SelectGet', 'BoxUsage')