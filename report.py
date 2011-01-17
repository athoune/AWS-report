import csv
from datetime import datetime
import calendar
import json

class Report:
	def __init__(self, f):
		self.f = f
	def __iter__(self):
		r = csv.reader(open(self.f), delimiter=',')
		r.next()
		for line in r:
			yield {
				'service' : line[0],
				'operation': line[1],
				'usageType': line[2],
				'start' : datetime.strptime(line[3], '%m/%d/%y %H:%M:%S'),
				'end'   : datetime.strptime(line[4], '%m/%d/%y %H:%M:%S'),
				'value' : float(line[5])
				}
	def sum(self, action, metric):
		total = 0.0
		for line in self.__iter__():
			if (line['operation'], line['usageType']) == (action, metric):
				total += line['value']
		return total
	def draw(self, *filters):
		data = []
		for filtr in filters:
			print filtr
			values = []
			for line in self:
				if (line['operation'], line['usageType']) == filtr:
					values.append([calendar.timegm(line['start'].timetuple()) * 1000, line['value']])
			data.append({
				'label': filtr[0],
				'data': values,
				'hoverable': True
			})
		tpl = open('index.tpl','r')
		target = open('index.html', 'w')
		target.write(tpl.read() % {'data': json.dumps(data, indent=4)})
		tpl.close()
		target.close()

r = Report('report.csv')
#for line in r:
#	print line
#print
#print 'requests', r.sum('SelectGet', 'Requests')
print 'box usage', r.sum('SelectGet', 'BoxUsage')
r.draw(('SelectGet', 'Requests'), ('PutAttributes','Requests'), ('GetAttributes', 'Requests'), ('ListDomains', 'Requests'))
#